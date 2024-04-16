# Mathematics of Civilization V

This article presents some of the mathematics of "Civilization V". It was originally published by [http%3A//forums.civfanatics.com/member.php%3Fu%3D97123](alpaca) at the [http%3A//forums.civfanatics.com/showthread.php%3Ft%3D389702](CivFanatics forum). Notice that this article represents the state of the game "before the [December%202010%20patch%20%28Civ5%29](December 2010 patch)"!
Updated on 6/13/2015: Unit Maintenance updated to reflect the actual formula in the DLL - monju125
Calculating Culture.
Border growth.
The cost of a border growth is, with t the number of tiles already claimed
formula_1
Formula for Social Policies.
The first thing we need to know when talking about anything [culture%20%28Civ5%29](culture)-wise is how to calculate it. From the game core XML files and in-game observations, it works like this: You calculate a base cost that depends on the number of policies, then multiply with a factor that depends on your number of cities. As follows:
formula_2: The number of cities in your empire
formula_3: The base cost of policy k. Depends "only on the number of policies"
formula_4: The cost factor depending on the number of cities in your empire
formula_5: The total cost of policy k. Depends on both the number of cities and policies already unlocked
The policy cost has to be modified depending on your difficulty setting, game speed and map size. I took the numbers from a post by Yamian. Define these modifiers as:
formula_6: The "game speed" modifier (3 for marathon, 1.5 for epic, 1 for normal and 0.67 for quick)
formula_7: The "difficulty" coefficient (0.5 for settler, 0.67 for chieftain, 0.85 for warlord, 1 otherwise)
formula_8: The "map size" modifier (0.3 for normal size and below, 0.2 for large, 0.15 for huge)
formula_9
formula_10
The policy cost scales linearly with the number of cities and exponentially with the number of policies. These factors are combined by multiplication, so the total cost is simply:
formula_11 rounded to the next multiple of 5
How fast do I acquire new policies?
This is very simple, and I'll just list it here to introduce some variable names. It depends on the culture your empire yields. With
formula_12: The total culture yield of your empire
formula_13: The cost of your next [social%20policy%20%28Civ5%29](social policy) (I will omit the dependencies for readability)
formula_14: The time in turns to unlock the next policy
we get the simple formula
formula_15
if we assume we just unlocked a new policy. If we introduce
formula_16: The culture already accumulated in the culture bucket
we get
formula_17
How do I calculate the total culture in my empire?
This is shown in the UI but again to introduce some concepts. Let
formula_18 : the average culture of each city in your empire
It makes sense to split c up into a part that depends on n and represents your "typical city culture", the culture each city you newly create will add to your empire, and a part that is constant in n and represents bonuses from wonders, landmarks and city states. This is exact if you immediately buy your typical culture buildings but normally it's an approximation (it represents an equilibrium you will not normally have reached)
formula_19: The typical culture per city
formula_20: The city state culture
formula_21
Before I continue let's look at the policy speed for large numbers
formula_22
formula_23
Also:
formula_24
So for large n, the average amount of culture per city is a good measure for the policy speed.
Will expanding increase or decrease policy speed?
This is the question Paeanblack and I discussed in said thread. To analyse this, we have to calculate the number of turns to the next policy and see how it's affected by going from n-&gt;n+1.
When we do the city number increase, both p and c change. Let p and c be the policy cost and culture yield before founding the new city and p' and c' be the respective numbers after the founding.
formula_25
formula_26
Then calculate t' and check when it gets smaller than t (this would signify an increased policy speed)
formula_27
formula_28
formula_29
formula_30
formula_31
For standard-sized maps, formula_32 so
formula_33
So if the base culture from city states is less than 7/3 times larger than the typical city culture (let's call this the culture ratio r_c), you will get an increased policy speed from expanding. If it's exactly equal to this, the speed will stay the same, and if it's more, policy speed will slow. It should be noted that, no matter the value of r_c, for large numbers of cities the increase or decrease for founding an additional city will be very small.
For larger maps, this will be a little different.
Numbers.
Now we can plug in some example numbers into our calculations. I will discuss the results only for the standard map size
To sum up, expanding will in almost all cases slow down your social progress. The only cases where it will speed it up are if you either aren't interested in city states and wonders, or if you play a civ with a culture bonus. The only somewhat realistic scenario where expansion could speed up your policy gain is in my opinion if you play Songhai because you'll really want the Mud Pyramid and a Monument isn't that expensive.
I'm not sure if city state bonuses scale with the map size but if they don't, expansion increasing your policy speed is a lot more likely on larger maps, probably happening at some time if you just have a monument and a temple or are playing France. If you play Songhai, or France with temples it will even happen pretty often in fact. This is another case where the game doesn't scale well (well in the sense of preserving the same effects on gameplay as on standard size) with map size.
Food.
Food cost.
The food cost for a city to grow is calculated as follows
formula_2: The number of citizens in the city
formula_35: Amount of food to grow to size n+1
formula_36
Comment: It is OUTDATED! [https%3A//forums.civfanatics.com/threads/new-city-growth-formula.403114/](Patch on Dec 2010). Now the formula is:
formula_37
Need to edit everything below.
Code:
What this means is that growing from size 5 to 6 costs 51 food, while growing from size 10 to 11 already costs 122 food. I would like to present a few ways of looking at this problem from different angles in the following.
Constant Food Surplus.
This simplification assumes that each new citizen will work a tile that's worth 2 food and you therefore have a constant amount of food surplus that is put into growth. For a normal city without any bonuses, the amount of turns you need to grow is simply given by
formula_38
where n is the number of citizens, f the food surplus and t the number of turns until growth, assuming you start at 0 food. Let's look at the numbers for df = 8
Code:
This kind of explains why growth feels so slow once you hit the teens: The number of turns cities need to grow becomes pretty large, even with a pretty decent food surplus. A city takes about the same time to grow from size 12 to 13 as from size 1 to 5.
Constant food per citizen.
Here, the assumption is that each citizen will yield a certain mean amount of food. To understand what happens there better, let's define another function, the average growth cost per citizen
formula_39
The last term is approximately n^0.8 and dominates for large n. As you can see, this function has a minimum at size 4 (about 3.75 in the continuous case) and then constantly grows a little less than linearly - but linear growth is an excellent approximation.
As you can see below, the function 0.41 n + 8.18 fits the data over this range perfectly but is much simpler (the functions agree at all integer places).
So how do you interpret this function? What it tells you is that, with a constant amount of food produced per citizen, your city will grow more quickly than before until it hits size 4, and then starts slowing down again. Or, to put it more simple, this function tells you the amount of food each citizen has to produce to let the city grow.
An alternative, but equivalent, point of view is that, if you're aiming for a constant city growth speed, each citizen has to become more efficient as your city grows, in an approximately linear function.
You should note that the amount of food generated per citizen will usually be larger for small cities due to the city square itself (especially with maritime CS).
Slightly more realistic.
Cities start with a center square that yields some food (this catches granary, maritime [City-state%20%28Civ5%29](city-states) and water mill food, too). So the assumption that the amount of food per citizen will stay the same isn't really completely applicable. So let's introduce a new variable, f_csq, the city square food amount.
The assumption of an average amount of food per citizen now makes sense if you leave the city square food out. So let's call the amount of food each citizen generates f_c. The total food per turn, f, is then given by
formula_40
More interesting for us is the food surplus. This is given by
formula_41
The amount of surplus food produced per citizen is then
formula_42
To get the number of turns we need for growth, we need to combine this with the food growth cost and get
formula_43
Since this function doesn't read too pretty, I'll just plop in some numbers and give you a graphical representation. Let's say f_csq = 2, which is the case if you don't have city state allies. If the city is to grow in a reasonable amount of time, f_c should be greater than 2.5, as you can see below
You will notice a local minimum evolving in the f_c = 4 case, which signifies the onset of the constant food per citizen approximation, which is the limiting case for f_csq = 0
Are granaries worth it?
Ultimately, that's for you to decide. I can give you some information so you can make an educated decision, though. Granaries increase f_csq from 2 to 4, so let's look at what happens to t if we make that change. Dashed are the values without granary, the full lines are with a granary
More useful to judge the granary's effects is looking at the difference between the case without a granary, and the case with a granary
As you can see, the difference quickly becomes essentially constant at a city size of 10 or more for any case of f_c &gt; 2. From this analysis, I'd say that for f_c values up to 3, a granary is generally worth it, because it saves you a turn or two per growth step. For f_c = 2.5 it's very much worth it, and this seems to be a more realistic case than the higher values because not every citizen will work a farm (the f_c = 4 case represents each citizen working a Civil Service/Fertilizer farm) and some won't produce any food at all, like specialists.
Other f_csq effects.
We can continue this analysis by increasing f_csq in steps. For example, a maritime CS will yield 2 extra food, as will a water wheel. Let's see what happens if we go from f_csq = 4 to f_csq = 6. I will omit the more unrealistically high cases from now on for a better overview. Shown is again the total number of turns needed and the difference between 4 and 6. This time, f_csq = 4 is dashed
So getting the second city-state isn't as good as getting the first, and getting a granary when you already have a city-state isn't so great, either. It still shaves off a turn (or three in the f_c = 2.5 case), though.
The next increase step, from 6 to 8 (the "before" being dashed as usual)
Now things start becoming somewhat underwhelming. As I said, if things are worth it for you is up to you to decide, but I'd definitely not build that water mill if I already have a granary and a city-state ally because the difference will only be something like two turns in three growth steps or so, which isn't exactly a lot.
f_c values &lt; 2.
After reading a comment from ehrgeix, I think it makes sense to extend the analysis to f_c values that are smaller than 2. The values greater than 2 are applicable if you want to let your city continue to grow for the rest of the game. Values smaller than 2 still make sense in transitionary periods, if you want a growth cap, or if you're fine with your growth speed slowing down even more than in the constant food surplus case discussed above.
Qualitatively, we can already see from looking at formula_44, which occurs as the denominator in the formula for t, that these functions will have a pole at a finite n, because f_c - 2 becomes negative. The locus of this singularity is given by formula_45. This singularity signifies the number of citizens where the city stops growing.
In the following are some graphs in the same way as above. First, f_csq = 2
If you increase f_csq you shift the position of the pole to the right, so the difference between t(csq = 2) - t(csq = 4) has a singularity at the same points as t. See the f_csq = 4 case below. Dashed is the "previous", in this case f_csq = 2
f_csq = 4 -&gt; f_csq = 6
f_csq = 6 -&gt; f_csq = 8
Unit maintenance.
As of 6/2015, the formula for unit maintenance as defined in all versions CvGameCoreDLL is calculated as follows:
 final cost = (n*b(1+g*m)/100)(1+(g/d))
Unit cost modifiers from traits are applied before the exponent. Unit cost modifiers from policies, handicap, and AI difficulty level are applied to the final cost.
Since there's no easy "each unit in turn t will cost this much" here's a table you can use as a rough reference. The first row is the number of turns, the first column the number of units
Here's an equivalent table detailing the cost per unit