# Efficiency (SMAC)

Efficiency is analogous to [corruption](corruption) in "[Civilization%20%28series%29](Civilization)" games. The farther away a base is from your [Headquarters%20%28SMAC%29](Headquarters), the higher the proportion of [Energy%20%28SMAC%29](energy) is lost due to inefficiency. [Minerals%20%28SMAC%29](Minerals) and [Nutrients%20%28SMAC%29](nutrients) are not affected due to a lack of efficiency. If you have a large number of bases, you will also receive more [Drone%20%28SMAC%29](drones) at bases due to "bureaucracy". The less efficient the base, the more drones will appear. Efficiency is modified by the [Map%20%28SMAC%29](map) size. On larger maps, the rate at which efficiency drops due to distance from your Headquarters decreases, and the number of bases required to increase bureaucracy drones increases.
You have an Efficiency rating based on your policies in [Social%20Engineering%20%28SMAC%29](Social Engineering). Certain policies, such as Planned economics, decrease your overall efficiency, and others, such as Democratic, will increase it. A negative efficiency rating can wreck the energy production of a large empire as well as exasperate drones.
A [Children%27s%20Creche%20%28SMAC%29](Children's Creche), among other benefits, increases the efficiency rating of its base by 2. This makes it one of the most important facilities.
Consider relocating your Headquarters to a central position in order to increase efficiency.
The [Human%20Hive%20%28SMAC%29](Hive) is immune to inefficiency. This means if the efficiency rating is negative, it is treated as 0, allowing the Hive to run both Police State and Planned simultaneously without penalty - although any efficiency bonuses, such as from Knowledge, will be simply absorbed.
The number of cities and the size of map will have an effect on Efficiency. There is a threshold, and once you pass that, the actual loss of energy and increase of drone will appear. A rule of thumb for this threshold is Huge Planet: 11 Bases. Large : 9. Standard : 6 . Small : 5 . Tiny : 3 Bases. 
The efficiency score ranges from -4 to 4. 
This addition of drones is Bureaucracy. The bureaucracy formula for drones is as follows: 
 BaseLimit = (8 - Difficulty) * (4 + Efficiency) * MapRoot / 2
 Difficulty = 0 to 5
 Efficiency = Efficiency score
 MapRoot = Sq. Root of # Map Squares / Sq. Root of 3200 (56.569)
The formula used to compute the energy lost to inefficiency by a base is: 
 Inefficiency = Energy * Distance / (64 - ((4 - Efficiency) * 8))
 Energy = Amount of energy produced by a base this turn
 Distance = Distance from Headquarters base
 Efficiency = Efficiency score (+2 for Children's Creche)
If the denominator reaches zero, all energy is lost to inefficiency.