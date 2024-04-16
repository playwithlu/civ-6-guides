# Bugs (Col)

Bugs are coding mistakes that cause errors during [gameplay](gameplay).
Known bugs for "[Sid%20Meier%27s%20Colonization](Sid Meier's Colonization)" include:
Hopping Passengers.
In "[Sid%20Meier%27s%20Civilization](Sid Meier's Civilization)" and "[Civilization%20II](Civilization II)", [unit](unit)s [sentry](sentried) on ships could be activated at sea to transfer them between ships sharing the same [Tile](space). In "Colonization", [List%20of%20units%20in%20Colonization%20%281994%29](units) transfer between any in the same space whether they are activated or not. This can be especially frustrating when loading ships in [Europe%20%28Col%29](Europe), as ships arriving from different points on the [Map%20%28Col%29](map) can end up bringing the wrong passengers to the wrong locations in the New World. One kludge is to cheaply fill the holds of the other ships with 1 ton each of different cargoes, stopping the ships from being able to steal units during transit. This cargo can then be carried to a [Colony%20%28Col%29](colony) or dumped overboard.
Pathfinding.
Units in "Sid Meier's Colonization" will optimize their paths on short routes. On longer ones, land units will take more linear routes even when it means ignoring [Roads%20%28Col%29](roads) or obstacles like lakes and [Ocean%20%28Col%29](inlets). [Indians%20%28Col%29](Indian) units can end up immobile when their direct path back to their original settlement becomes blocked by European units or colonies. (It can also happen that the first Indian "walker" spawns on a different landmass than the village if the landmasses are close by.) On longer routes, ships inexplicably mimic great circle routes despite this frequently lengthening their journey. They also don't avoid offensive enemy units even though these frequently slow their passage, leaving them open for attack. Land units, on the other hand, will sometimes go needlessly out of their way (even in the opposite of the intended direction) when told to travel past an enemy unit, despite it being unable to block their passage.
Corner Squares.
Normally, armed ships ([Privateer%20%28Col%29](Privateers), [Frigate%20%28Col%29](Frigates), [Man-O-War%20%28Col%29](Men-O-War)) slow enemy ships passing by adjacent squares. However, when moving diagonally into the map squares diagonally adjacent to such ships, this effect is frequently avoided.
Random Number Generator.
The original DOS edition of "Sid Meier's Colonization" had a buggy random number generator that can lead to long strings of consecutive victories or defeats.
In the basic game, the only solution is to reload saved games or take other actions (such as movement or trading) that help to reset the counter. 
In 2004, the user brut posted a fix at [CivFanatics](CivFanatics):
 Do following.
 1. Open viceroy.exe in your hex-editor.
 2. Find such bytes: A3 EE 28 C7 06
 3. Replace A3 with 5D, and EE with CB, so you get 5D CB 28 C7 06
 4. Bug was removed!
This fix, however, produces the new bug that the game will consistently generate the same map on startup. To counter this, the original viceroy.exe file can be kept alongside a second vicefix.exe one that includes brut's edit. Begin the game normally, producing various new maps. Once a map has been created, load and play the map by starting directly from the vicefix.exe file.
A second fix tested to work in version 3.0 ([Steam](Steam) ed.) is to find the same bytes as before but replace C7 with 5D and 06 with CB. This produces much more randomized battles while still preserving the random map generator.
Other (minor) issues with the fix are:
Cathedral Issues.
In the early versions of the DOS edition of "Sid Meier's Colonization", [Cathedral%20%28Col%29](Cathedrals) could only be built in colonies of size 16, rather than the correct size 8. This was fixed by one of the patches.
Unit destroyed instead of demoted.
Military units, like [Dragoons%20%28Col%29](Dragoons) and [Continental%20Cavalry%20%28Col%29](Continental Cavalry) units in "Sid Meier's Colonization" that attack and lose the fight can randomly be destroyed instead of demoted. This can happen with any unit type and can happen to the [AI](AI), as well as the player. The only solution is to start a new game. The bug may potentially fix itself after many turns have passed (unconfirmed).
Attacks during peace or without contact.
Other European powers in "Sid Meier's Colonization" that you have met can randomly attack your colonies without declaring war and while keeping the peace status in the foreign affairs advisor screen. A bug related to this was fixed in 3.0.
It is legal for any power (AI and human) to attack colonies harboring Privateers without entering a state of war.
Glitched Hot-Seat Multiplayer/Nation selection.
By selecting the area where a 5th button would be, a glitched nation can be selected (shown in the screenshot is the German version). This causes several graphical glitches in the menus, as well as later in the game, but allows the human control of all 4 nations right out of the box. There are reports that saving/loading breaks this glitch though. You can also press the mouse down on one of the nation buttons and drag it around the screen. The selection will snap onto the glitch nation when you enter its square at the bottom.
This glitch only works on version 2.26 or below and does not work on 3.0.
A mostly glitch-free alternative is to use savegame editing, which is possible with certain tools.
Arawak "levelling up".
The [Arawak%20%28Col%29](Arawak) tribe may experience memory corruption, so that their villages upgrade to [Aztec%20%28Col%29](Aztec) or [Incas%20%28Col%29](Inca) villages, complete with respective riches. This can happen early on, or late in the game too. The cause is unknown, but it is most likely not intended.
Small glitches/bugs.
At some point in the game, you may be able to observe the move of an AI [Colonist%20%28Col%29](Colonist) in an area where you have no vision at all. This is commonly a [Petty%20Criminals%20%28Col%29](Criminal). This glitch may indicate something starting to go wrong in the game's internal memory.
Indian villages sometimes give nothing to your [Scouts%20%28Col%29](Scouts), even though nobody else could have possibly visited them in the meantime. This may be an intended feature for higher [Difficulty%20level%20%28Col%29](difficulties) though.
Like in many other Civ1/2-style games, [Pioneers%20%28Col%29](Pioneers) can "pre-charge" their building, causing them to finish building roads/cutting [Forest%20%28Col%29](forests)/[Plow%20%28Col%29](plowing) instantly. To do this, you must start any operation on an "expensive" tile, after a few turns abort it, and move the Pioneer (without selecting the job menu in a colony with him) to the target tile and start the desired operation there. It should instantly be done. A variation of this is to use 2 Pioneers to plow the same forest tile. While they will not make the cutting down of the forest any faster, the second Pioneer will charge its plowing, causing the tile to instantly receive plowing once the forest has been cut down and the Pioneer unit "acts". (So if the second Pioneer unit causes the forest to be cut down instead, while the first one has already been evaluated by the game, you need to wait for another turn.)
AIs can spam massive armies around each others' colonies and inside their own, but never engage in combat, causing them to pile up until the game runs out of unit slots. This can especially happen on Viceroy difficulty.
Rum producing buildings can employ an unlimited number of workers.