# Global warming (Civ4)

Global warming is a game element in "".
## Overview

The following information comes from the 3.17 changelog:
 Global warming in forests and jungles just removes those features, without turning plot to desert
 Global warming takes into account the number of forests and jungles in the world
 Global Warming is affected by unhealthy buildings in addition to nuclear explosions.
Global warming is caused by pollution (namely, "[Health%20%28Civ4%29](unhealthy)" [List%20of%20buildings%20in%20Civ4](buildings)) and nuclear explosions (which may sound counter-intuitive but is seemingly normal in the [Civilization%20%28series%29]("Civilization" series)). It is adverted by a large number of forests and jungles present on the [Map%20%28Civ4%29](world map). Its effects are to reduce the production of [Tile%20%28Civ4%29](tiles), usually turning random tiles into desert. The tiles affected when global warming strikes are picked randomly, regardless of how much each nation contributed to its occurrence.
Mechanics.
The mechanics of global warming are explained in detail below. The original post was written by Refar, a user of the [CivFanatics](CivFanatics) forums.
The XML tags.
All found in GlobalDefines.XML. New ones (or those believed to be new) are highlighted.
Code.
 &lt;Define&gt;
 &lt;DefineName&gt;GLOBAL_WARMING_TERRAIN&lt;/DefineName&gt;
 &lt;DefineTextVal&gt;TERRAIN_DESERT&lt;/DefineTextVal&gt;
 &lt;/Define&gt;
 &lt;Define&gt;
 &lt;DefineName&gt;GLOBAL_WARMING_PROB&lt;/DefineName&gt;
 &lt;iDefineIntVal&gt;20&lt;/iDefineIntVal&gt;
 &lt;/Define&gt;
 &lt;Define&gt;
 &lt;DefineName&gt;[B][COLOR="SeaGreen"]GLOBAL_WARMING_FOREST[/COLOR][/B]&lt;/DefineName&gt;
 &lt;iDefineIntVal&gt;50&lt;/iDefineIntVal&gt;
 &lt;/Define&gt;
 &lt;Define&gt;
 &lt;DefineName&gt;[B][COLOR="SeaGreen"]GLOBAL_WARMING_UNHEALTH_WEIGHT[/COLOR][/B]&lt;/DefineName&gt;
 &lt;iDefineIntVal&gt;20&lt;/iDefineIntVal&gt;
 &lt;/Define&gt;
 &lt;Define&gt;
 &lt;DefineName&gt;[B][COLOR="SeaGreen"]GLOBAL_WARMING_NUKE_WEIGHT[/COLOR][/B]&lt;/DefineName&gt;
 &lt;iDefineIntVal&gt;50&lt;/iDefineIntVal&gt;
 &lt;/Define&gt;
Derived Variables.
The code on Global Warming is within CvCity.cpp; doGlobalWarming();
GW_DEFENSE = #FOREST / #LAND * GLOBAL_WARMING_FOREST
GW_VALUE = #BAD_HEALTH * GLOBAL_WARMING_UNHEALTH_WEIGHT / #_PLOTS + #NUKES_EXPLODED * GLOBAL_WARMING_NUKE_WEIGHT / 100
Global Warming Probability.
On every turn there will be GW_VALUE independent random tests, each with a probability to cause Global Warming:
 PROB1 = ( GLOBAL_WARMING_PROB - GW_DEFENSE ) / 100
This results in a chance of no GW at a given turn:
 PROBtotal_no_GW = (1 - PROB1)GW_VALUE
And hence the chance of at least one GW event on any given turn:
 PROBGW_strikes = 1 - (1 - PROB1)GW_VALUE
With the standard XML values.
 GW_DEFENSE = #_FOREST / #_LAND * 50
 GW_VALUE = - #_BUILDING_BAD_HEALTH / #_PLOTS * 20 + #_NUCLEAR_EXPLOSIONS * 1/2
 PROBGW_strikes = 1 - (0.8 + #FOREST/#LAND * 0.5)GW_VALUE
Effect of Global Warming.
If Global Warming strikes, a random land PLOT which is not a [City%20%28Civ4%29](city) will be chosen.
There is no regional, player, team or other bias in choosing the target plot for Global Warming. It does not matter who, where or why caused the nuclear explosions, built the polluting buildings, chopped or preserved the forests.
If PLOT has a feature (Forest, Jungle, Floodplain, Oasis), this feature will be removed, but the terrain type does not change (unless the feature is Fallout, in which case nothing happens at all).
If PLOT has no Feature and can give any yield (i.e. is not desert or frozen), then it will be turned into GLOBAL_WARMING_TERRAIN, which is - per standard XML - desert.
Note on probability.
This de facto reduces the Probability of Global Warming with increasing amount of useless land plots on the map. Since if a plot is chosen to be victim of Global Warming, that can not be worked anyway, nothing happens. So actually:
 PROBGW_strikes = 1 - (1 - PROB1 + PROB1*#BADLAND/#LAND)GW_VALUE
Depending on how high PROB1 actually is and how much "bad land" we have it might result in 5-10 % (or even more in really extreme cases) less visible GW.
Same thing with fallout. Should be negligible in most games, but could become interesting in a huge Nuclear War, where the Fallout will actually help preserve the terrain under it. Of course, as soon as you clear the Fallout after the war, the plots will become affected by Global Warming again.
Notes.
Nukes now count only half. This means that a single explosion (say a meltdown) will not cause GW by itself. However this is only true if there are no other sources of GW.
The from buildings is weighted by map size (number of plots). To give an idea of its impact let's assume a Standard size map:
 1 * 20 / 4368 = ~0.005
So ~110 from buildings would have the same effect as one Nuke, giving us a half of a GW_VALUE point. Also since there is integer division involved and assuming no nukes, the first ~220 are free (as long as #BAD_HEALTH * GLOBAL_WARMING_UNHEALTH_WEIGHT / #_PLOTS &lt; 1).
One city with all possible pollution sources and no [Recycling%20Center%20%28Civ4%29](Recycling Center) can "provide" 17 (give or take 1-2 points).
Green World.
To completely avoid Global Warming we would need to:
Modding.
Setting GLOBAL_WARMING_PROB = 0 will still remove all GW. However, the method examining all plots and cities will still run, so it would be a bit faster to put a check there and skip the rest if == 0.
GLOBAL_WARMING_FOREST is a positive modifier - increasing the value will make fewer Forests/Jungles needed to avoid GW. A GLOBAL_WARMING_FOREST = 100, for example, would make only 20% of forested Landmass needed to count as a green planet.
Also note again - while talking FOREST we actually mean all Features that can grow.
GLOBAL_WARMING_UNHEALTH_WEIGHT and GLOBAL_WARMING_NUKE_WEIGHT are negative modifiers - reducing those will result in fewer Global Warming events.