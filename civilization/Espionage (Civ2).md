# Espionage (Civ2)

Espionage is a suite of special abilities and mechanics in "[Civilization%20II](Civilization II)" used by {{Link|2|pre=cat|espionage units}}, namely, {{Link|2|Diplomat}}s and {{Link|2|Spy|Spies}}. Espionage can provide a player with information about rival {{Link|2|civilizations}}, means of sabotaging opponents ouside of a formal [war](war), and even converting {{Link|2|unit}}s and {{Link|2|City|cities}} to the player's control.
Espionage actions do not require the {{Link|2|Espionage (advance)|Espionage}} {{Link|2|advance}}; most are available to the appropriate units inherently, although [%23Plant%20Nuclear%20Device](nuclear terrorism) has specific technological requirements.
## Overview

Espionage units.
Espionage is conducted by specific units: {{Link|2|Diplomat}}s (available with {{Link|2|Writing}}) and {{Link|2|Spy|Spies}} (available with {{Link|2|Espionage (advance)|Espionage}}). In general, diplomats are "one-shot", while spies can escape detection and return to friendly territory after a mission; successful operations and [%23Technology%20theft](counter-espionage) can award {{Link|2|veteran}}cy, improving odds of evading detection.
Espionage units can conduct missions against rival units and cities, regardless of {{Link|2|Diplomacy|diplomatic relation}}, by moving into their {{Link|2|Map|sec=Tile|tile}}. Certain missions are considered acts of aggression and will provoke an [%23International%20incidents](international incident) if exposed.
Unit missions.
Espionage can be conducted against any individual (non-[stack](stack)ed) unit. Units of any domain, including {{Link|2|pre=cat|Sea units|sea}} and {{Link|2|pre=cat|Air units|air}}, can be targeted.
Unit missions are guaranteed success regardless of unit; Spies conducting [%23Sabotage](sabotage) may be captured after the mission, otherwise they return to the player's nearest city, potentially earning veterancy.
Bribe.
Pay a variable {{Gold2|y|y}} price to convince the unit to defect to the player, determined by the following equation:
{{math|"b" {{=}} {{sfrac|37.5|"d" + 2}} × {{sfrac|1 + "t"|750}} × "s"}}
where {{math|"d"}} is the target's distance from its {{Link|2|capital}},{{refn|group=note|name=distance|Normalized to a maximum of 16, or 10 under {{Link|2|Communism}}. The distance between tiles is computed in a "zig-zag" pattern following directions; see Sections 4.31–4.33 in [%23References]("Info: Diplomats and spies") for an explanation of the exact maths.}} {{math|"t"}} is the target civ's [treasury](treasury), and {{math|"s"}} is the unit's {{Production2|y|y}} value. {{Link|2|pre=cat|Worker units}} incur double the normal price.
The defecting unit is assigned a [home%20city](home city) as per normal mechanics; if the closest city is not controlled by the player, the defector's home is {{mono|NONE}}.
The espionage unit will attempt to move into the target unit's tile, but the action itself does not expend movement points.
Sabotage.
Available to Spies. Damages half of the target unit's current hitpoints, rounding down.
City missions.
Diplomats are expended after every mission; Spies have a chance to evade capture and return to the player's nearest city, potentially earning veterancy. Actions with guaranteed success are "free" for spies, consuming a partial movement point (as if moving on a {{Link|2|road}}) and leaving them available for further missions.
Establish Embassy.
Permanently provides expanded intelligence on the civilization to the {{Link|2|Foreign Minister|sec=Embassy|Foreign Minister}}. Free action for Spies.
Investigate City.
Allows viewing the target's {{Link|2|city screen}} for the remainder of the {{Link|2|turn}}. Free action for Spies.
Industrial Sabotage.
Destroys a {{Link|2|city improvement}} or resets {{Production2|p|y}} progress. Can cause international incident.
Steal Technology.
Steals a {{Link|2|Advance|civilization advance}}, if available. Can cause international incident.
Diplomats provide a random advance, and are guaranteed success if no [%23Counter-espionage](opposing agents) are garrisoned. Spies can target a specific advance.
A city that has suffered technology theft will guard against subsequent attempts,{{refn|group=note|This flag is reset if the city changes ownership.}} preventing further attacks from diplomats; spies cannot steal a specific advance, and can be captured before completing the mission.
Poison Water Supply.
Available to Spies; reduces the target's {{Link|2|Citizen|population}} by 1. Not applicable to 1-citizen cities. Can cause international incident.
Plant Nuclear Device.
Available to Spies; requires that the player possess {{Link|2|Nuclear Fission}} and {{Link|2|Rocketry}}, and any civ has completed the {{Link|2|Manhattan Project}}. Can cause a unique, "major" international incident.
Detonates a bomb with equivalent effect of a {{Link|2|Nuclear Msl.}}, bypassing {{Link|2|SDI Defense}}s. Despite the wording of popup messages, the spy is not sacrificed in the mission, and will escape even if exposed.
Incite Revolt.
Pay a variable {{Gold2|y}} cost to convince the city and all {{Link|2|support}}ed units garrisoning and immediately adjacent to defect to the player. The base cost is determined by multiple factors including the city size, owning civ's treasury, and distance from the capital, with a mitigating bonus if the city is suffering {{Link|2|civil disorder}}. Spies further discount the cost by one-sixth, veteran Spies by one-third. Full equation as follows:
{{math|"b" {{=}} {{sfrac|1000|"d" + 3}} × {{sfrac|1 + "t"|1000}} × "p"}}
where {{math|"d"}} is the distance of the bribing unit from the target civ's capital,{{refn|group=note|name=distance}}{{refn|group=note|name=capital|Capital bribe immunity is based on the espionage unit's distance "from" the Palace, rather than the presence of the Palace itself. A unit immediately adjacent to the rival capital cannot bribe other nearby cities.}} {{math|"t"}} is the target civ's treasury, and {{math|"p"}} is the city' population. {{sfrac|1000|"d" + 3}} is further modified by the following "cumulative" factors:
In a normal revolt, any {{Link|2|Temple}}s, {{Link|2|Courthouse}}s, and {{Link|2|Cathedral}}s are instantly destroyed. Cities can also be subverted for twice the price, preserving improvements, suppressing {{Link|2|Partisans|sec=Resistance|partisan resistance}}, and preventing an [%23International%20incidents](international incident);{{refn|group=note|Subversion may, however, cancel a treaty without notice.}} this can only be conducted against civilizations with which the player has an active diplomatic treaty (Cease-Fire, Peace, or Alliance). Revolts can also provide gold and advances, as if the city was taken by force; the city will lose 1 citizen, to a minimum size of 1.
Counter-espionage.
Technology theft.
Espionage units stationed in cities provide a percent chance of thwarting technology theft. Up to three units can provide a compounding bonus, according to the following equation:
{{math|"S" {{=}} 1 - ("e"{{sub|1}} × "e"{{sub|2}} × "e"{{sub|3}})}}
Successful counter-espionage awards veterancy. Thwarted units forfeit their turn, leaving them vulnerable to expulsion or attack on the defender's turn.
International incidents.
Aggressive espionage actions (theft, sabotage, and city sedition) grant the victim "" to immediately retaliate without forfeiting {{Link|2|Diplomacy|sec=Reputation|international reputation}} if the perpetrator is exposed. At {{Link|2|Difficulty level|difficulties}} higher than Chieftain, an international incident damages the player's reputation by 1 level. Diplomats will always provoke an incident; Spies will only cause an incident if they are captured "after" the mission completes.
Planting a nuclear device provokes a major incident if exposed: all other civilizations immediately declare war against the perpetrator. Unlike other incidents, this does "not" damage the player's reputation.
Governments.
Certain {{Link|2|government}}s have special effects for espionage:
Modding.
Espionage and diplomatic notifications and dialogs are defined in {{Link|2|Modding|sub=Popups|Game.txt}}. While all mechanics are hard-coded, the player can be prevented from conducting missions by deleting their options from the relevant menus;{{refn|group=note|"Establish Embassy" and "Investigate City" cannot be disabled for spies: the "(Free)" suffix is applied externally and re-enables the menu option.}} this does not prevent {{Link|2|AI|computer opponents}} from accessing the missions.
Espionage {{Link|2|Modding|sub=Sounds|sec=Interface|sound effects}} encompass three files: {{mono|FEEDBK03.WAV}} (expelling), {{mono|SMALLEXP.WAV}} (sabotage), and {{mono|SPYSOUND.WAV}} (general espionage).
"Plant Nuclear Device" requires the {{Link|2|Manhattan Project}} be completed, and the player possess {{Link|2|Nuclear Fission}} and {{Link|2|Rocketry}}; a successful detonation uses {{mono|NUKEXPLO.WAV}} and the mushroom cloud animation (Image 21 / {{mono|GIFS/85}} in {{Link|2|Modding|sub=Graphics|sec=DLL files|Tiles.dll}}).