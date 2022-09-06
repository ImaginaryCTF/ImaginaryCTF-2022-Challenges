CREATE USER 'ethan'@'127.0.0.1' IDENTIFIED BY 'p4ssw0rd10';
CREATE DATABASE ictf;
USE ictf;
CREATE TABLE ictf (flag varchar(255));
INSERT INTO ictf (flag) VALUES ('ictf{ssH_p0rt_f0rw4rding_1s_uSeful_0eb24f93}');
GRANT SELECT ON ictf.ictf TO 'ethan'@'127.0.0.1'
