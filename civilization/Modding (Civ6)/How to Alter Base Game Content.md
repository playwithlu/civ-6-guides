# Modding (Civ6)/How to Alter Base Game Content

There are two ways to alter the base game content:
To replace a game file, you need to make a file with the same name and contents in your project, then make your changes. Then, you need to add an Import Files action to your mod, and add the file to that action. This will have the mod overwrite the base game file of the same name.
To alter the game database with SQLite, first make a new SQL file in your mod, and name it whatever you want. We will be using the following command:
 codice_1
codice_2 defines the Table to be updated. All of the table names can be found in codice_3 in codice_4 or you can look in the XML database files.
codice_5 defines the changes that will be made to the column values for the table. Multiple columns can be changed in one statement, separated by a comma.
If we put on a semi-colon and just stopped here, our command would change "every" column value in the table! For example, the command: codice_6 would make all the game buildings have a base cost of 10,000 production.
codice_7 defines which rows will be changed. Only the rows which have a value of B in the column 'codice_8' will be changed. You can also extend the codice_9 expression to change multiple types of rows at a time: codice_10
Lets change the Ranger unit so that is has a base sight of 5 tiles, turn off its zone of control, and change is required technology to Computers. First, we need to find the table that we need to update. We can find it in codice_11, where there is a table called "Units". We can see that there is a row with the primary key 'codice_12' and that the column names for the stuff we want to change is related to BaseSightRange="3", ZoneOfControl="true", and PrereqTech="TECH_RIFLING". Now, we are ready to make our SQLite command:
codice_13
Once we have saved our SQL file, we just need to add an codice_14 action to our mod, then add our SQL file to that action. ("It would be really useful to explain this in more detail. For example, would editing a unit be a front end action or In-game Action?")
Tips:
- String values in SQLite are defined with single quotes rather than double quotes.
- Boolean (true or false) values in SQLite are handled with integer 0 and 1.
- You can add comments (the file will ignore these) in SQLite by putting a double hyphen at the beginning of the line --