# Happiness (Civ2)

Happiness in "[Civilization%20II](Civilization II)" is a mechanic that determines the general satisfaction of s within a given . In addition to its contribution to [%23Scoring](game score), maintaining happiness is important for a 's internal stability. When citizens are unhappy, city [%23Civil%20disorder](shuts down), and the population is more susceptible to ; under , sustained riots will trigger . Conversely, happy cities provide [%23We%20Love%20the%20King%20Day](improved production), and are more resistant to subversion.
Happiness is chiefly managed through two tracks: mitigation of unhappiness with [%23Improvements](improvements) and [%23Wonders](Wonders), and promotion of happiness via [%23Luxuries](luxury spending). The provides an at-a-glance overview of the empire's happiness.
Happiness levels.
Each citizen working a is coloured to one of four ranks of happiness, ordered left to right in the :
Modifiers generally raise a citizen's happiness to the next available level: Angry to Unhappy, Unhappy to Content, and Content to Happy. However, [%23Luxuries](luxuries) prioritize converting Angry citizens directly to Happy.
s are not subject to happiness.
Happiness factors.
Happiness is determined by a number of factors, some specific to individual cities, and some applied across the civilization. Modifiers are applied in a sequential order, listed here as they appear in the 'Happy' window of the city screen:
Difficulty and empire size.
The player's determines cities' base level of contentment before unhappy citizens appear:
A civilization controlling many cities experiences additional unhappiness. The base "riot factor" is defined by (14 in a standard game), modified by difficulty, , and size. The more cities a civ controls beyond this optimum, the greater the unhappiness across the empire; this is the principal source of  [%23Happiness%20levels](Angry) citizens.
 uniquely disregards sprawl-related unhappiness entirely, while [%23Fundamentalism](Fundamentalism) overrides its effect.
Luxuries.
Happy citizens are primarily earned through . For every two luxuries generated in the city, one citizen becomes ; if no content citizens exist, luxuries instead make one citizen , or one citizen .
The proportion of   devoted to luxuries is determined by the civilization's . including s, s, and s increase a city's net Luxury output by 50% each; do not increase luxuries directly, but boost the city's revenue. Luxuries can also be generated locally by s: each supplies 2 Luxuries.
Improvements.
Several work to reduce unhappy citizens, with certain s increasing their effectiveness:
Government.
In addition to mitigating unhappiness from [%23Difficulty%20and%20empire%20size](city sprawl), different s provide specific happiness-related effects that can be beneficial or deleterious:
Martial law.
"Military" governments (, , , and ) feature martial law: up to three stationed in a city automatically suppress unhappiness, at a rate of -1 per unit. Under Communism, martial law is doubly effective (-2 per unit).
Democracy and Republic.
Under "civilian" governments ( and ), military units deployed in the field (not garrisoned in a city or occupying a within three tiles of an owned city) cause unhappiness ("war weariness") in their home city. Under Republic, each unit after the first creates one citizen; under Democracy, "every" unit creates "two" citizens. s and the mitigate war weariness.
Fundamentalism.
 completely eliminates unhappiness within the civilization, at the cost of significant penalties to production. Happiness-related improvements (, , ) have their costs waived, instead providing equal to the number of citizens they placate.
Wonders.
Happiness-related s can be divided into two groups: Wonders that modify or substitute for , and Wonders that provide happiness directly.
Celebration and Disorder.
At sufficient happiness or unhappiness, a city will host a celebration in the leader's honour or descend into disorder, respectively. Celebration and disorder are calculated at the start of the player's turn, and will persist for as long as their conditions are met. If enabled in , notification popups are issued when a change in happiness status occurs.
Civil disorder.
Civil disorder occurs when a city's / citizens outnumber its citizens. During disorder, economic activity (, , ) is suspended, although is still stockpiled. Cities in disorder are also cheaper to .
 governments are uniquely sensitive to unrest: if any city is experiencing disorder within two consecutive turns, the government collapses into .
We Love the King Day.
"We Love the King Day", also known as celebration and abbreviated WLtKD, occurs when at least half a city's population is and no / citizens are present. A city requires a minimum population of 3 to celebrate. During celebration, the city experiences a production bonus based on its government type:
Scoring.
Happiness directly influences the player's . Each citizen supplies 2 points, and each or // Specialist citizen supplies 1. and citizens provide no points.
Civilopedia entry.
&lt;br&gt;
Once you have built a certain number of cities, your citizens start to worry about your ability to effectively govern your civilization. When this occurs, additional unhappy citizens appear in each city.
The number of cities you can build before causing additional unhappiness is based on a number of factors, including game difficulty level and government type. The number of cities is higher for more advanced governments and lower levels of difficulty.
Modding.
Cities' default unhappiness threshold is defined at Line 8 of the section in , while the "riot factor" for empire size is defined at Line 9. In "", citizens' score value can be customized on Line 23; the given integer is the bonus from Content/Specialists, and is doubled for Happy.
Most other happiness mechanics are hard-coded. Certain s modify the effects of city improvements: s only work if a civ possesses and/or ; s are boosted by ; and and increase and decrease s' effect, respectively.
War weariness from under [%23Democracy%20and%20Republic](civilian governments) varies based on their : Air Superiority units do not cause unhappiness, while all other types continue to incur unhappiness even when stationed in cities.