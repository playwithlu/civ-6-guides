# Healing (Civ4)

Healing is the process by which damaged [List%20of%20units%20in%20Civ4](units) regain their strength. 
Hitpoints.
Damage is tracked using a mechanism called hitpoints ([HP](HP)); all units have 100 hitpoints. When a unit is damaged, its hitpoints are reduced. A unit at 0 HP is destroyed. Units with between 1 and 99 hitpoints are damaged, and may be eligible to heal.
Healing via Promotions.
When a unit takes the Heal Instantly [Promotion%20%28Civ4%29](promotion) it immediately heals half of its total damage. That is, if it is at "HP" hitpoints, it will end up at:
 HP + 0.5 * (100 - HP) hitpoints
Promotion healing is an entirely separate mechanism from normal healing; the rest of this article describes normal healing.
Timing of Healing.
Healing takes place at the beginning of each [List%20of%20civilizations%20in%20Civ4](civilization's) turn. Thus, other civs will have a chance to attack a damaged unit before it can heal. Also, this means that fortified defenders who are attacked but not destroyed by an enemy get to heal in their own turn.
Eligibility for Healing.
A unit will only heal if it is damaged, and if it is eligible for healing. A unit with the [March%20%28Civ4%29](March) promotion is "always" eligible for healing, regardless of what it does during its turn.
For units without March, to be eligible to heal a unit may do very little in its turn. Specifically, performing any of the following actions render a unit ineligible to heal:
The following actions do not affect a unit's eligibility for healing:
Rate of Healing.
The rate that units heal can vary widely depending on many factors. These are described in this section. Healing rates are always calculated in hitpoints. Note that in a lot of Civ4 documentation you will not see healing rates given in hitpoints, but rather in percentages. Since all units have 100HP, using percentages is a way of describing the rate while hiding the hitpoint mechanism. 
A unit's heal rate is determined by adding its base healing rate to, if applicable, any medic healing and [Hospital%20%28Civ4%29](Hospital) healing. 
Base Healing Rate.
The base healing rate a unit gets varies depending on whether or not it is in a [City%20%28Civ4%29](city). In a city, eligible units will heal:
Otherwise (that is, not in a city), eligible units heal:
The terms "enemy", "neutral", and "allied" used above are defined as follows:
Medics.
Units that have [Medic%20%28Civ4%29](Medic) promotions (and also [Woodsman%20%28Civ4%29](Woodsman III)) have a healing effect. Such units are called medics. Medics operate on units based on where they end their move (since healing actually happens at the beginning of the next turn). Note that movement (and the many other things listed above) may make the medic unit itself in ineligible for healing, but it will not affect its ability to heal other units. A medic will heal all eligible units it its range, including itself. Medics of any kind can heal land, air and naval units. Medics will heal the units of an allied civilization.
The hitpoints healing by medics, and their range, are as follows:
Medics cannot heal units across a land/sea boundary. All units in a [Port%20%28Civ4%29](port) are considered to be on the land side of the land/sea boundary.
No more than one medic can operate on a unit eligible for healing each turn. If multiple medics are in range of a unit, then the one with the best healing rate for that unit will be used.
Hospitals.
A Hospital does not work in a city during resistance. Otherwise, the Hospital heals all eligible units on its tile +10HP. (Its tile is the city center tile of the city it is built in.) All units includes allied and neutral units. 