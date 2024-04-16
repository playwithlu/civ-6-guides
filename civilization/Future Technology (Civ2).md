# Future Technology (Civ2)

 Future Technology is a -era in "[Civilization%20II](Civilization II)", available with and .
Future Tech typically heralds the end of new . It is a uniquely repeatable advance, with each iteration providing a 5-point bonus to the 's .
Strategy.
Although future tech can be researched in perpetuity, a maximum 255 instances will actually contribute to the player's score (for a sum bonus of 1275), after which an occurs. The research option "Future Technology 256" instead resolves as "Future Technology 0" and resets the counter, wiping the score bonus and starting the cycle again. Thus, upon completing Future Tech 255, the sector is rendered redundant: can be sold, reassigned, and the reallocated to suspend further research.
Future tech cannot be stolen through or conquest, nor traded in . It is not listed in a civilization's , although its discovery will still be announced if an embassy is active.
Integer overflow exploits.
Future tech can also cause beneficial integer overflows in other mechanics. After researching 256 advances (~Future Tech 168 for a civ with all other research complete and no starting advances), the ramp-up cost is reset, potentially leading to a cascade of multiple discoveries in a single from beaker spillover. Likewise, excess advances will reset the modifier to the civilization's factor.
Civilopedia entry.
Since the dawn of mankind, human needs and desires have combined to produce ideas and inventions that make life easier and more productive. New technological breakthroughs have become an almost daily occurrence in the modern era, and new ideas will continue to drive human knowledge to higher and higher levels well into the future.
Modding.
Future Technology is defined in the 90th line of the section of . Its internal ID is ; although labeled in the Rules file, this is not recognized by the game and attempting to use it will cause a crash. Future tech MUST be directly accessible within the research tree (i.e. not disabled or dependent on advances only obtainable through ), or the game will crash.
Future tech can "technically" be used a prerequisite to other advances, but these will not appear as research options to the human player; players can research them normally, however. Future tech does not work with the "ReceivedTechnology" event macro.
Future tech does not render s or s [Obsolete%23Civilization%20II](obsolete). Items that call it as a prerequisite will not appear as build options for .
In original versions of "Civilization II" through to , the score bonus is fixed to 5 points; in "", it is customizable at the 28th line of the section of .