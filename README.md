#ComputerScience/Internal/Programming

The classic game, with some cool *extra stuff*

## Gameplay

### Attacking changes
#### Targeting mechanics

In order to fire a projectile, guided or not, you normally feed it or its firing vessel the target coordinates. Certain weapons systems are able to do this faster and more accurately than others; the general rule of thumb is the larger the weapon, the poorer the targeting.
##### Stats

- **Fighters** have a 60% chance to hit their target once locked, which increases by 10% for each **Carrier level**. If the enemy has a **Level 3 Submarine** using *Matrix Array*, it reduces fighter efficacy to 30%.
- **Guns** have a 70% chance to hit their target once locked, unless the enemy has a **Level 3 Destroyer** using *Advanced Active Defense*, which reduces cannon efficacy to 50%.
- **Missiles** have a 100% chance to hit their target once locked, unless the enemy has a **Level 3 Submarine** using *Matrix Array*, which reduces missile efficacy to 75%.
- **Torpedoes** have different chances to hit based on the target ship type.
	- There is a 30% chance to hit a **Frigate**.
	- There is a 40% chance to hit a **Submarine**.
	- There is a 50% chance to hit a **Destroyer**.
	- There is a 70% chance to hit a **Battleship**.
	- There is a 90% chance to hit a **Carrier**.
- **Autocannons** have a 90% chance to hit their target once locked. No enemy ship ability is able to reduce the accuracy of an autocannon thanks to its high fire-rate. However, it has only 20% accuracy against **Submarines**.

#### Damage mechanics

- **Fighters** have huge payload potential; their strikes bypass *Active Defense* and *Armor*. If they manage to get past AA and *jamming*, their payloads are a direct hit. They have a flat 20% chance to cause collateral damage, dealing an extra hit point of damage to an adjacent section of the ship.
- **Guns** have the most straightforward damage application; each volley, upon contact, will delete one hit point.
- **Missiles** behave the same; one hit point, one square.
- **Torpedoes** deal one hit point of damage to their targeted square, but have a dynamic chance to instantly sink the ship.
	- There is a 75% chance to instantly sink a **Frigate**.
	- There is a 75% chance to instantly sink a **Submarine**.
	- There is a 55% chance to instantly sink a **Destroyer**.
	- There is a 15% chance to instantly sink a **Battleship**.
	- There is a 5% chance to instantly sink a **Carrier**.
- **Autocannons** fire in bursts and thus have a 25% chance to split their damage across two sections of a ship. From the enemy's perspective, two sections of their ship will illuminate *yellow*, but from the player's perspective they can only see one section (the one they targeted) turn *yellow*. They will need to find the other section they hit (one square away in any direction).

#### Reloading mechanics

- **Fighters** need one turn to re-arm and re-fuel, unless the **Carrier** has a *Rapid Deployment Backup* on standby, allowing for instant re-use. However, if there is a **Level 3 Carrier** with *Expanded Payload*, their fighters will take two turns to re-arm and re-fuel.
- **Guns** have instant cooldown and can be fired again on the next turn. A **Level 2 Battleship** with *Precision Targeting* takes one turn cooldown to reload and reprogram the firing data.
- **Missiles** have a two-turn cooldown to prepare the vertical launch cell, which requires heavy maintenance and an onboard crane to load the new missile. A **Level 3 Destroyer** with *Hurricane* can launch multiple missiles with no cooldown.
- **Torpedoes** have two launch tubes; there is no cooldown while there is at least one torpedo in the tube, but reloading the tubes takes five turns. A tube cannot be reloaded while there is still a torpedo in the other.
- **Autocannons** have instant cooldown, but using them three times in a row gives them a 50% to overheat and jam, leaving them on a four-turn cooldown. Using them four or more times in a row gives them a 99% chance of overheating. A **Level 2 Frigate** with *Gyrostabilizer* allows for one extra use before overheating penalties. A **Level 3 Frigate** with *BRRRT* has a one-turn cooldown to let the **rotary autocannons** cool down.

#### Battleships
##### Main Armament: **Guns**

Battleships are renowned for their extraordinary firepower, often featuring arrays of large-caliber guns. They deal consistent damage with good accuracy.

##### AA Armament: **AAA**

Battleships have classical "triple-A", anti-aircraft-artillery. They deal constant damage to fighters that increases as they get closer.

##### Unique Mechanic: *Broadside*

