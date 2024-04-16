# Multiplayer (Civ5)

"[Civilization%20V](Civilization V)" offers a vast number of multiplayer game options.
What is "Multiplayer?".
Multiplayer is the same as [single%20player](single player) except that instead of [AI](AI)s, real people play against other real people. AIs may also be added to multiplayer if more players are required. Multiplayer is a simple term: "multi-" is an abbreviated version of "multiple," meaning "many," so a "multiplayer" game allows many players to participate.
Differences from Single Player.
Multiplayer does not offer as much variety in terms of playable [Map%20%28Civ5%29](maps). Maps like "The British Isles" (included in the [DLC%20%28Civ5%29](DLC)) may not be played; the only maps that are playable are the ones with adjustable sizes. [Civilizations%20%28Civ5%29](Civilizations) from DLC packs may be played in multiplayer; however, this must be enabled in the options menu, and doing so means that players who do not have that DLC may not participate. In-game players may talk using a talk panel beside the Diplomacy screen. Players may also trade and work in teams.
Also the AI is known to be highly "dumbed down" in comparison to the AI in single player. They will not initiate [Diplomacy%20%28Civ5%29](diplomacy) in the form of trade or research agreements with you.
Furthermore, the [Leaders%20%28Civ5%29](leader) animation screens that are shown when you initiate diplomacy with the AI in single player are removed from multiplayer. They are replaced by simple text boxes.
Multiplayer Tips.
NOTE: The information below was originally compiled for version 1.0.0.20 (before the release of ' and '), so portions of it may now be outdated. (Please remove this note if up-to-date information is added.)
Introduction.
"Civilization V" can be fun to play multiplayer. However, there are some "quirks" that can make things frustrating or difficult. This article attempts to list the quirks and workarounds to ensure people can have an enjoyable game. It assumes the reader is familiar with "Civilization V" in single player mode. The information provided here relates to version 1.0.0.20 - it may apply to previous or subsequent versions, but no guarantees can be made.
Simultaneous Turns.
This option enables the players to carry out their tasks at the same time, rather than waiting for their [turn](turn).
Playing Out of Turn.
In the current version (1.0.1.511) this seems no longer possible - every action taken will automatically cancel the "Next Turn" action (check this please).
Unit Focus.
Fixed in 1.0.0.62! There is now an option to stop focus stealing in the options menu.
Saving/Loading.
"Civilization V"'s multiplayer saving and loading for multiplayer games is currently a bit unpolished and inconsistent at present. Here are the current observations:
Converting Multiplayer Save to Moddable Single-Player Save.
To play a multiplayer game with mods in single player mode, open the save file with a hex editor of your choice. At the offset , you should find the value for a multiplayer save game. Change that value to , save, and exit. After this you can load the new save game as a single-player game and mod away.