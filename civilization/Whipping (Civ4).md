# Whipping (Civ4)

Whipping (sometimes called pop rushing) is an action that [Civilizations%20%28Civ4%29](civilizations) can perform while running the [Slavery%20%28Civ4%29](Slavery) [List%20of%20civics%20in%20Civ4](civic) in "[Civilization%20IV](Civilization IV)" and its expansions. It allows them to sacrifice a [City%20%28Civ4%29](city's) [Population%20%28Civ4%29](Population) for an immediate [Production%20%28Civ4%29](Production) bonus.
Preconditions.
A civ must be running the Slavery civic to whip. In Slavery, any city has the potential to whip. [List%20of%20wonders%20in%20Civ4%23Projects](Projects) are not whippable; the city must have a [List%20of%20units%20in%20Civ4](unit) or a [List%20of%20buildings%20in%20Civ4](building) at the top of the build queue. And finally, a city can whip only if it would not kill too many pop. A city is allowed to whip if the number of citizens required to finish the current build-queue item is less than or equal to half of the city's population (rounding fractions down).
How to Whip.
When a city is allowed to whip, the left "Hurry "X"" button will be active (lit up) when you select the city, and in the city's city view screen. The button has a tooltip that shows the amount of pop that will be whipped, and the duration of unhappiness. The tooltip does not show the hammers gained.
When the "Hurry "X"" button is active, you may click it to whip. Population is immediately killed, and hammers added to the current item in the production queue.
Conversion Computation.
Here is how the conversion of population into hammers in a city is computed.
Each citizen sacrificed is converted into 30 base hammers of production. This amount is scaled up or down by the [Speed%20%28Civ4%29](speed) of the game; on Epic, you get 45 base hammers per pop. The number of hammers that are added to the build queue are the base hammers times whatever production multipliers apply in the city with respect to the item in production. For example, if you have a [Forge%20%28Civ4%29](Forge) in a city and are building a unit, you have +25% production. If a whip uses 2 population, you would get
formula_1
hammers.
There are two circumstances when whipping is made less efficient. First, when you have zero hammers in the production box for an item, each pop gains only 20 base hammers. Thus, whipping should rarely be done without at least 1 hammer in the production box.
Second, although it is allowed, whipping is also made less efficient for producing [List%20of%20wonders%20in%20Civ4%23Wonders](wonders). When you whip a great wonder or the late-game national wonders (i.e., the [National%20Park%20%28Civ4%29](National Park)), you get just 15 hammers/pop (and just 10 hammers/pop if the production box is empty). When you whip an early-game national wonder (i.e., the [Globe%20Theatre%20%28Civ4%29](Globe Theatre)), you get 22.5 hammers/pop.
Effect of Whipping.
When you whip a city, the immediate effect is removal of the population and addition of hammers (as per the computation above) to the production of the top item in the build queue. Note that the addition is irrevocable and immediate, but the actual completion of the item cannot happen until the end of the [turn](turn). Thus, it is possible to get the hammers from a whip but to forestall the completion of the item by twiddling the queue.
With each whip, temporary [Happiness%20%28Civ4%29](unhappiness) caused in the city. Each time you whip, no matter how many or how few citizens were sacrificed, you get +1 for a while. The duration is 10 turns on Normal speed, but it is scaled by game speed. So on Epic speed, it is 15 turns, 7 on Fast, and 30 on Marathon. The unique building for the [Aztec%20%28Civ4%29](Aztecs), the [Sacrificial%20Altar%20%28Civ4%29](Sacrificial Altar), halves the unhappiness time for whips in Aztec cities with it.
Unhappiness caused by whipping "stacks" - that is, it adds to earlier unhappiness, causing additional unhappiness in the city. This is computed by simple addition of turns to the unhappiness counter, then scaling the whip anger based on the turns left of unhappiness. Each new whip adds 10 turns (scaled) to the unhappiness counter; the unhappiness caused in the city is simply the numbers of turns left, divided by 10 (scaled), and rounded up. For example, on Normal speed if you whip two times with two turns in between, you will see:
Turn 0: no on turn 0
 "(you whip)"
Turn 0: +1 for 10 turns
 "(end turn --&gt; whipped item is produced)"
Turn 1: +1 for 9 turns
 "(put new item in queue; end turn --&gt; item gets hammers)"
Turn 2: +1 for 8 turns
 "(you whip)"
Turn 2: +2 for 18 turns
 "(end turn --&gt; whipped item is produced)"
Turn 3: +2 for 17 turns
Turn 9: +2 for 11 turns
 "(end turn)"
Turn 10: +1 for 10 turns
Thus, even though the tooltip reports "+2 unhappiness for 11 turns", that is not really the case. Really it is +2 unhappiness for 1 turn, then +1 unhappiness for 10 more turns after that.