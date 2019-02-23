#!/bin/sh

set -e

export PGUSER="$POSTGRES_USER"
export PGPASSWORD='postgres'
OPTION=''

psql $USER $ADDR -c "SELECT * FROM pg_available_extensions WHERE name='postgis';" | grep -q postgis
if [ $? = 0 ] ; then
   echo 'postgis extension(s) detected, ready to process'
else
   echo 'geographic data extensions to postgres must be installed'
   echo 'see http://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS23UbuntuPGSQL96Apt'
fi

# Initialize GIS
sed 's/db_id/intersection/' /docker-entrypoint-initdb.d/sql/makegisdb.sql | psql

pg_restore -d intersection /docker-entrypoint-initdb.d/my_intersections.dump
# # Create the schema that will accept CSV
# psql -f /docker-entrypoint-initdb.d/sql/edmonton_intersection.sql -d intersection
# # Import the CSV into the DB
# echo "\copy edmonton_raw(id,endpoint_id,on_street_name_full_parent,at_street_name_full_parent,on_street_name_full,at_street_name_full,latitude,longitude,location) FROM '/docker-entrypoint-initdb.d/intersections.csv' DELIMITERS ',' CSV HEADER;" | psql -d intersection
# # Transform the lat/long from the CSV into POINTs
# psql -f /docker-entrypoint-initdb.d/sql/convert_edm.sql -d intersection