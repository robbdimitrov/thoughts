CREATE SCHEMA IF NOT EXISTS thoughts;

CREATE TABLE IF NOT EXISTS thoughts.users (
  id serial PRIMARY KEY,
  username varchar(20) UNIQUE NOT NULL,
  email varchar(100) UNIQUE NOT NULL,
  name varchar(100) NOT NULL,
  password varchar(100) NOT NULL,
  bio varchar(250) DEFAULT '',
  reg_date timestamp NOT NULL DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS thoughts.followers {
  user_id integer REFERENCES thoughts.users(id),
  follower_id integer REFERENCES thoughts.users(id)
}
