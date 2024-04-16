# Espionage (Civ2)

Espionage is a suite of special abilities and mechanics in "[Civilization%20II](Civilization II)" used by , namely, s and . Espionage can provide a player with information about rival , means of sabotaging opponents ouside of a formal [war](war), and even converting s and to the player's control.
Espionage actions do not require the ; most are available to the appropriate units inherently, although [%23Plant%20Nuclear%20Device](nuclear terrorism) has specific technological requirements.
## Overview

Espionage units.
Espionage is conducted by specific units: s (available with ) and (available with ). In general, diplomats are "one-shot", while spies can escape detection and return to friendly territory after a mission; successful operations and [%23Technology%20theft](counter-espionage) can award cy, improving odds of evading detection.
Espionage units can conduct missions against rival units and cities, regardless of , by moving into their . Certain missions are considered acts of aggression and will provoke an [%23International%20incidents](international incident) if exposed.
Unit missions.
Espionage can be conducted against any individual (non-[stack](stack)ed) unit. Units of any domain, including and , can be targeted.
Unit missions are guaranteed success regardless of unit; Spies conducting [%23Sabotage](sabotage) may be captured after the mission, otherwise they return to the player's nearest city, potentially earning veterancy.
Bribe.
Pay a variable price to convince the unit to defect to the player, determined by the following equation:
where is the target's distance from its , is the target civ's [treasury](treasury), and is the unit's value. incur double the normal price.
The defecting unit is assigned a [home%20city](home city) as per normal mechanics; if the closest city is not controlled by the player, the defector's home is .
The espionage unit will attempt to move into the target unit's tile, but the action itself does not expend movement points.
Sabotage.
Available to Spies. Damages half of the target unit's current hitpoints, rounding down.
City missions.
Diplomats are expended after every mission; Spies have a chance to evade capture and return to the player's nearest city, potentially earning veterancy. Actions with guaranteed success are "free" for spies, consuming a partial movement point (as if moving on a ) and leaving them available for further missions.
Establish Embassy.
Permanently provides expanded intelligence on the civilization to the . Free action for Spies.
 civs with positive may also choose to provide an embassy, without requiring espionage units.
The and s provide embassies with every active civilization.
Investigate City.
Allows viewing the target's for the remainder of the . Free action for Spies.
Industrial Sabotage.
Destroys a or resets progress. Can cause international incident.
Diplomats are guaranteed success against a random target. Spies have the option to select a specific target, at risk of capture before the mission completes. are the lowest priority target and incur additional risk. The and are immune to sabotage.
The following table details spies' probability of interception when assigned a specific target:
Steal Technology.
Steals a , if available. Can cause international incident.
Diplomats provide a random advance, and are guaranteed success if no [%23Counter-espionage](opposing agents) are garrisoned. Spies can target a specific advance.
A city that has suffered technology theft will guard against subsequent attempts, preventing further attacks from diplomats; spies cannot steal a specific advance, and can be captured before completing the mission.
Poison Water Supply.
Available to Spies; reduces the target's by 1. Not applicable to 1-citizen cities. Can cause international incident.
The mission is guaranteed success, with probability of capture as follows:
Plant Nuclear Device.
Available to Spies; requires that the player possess and , and any civ has completed the . Can cause a unique, "major" international incident.
Detonates a bomb with equivalent effect of a , bypassing s. Despite the wording of popup messages, the spy is not sacrificed in the mission, and will escape even if exposed.
Incite Revolt.
Pay a variable cost to convince the city and all ed units garrisoning and immediately adjacent to defect to the player. The base cost is determined by multiple factors including the city size, owning civ's treasury, and distance from the capital, with a mitigating bonus if the city is suffering . Spies further discount the cost by one-sixth, veteran Spies by one-third. Full equation as follows:
where is the distance of the bribing unit from the target civ's capital, is the target civ's treasury, and is the city' population. is further modified by the following "cumulative" factors:
In a normal revolt, any s, s, and s are instantly destroyed. Cities can also be subverted for twice the price, preserving improvements, suppressing , and preventing an [%23International%20incidents](international incident); this can only be conducted against civilizations with which the player has an active diplomatic treaty (Cease-Fire, Peace, or Alliance). Revolts can also provide gold and advances, as if the city was taken by force; the city will lose 1 citizen, to a minimum size of 1.
Capital cities (those containing the ) are immune to revolt.
Counter-espionage.
Expulsion.
 with permanent relations (Cease-Fire or higher) have the option to expel espionage units that are closer to the player's cities than a rival civ's. The offending unit returns to the rival civ's (or otherwise nearest city). Expelling units does not incur a movement cost. Note that only single units can be expelled: [stack](stack)ed units can only be attacked normally.
Technology theft.
Espionage units stationed in cities provide a percent chance of thwarting technology theft. Up to three units can provide a compounding bonus, according to the following equation:
where is the percent chance of success times 100, and equals 1 minus 0.2 (Diplomat), 0.4 (Spy), or 0.6 (Veteran Spy). The following table provides a rough outline of how the bonus compounds:
Successful counter-espionage awards veterancy. Thwarted units forfeit their turn, leaving them vulnerable to expulsion or attack on the defender's turn.
Bribery.
A city with a halves the effective distance when calculating the bribe cost. A city celebrating also increases the bribe price.
International incidents.
Aggressive espionage actions (theft, sabotage, and city sedition) grant the victim "" to immediately retaliate without forfeiting if the perpetrator is exposed. At higher than Chieftain, an international incident damages the player's reputation by 1 level. Diplomats will always provoke an incident; Spies will only cause an incident if they are captured "after" the mission completes.
Planting a nuclear device provokes a major incident if exposed: all other civilizations immediately declare war against the perpetrator. Unlike other incidents, this does "not" damage the player's reputation.
Governments.
Certain s have special effects for espionage:
Modding.
 are designated by the "Diplomat" role in ; such units do not require or provoke , regardless of their statistics. and feature certain hard-coded attributes; consult their modding sections for details.
Espionage and diplomatic notifications and dialogs are defined in . While all mechanics are hard-coded, the player can be prevented from conducting missions by deleting their options from the relevant menus; this does not prevent from accessing the missions.
Espionage encompass three files: (expelling), (sabotage), and (general espionage).
"Plant Nuclear Device" requires the be completed, and the player possess and ; a successful detonation uses and the mushroom cloud animation (Image 21 / in ).