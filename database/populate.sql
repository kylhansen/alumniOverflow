/* Fills Participants table */
INSERT INTO Participants VALUES ("Bob","lack","bob@email","1800-01-01","Westmont","1812","Old English");
INSERT INTO Participants VALUES ("May","Jane","may@email","2000-12-25","Blestmont","2020","BioChem");
INSERT INTO Participants VALUES ("Rudy","Tryhard","rudy@email","1980-04-21","UCSB","2000","Buisness");
INSERT INTO Participants VALUES ("schlop","linksy","schlop@email","1962-01-01","SBCC","1985","Math");
INSERT INTO Participants VALUES ("Bingbong","low","bingbong@email","2050-06-13","UCSD","2071","Reading");

/* Fills QuestionFour table */
INSERT INTO QuestionFour VALUES ("bob@email","finance","How does one make money");
INSERT INTO QuestionFour VALUES ("may@email","finance","Is money green");
INSERT INTO QuestionFour VALUES ("rudy@email","job search","What are some interview tips");
INSERT INTO QuestionFour VALUES ("schlop@email","finance","how do loans work");
INSERT INTO QuestionFour VALUES ("bingbong@email","life tips","Is time actually an illusion");

/* Fills PublishedQuestions table */
INSERT INTO PublishedQuestions VALUES ("How do loans work","thisisafakeline.com","finance");
INSERT INTO PublishedQuestions VALUES ("how do you do block comments in python","pythonquesiton.com","CompSci");
INSERT INTO PublishedQuestions VALUES ("What are some interview tips","interview.com","Job Search");
INSERT INTO PublishedQuestions VALUES ("Is money green","money.com","general");
INSERT INTO PublishedQuestions VALUES ("How does one make money","money.com","finance");

/* Fills Alumni table */
INSERT INTO Alumni VALUES ("oldman@email","Retired","Bill");
INSERT INTO Alumni VALUES ("oldwoman@email","Stock Broker","Michelle");
INSERT INTO Alumni VALUES ("iamabillionair@email","ceo","Gabe");
INSERT INTO Alumni VALUES ("theycallmerich@email","software developer","markcubannorelation");
INSERT INTO Alumni VALUES ("meme@email","professional meme creator","pepe");

/* Fills RespondsTo table */
INSERT INTO RespondsTo VALUES ("icanhelp0@email","2012-01-15","helpinglink0.com","Get a job");
INSERT INTO RespondsTo VALUES ("icanhelp1@email","2018-06-08","helpinglink1.com","try this");
INSERT INTO RespondsTo VALUES ("icanhelp2@email","2017-11-05","helpinglink2.com","maybe go here");
INSERT INTO RespondsTo VALUES ("icanhelp3@email","2018-01-30","helpinglink3.com","send me your resume");
INSERT INTO RespondsTo VALUES ("icanhelp4@email","2017-06-27","helpinglink4.com","you can work for me");

/* Fills ConnectsWith table */
INSERT INTO ConnectsWith VALUES ("yeet@email","oldman@email","letsconnect.com");
INSERT INTO ConnectsWith VALUES ("may@email","oldwoman@email","letsconnect.com");
INSERT INTO ConnectsWith VALUES ("rudy@email","iamabillionair@email","letsconnect.com");
INSERT INTO ConnectsWith VALUES ("schlop@email","heycallmerich@email","letsconnect.com");
INSERT INTO ConnectsWith VALUES ("bingbong@email","meme@email","letsconnect.com");

/* Fills QuestionOne table */
INSERT INTO QuestionOne VALUES ("bob@email","finance");
insert into QuestionOne values ("rudy@email","buisness");
insert into QuestionOne values ("schlop@email","life advice");
insert into QuestionOne values ("bingbong@email","history");
insert into QuestionOne values ("may@email","loans");

/* Fills QuestionTwo table*/
insert into QuestionTwo values ("bob@email","loans");
insert into QuestionTwo values ("rudy@email","history");
insert into QuestionTwo values ("schlop@email","finace");
insert into QuestionTwo values ("bingbong@email","life advice");
insert into QuestionTwo values ("may@email","buisness");

/* Fills into QuestionThree table*/
insert into QuestionThree values ("bob@email","computer science");
insert into QuestionThree values ("rudy@email","data analytics");
insert into QuestionThree values ("schlop@email","english");
insert into QuestionThree values ("bingbong@email","math");
insert into QuestionThree values ("may@email","chemistry");

