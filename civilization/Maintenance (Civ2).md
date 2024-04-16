# Maintenance (Civ2)

Maintenance or upkeep is a game mechanic in "[Civilization%20II](Civilization II)" modeling the operating costs required for s and s to function. Maintenance is automatically paid at the start of the player's ; if expenses exceed income (or [%23Support](support) exceeds ), improvements will be and units [disband](disband)ed.
City maintenance.
Most city improvements incur a persistent upkeep cost. At the beginning of the player's turn, maintenance expenses are subtracted from the empire's gross income. If net taxes are positive, the surplus is added to the [treasury](treasury); if negative, the treasury pays the difference. Revenue and expenses are detailed in the screen () and (+); the former also tallies the number and upkeep of each improvement type.
If maintenance costs exceed available funds, city improvements are automatically to generate liquidity. Improvements are liquidated quasi-randomly, with more valuable improvements sold to pay off larger deficits. Unlike manual selling, a city can liquidate multiple improvements during the update phase.
 is a that waives the maintenance for improvements costing 1. also waives upkeep on s, s, and s.
Unlike "[Civilization%20III](Civilization III)", Wonders that provide an improvement's effect (such as the for ) do not waive the maintenance cost of existing improvements; these must be manually sold to reduce overhead.
Unit support.
s are maintained with city , referred to as support: most units with a Defense strength of 1 or higher require 1 per turn from their [home%20city](home city), excepting and units. Certain s provide each city with a fixed quantity of "free" units that will not incur support.
If a city's net production is negative at the start of the turn, supported units will be randomly [disband](disband)ed until net are 0 or higher, prioritizing those stationed outside the home city. Units stationed in a city do not reimburse their value as they would if manually disbanded.
Units without a home city () do not incur support costs of any kind.
Workers.
 also require support, independent of production allowances. A city facing famine will disband workers ahead of sacrificing s. The specific food upkeep varies based on government: , , and require 1, while , , , and require 2.
Modding.
Improvement maintenance is defined at the third parameter of the relevant line in the section of . Wonders can also be assigned upkeep costs, although this is not used in the base game. Note that maintenance increases by 1 each if the player possesses and/or .
Unit maintenance is largely hard-coded. upkeep is defined on Lines 6 and 7 under the section of Rules.txt for "early" and "late" governments, respectively; free support for Monarchy, Communism, and Fundamentalism are defined on Lines 14–16, respectively. Units with a Defense strength of 0 do not require production support, nor do any units with the or role.