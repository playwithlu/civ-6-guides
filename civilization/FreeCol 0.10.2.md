# FreeCol 0.10.2

[FreeCol%20versions](FreeCol version) 0.10.2 was released on 5 September 2011. See http://www.freecol.org/news/releases.html. Fixes many bugs, should be compatible with all versions from 0.9.x. 
Still not perfect. 
Job selection.
For example, a right-click on a colonist may fail to offer all the jobs that he can do:
If you drag him to a tile you want him to work, and right-click again, you generally get the option of what you want him to harvest there. However, there is a high probability that the program wil flip him to another, poorer, tile when you click the option. So keep an eye on him and drag him back if necessary!
End of turn.
A relatively new feature may pop up at the end of a turn inviting you to reconsider units that might be able to move further. Excellent idea. It will be excellent in practice when it manages to avoid wasting your time asking about units that cannot move in any way, notably ships under repair but commonly also units that have only one movement point left but are surrounded by hills, mountains, or other "2-movement-point" tiles.
Roads.
The depiction of roads differs considerably from the 0.9.x versions. Instead of a wavy brown line joining the middle of the tile to a corner or to the middle of a side, there is now a dead straight line from the middle of the tile if there's only one adjoining road but a geometrically-precise curved line (or more than one) if there are two or more, often not reaching the middle of the tile and consequently risking being totally hidden behind forests to the south-west or south-east. 