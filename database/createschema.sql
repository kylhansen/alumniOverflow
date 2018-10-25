/*
Create all tables for the 2468 database
*/

CREATE TABLE Participants (
    name            VARCHAR(20),
    email           VARCHAR(50) PRIMARY KEY,
    birthday        DATE,
    school          VARCHAR(20),
    class_year      INTEGER,
    major           VARCHAR(20),
    q1              VARCHAR(300),
    q2_1            VARCHAR(50),
    q2_2            VARCHAR(50),
    q2_3            VARCHAR(50),
    q2_4            VARCHAR(50),
    q3_1            CHAR(1), /* A yes/no answer */
    q3_2            CHAR(1),
    q3_3            CHAR(1),
    q3_4            CHAR(1),
    q4_1_category   INTEGER,
    q4_1_question   VARCHAR(300),
    q4_2_category   INTEGER,
    q4_2_question   VARCHAR(300)
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
    participant_email   VARCHAR(50) PRIMARY KEY,
    alumni_email        VARCHAR(50) PRIMARY KEY,
    link                VARCHAR(100)
    );



