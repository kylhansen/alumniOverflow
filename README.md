# alumniOverflow

# TODO:
  * Design Database [Christian, Kyle]
  * Fill out TODO
  * Connect sqlite with python [Christian,Jared,Tanner]

# SETUP
  * Install SQLite
  * To access database, in "database" directory, type the following:
    ```
    sqlite3 2468
    ```
    This will create a database file "2468" in the database directory
    
# PYTHON
  * app.py
    * To begin a local session, in terminal execute the following command from the main directory:
      ```
      python app.py
      ```  
  * survey.py
    * Testing:
      * Run `app.py` as above and in a web browser navigate to "<local_host>/survey_q0.html".
      * Follow directions on screen and fill out the survey.
    * Bugs: 
      * Javascript for q3 doesn't work with flask to allow "disabling" other selected options as of right now, so that a user could select the same question multiple times. Could be changed to a checkbox system as in other questions, though we would need to make sure they can only select 4 at most.
      * Need to force some questions to be answered (like email, and some from q3)
    
# DATABASE
  * Create/enter the database called "2468" by typing the following command
    ```
    sqlite3 2468
    ```
  * To test, for now, do the following:
    * From the "database" directory, enter "sqlite3 2468" database
    * Execute ".read createschema.sql" to create tables
    * Try inserting and deleting various things in the database
    * When finished, remove all data and drop tables by executing ".read dropschema.sql"
  
  __TO DO [Tanner, Christian, Jared]:__
  * ~~Add keys~~
  * Connect to Python
  * Write scripts for incremental database design
  * Modify to make Q4 its own table (instead of the whole survey) -- for future, add tables for other questions as well
  * Create a test dataset
  * Make an automated test

# HTML TEMPLATES
Fully functional pages:
  * survey_q#.html
    * the #th page which a visitor will view while taking a survey
Skeleton templates:
  * editor.html
    * the page for an editor to edit and publish new questions
  * answer.html
    * the page for responders to answer questions
  * responses.html
    * the page for viewing responses
