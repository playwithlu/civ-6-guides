# Map (Civ2)

The map is the playing board on which a game of "[Civilization%20II](Civilization II)" takes place. It is organized as a rectangular grid using [Isometric%20view](isometric) projection. A map can either be cylindrical (eastern and western edges connect, allowing continuous horizontal movement) or flat (boundaries are fixed and cannot be traversed). The forms the main game interface; it includes a "minimap" showing a simplified profile of the world that can be used to quickly re-center the view at a different section of the main map.
In "", a game can incorporate up to four maps simultaneously. Depending on the specific or rules, s can move between maps either through prescribed ability, or via s.
Display.
The map is the largest portion of the main game screen. How much of the entire map is shown varies based on the window's resolution and current zoom level, adjustable from the and/or hotkeys and ; there are 16 possible zoom levels, with graphics optimized to Level 9 (+).
The minimap is located in the upper right of the screen, displaying a simplified map of the whole world distinguishing land and tiles, and locations color-coded by . A white rectangle outlines the portion of the map currently on display; clicking within the minimap centers the view on the given coordinate.
In "Test of Time", the minimap is colored to the specific [%23Terrain](terrain). Using ToT's default map layout, the minimap initially appears as a rotating globe; clicking on it expands to the flat layout as in original "Civ II". Games with multiple maps include arrow buttons to navigate between map layers.
Tile.
A tile is the basic unit of distance on the map. Tiles can contain a number of elements, rendered in ascending order as follows:
Terrain.
Each tile represents a type of terrain that determines unit movement cost, , and . Terrain divides between two domains: land and .
Adjacency.
For most purposes, adjacent tiles are the eight tiles surrounding a given coordinate. Two special considerations exist:
Map generation.
When starting a , the player can choose between a randomly-generated map, or a pre-existing file that may have assigned starting locations for different civilizations.
Random map.
"Start a New Game" and "Customize World" will create a randomly-generated map to the specified size. "Customize World" allows the player to configure additional attributes of the world:
"Test of Time" games using multiple maps apply additional layers after the main game setup. By default, they use the same settings as the initial map; certain mods use special logic to configure landmass composition and player starting locations. See "[%23Multi-maps](Multi-maps)" for details.
Premade world.
"Start on Premade World" allows the user to load an existing [%23Map%20files](map file). Premade maps may specify the starting location of specific civilizations, otherwise initial are placed randomly. The player is given options to force randomization of starting locations, and/or the determining placement of and s.
The game does not compute the actual size of premade worlds when configuring internal settings such as maximum turns, but uses the dimensions of the most recent random map configuration in memory. Therefore, to ensure accurate gameplay, the user must first specify the map size through [%23Random%20map](random map) options, then begin a premade start.
Prompts for additional maps in appropriate "Test of Time" game modes occur after all other game settings are configured. A file must be provided for each layer; a random map cannot be generated. Unlike other options, cancelling map selection aborts game setup and returns to the main menu.
Modding.
"Civilization II" includes an external with tools for drawing s, assigning civs' starting locations, and altering the seed used to distribute resources and villages. The editor can import map data from [Saving%20and%20loading](saved games), but not () files.
The map can also be edited in-game through the function "Change Terrain At Cursor"; in addition to modifying terrain, this also allows adding/removing s and . "Change Terrain" cannot modify rivers or tiles containing cities. The "ChangeTerrain" will modify tiles within a rectangular set of coordinates; this removes all units, cities, and features present.
Graphics for terrain, tile features and yield-boosting improvements, and the general map interface (selection marker, tile edge mask) are defined in ; graphics for markers, military improvements, and Transporters are defined in .
Multi-maps.
Additional maps are generated for each line under the section of , up to three. Each line consists of a set of 18 numbers that determine the world's topography. Settings of generate a standard random world; if the first parameter is 0, no map will be created. Map names are defined under the section of .
Each additional map layer uses a unique version of definitions (, , ); these can also be given their own . Likewise, each layer uses its own terrain graphics files (, , ). River names are defined per-map under the section of ; the first line supersedes the label in .
The in-game allows importing a map file into the next unused layer, and exporting the active layer to an external file; unlike importing saved games through the Map Editor, these files retain tile improvement data. The map menu also allows toggling between layers (++) as a substitute for missing minimap arrows if no secondary maps are defined in .
Importing maps will restore explored villages and hide city sprites from existing maps; names are still visible but the cities themselves are unselectable on the map screen. It is therefore recommended to have all map layers in place before founding cities outside the player's control.
By default, all players begin on the first map layer. The section of allows assigning each civilization a different starting layer, and a primary and secondary unit different from the normal Settlers.
Transporters.
Unlike most settings defined in , relationships are written to the session at the start of the game and can only be modified through . It is therefore strongly recommended when creating a scenario to generate the initial game using a custom Rules file with Transporter settings preconfigured.
Tile-based transporter relationships are defined in the section of . Up to 16 lines can be entered; each line comprises two numbers separated by a comma, defining a link between the respective map layers (0–3). A link between a map and itself (e.g. ) is ignored.
Up to three separate transporters are available, with graphics defined in the bottom-right of . Each transporter encompasses every map link on the "n"th line in (so Sprite 1 reads Lines 1, 4, 7; Sprite 2 reads Lines 2, 5, 8, etc.). Note that individual transporter improvements only provide one map link at a time. Transporter names are defined at lines 882–884 under the section of .
The functions similarly to : a city can send or receive one unit per turn, subject to its transporter permissions.
Units.
Unit map transport settings are controlled by several fields under the section of . All fields are byte-values written in programming notation and read right to left; excepting Column B, the fields are 16 , corresponding to the pairings in :
Unit transporter rules can be modified in-game through the , without requiring hex editing.
Unit transporter attributes in the Civilopedia are defined on lines 922 (use) and 923 (native teleport) in the section of . The "Transport" order is named at Line 17 under the section of ; it uses the hotkey .
Map files.
Discrete map files are saved with the extension. "Civilization II" includes several maps, located in the main game directory:
In addition to the source maps for the , "Test of Time" includes several additional maps, sourced from scenarios previously featured in the ":