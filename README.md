# Overview
- **High Level Concept:** Dverentos is a 2D, looter RPG focused on account progression through dungeon crawling, grinding combat encounters, gathering resources, and upgrading your character and equipment.
- **Game Objectives:** It's a looter - the goal is basically to gear up to be able to take on harder challenges, which rewards you with better gear so you can take on even harder challenges. The goal of the game is what you decide to grind for, be that a specific piece of maxed out equipment, collectables, or just to be able to speedrun endgame content.

# Rank
- **Definition:** Rank is the primary measure of account progress. The following things contribute to Rank:
    - **Mastery:** All weapon Mastery is summed and added to Rank.
    - **Integrated Weapons:** When a weapon is fully integrated, all it's stats are summed and added to Rank.
    - **Integrated Components:** When a suit component is fully integrated all its stats are summed and added to Rank.
    - **Integrated Suits:** When a suit is fully integrated, all its stats are summed and added to Rank. In a sense, you are getting double Rank contribution from the components that you already integrated in order to integrate the suit. However this is balanced by the fact that the components cannot be sold or scrapped after being integrated into the suit.

# Stats
- **Vitality (VIT):**
    - Generally affects bodily strength and health
    - Sets base chemical damage resistance
    - Sets HP
    - Affects how quickly HP is recovered
    - Primarily affected by Reactor Core components
- **Constitution (CON):**
    - Generally affects restistance to adverse effects
    - Sets base energy damage resistance
    - Sets resistance to Statuses
    - Sets how much Durability your non integrated equipment loses when it's used
    - Primarily affected by Power Transport components
- **Strength (STR):**
    - Sets carry weight
    - Sets base kinetic damage resistance
    - Defines the threshold for how heavy a weapon you can carry
    - Sets how many inventory slots are available (max 64)
    - Primarily affected by Tensile Fibres components
- **Agility (AGI):**
    - Generally affects things related to speed and reaction time
    - During combat, AGI affects how fast the timeline moves (high agility makes you move quicker, meaning that the timeline moves slower)
    - Contributes equally to the Stealth skill along with PER
    - Some nodes will be locked behind an AGI check (you had to leap precisely to gain access to something)
    - Primarily affected by Actuator components
