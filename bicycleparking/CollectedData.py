# MIT License
# Copyright 2017,Code 4 Canada
# written by and for the bicycle parking project, a joint project of 
# Civic Tech Toronto, Cycle Toronto, Code 4 Canada, and the 
# City of Toronto
#
# Created 2018 07 05
# Purpose provide (user) dashboard access to approved requests
# 
# Modified 
# Purpose 
# 

import requests
import datetime
import json
import django.utils as utils
from bicycleparking.models import Event, Area, SurveyAnswer, Intersection2d, Approval, Picture
from bicycleparking.LocationData import LocationData

class CollectedData (object):
  """Encapsulates methods for accessing the geographical databases and 
  returning request data as approved by a moderator."""

  latLimits = (53, 54)
  longLimits = (-114, -113)

  def __init__ (self, upperLeft = None, lowerRight = None) :
     """Defines the local variables: and the bounding box"""
     if (upperLeft and lowerRight) :
        self.limits = ((upperLeft [0], lowerRight [0]), (lowerRight [1], upperLeft [1]))
     elif (upperLeft) :
        self.limits = ((upperLeft [0], CollectedData.longLimits [1]), 
                       (CollectedData.latLimits [0]), upperLeft [1])
     elif (lowerRight) :
        self.limits = ((CollectedData.longLimits [0], lowerRight [0]), 
                       (lowerRight [1], CollectedData.latLimits [1]))         
     else :
        self.limits = (CollectedData.longLimits, CollectedData.latLimits)
     self.errors = []

  def get (self) :
     """Gets the list of approved items from the request database""" 

     result = []
     approved_photos_ids = Approval.objects.all().values('approved__answer__picture__id')
     list = SurveyAnswer.objects.filter(picture__in=approved_photos_ids)

     for survey in list :
         if self.bounded (survey) :
           result.append (self.accessItem (survey))
     return result

  def accessItem (self, answer) :
      """Takes the specifications for each individual item and constructs a single
      description object."""
      fromSurvey = [ { 'id' : 'duration', 'path' : ['happening', 0, 'time'] },
                     { 'id' : 'problem', 'path' : ['problem_type'] },
                     { 'id' : 'time', 'path' : ['happening', 0, 'date'] } ]

      result = {}
      location = LocationData(answer.latitude, answer.longitude).getIntersectionNames()
      result['intersection'] = location['closest']
      result['majorIntersection'] = location['major']
      survey = answer.survey
      for field in fromSurvey :
          try :
              key = field ['id']
              result [key] = self.fromSurvey (survey, field ['path'])
          except Exception as err:
              errors.append (err.msg)
                     
      result ['pic'] = [answer.picture.photo_uri]
      result ['longitude'] = answer.longitude    
      result ['latitude'] = answer.latitude
      result ['comments'] = answer.comments
      result ['id'] = answer.id
      return result

  def fromSurvey (self, base, indices) :
      """Gets the item in the survey by recursively scanning the index list until
      the list is empty. If the index is invalid for the type of object in the
      structure, returns empty string."""
      if len (indices) == 0 :
          return base
      else :
          current = indices [0]
          remaining = indices [1:]
          if ((type (base) is list and type (current) is int and current < len (base)) or
              (type (base) is dict and current in base)) : 
             return self.fromSurvey (base [current], remaining)
          else :
             return "" 
      
  def bounded (self, survey) :
      """Determines whether or not a pin falls within the boundaries associated
      with the request."""

      return self.limits [0][0] < survey.longitude < self.limits [0][1] and \
             self.limits [1][0] < survey.latitude < self.limits [1][1]  