In order for a battleship to unleash its maximum firepower, it must face perpendicular to the enemy side (horizontal). If it is not, the guns will only deal 0.5 hit points and the *Wider Turrets* upgrade is disabled. The exception to this mechanic is the *Glass Railcannon* upgrade, which cannot be placed to broadside.

### Progression System

The backbone of this battleships game is its progression system. As the user wins games against the AI, they will accumulate points (based on the difficulty setting). These points can be spent on better ships which have more defense and firepower (more on that later.)

#### Level 0 - **Basic**

**Basic** ships are the most basic version of that ship type. They behave like their standard real-game counterparts, along with universal features added to provide more detail. Everyone starts with a Level 0 ship.

#### Level 1 - **Standard**

**Standard** ships are slightly beefier versions of their basic variant. They have enhanced defensive traits based on their type:
- **Carriers** have more *Runway Integrity*, allowing them to sortie after one extra hit compared to their basic variant.
- **Battleships** have *Armor*, giving them a small chance to sustain a hit without losing health.
- **Destroyers** have *Active Defense*, allowing their AA defense to have a medium chance to intercept an incoming **missile** or **torpedo** within 1 square adjacent to it. This can be used to defend other ships, which is a trade-off as it makes your destroyer extremely vulnerable.
- **Submarines** have *Stealth*, giving them a small chance to get hit without notifying the other player (they will think they missed).
- **Frigates** have *Evasion*, giving them a small chance to dodge an incoming projectile.

#### Level 2 - **Enhanced**

**Enhanced** ships have the same defensive bonuses as their Standard counterparts, along with bonuses to their offensive capabilities:
- **Carriers** have the *increased capacity* ability, where one out of every three fighter groups they dispatch will be accompanied by a second fighter group. This group can have several functions:
	- *Double Strike* allows a dispatch to attack a second region independently of the first.
	- *AA Jammer* will actively jam ship anti-air targeting the first fighter group, making them safer as they deliver their payload. However, ship air defense is still able to target the second fighter group, and if they are shot down, the first group will be vulnerable again.
	- *Rapid Deployment Backup* simply keeps the extra group on the carrier for use during the other's cooldown.
- **Battleships** have *upgraded guns*, allowing for a buff in one of three traits:
	- *Wider Turrets* increases the number of onboard guns, allowing for an outgoing volley to spread across the neighboring left and right square, reducing **accuracy** but drastically increasing **damage** potential. It also makes *Advanced Active Defense* less effective against it.
	- *Precision Targeting* allows for more **accuracy** at the cost of increased **firing cooldown**.
- **Destroyers** have **better missiles**, allowing for better defensive or offensive capabilities:
	- *Better Guidance* increases the effectiveness of their **anti-air** systems, allowing for easier downing of incoming **Fighters** and **Missiles**. It also allows AA to shoot while jammed, but only to a limited extent.
	- *Larger Warhead* increases the missile's chance to deal **collateral damage**.
- **Submarines** have an increased bonus to *Stealth* and they unlock the *Sonar* ability, allowing them to scan a 3x3 section of the enemy territory to see if there are any ships. There is a 20% chance for this to be a false-positive/negative.
- **Frigates** have different types of autocannons they can swap out for:
	- *Gyrostabilizer*-fitted autocannons have a slower rate of fire with more precise bursts, slower overheating, and higher accuracy. However, if an enemy **Level 3 Destroyer** has *Advanced Active Defense*, the accuracy decreases to 60%.

#### Level 3 - **Superior**

**Superior** ships represent the pinnacle of naval warfare. Featuring powerful abilities that drastically sway the tide of battle (literally), they are difficult to get, but very worth the investment. They have all the bonuses as previous variants, and these upgrades double down on or complement their previous enhancements: 
- **Carriers** can have one of the following abilities:
	- *Hornet's Nest* dispatches a swarm of fighters that stay in the air for three turns before returning to the carrier. During this time, the carrier cannot launch any more fighters, and once they land, they enter a four-turn cooldown. While the fighters are airborne, they can split into four standard strike groups. Any group can assume the role of a strike package, anti-aircraft defense, or any secondary fighter group from the *Enhanced* upgrades.
	- *Scout Carrier* converts all **fighters** to **stealth UAV's**, effectively removing all offensive and defensive capabilities. All **UAVs** must fly in a singular group formation and can scan a 3x3 section of the enemy map with perfect resolution, and detect ship signatures one square away from the HD section. When launched, they start near the carrier. On the next turn, they can move freely through friendly space, or move one square into enemy space. They repeat this until finding a ship. They must return to the carrier to refuel after eight turns for a two-turn cooldown. While drones are airborne, your **missiles** are disabled but **guns**, **autocannons**, and **torpedoes** can be used normally on a turn while also moving the drones. If they travel within one square next to an enemy ship, they can be detected and shot down. Enemy missiles with their flight paths passing the drone formation can reveal their location to the enemy for that one turn. Due to the fragility of the drones, runway integrity is reduced to 2.
