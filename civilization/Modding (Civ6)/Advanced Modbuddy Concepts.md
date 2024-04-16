# Modding (Civ6)/Advanced Modbuddy Concepts

Edited Version of Steam User Angryr's Modding Guide and Tips: ([http%3A//steamcommunity.com/sharedfiles/filedetails/%3Fid%3D888669713](Here is the original guide with images on Steam) )
Folders &amp; Paths.
These folders may be referenced in this guide or may be helpful when modding (i.e. GameData &amp; GameText). 
ModBuddy.
Creating a new mod.
Open up the mod tools and click ModBuddy. To start a new mod click "New Mod...", make sure you have "Civilization VI" selected (should be by default), then choose "Empty Mod". Note the settings that mark the directory your mod will be stored at. The checkbox indicates that there will be an additional folder added to the end of the "Location:" field with the name of your solution.
Mod Information.
There should be a small dialog with some basic information such as mod name, description, author, etc. Just hit okay, I will show you how you can change that later. You should focus on learning what you can do, not what you want to do; especially for your first mod.
Next, delete the ModArt.xml file. You won't be needing it, not for your first mod anyways. If you do need it you're probably biting off too much. The purpose of your first mod is to get you familiar with the environment, not to actually make a meaningful mod.
Mod Configuration.
To see the mod's configuration right click the Project file ("EmptyMod1" in the image below) and choose Properties (bottom option). The project file will be opened and you'll be immediately taken to the "Mod Info" tab. Here is where you can change, at any time, the information you skipped when creating the project (i.e. Mod Name, Description, etc.).
Now, I'm showing you this first because this is the "center" of the mod. The project file contains the information telling the mod what to do with the files. If you just make a mod, add the files and don't touch this part, it won't do anything.
Adding Files to a Project.
The project file will contain the "FrontEnd Actions" and the "In-Game Actions" tabs. 90% of the time you will be using the "In-Game Actions" tab. The "FrontEnd Actions" tab is only for things before you start the game (MainMenu, Game Setup Screen, etc.). The "In-Game Actions" tab should contain the code for pretty much everything else.
"MadManCam:" In either "FrontEnd Actions" or "In-Game Actions", select "Add Action" to give your mod an action. With the new action selected, you can give it a name and select the type of action from the dropdown list on the right. The action type tells the game what to do with the mod files. To give one of your project files an in game action, select "Add" on the far right in the "Files" section, and use the window to select your project file. Now your mod will actually use your file.
Tools.
Here are the tools (applications) I use while modding (other than the obvious Civilization VI SDK):
Both of these are open-source applications. Neither is needed though the SQLite browser is highly recommended.
SQLite Browser Setup &amp; Usage.
The SQLite browser is immensely helpful when searching for examples of certain modifiers, requirement types, etc. It's slightly less helpful if you do not know SQL.
Errors &amp; Troubleshooting.
The most common set of errors you'll run into when starting out are syntax and foreign key reference errors. These are caused by typing something wrong (syntax) or not inserting a value (foreign key reference; which also can be caused by inserting a reference to something before it has been inserted itself).
Syntax and XML/SQLite database operation errors populate the database.log file in the Log Folder (See [%23Folders%20%26amp%3B%20Paths](Folders &amp; Paths) section) when the game was at the loading screen.
Note: The reason I suggested Notepad++ in the tools section is that you might have the log file open before the error is thrown in there. With the regular Notepad you'll have to re-open the file. However, Notepad++ will detect that the file has been changed and will ask you if you'd like to reload it.
The log files inside the Log Folder are a valuable set of files. Some of them more than others. For instance, the database.log shows syntax and database errors and the gameeffects.log shows issues with modifiers. If you happen to be adding Lua files to the game, the lua.log shows syntax errors and issues related to Lua files.
Quite commonly the symptoms of there being an error in the database.log file is that something you've attempted to change is just not even remotely in the game. This was happening to me a LOT before I knew about these log files. After I found out, it started taking me less and less time and I started correcting the behaviors that caused those errors in the first place (e.g. forgetting semicolons after SQL statements).
Pitfalls.
Below I will list some of the pitfalls of modding that I have discovered so far.
Arguments.
I have found that if you misstype an argument (e.g. ModifierArguments, RequirementArguments, etc.), no error will be presented. I had "GENREAL" instead of "GENERAL" for a 'GreatPersonClassType' argument and it never displayed an error anywhere.
CollectionTypes.
If you attach a modifier to the wrong CollectionType (defined in ModifierType AKA DynamicModifiers table) it's not necessarily going to come right out and tell you that it's wrong. It may simply just fail to work without showing any errors.
So becareful and double check these things when you've checked there are no errors and your mods aren't working (e.g. in these cases my text changes were occurring but the actual change wasn't taking place).
Text &amp; Localization.
Civilization VI Text.
In Civilization VI there is a "lot" of text. Text for units, civilizations, traits, promotions, etc., etc. You might think that it would make sense to put each unit's name, description, etc. in the unit table along with its attributes like cost, movepoints, etc. but this is bad (see reasons below).
LocalizedText.
Alright, so we've concluded that the text for each entity in the game is stored in a text table. That table's name is LocalizedText (I believe there are other very, very minor ones but they're not important; if they even exist). The table is part of the database "DebugLocalization.sqlite". The core of this table is represented by the following columns:
The gender have the article appended, e.g. "an" (as for "Airport": "an Airport" or "Alhambra": "the Alhambra"). It may also be the text "no_article" describing that the word is never used with an article (e.g. "Big Ben" and not "The Big Ben") and other, language-dependent modifiers (like "no_space" in German suppressing the space-separation to the next word for word combinations as in "Elite-")
Just look in the table for more examples and I'm sure you other language speakers can figure it out.
Tags &amp; Conventions.
If you look in the LocalizedText table you'll notice that 95% of the tags in there begin with 'LOC_' and have underscores separating words. This is the convention that Firaxis used; quite often you can simply just know what a string is used for by reading the tag. Or, if you don't know the tag for something, you can guess it based on what it is. For example, you want to know the tag for the warrior unit. Well, based on Firaxis' convention, start with 'LOC_', what it is 'UNIT_', its base name 'WARRIOR_', and what you want 'NAME'. So the tag for the warrior unit's name is 'LOC_UNIT_WARRIOR_NAME' which when you're looking at the data or code for the unit it seems obvious and excessive but can be helpful at certain times.
Note that there is one single benefit to not using Firaxis' conventions and that is if you use some other prefix other than 'LOC_' you almost guarantee yourself to never have a conflict. I still recommend using a convention, whether you stick with Firaxis' convention is up to you.
Creating your own text.
Let's say you're me and you've created a leader trait for Catherine De Medici. The trait has two pieces of text associated with it: the name and a description. These two pieces of text will each need their own entries "for each language you want to implement" (I only do English because, again I don't know any other spoken languages). Below shows the SQL syntax for inserting the text records for my Catherine's Scout trait mod.
codice_1
The tricky thing to note here is that if you want to use an apostrophe in SQL you need to do two of them to "escape" it. Otherwise you'll get syntax errors because it thinks that's the end of the string.
Four "small" sections later and you now know everything I know on mod text in Civilization VI.
Kinds &amp; Types.
At the base of the Civilization VI modding hierarchy there are two tables: Kinds and Types. It is likely you will need to create an entry in the Types table for almost every piece of functionality or content you mod in Civilization VI.
Kinds.
The Kinds table is a table where the game's code and scripting meets the game's data. Somewhere in the game's code the kind KIND_ERA is hardcoded to be exactly that, what we think of to be an era in game. Likewise, the kind KIND_DIFFICULTY is used to tell the type DIFFICULTY_SETTLER that it is a kind of difficulty and to list it as such.
Types.
The Types table is the basis for almost everything in the game. If it's in the game, chances are there's a type associated with it. Each belief has a type, each building has a type, each unit has a type, and so on and so forth. Each type is associated with a Kind from the Kinds table so that the game's engine knows how to handle that Type. So as I stated above, the DIFFICULTY_SETTLER type is associated with the KIND_DIFFICULTY so that the game knows that it has to list it as a difficulty in the difficulty settings drop down. However, a type is not the "only" thing you need in order create a difficulty setting but it's the start.
The Hierarchy and its tables.
Below I'm going to review each table's columns and how they associate with each other. I'm going to use the Difficulties hierarchy (all tables involved in creating a difficulty setting) as an example so you're not just seeing the theory of Kinds and Types but how they exist in game.