CREATE TABLE edmonton_raw
(
  gid serial NOT NULL,
  id bigint,
  endpoint_id bigint,
  on_street_name_full_parent character varying(250),
  at_street_name_full_parent character varying(250),
  on_street_name_full character varying(250),
  at_street_name_full character varying(250),
  latitude float,
  longitude float,
  location character varying(250),
  the_geom geometry,
  CONSTRAINT edmonton_raw_pkey PRIMARY KEY (gid),
  CONSTRAINT enforce_dims_the_geom CHECK (st_ndims(the_geom) = 2),
  CONSTRAINT enforce_geotype_geom CHECK (geometrytype(the_geom) = 'POINT'::text OR the_geom IS NULL),
  CONSTRAINT enforce_srid_the_geom CHECK (st_srid(the_geom) = 4326)
);

-- Index: landmarks_the_geom_gist

-- DROP INDEX edmonton_raw_the_geom_gist;

CREATE INDEX edmonton_raw_the_geom_gist
  ON edmonton_raw
  USING gist
  (the_geom );