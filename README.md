# alumniOverflow

# TODO:
  * Create global DATABASE accessing functions (such as global DB_NAME, DB_CONNECT, and maybe some other functions).
    * Should there be a python script specifically dedicated to commonly executed SQL commands?
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
    
  * From the "database" directory, enter "sqlite3 2468" database
  * Execute ".read createschema.sql" to create tables
  * Execute ".read populate.sql" to fill tables
  * Execute ".read dropschema.sql" to empty tables
  * When finished, remove all data and drop tables by executing ".read dropschema.sql"
    
# PYTHON
  * app.py
    * To begin a local session, in terminal execute the following command from the main directory:
      ```
      python app.py
      ```  
  * survey.py
    * Testing:
      * Run `app.py` as above and in a web browser navigate to `<local_host>/survey_q0.html`.
      * Follow directions on screen and fill out the survey.
    * Bugs: 
      * Need to force some questions to be answered (like email, and some from q3)
      * When selecting top 4 categories, allows for selecting an empty category (need to disable base option)

  * list_questions.py
    * Purpose: to list all questions and categories in the database
    * Testing:
      * Run `app.py` as above, and in a web browser navigate to `<local_host>/list_questions/<user>` where `<user>` can be any string, but the only meaningful strings should be "moderator" and "expert". Alternatively, from the home page click "view all questions", which will navigae to the page without any `<user>` variable declared.
      * Try putting in various strings for `<user>` and see the greeting at the top of the page change
      * A list of test categories and test questions should display. Click on any question to be taken to the next page, which is currently a template, which the `<user>` variable has been passed into. Verify this by checking the message that shows up.
    * Bugs:
      * Unknown as of right now.
    * TODO:
      * Connect to database and fetch data from there (currently data is hardcoded in)
# DATABASE
  * Create/enter the database called "2468" by typing the following command
    ```
    sqlite3 2468
    
    ```  
  __TO DO [Tanner, Christian, Jared]:__
  * ~~Add keys~~
  * ~~Connect to Python~~
  * Write scripts for incremental database design
  * ~~Modify to make Q4 its own table (instead of the whole survey) -- for future, add tables for other questions as well~~
  * ~~Create a test dataset~~
  

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
