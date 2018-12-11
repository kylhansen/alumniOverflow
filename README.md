# alumniOverflow

# TODO
  * Unify style
  * Fix alignment for checkboxes
    * Survey_q1
    * Survey_q3

# SETUP
  * Install SQLite
  * To access database, in "database" directory, type the following:
    ```
    sqlite3 2468
    ```
    This will create a database file "2468" in the database directory
  * Once the database is set up:
    * From the "database" directory, enter "sqlite3 2468" database
    * Execute ".read createschema.sql" to create tables
    * Execute ".read populateCategories.sql" to fill the category table
    * Execute ".exit" to finish set up
  * Extra:
    * Execute ".read populate.sql" to fill tables with test data
    * Execute ".read dropschema.sql" to remove all tables
  * When finished with the app, remove all data and drop tables by executing ".read dropschema.sql"
    
# PYTHON
  * app.py
    * To begin a local session, in terminal execute the following command from the main directory:
      ```
      python app.py
      ```  
    * Home page
  * survey.py
  * list_questions.py
    * Lists all questions under the appropriate category in the database
  * question_view.py
    * View a question and its responses
    * As a moderator, publish or delete question, or choose to edit it
    * As an expert, answer quesion
  * edit.py 
    * As a moderator, edit a question's text or category
  * database_helpers.py
    * Database helper functions
    
# DATABASE
  * Create/enter the database called "2468" by typing the following command while in database directory
    ```
    sqlite3 2468
    ```  
  * createschema.sql
    * create the schema for the database
  *  populatecategories.sql
    * populate the "categories" attribute for the database
  * dropschema.sql
    * drop all schema from the database
  * populate.sql
    * sample data for populating the database

# HTML TEMPLATES
  * survey_q#.html
    * the #th page which a visitor will view while taking a survey
  * survey_end.html
  * home.html
  * list_questions.html
  * question_view.html
  * edit_questions.html
