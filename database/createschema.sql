/*
Create all tables for the 2468 database
*/

CREATE TABLE Participants (
    firstname            VARCHAR(20),
    lastname VARCHAR(20),
    email           VARCHAR(50) PRIMARY KEY,
    birthday        DATE,
    school          VARCHAR(20),
    class_year      INTEGER,
    major           VARCHAR(20)
    );

CREATE TABLE QuestionFour (
	email VARCHAR(50),
  	question VARCHAR(300),
  	category VARCHAR(50)	
);

CREATE TABLE PublishedQuestions (
    text        VARCHAR(300),
    link        VARCHAR(100),
    category    VARCHAR(30)
    );

CREATE TABLE Alumni (
    email       VARCHAR(50) PRIMARY KEY,
    occupation  VARCHAR(20),
    name 	VARCHAR(20)
    );


CREATE TABLE RespondsTo (
    responder_email VARCHAR(50),
    date_responded  DATE,
    link            VARCHAR(100),
    answer          VARCHAR(500)
    );

CREATE TABLE ConnectsWith (
    participant_email   VARCHAR(50),
    alumni_email        VARCHAR(50),
    link                VARCHAR(100),
	PRIMARY KEY(participant_email, alumni_email)
    );
