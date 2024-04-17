# Health (Civ4)

Health, {{Health4}}, is "a condition in which someone or something is thriving or doing well." In "[Civilization%20IV](Civilization IV)", health is an attribute of [City%20%28Civ4%29](cities). It is a game mechanic that serves as a soft limit on their growth. 
Seeing health.
The health of each city is encoded as two small integers. One is a sum of all of the positive contributions to that city's health. This number is usually what people mean when they talk about a city's health. However, we refer to it in this article as the city's health limit. Health comes from many sources: the city's site, [List%20of%20buildings%20in%20Civ4](buildings), [List%20of%20wonders%20in%20Civ4](wonders), and [Resource%20%28Civ4%29](resources).
The other integer is a sum of all of the negative contributions to the city's health, that is, its unhealthiness. Unhealthiness mostly comes from [Population%20%28Civ4%29](population), but some buildings and resources cause it.
You can see the health limit of a city, and its unhealthiness, on its city screen, in the upper right of the screen just to the right of the food bar. The health limit is shown first, with a {{Health4}} symbol. The unhealthiness is shown with a {{Unhealthiness4}} icon. In between is a ](", "=", or "&lt;" sign, depending on the numbers.
Effect.
There is one important effect of health: when a city's unhealthiness is greater than its health limit, each point of population above the health limit eats 3 {{Food4}} apiece, instead of the normal 2 {{Food4}}. When a city has at least one point of population above the health limit, it is unhealthy, and it is shown on the main [Map%20%28Civ4%29](map) with a greenish haze around it.
There is also a minor effect of health. An unhealthy city is not eligible to have a "[We%20Love%20the%20King%20Day%20%28Civ4%29](We Love the King)" celebration.
Computing unhealthiness.
A city's unhealthiness is largely a function of its population: every city gets +1 {{Unhealthiness4}} for each point of population. There is one exception: there is no unhealthiness from population for if the city has built the [National%20Park%20%28Civ4%29](National Park) wonder. Additional unhealthiness is caused by buildings, and the city's site.
Unhealthy sites.
Both floodplains and jungle in the city's [big%20fat%20cross](big fat cross) cause unhealthiness, as follows:
The total unhealth caused must be an integer, and is computed by summing the features' unhealth and rounding down the total. Thus, a city with two floodplain tiles and three jungle tiles has a health malus of 0.4 {{Unhealthiness4}} * 2 + 0.25 {{Unhealthiness4}} * 3 = 1.55 {{Unhealthiness4}}, which is rounded down to 1 {{Unhealthiness4}}.
Unhealthy buildings.
Some buildings give a health malus to their city. These are listed here.
When cities have access to [Power%20%28Civ4%29](Power), they also get +2 {{Unhealthiness4}}. If the power is from coal, it causes +4 {{Unhealthiness4}}. 
Computing the health limit.
Here is how the health limit is computed. All cities get a base health limit, based on the [Difficulty%20level%20%28Civ4%29](difficulty level) of the game. To this base level are added bonuses from the site, buildings, wonders, and resources.
Site bonuses.
There are several significant health bonuses available for cities based on their siting. First, a city built on any tile with [Fresh%20water%20%28Civ4%29](fresh water) gets +2 {{Health4}}. Another bonus that is not obvious is that only [Coastal%20%28Civ4%29](coastal) cities can build [Harbor%20%28Civ4%29](Harbors), and thus avail themselves of extra health bonuses for seafood. Since almost all coastal cities will eventually build a Harbor, and you'll usually have access to all three seafoods eventually, this means that in effect coastal sites get +3 {{Health4}}.
One other bonus coming from a city's site is the +0.5 {{Health4}} from each [Forest%20%28Civ4%29](forest) in the city's [big%20fat%20cross](big fat cross). This bonus is rounded down, so in general it is best to keep even numbers of forest tiles in a city.
Resources and buildings.
All [Resource%20%28Civ4%29%23Food%20Resources](food resources) give +1 {{Health4}}. Some other types of resources give health, but only in combination with buildings.
Many buildings give a health bonus to their city. Some require certain resources for this; others give their bonus unconditionally. Here is a listing of non-unique buildings giving health.
In addition, [Hydro%20Plant%20%28Civ4%29](Hydro Plants) and [Nuclear%20Plant%20%28Civ4%29](Nuclear Plants) provide clean power, which will negate the unhealthiness effect of a Coal Plant in a city if there is one. [Recycling%20Center%20%28Civ4%29](Recycling Centers) negate "all" unhealth from buildings.
Wonders.
The [Hanging%20Gardens%20%28Civ4%29](Hanging Gardens) wonder gives a bonus of +1 {{Health4}} to every city in its [List%20of%20civilizations%20in%20Civ4](civilization).