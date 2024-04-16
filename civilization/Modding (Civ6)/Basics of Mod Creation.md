# Modding (Civ6)/Basics of Mod Creation

This page walks you through with installing the "[Civilization%20VI](Civilization VI)" modding tools.
Please note that the mod creation tools are only available on Windows. Mods still work on Mac and Linux, however.
First, you need to install the Software Development Kit (SDK). Go to your Steam client, then click "Library" and select "Tools" from the drop-down under the "Home" button. Find the Sid Meier's Civilization VI Development Tools entry, right click it and install it. Note that you do "not" need to install the "[Modding%20%28Civ6%29/Development%20Assets](Sid Meier's Civilization VI Development Assets)" package (An error stating "The "GeneratePantryPaths" task was not given a value for the required parameter "AssetsPath". May happen if these are not installed).
After the installation has finished, run it and select "ModBuddy". If it asks you to install some Visual Studio items, you must first download and install those also.
ModBuddy launches into a mostly empty, black screen:
In order to start creating a new mod, click "FILE | New | Project..." which greets you with a wizard like this:
Excellent! Pick one of the Starter items, type a name for it, and click OK. You are then shown the following instructions:
"Congratulations! You've taken your first steps into modding for Sid Meier's Civilization VI. These starter projects are designed to be a turn-key solution that you can use immediately."
"Before you are able to use your mod, you must first build it. To build the mod, click on the "BUILD" option in the top menu and select "Build Solution". Alternatively, you can press Ctrl+Shift+B (assuming you haven't changed the defaults). This will copy content into /My Games/Sid Meier's Civilization VI/Mods/'."
"First, let's make sure the mod is installed. Start up Civilization VI and navigate to "Additional Content". Under the list of installed mods, you should now see your newly created mod. Ensure the mod is marked as 'enabled'."
"Create a new game and enjoy the results!"
"The starter mods provide basic files to perform the task described in the project description. Double clicking on these files in the solution explorer will allow you to view and possibly modify them."
"If you wish to add new files to the mod, right click on the Mod in the solution explorer and select "Add-&gt;Add New Item..."."
You have now successfully installed the required tools and are ready to delve deeper into the world of modding "Civ6"! Hint: take a look at those XML files in the Solution Explorer, at the left side of the ModBuddy. If you don't see the Solution Explorer, enable it from the "VIEW" menu.