UPDATE edmonton_raw
SET the_geom = ST_GeomFromText('POINT(' || longitude || ' ' || latitude || ')',4326);