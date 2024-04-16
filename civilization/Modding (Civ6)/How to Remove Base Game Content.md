# Modding (Civ6)/How to Remove Base Game Content

There are two ways to remove the base game content:
To replace a game file, you need to make a file with the same name and contents in your project, then make your changes. Then, you need to add an Import Files action to your mod, and add the file to that action. This will have the mod overwrite the base game file of the same name.
To delete from the game database with SQLite, first make a new SQL file in your mod, and name it whatever you want. We will be using the following command:
codice_1
codice_2 defines the Table to change. All of the table names can be found in GameplaySchema.sql in Base\Assets\Gameplay\Data\Schema\, or you can look in the XML database files.
If put on a semi-colon and just stopped here, our command would delete "every" row in the table! For example, the command codice_3 would remove all of the game buildings, so be careful.
codice_4 This part defines which rows will be deleted. Only the rows which have a value of A in the column 'Column1' will be deleted. You can delete from other rows as well by extending the expression: codice_5 adding as many 'or ColumnX=N' as you like.
Lets remove the Missionary from the game. We need to find all of the tables that contain data about the missionary, and then delete from those tables. We do a search in the game files for tables that contain rows with 'UNIT_MISSIONARY'.
codice_6
codice_7
codice_8
codice_9
codice_10
codice_11
codice_12
If we wanted to be extra thorough to make sure the game doesn't even try to implement modifiers or requirements having to do with missionaries, we can delete from modifier and requirement tables:
codice_11
codice_14
codice_15
codice_16
codice_17
codice_18
codice_19
codice_20
codice_21
codice_22
Once we have saved our SQL file, we just need to add an UpdateDatabase action to our mod, then add our SQL file to that action.
Tips:
- String values in SQLite are defined with single quotes rather than double quotes.
- Boolean (true or false) values in SQLite are handled with integer 0 and 1.
- You can make a line into a comment in SQLite with two hyphens at the beginning --