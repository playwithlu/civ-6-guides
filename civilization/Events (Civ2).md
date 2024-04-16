# Events (Civ2)

This page is provided for historical reference purposes.
Civilization II® from Microprose® initially did not start with a macro(event)language. Civilization II started out with scenario (.scn) files . These are basically savegames with the initial setup (maps, units, city placements, civs in place etc..). The macro(event)language was gradually added to Civilization II by the developers in later releases.
The first use of events started with the release of the datadisk Conflicts in Civilization. This was further improved in Fantastic Worlds and finally in Civilization II - Multiplayer Gold Edition.
All the text which follows pertains to Civilization II - Multiplayer Gold Edition events.
Tutorial.
There are two distinct components of the event system, a "trigger" and an "action". A "trigger" argument must be satisfied to cause an "action" to happen. Consider that the input. An "action" is what happens after the "trigger" is satisfied. Consider that the output.
An "event" declaration starts with an @IF statement and ends with a @ENDIF statement. An "event" looks like so:
 @IF
 CITYTAKEN
 city=New York
 attacker=British
 defender=Americans
 @THEN
 JUSTONCE
 TEXT
 New York has been captured by the British! France declares war on the British!
 ENDTEXT
 MAKEAGGRESSION
 who=French
 whom=British
 @ENDIF
Explanations of the trigger or action will be written in parentheses.
A (***) sign signifies a quirk with an explanation at the bottom of this post.
Triggers (@IF Triggers:)
1) Unit Killed:
 @IF
 UNITKILLED
 unit=Settlers (the unit that is to be killed to trigger)
 attacker=ANYBODY (***) (which civ is attacking the unit)
 defender=Romans (the defending civ)
2) City Taken:
 @IF
 CITYTAKEN
 city=New York (the city captured)
 attacker=British
 defender=Americans
3) Turn Number: (Cannot be used in the same Trigger as "Turn Interval")
 @IF
 TURN
 turn=1 (Actual turn in the game, not the date.)
4) Turn Interval:
 @IF
 TURNINTERVAL
 interval=5 (Number of turns elapsed before the trigger is triggered)
5) Negotiation:
 @IF
 NEGOTIATION (***)
 talker=British (the civ who would be contacting)
 talkertype=HumanOrComputer (whether the civ "talker" is human or AI)
 listener=Americans (the civ who would be contacted)
 listenertype=HumanOrComputer (whether the civ "listener" is human or AI)
6) Scenario Loaded:
 @IF
 SCENARIOLOADED (Upon loading the scenario Trigger will set off Event)
7) Random Turn:
 @IF
 RANDOMTURN
 denominator=10 (random number that must be picked to cause an event)
8) No Schism:
 @IF
 NOSCHISM
 defender=Romans (Prevents a civil war in the defender civ. The "ANYBODY" value may be used just once here to prevent all civs from having civil wars - usually caused by their capital falling***)
9) Received Technology
 @IF
 RECEIVEDTECHNOLOGY
 technology=0 (Numerical line in the rules.txt file that denotes a certain tech)
 receiver=ANYBODY (Who has received the tech)
Actions (@THEN Events:)
1) Text Pop Up Window
 @THEN
 TEXT
 Test Text (Text that will pop up when Event is Triggered)
 ENDTEXT
 @ENDIF
2) Move Unit
 @THEN
 MOVEUNIT (***)
 unit=Settlers (the unit that will be moved)
 owner=Romans (the owner of the "to be moved" unit)
 maprect
 15,15,0,0,0,0,0,0 (The coordinates of the tile that the unit is standing on)
 moveto
 20,25 (the destination tile coordinates)
 numbertomove=2 (The number of identical units to move)
 @ENDIF
3) Create Unit:
 @THEN
 CREATEUNIT
 unit=Warriors (the unit to be created)
 owner=Romans (the owner of the "to be created" unit)
 veteran=no (Whether or not it will be a veteran)
 homecity=New York (The created unit's home city)
 locations
 15,50 (1st and only location that it will be created)
 15,10 (2nd location it will be created if 1st location is occupied by enemy)
 15,12 (3rd location it will be created if 2nd location is occupied by enemy etc...)
 endlocations
 @ENDIF
4) Change Money:
 @THEN
 CHANGEMONEY
 receiver=Romans (The civ who will have the amount added into the treasury)
 amount=100 (the amount of the additional funds - can be negative to subtract funds)
 @ENDIF
5) Play Sound:
 @THEN
 PLAYWAVEFILE
 TEST.WAV (the wave file to be played)
 @ENDIF
6) Make Aggression:
 @THEN
 MAKEAGGRESSION
 who=Babylonians (who will be attacking or just declaring war)
 whom=Romans (who will be attacked or declared war on)
 @ENDIF
7) Just Once:
 @THEN
 JUSTONCE (signifies that the event will be triggered only once in the game)
 @ENDIF
8) Play CD track:
 @THEN
 PLAYCDTRACK
 15 (Track number to be played on CD in CD-ROM drive - used with Civ2 CDs mostly)
 @ENDIF
9) Don't Play the Wonder Movies:
 @THEN
 DONTPLAYWONDERS (Used if the Wonders have been changed and the author doesn't want the .avi moviews to be played)
 @ENDIF
10) Change an area of terrain tiles to another kind of terrain:
 @THEN
 CHANGETERRAIN
 terraintype=0 (Line number of terrain type in rules.txt)
 maprect
 15,20,0,0,0,0,0,0 (Coordinates of the area that will be changed. Each of the four sets designates a corner of a polygon on the map - Use the coordinates of one tile four times to designate that only one tile will be changed.)
 @ENDIF
11) Kill a civ:
 @THEN
 DESTROYACIVILIZATION
 whom=Aztecs (The civ that will be destroyed. Can be used in the context of "Kill the first vampire, kill all the vampires" sort of way.)
 @ENDIF
12) Give tech:
 @THEN
 GIVETECHNOLOGY
 receiver=Romans (Who will receive the tech)
 technology=2 (the line number that the tech is on in rules.txt)
 @ENDIF
"This page contains material from the Freeciv Wikia at [w%3Ac%3Afreeciv%3ACivilization%20II%20events](w:c:freeciv:Civilization II events). That Wikia says it is under the GPL but does not explain what conditions, if any, apply to copying of the material. Modification of this page is perhaps not permissible.