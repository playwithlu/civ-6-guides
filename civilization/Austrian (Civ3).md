# Austrian (Civ3)

The Austrian people represent a [Civilizations%20%28Civ3%29](civilization) that was slated to appear in "", but was cut from the game before its release. They are led by [Charles%20V%20%28Civ3%29](Charles V). Because of a hardcoded civilizations limit, another civ must be replaced with Austria to play as them.
The leader portraits, [List%20of%20units%20in%20Civ3](unit) images, and [Civilopedia](Civilopedia) entries are included with "Civilization III: Conquests", but were not implemented in the finished software.
How to.
So the first step is to open the editor. (Civ3ConquestsEdit.exe)
Go to Civilizations Tab. Open the dropdown menu of civs, click Sumeria. Hit Rename and type in Austria. You now fill in the settings.
To get the traits that were intended, go to the Conquests root, then Text, then pediaicons.txt. It says Militaristic and Industrious. You can use these same traits, or choose others, up to you. The techs are not binded literally to the traits, so on the right, you see Free Techs. You put the usual free techs there that the traits receive (Warrior Code/Masonry). 
Put the civ entry as RACE_AUSTRIA in the middle of the page. Put the Index as 32, instead of -1.
Set Culture Group as European for the city graphics.
You can change the team colours at the bottom to something else, or leave it as the Sumerian one.
Bottom left are the Flics, or the animations you see of the leaderheads in the player setup and diplomacy. This is the most crucial part besides the entry for getting it to load ingame without crashing. In Conquests/Flics is where the files are located. I'll go from ancient to modern here. Make sure the drop down menu is on the era you want.
Art\Flics\X2_Charles_ancient_fwrd.flc
Art\Flics\X2_Charles_ancient_bwrd.flc
Art\Flics\X2_Charles_mid_fwrd.flc
Art\Flics\X2_Charles_mid_bwrd.flc
Art\Flics\X2_Charles_indust_fwrd.flc
Art\Flics\X2_Charles_indust_bwrd.flc
Art\Flics\X2_Charles_mod_fwrd.flc
Art\Flics\X2_Charles_mod_bwrd.flc
Reverse is Bwrd. Make sure each one goes in its proper slot. Of course, if you want Industrial animations in ancient, you could do that. 
Set the fav gov, title, name, adjective, build often flags as you want. But for Build Often flags, do not have more than 4 flags. The build often flags make the civ more unique between each AI. It's what dictates their city buildings behaviour.
You should replace the cities, military leaders and sci leaders, but up to you. You can leave what is there so it doesn't crash. I assume you want to at least change the cities. Just so you know, make sure you have it in the same layout as default, and do not leave extra spaces, otherwise that could cause a crash ingame.
Finally, go to Units Tab, and go to enkidus (near the bottom), and take it away as available for your civ by clicking it while holding CTRL. Now hit Add Unit, name Hussar. Give it what stats you want. I think 3 or 4 movement is what is wanted according to the civilopedia. 3 movement is standard for cavalry. Then probably 6 attack and 3 defense. Give it Saltpeter and Horses as required resources. Set it as available for your civ. In the Unit Abilities, Hold CTRL so you can pick the stats individually. The usual one used here is Start Golden Age. Set Prerequisite as Military Tradition. Set Shield cost as 80 or whatever desired. 80 is what usual cavs have. In Special Actions on the right, tick Load, Airlift, Pillage, Upgrade Unit, and Capture. Load, Pillage, and Capture are hard-coded for the AI Strategies to appear for Offense, which with Defense, makes the AI to use them as a unit. Civilopedia Entry is PRTO_Hussar. Give it Zone of Control too I suppose, since default cavalry have that. Icon is 188 (this is what shows in the city screen, but is not necessary for launching without error).
You would want to set the default Cavalry as not available for Austria (originally Sumeria). Set Warrior as available for Austria. Next find the Cossack unit. Set under the "Upgrade to:" box, as Hussar. Go ahead and tick Upgrade Unit on the right as well.
It is also necessary to assign leader images, otherwise, when you try to load them in the game, an error will pop up and the game will be forcibly closed.
To prevent this, go to PediaIcons.txt, here in each case you need to replace "SUMERIA" with "AUSTRIA" and "Gilgamesh" with "Charles_V". In some sections, Charles V is already assigned and it is not necessary to change them.
Civilopedia entry.
The Austrians are [Militaristic%20%28Civ3%29](militaristic) and [Industrious%20%28Civ3%29](industrious). They start the game with [Warrior%20Code%20%28Civ3%29](Warrior Code) and [Masonry%20%28Civ3%29](Masonry) and build [Hussar%20%28Civ3%29](Hussars) instead of [Cavalry%20%28Civ3%29](cavalry). 