- **Dexterity (DEX):**
    - Generally affects things related to fine motor skills
    - During combat, DEX affects how many actions you can take across the entire timeline (high dexterity means you were able to use your hands more precisely and fit in more actions)
    - Some nodes will be locked behind a DEX check (it wasn't quite a lockpick, but you had to fiddle with a container to get it open)
    - Primarily affected by Nano Fiber components
- **Perception (PER):**
    - Generally affects the senses and awareness
    - Contributes to your chances of being able to leave a combat encounter without taking damage while fleeing
    - Contributes equally to the Stealth skill along with AGI
    - Contrbitues to the Threat mechanic where you may get a warning before an enemy appears on a quiet tile (high Perception gives you more warning and a chance to leave before the threat appears)
    - Some nodes will be locked behind a PER check, showing you that if the Stat had been higher, you would have seen the node and had access to it
    - Primarily affected by Sensor components
- **Intelligence (INT):**
    - Cleverness and insight
    - Charisma and speech related skills
    - Knowledge of technical topics and history
    - Some nodes will be locked behind a INT check if knowledge about some topic would realistically provide access to the node
    - Primarily affected by Neural Network components
- **Rationality (RAT):**
    - Logical reasoning
    - Systems thinking
    - Mental fortitutde and ability to stay calm under pressure
    - Some nodes will be locked behind a RAT check if reasoning and problem solving would realistically provide access to the node
    - Primarily affected by Logic Registers components

At all times, your stat totals reflect individual stat contributions from your equipped suit and components. Stats change as you swap out different equipment, and are not permanently increased

# Skills
Skills are separated into four subcategories: 4 gathering skills, 4 activity skills, and 4 crafting skills. Unlike Stats, Skills are permanent scores stored on the account. Generally speaking, exercising a skill levels it up. Each Stat also provides bonuses to two Skills. Some Skills provide permanent bonuses to other Skills.

- **Navigation**
    - Anything related to moving through environments
    - AGI provides a slight bonus
- **Stealth**
    - Stealth is a mechanic available on some tiles providing options to sneak past enemies or avoid detection
    - If the Threat mechanic causes an enemy to appear on a quiet tile, a Stealth check determines if you are detected
    - AGI provides a significant bonus
- **Combat**
    - Anything related to fighting enemies
    - STR provides a significant bonus
- **Hunting**
    - Hunting has the broadest range of encounters per location as you could be hunting anything from a small animal that is literally terrified of you and running away, to large dangerous animals which pose a large threat
    - The Hunting skill would also apply to bounty hunting if that ever gets added to the game
    - A fun detail is that some enemies when defeated and depending on the environment and circumstances will give Hunting XP, because it required a bit of a hunt to get them
    - PER provides a significant bonus
- **Recovery**
    - Anything related to using healing items
    - Increases when repairing armor
    - VIT provides a significant bonus
- **Salvaging**
    - Anything related to exploration, looting equipment, collecting resources, and dismantling items
    - This is the main skill that affects how much and the rarety of resources you get from collecting resources and dismantling items, balanced relatively against the level of the tile
    - DEX provides a slight bonus
- **Resources**
    - Metals and various minerals are vital components of every component, weapon and tool, so you mining will be involved in this game
    - This is the main skill that affects how much and the rarety of resources you get from mining resource nodes
    - INT provides a significant bonus
- **Alchemy**
    - Anything related to crafting and resource refining
    - Also somewhat related to protoform work (the raw material side of things)
    - This is not a throwaway skill. A completely viable way to play the game is to walk around in high level areas embarrassingly underlevelled and just continuously popping consumables to stay alive and win fights. If you have high Alchemy, you can craft all the consumables you need very economically.
    - If your Alchemy is high compared to the tier of consumable you’re crafting, you get advantages like bonus quantity crafted or higher tier of consumable crafted, if applicable
    - Equally increases chance of successfully decrypting a Protoform along with Cryptography
    - PER provides a significant bonus
- **Bartering**
    - Anything related to buying and selling items
    - Reduces or even eliminates special item taxes
    - PER provides a slight bonus
- **Lockpicking**
    - Many doors or containers are secured with a physical lock
    - While attempting to pick the lock, higher Lockpicking offers a higher chance of success
    - DEX provides a significant bonus
- **Cryptography**
    - Access to some areas are only available if you pass a Cryptography check (think of this as your hacking skill)
    - While hacking digital locks, a higher Cryptography skill offers a higher chance of success
    - Equally increases chance of successfully decrypting a Protoform along with Alchemy
    - RAT provides a significant bonus
- **Engineering**
    - Anything related to machinery and electronics
    - Similar to how certain areas are blocked by Lockpicking or Cryptography checks, Engineering checks can require a mechanical system to be repaired to open a door or container (it's a nontraditional third lockpicking/hacking type skill)
    - RAT provides a slight bonus
    - Increases when repairing weapons
- **Gunsmithing**
    - Anything related to crafting weapons
    - Certain weapon blueprints are locked behind a Weaponcrafting stat check
    - If your Weaponcrafting is high compared to the tier or weapon you’re crafting, you get advantages like better stats, higher rarity and even the possibility of crafting additional scraps or even an entire second weapon
    - VIT provides a slight bonus
- **Bladecasting**
    - Anything related to crafting melee weapons
    - CON provides a slight bonus
- **Neuralforging**
    - Anything related to crafting bodies and components
    - Certain component blueprints are locked behind a Neuralforging stat check
    - If your Neuralforging is high compared to the tier of component you’re crafting, you get advantages like better stats, higher rarity and even the possibility of crafting additional scraps or even an entire second component
    - INT provides a slight bonus
- **Armorcrafting**
    - Anything related to crafting armor
    - STR provides a slight bonus

# Mastery
- As you get kills with a weapon, you gain mastery in that weapon's archetype
- To integrate a weapon and no longer lose it on death, you spend some of your earned mastery
- Some weapon crafts and vendor sales are locked behind a Mastery 

# Weapon Categories
- **Carbine**
    - Assault rifle style class
- **Subcarbines**
    - SMG style rifle class
- **Lancers**
    - DMR style rifle class
- **Suppressors**
    - LMG style class
- **Handcannons**
    - Revolver/Pistol class
- **Breachers**
    - Slug shotgun heavy weapon class
- **Launchers**
    - Grenade/Rocket launcher class
- **Greatswords**
    - Big sword class
- **Knives**
    - Awesome knife sidearm class

# Range Mechanic
- Different weapons areeffective at different ranges.
    - **Close Range**
        - Lancers:      medium
        - Carbines:     medium
        - Subcarbines:  high
        - Suppressors:  high
        - Handcannons:  high
        - Breachers:    high
        - Launchers:    unusable (likely suicidal, 90%-99% max health dealt as self damage)
        - Greatswords:  high
        - Knives:       high
    - **Mid Range**
        - Lancers:      high
        - Carbines:     high
        - Subcarbines:  medium
        - Suppressors:  medium
        - Handcannons:  medium
        - Breachers:    medium
        - Launchers:    high
        - Greatswords:  unusable (0 damage)
        - Knives:       unusable (0 damage)
    - **Long Range**
        - Lancers:      high
        - Carbines:     medium
        - Subcarbines:  low
        - Suppressors:  low
        - Handcannons:  low
        - Breachers:    low
        - Launchers:    medium
        - Greatswords:  unusable (0 damage)
        - Knives:       unusable (0 damage)

# Tile Level
- Each tile has a level value set internally which defines:
    - Enemy difficulty
    - Environmental hazard check difficulty
    - Node access check difficulty
    - Rarity of loot dropped on the tile

# Bodies
- **Body Gameplay Loop:**
    - The bodies that you remotely control as you explore have fixed base stats and a specific name
        - In the lore, the body is actually a replicated body of an ancient Mindspawn which is why they have fixed starter components and base stats
    - Unlocking a new body permanently adds it to your account
    - Bodies are not found or bought in entirety, they are crafted by visiting a particular vendor tile and handing in 8 components which complete the blueprint for a particular body
    - After that, you receive the body which has its base stats, but has no components slotted in (they were consumed to make the body)
    - The base stats are still determined by the components used to craft the body, so because component stats are randomly rolled, different freshly crafted bodies get differently rolled stats
        - This creates an interesting situation where you may hold on to specific high stat components to craft a new copy of a body you really like, just to get high base stat rolls
- **Body Leveling:**
    - The body gains XP whenever an action is performed while wearing it
    - Each level provides a tiny stat increase
    - You can slot any components into a body as you level it
- **Body Integration:**
    - Fully integrating a body provides a significant stat bonus
    - Integrating a body locks in its 8 slotted components, so it is a commitment
    - Integrated Suits can be sold to vendors who will accept them
    - There is also a gamble mechanic to sacrifice a fully integrated Suit for a shot at high value rewards

# Components
- **Component Stats:**
    - Components don't have base Stat rolls. Components roll with random Stats with the Component's prime stat usually being the highest (for example, Reactor Core prime stat is VIT, Power Transport's prime stat is CON, etc.)
    - There is an unofficial tier system for Components:
        - Most roll with three stats
        - Fewer roll with four stats
        - Even fewer roll with five stats
    - There is a rare RNG which can cause any tier of Component to roll where it's prime stat is not its highest. In this "corrupted" scenario, the Component will actually have two other stats at quite high value within 3 of each other. These Components are extremely rare and valuable with the potential for making broken builds.
    - There is an even rarer RNG where any tier of Component can roll with two stat of the same stats, doubling up the contribution to that stat
- **Component Post Integration Grind:**
    - Once a Component is integrated, a currency can be applied which will lock in its highest stat, but reroll the rest. The total of all rerolled stats will not change, meaning that realistically you'll save the currency for rerolling Components with high base rolls.
    - During rerolls, the rare corruption or double stat thing can happen, which could turn a decent Component into an amazing buildcrafting option
- **Component Gameplay Loop:**
    - You don't lose components on death
    - Components also stay locked on your body unless you are in your base
    - Component management is entirely done off tile, so if you do loot components you want to keep, you really do need to stay alive to get back to base with them

# Weapons
- **Weapon Gameplay Loop:**
    - Generally the goal with weapons is integrate them, however the result of integration with weapons is different than with suits
    - Any non integrated weapons are lost on death but integrated weapons are permanent additions to your account (unless you sell them) and are retained on death
    - As you use a weapon, you gain mastery in its particular category
    - You can effectively "spend" mastery to integrate a weapon that you particularly like and no longer risk losing it on risky activities
- **Weapon Stats:**
    - Weapons have fixed combat stats
    - Weapon variation comes from Traits which are randomly rolled
    - Some traits are shared between archetypes, and some are unique to specific archetypes
    - Generally speaking because weapons have fixed base damage and crit stats, the higher the stats the better the weapon is, but the traits that roll on the weapon make or break it, especially when you take your entire build into consideration
    - As such, there simply are many low tier weapons that have low base stats, and even if rolled with the best possible traits for the particular weapon, is still not going to be as good as a higher tier weapon with its higher base stats rolling with that same best possible trait (a completionist would try to integrate one copy of it probably as a collectors item and just move on)
    - **Range:**
        - Each weapon archetype has different effectiveness at close, mid, and long range
        - Effectiveness is a simple fixed multiplier which scales the final calculated damage of an attack action, meaning that you can have an amazing roll on a weapon, but it just does significantly reduced damage when used at the wrong range
        - It's a hardcore game with realistic tradeoffs, as well as unbalanced mechanics that just are what they are
            - Long Rifles and Carbines are simply the best weapon archetypes for covering all ranges, meaning that you will struggle with the range mechanic if you build into other weapon archetypes
            - The game will not prevent you from playing melee only, but you will not be able to deal damage at mid and long range (just like in a realistic scenario, you will have to rely on evasion and stealth to deal with those sort of combat scenarios)
    - **Base Damage:**
        - Weapon base damage scales by the sum of all your stats
    - **Critical Chance:**
        - Chance to perform a Critical hit which applies the Critical Multiplier to Base Damage
        - Scales with RAT
    - **Critical Multiplier:**
        - How much Base Damage is multiplied during a Critical hit
        - Scales with VIT
- **Weapon Traits:**
    - Weapon Traits are not limited to affecting only the weapon's stats, they can also affect other parts of your build
        - Equipping a secondary weapon is often a crucial part of buildcrafting just for the weapon's passive traits, even if you don't generally use the weapon in raid
- **Weapon Integration:**
    - To integrate a Weapon, you spend an amount of mastery from that weapon category
    - Weapon integration randomly rolls an extra trait on that weapon
    - A rare currency can be used to perform targeted trait rerolls on integrated weapons

# Armor
- **Armor Mechanics:**
    - Armor is always lost on death and is one of the long term currency sinks since it cannot be insured
    - Armor can often be looted off of enemy corpses, but it will likely be damaged
    - Armor can be repaired

# Vendors
- Permanent Vendors are available on overworld maps. They are the main way to sell unwanted equipment and resources to earn primary currencies
- Some rare Vendors only appear randomly either on overworld tiles or in dungeons. These can be highly sought after encounters as RNG vendors are unique sources of some equipment and resources
- Vendors exist in an economy
    - Resources which are known to be plentiful on a particular location will be worth less by Vendors on that location. It is best to haul resources to location where they are more scarce to make more money on them. 
    - Flooding a local economy with one particular resource reduces the demand and therefore price for that item. Likewise, buying a ton of one particular item increases the demand and price of that item.
    - RNG events can flood a market with one particular item or create a high demand for something for a period of time
- Most Vendors deal in either krezhna or one of the other more specialized currencies
- Some Vendors offer some or all items for barter only
- Some tiles offer gamble mechanics to gamble either resources or sacrifice equipment for potential rewards. These are still considered Vendors even if there isn't a character selling stuff
- The economy is always changing between different Locations and Destinations and it can be fun and rewarding in and of itself to just buy, sell, and craft your way between the different markets for a profit or for a particular item you want

# Maps
Every screen in the game exists at one of four location "layers"
1. **Orbit:**
    - From here you can navigate between star systems and see each planetary overworld location
    - You navigate directly to a Destination, not the planet/moon itself
    - Some planets or moons may have multiple Destinations.
2. **Destination:**
    - This is a large map of an open world area
    - Destination maps generally present wide open spaces with many directly visitable Tiles
    - Destination maps have clearly marked nodes showing individual Locations which can be visited
3. **Location:**
    - A Location is any self contained area such as a building, a town, a hand crafted dungeon, or a procedurally generated raid
    - The contents of the Location is not important - a dangerous dungeon and a non combat NPC area are both considered to be Locations
    - Just like on the Destination itself, Locations have tiles which can be directly visited
4. **Tile/Encounter:**
    - Clicking on a visitable Tile from either a Destination or Location will bring you to a single screen Encounter
    - The terms Tile and Encounter are almost interchangable, but Tile generally refers to the clickable are on a Destination or Location which has specific coordinates, and Encounter generally refers to what happens on the Tile
    - The Encounter itself could be a combat encounter with one or more enemies, a resource encounter with one or more resource nodes to collect, or many other possible things
    - Locations can have Encounters that are just a locked door - unlocking the door provides access to more tiles on the Location

# Crafting
- Many items can be crafted if the blueprint is known
- All crafting actions increase the Alchemy Skill
- Normal items blueprints can be unlocked by bringing multiple copies of the item to a specific vendor and trading them for the blueprint:
    - Consumables: 5-10
    - Weapons: 2-5
    - Armor: 2-5
- Other blueprints can be learned by dismantling the item and getting a higher and higher change of learning the blueprint
- Components cannot be crafted due to them rolling with random Traits (craftable items, especially Weapons, are designed to support the idea that you may very well need multiple of them while Components and Tools present a different aquisition challenge and potential reward due to the RNG Traits)
- Protoform items also cannot be crafted due to their unique and rare nature

# Protoforms
- **Resolving Protoforms:**
    - Protoforms drop as unidentified masses of encrypted matter, and can be "resolved" into an item in the following ways:
        - The primary way of resolving Protoforms is to run a specific activity on a Destination. This activity will have you slot a Protoform into a device and then defeat waves of enemies while it decrypts.
        - Additionally, if you leave an encrypted Protoform in your inventory, it passively picks up XP from any Encounter, and will, given enough time, gain enough XP to decrypt on its own. This is very time consuming however and the normal way to decrypt is to run a decrypt activity. However, the waves of enemies scales with how much XP needs to be absorbed by the Protoform, so you can reduce the number of enemy Encounters by slotting a partially decrypted Protoform.
        - Once the Protoform is decrypted, you can attempt to resolve it into an item. The Cryptography and Alchemy Skills equally contribute to your chances at a successful resolution. If the resolution is unsuccessful, the Protoform may revert to its encrypted state where you'll need to try again, be lost entirely, or even split into two encrypted protoforms which is quite rare. The mechanic is designed to be unpredictable, high effort, often high risk, and high potential reward.
- **Protoform Components:**
    - Protoform components roll with five Stats, often with wild distributions
    - They are the only Components that can roll with negative stats
    - They cannot be rerolled like normal Components
- **Protoform Weapons:**
    - Protoform Weapons are considered integrated don't level
    - Their Specs are randomly rolled, often with wild distributions
    - They are the only Weapons that can roll with negative stats
    - They cannot reroll their Traits like normal integrated Weapons
- **Protoform Suits:**
    - Protoform Suits are considered integrated don't level
    - They are extremely rare and are considered the highest tier of endgame chase item
    - Their Stats are the same as the base stat version, keeping the identity of the Suit recognizable, but with random buffs or nerfs applied to any of the six Stats, so a Stat can roll negative
    - They cannot gain the post integration Stat boosts like normal integrated Suits

# Archive
The Archive contains a ton of information about the game.
- Explanations of all stats information important to understanding builds
- Library of all enemies, animals, locations etc. discovered by the account
- Displays the current probability of unlocking a blueprint on the next dismantle of an item

# What happens when you die?
- You keep your body and slotted components
- You keep any integrated weapons
- You lose any non integrated weapons
- You lose all armor
- You lose your current inventory
 
# Threat mechanic
- PER contrbitues to the Threat mechanic where you may get a warning before an enemy appears on a quiet Tile or after you've killed enemies and are lingering on a Tile (high PER gives you more warning and a chance to leave before the threat appears)

# Account item transfer tool
- Accounts are encrypted
- A dedicated feature lets you load two files and transfer items such that they cannot be duplicated

# Keys
- Keys can be found or purchased which can open specific doors or containers in dungeons

# Bosses
- The general gameplay loop for any given destination is that the destination has one or more bosses to defeat (inspired by boss rush games)
- There is a final boss for that destination which always has some special mechanic, often tied to the destination itself which presents a meaningful gear up requirement before the boss can be defeated and the destination fully cleared
- There may also be side bosses on the destination

# Special mobs
- Very rarely you will encounter a special (think shiny) variant of a normal enemy or animal which drops special items

# Progression and Endgame
- Progression is fundamentally tied to looting and rerolling components
- Generally speaking a progression loop involves starting on a new destination and grinding out the new components available on that destination to:
    - Craft new bodies available from those components
    - Get the best in slot components which increases your damage and survivability
    - Reroll stats on those components to fit your build
    - Integrate a body using your choice of components for a final stat boost
