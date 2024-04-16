# Trade route (Civ4)

Each [City%20%28Civ4%29](city) may have one or more trade routes which give it extra . 
Assignment of Trade Routes.
Each turn, trade routes are automatically computed by the game. All cities which a city has trade connections to are considered, with the better ones (foreign, intercontinental) being assigned to the bigger cities. A [Civilizations%20%28Civ4%29](civilization) gets no more than one trade route assigned to each foreign city. All other trade routes must be domestic, and there is no limit on the number of domestic trade routes that can go to any particular city.
In spite of their name, "trade" routes are not two-way, but one way. The city with a trade route gets benefit from its partner, but there is not necessarily any benefit the other way. In particular, it is possible to trade with a city that cannot trade back; this is fairly common for the first civilization to get to [Astronomy%20%28Civ4%29](Astronomy). You can also [Blockade%20%28Civ4%29](blockade) a civilization using [Privateer%20%28Civ4%29](Privateers) so that it cannot trade "out" while your trade still comes in.
Seeing Trade Routes.
A city's trade routes can be seen in the city screen, on the left. They are labeled using the partner city. You can mouse over each trade route to get a tooltip, which will show how its value is computed.
Number of Trade Routes.
Each city has a maximum number of trade routes, which is determined as follows:
Usually every city will get its maximum number of routes. However, a city may not get its maximum number of routes if it does not have trade connections with at least that many cities. In particular, especially early in the game a city may have "no" trade routes because it is not connected to any other cities.
Value of Trade Routes.
The commerce value of trade routes is computed from a base value, which then gets percentage modifiers. Trade routes values are computed down to .01 commerce, so that rounding effects will be minimal.
The base value in [commerce](commerce) of a trade route in city "From" to a partner city "To" on a map of size "mapsize" is computed as follows:
 base_value = max(1.0, min(pop(To)/10, dist_factor(mapsize)*plotDistance(From, To))
where:
Put in English, what that equation encodes is as follows:
The base value is then multiplied by a factor that has a base of 100%, with the following additions:
[Vassal%20State%20%28Civ4%29](Vassal) cities count as foreign for this purpose.