- **Battleships** can have one of the following abilities:
	- *Bastion Mode* immensely increases the ship's defensive abilities; its *Armor* can now nullify 60% of all hits and 100% of all half-hits. It cannot suffer **collateral damage** (unless hit by a *Glass Cannon*) or **instant-sinking**, and once every ten turns it can regenerate one hit point as long as it has at least 2 hit points remaining. All **fighters** that come within two squares of this beast get shot down instantly, even if the ships is being jammed. This comes at a significant cost of firepower though; shots can only deal half a hit point of damage and this upgrade is incompatible with the *Enhanced* upgrade *Wider Turrets*. It also makes the ship extremely easy to hit; all incoming attacks have 100% accuracy. Concentrated firepower is mandatory to sink this beast.
	- *Glass Railcannon* does the complete opposite; it eliminates any *Armor* protection and increases **collateral damage** and **instant-sinking** chances by 50 and 20% respectively. However, it has a **50" main railgun** with 95% accuracy that can **instant-sink** any ship apart from a *Bastion Mode* **Level 3 Battleship** (which will instead deal 3 hit points and reduce effective *Armor* protection to 10%). This ship must be placed vertically (parallel to the enemy) and not fired more than 5 degrees off center, otherwise the recoil generated by the gun firing will tip the vessel over. It must wait five turns to reload and can only fire three times throughout the whole game. This upgrade is incompatible with the *Wider Turrets* enhancement. This upgrade also completely removes AA protection, making it dependent on other ships for survival. However, no other ship may be next to (including diagonally) the front most section of the ship or it will instantly die from the projectile vortex and sonic boom. Absolute bullet sneeze.
- **Destroyers** can have one of the following abilities:
	- *Hurricane* adds extra vertical launch cells with rapid reloading directly from the ammo racks. This allows up to three missiles to be launched on the same turn with no firing cooldown. These missiles can be fired at completely different ships, or concentrated on a single target. However, the ship can only fire a total of 6 missiles during the game and this upgrade is incompatible with *Larger Warhead*. It also disables *Active Defense* and AA protection.
	- *Advanced Active Defense* significantly expands the capabilities of *Active Defense*. It can now intercept **gun** shells and increases overall effectiveness and range against all incoming projectiles. Furthermore, it is able to intercept slow-firing **autocannons** and all **fighters**/**scout UAVs** within two squares get shot down. However, this completely disables all offensive capabilities.
- **Submarines** can have one of the following abilities: 
	- *Matrix Array* adds a complete electronic warfare suite to the submarine. It severely reduces the efficacy of all missiles, fighters, drones, and sonar used by the enemy. It also increases *Stealth* to 80%, making it nearly undetectable. It is invisible to scout drones and sonar; the only way to reliably detect it is how disrupted and jammed weapons platforms are in certain areas. Its sonar grid is now 4x4. However, to accommodate for this technology there is only one torpedo tube.
	- *SSBN* removes all
- **Frigates** can have one of the following abilities:
	- *Tugboat* allows the ship to turn 90 degrees left/right, move two squares forward, or one square forward while pulling another ship, on each turn. Its evasion factor is halved, and when pulling a ship it is nullified. This completely disables all offensive capabilities and causes the ship to sink immediately after being hit once, but it can reposition other ships. This can be very helpful for moving an enemy into the firing envelope of *Glass Railcannon* or the defense envelope of *Advanced Active Defense*.
	- *BRRRT* retrofits the ship with a **rotary autocannon** which has high damage but is also **range-restricted**, the ship must be put in the top three rows or it will not reach the entire enemy grid. It must wait one turn cooldown due to the immense heat generated by the weapon. It can spread its damage across two squares dealing one hit point each, but it has 75% accuracy.