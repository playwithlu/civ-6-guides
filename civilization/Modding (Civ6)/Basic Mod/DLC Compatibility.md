# Modding (Civ6)/Basic Mod/DLC Compatibility

Sometimes when you are making changes to the game, you need to make sure that your mod will work with other mods. Some people might have other mods or not have a DLC (which the game interprets as a mod,) and you want to make sure that your mod will work for your user no matter what they have.
Sometimes its obvious that your mod is an addition to another mod/DLC and it requires the other to be loaded. Otherwise, in many cases you can add some basic mod compatibility into your mod using SQLite Triggers. These are pieces of code that will only be run after something you specify happens. Create a new SQL file for your mod project. Here is the command we will be using:
codice_1
codice_2
codice_3
codice_4
codice_5
codice_6
Let's look at how this statement is constructed:
codice_7 This just creates the trigger and assigns it a name. Make sure the name is unique.
codice_2 This is what causes the trigger to be fired and when to perform the operation. In this case, the trigger fires after a new row is inserted into 'Table'. Alternatively, you can have the trigger do something before the operation occurs, with BEFORE INSERT ON Table. You can also have the trigger fire before/after an UPDATE on the table, but in the case of mod compatibility its usually after inserts.
codice_3 This further specifies that the trigger should only fire when the new row inserted into the table has a value of A for column 'Column1'.
codice_10 These are the statements you want to execute when the conditions for the trigger are met. The statements can include the usual basic queries:
codice_11
codice_12
codice_13
Example 1 (Mod): Lets say we are removing missionaries from the game, just like in the example for removing base game content. Many people have another mod that adds a bunch of cool stuff to the game. However, one part of this mod also adds missionaries to a new ability class. If people try to load this mod and our mod at the same time, it won't work because we deleted the missionary data from the game tables in our mod! We can solve this issue by having SQLite triggers handle the inserts of the other mod:
codice_14
Now with these triggers, people who have your mod enabled will also be able to load the other mod and enjoy all of its other features.
Example 2 (DLC): Lets say that we are adding a unit with a new type of ability class. Most of our mod deals with base game content, but for our new unit's ability class, we want to give it the ability to receive the Spear of Fionn ability from going next to the natural wonder. However, this is a wonder that was added in a DLC. If we just add this directly to our mod, then users of our mod that don't have the Vikings DLC won't be able to load the mod! We can handle this with an SQLite trigger:
codice_15
Now people with the Vikings DLC will have the new unit able to gain this ability, while people without the Vikings DLC will still be able to load your mod and enjoy its other features.
It takes some digging through the other mod's files and some testing to make your mod compatible with it, but its worth it if people can use your mod with other mods that they enjoy.