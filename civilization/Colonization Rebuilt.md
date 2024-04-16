# Colonization Rebuilt

 
Colonization Rebuilt is a new implementation of the "[Sid%20Meier%27s%20Colonization](Sid Meier's Colonization)" game published in 1994.
Motivation.
The main motivation is to adapt the maximal number of [unit](unit)s (very frustrating on late 
game) and to update the interface's mechanism in order to be closer to current standards 
("[Civilization%20V](Civilization V)" and "[Civilization%20VI](VI)"). The development started mid-2016.
As much as possible, graphical elements remains so as to preserve the so atypical ambiance. Particularly, most of pictures are taken from the original game. The game mechanism is also meant to be as close as possible from the original game 
(production calculation, Sons of Liberty, [Europe](Europe) price, score, migrants arrival, 
[Founding%20Father](Founding Father) arrival, bonus, etc.).
Rebuilt reshuffle.
Main additions concerns the interface with the player.
The size of the window is adaptive, in full screen at the launch but can be reduced. 
During the map game phase, informative popups appear when the cursor remains on an element.
Report displays have been renewed, in particular the religious report.
It is now possible to navigate between report pages through new buttons.
The almost-dynamic management of game languages is working, at this stage English and 
French are available.
The save management has been improved so that there is no limit to the number of saves.
Project status.
The [AI](Artificial Intelligence) of [Native%20American](Indians) and interaction with the player has been implemented.
Background music and sound effects have been added.
It is possible to use 3 zoom levels on the map.
Statistics records are available on the window from F11, all elements can be visualized.
All calculations are now realized by a thread synchronized to the GUI one. Such calculations are the game creation, loading, saving, path research, various actions on leader.
There is still the Artificial Intelligence of foreign leaders and King which has to be implemented. The interaction between the player and these elements doesn't exist yet.
Contribution.
Some new vignettes still have to be drawn:
 - picture describing a mountainous landscape (128x84)
 - picture describing a mid flat / mountainous landscape (128x84)
 - picture describing a flat landscape (128x84)
Please send your masterpiece (see [Colonization%20Rebuilt%23External%20links](below) for contact e-mail).
Download and installation.
Releases are available on the following link, copy the shortcut from right click, open a new tag and paste it on the URL bar.
https://share.net-c.com/?key=LUHEiMG7T4DrmiHAfeN7qpnAYY9xvNhf%2BNlxtUXld7L85FFtkZcMwA%3D%3D
If one choose a folder installation on "Program Files" please launch the game on administrator mode, the save of a game isn't available otherwise. An alternative is to change the save folder on configuration files ".cfg", search the tag "#issue on saving".
More generally, the game can't create files on "C:\Program Files" if it isn't launched on administrator mode, following functionalities are impacted:
 - not possible to save game,
 - the .log file isn't created.
An alternative to give rights is to run the game in a portable mode, just need to place the game folder on "Documents" or anywhere else.
The texture loading functionality requires to write files on the system, the default location of these temporally files is "C:\Users\Public" but it can be changed on configuration files ".cfg" if needed.
Requirements.
This needs Windows and at least the Visual C++ redistributable for Visual Studio 2015 14.0 (see https://www.microsoft.com/en-us/download/details.aspx?id=52685 for downloading it)