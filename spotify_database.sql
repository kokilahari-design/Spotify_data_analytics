use spotify_db;
drop table if exists spotify_tracks;
create table if not exists spotify_tracks(
 track_id varchar(255) primary key,
 track_name varchar(255),
 artist varchar(255),
 album varchar(255),
 popularity int,
 duration_ms FLOAT
 );
 desc spotify_tracks;
 select * from spotify_tracks;
