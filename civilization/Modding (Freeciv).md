# Modding (Freeciv)

Modding in "[Freeciv](Freeciv)" is the creation of custom scenarios/maps, game rules (rulesets), game graphics (tilesets), and sounds, all of which the game supports. Most of the customization can be done by editing human readable section files with a text editor. The section files should have comments documenting what is going on.
Some scenarios, rulesets and tilesets are bundled with "Freeciv". "Freeciv" includes a program to download and install new mods.
Scenarios.
A scenario is an edited save game. A save game is a section file. The bundled tutorial is a scenario. It uses Lua code to advice the player. The bundled maps are also scenarios.
The content of a scenario varies. The bundled tutorial scenario doesn't even include a map. On the opposite end of the spectrum is the Greatturn community's Europe1901 scenario. It uses a map, cities, units and even alliances to model the Great Powers of Europe before the outbreak of WWI. A common scenario kind is a map with pre set start position for certain nations.
"Freeciv" includes an editor. It can change the current game. The result can be stored as a scenario.
Rulesets.
A [http%3A//freeciv.wikia.com/wiki/Editing_rulesets](ruleset) is a collection of game rules. It is mostly made of section files. Lua scripting is used for some game logic. It is possible to create new nations, unit types, tile extra types (like Road, Airbase, River, Whales, etc.), building types, techs and terrain types without knowing how to program in Lua. A minimal ruleset editor is included in the unfinished 2.6 version.
Tilesets.
A tileset is a collection of game graphics. The graphics for game pieces like unit types and terrain types live here. It is made of section files and png images.
Soundsets.
A collection of game sounds is called a soundset. It is made of section files and Ogg Vorbis sounds. Separate music sets are supported in the unfinished 2.6 version.