# Corruption (Civ3)

Corruption in "[Civilization%20III](Civilization III)" is a mechanic that reduces the output of [Production%20%28Civ3%29](production) and [Commerce%20%28Civ3%29](commerce) in a [List%20of%20civilizations%20in%20Civ3](civilization's) [City%20%28Civ3%29](cities). Corruption that affects production output is called Waste, although its mechanics are otherwise exactly the same.
It is primarily affected by [Government%20%28Civ3%29](Government type), distance from the civilization [Capital%20%28Civ3%29](capital) and the total number of cities (relative to [Map%20%28Civ3%29%23World%20Size](World Size)). There are ways to reduce corruption and waste, either by connections to the [Trade%20network%20%28Civ3%29](trade network) or local [List%20of%20buildings%20in%20Civ3](city improvements) like the [Courthouse%20%28Civ3%29](Courthouse).
Corruption and Waste.
The total amount of corrupted Commerce and Production is governed by two types of corruption combined together to form total corruption for a particular city:
Distance Corruption.
Distance corruption is based on a particular city's physical distance in tiles from the nearest [Palace%20%28Civ3%29](Palace)-type structure. The following formula is used to calculate distance, which results in peculiarities:
formula_1
where formula_2 and formula_3 are the cardinal distance from the capital on a 2D plane. Instead of observing Pythagoras' theorem, the distance is simply found by counting tiles from the capital with diagonal distances counted as 1.5.
This raw distance is now an adjusted to determine an effective distance to the nearest Palace-type structure. For every anti-corruption improvement (Courthouses, [Police%20Station%20%28Civ3%29](Police Stations)) the effective distance of the city is halved. Additionally, being connected to the trade network and having a [Democracy%20%28government%29%20%28Civ3%29](Democratic government) also reduces distance corruption (while having a [Despotism%20%28Civ3%29](Despotic government) increases it). Distance corruption is ultimately scaled to World Size and has a cap. Waste is calculated the same way, except when the city is under celebration the effective distance is halved for Waste purposes (Corruption remains unaffected though).
Rank Corruption.
Rank corruption increases with the number of cities relative to World Size.