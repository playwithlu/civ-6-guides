# Modding (Civ6)/How to Create a Unit

Creating a Unit Mod.
This page goes over creating a basic unit with the "[Civilization%20VI](Civilization VI)" modding tools.
The starter project does not work right away. A couple of tweaks are required.
Making a Working Mod.
Start by creating the starter project as described on the [Modding_%28Civ6%29/Basics_of_Mod_Creation](mod basics page). In this example, the mod will named "My First Mod".
The areas that need attention are all in the properties of the mod. Find the item with the mod name (My First Mod) in the Solution Explorer on the left, right-click on it and select Properties.
Editing the Mod Info section is recommended, but not required.
The other edits will all be under the In-Game Actions section.
Each subsection is attempting to load a file, but every one of the files has the wrong name. Luckily, this is easy to fix. In the In-Game actions section, click on the UpdateDatabase subsection. Select the existing entry NewUnit_Gameplay.xml and remove that, because that is not what our file is named. Now, simply press the Add button and select My_First_Mod_Gameplay.xml. This name can be found in the Solution Explorer on the left.
The change should look like this. Notice the files on the left and corrected XML on the right.
This will need to happen for the UpdateIcons and UpdateText section the same way.
Now build the mod and start a new game. (Loading a save may have mixed results.)
New Unit in the Game.
The easiest way to make sure that the unit has been loaded is to check the [Civilopedia%23Civilization_VI](Civilopedia).
But since the "Peon" unit has no requirements, it can be built right away as well.
Making Changes.
The stats for the unit are defined in the My_First_Mod_Gameplay.xml file. The most basic stats are as follows.
As stated in a comment in the file, more advanced stats can be found by looking at the existing units in steamapps\common\Sid Meier's Civilization VI\Base\Assets\Gameplay\Data\Units.xml.
For example, the {{Strength6}} Combat Strength stat is Combat. Please note that the Peon is currently a [Civilian_unit](Civilian Unit) so change the FormationClass to FORMATION_CLASS_LAND_COMBAT before adding a combat stat.
To add a prerequisite [Technology_%28Civ6%29](Technology) to the unit, use PrereqTech with a value such as TECH_BRONZE_WORKING.