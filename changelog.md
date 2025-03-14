# 5.0.0

Saves from 3.x are not compatible with 5.0.

## Features/Improvements

## Fixes

# 4.1.0

Saves from 4.0.0 are compatible with 4.1.0.

## Features/Improvements

* **[Campaign]** Air defense sites now generate a fixed number of launchers per type.
* **[Mission Generation]** Improvements for better support of the Skynet Plugin and long range SAMs are now acting as EWR
* **[Plugins]** Increased time JTAC Autolase messages stay visible on the UI.
* **[UI]** Added ability to take notes and have those notes appear as a kneeboard page.
* **[UI]** Hovering over the weather information now dispalys the cloud base (meters and feet).
* **[UI]** Google search link added to unit information when there is no information provided.
* **[UI]** Control point name displayed with ground object group name on map.

## Fixes
* **[UI]** Statistics window tick marks are now always integers.
* **[Mission Generation]** The lua data for other plugins is now generated correctly
* **[Flight Planning]** Fixed potential issue with angles > 360° or < 0° being generated when summing two angles.

# 4.0.0

Saves from 3.x are not compatible with 4.0.

## Features/Improvements

* **[Engine]** Support for DCS 2.7.2.7910.1 and newer, including Cyprus, F-16 JDAMs, and the Hind.
* **[Campaign]** Squadrons now (optionally, off by default) have a maximum size and killed pilots replenish at a limited rate.
* **[Campaign]** Added an option to disable levelling up of AI pilots.
* **[Campaign]** Added Russian Intervention 2015 campaign on Syria, for a small and somewhat realistic Russian COIN scenario.
* **[Campaign]** Added Operation Atilla campaign on Syria, for a reasonably large invasion of Cyprus scenario.
* **[Campaign AI]** AI will plan Tanker flights.
* **[Campaign AI]** Removed max distance for AEW&C auto planning.
* **[Economy]** Adjusted prices for aircraft to balance out some price inconsistencies.
* **[Factions]** Added more tankers to factions.
* **[Flight Planner]** Added ability to plan Tankers.
* **[Modding]** Campaign format version is now 7.0 to account for DCS map changes that made scenery strike targets incompatible with existing campaigns.
* **[Mods]** Added support for the Gripen mod.
* **[Mods]** Removes MB-339PAN support, as the mod is now deprecated and no longer works with DCS 2.7+.
* **[Mission Generation]** Added support for "Neutral Dot" label options.
* **[New Game Wizard]** Mods are now selected via checkboxes in the new game wizard, not as separate factions.
* **[UI]** Ctrl click and shift click now buy or sell 5 or 10 units respectively.
* **[UI]** Multiple waypoints can now be deleted simultaneously if multiple waypoints are selected.
* **[UI]** Carriers and LHAs now match the colour of airfields, and their destination icons are translucent.
* **[UI]** Updated intel box text for first turn.
* **[UI]** Base Capture Cheat is now usable at all bases and can also be used to transfer player-owned bases to OPFOR.
* **[UI]** Pass Turn button is relabled as "Begin Campaign" on Turn 0.  
* **[UI]** Added a ruler to the map.
* **[UI]** Liberation now saves games to `<DCS user directory>/Liberation/Saves` by default to declutter the main directory.

## Fixes

* **[Campaign AI]** Fix procurement for factions that lack some unit types.
* **[Campaign AI]** Fix auto purchase of aircraft for factions that have no transport aircraft.
* **[Campaign AI]** Fix refunding of pending aircraft purchases when a side has no factory available.  
* **[Mission Generation]** Fixed problem with mission load when control point name contained an apostrophe.
* **[Mission Generation]** Fixed EWR group names so they contribute to Skynet again.
* **[Mission Generation]** Fixed duplicate name error when generating convoys and cargo ships when creating manual transfers after loading a game.
* **[Mission Generation]** Fixed empty convoys not being disbanded when all units are killed/removed.
* **[Mission Generation]** Fixed player losing frontline progress when skipping from turn 0 to turn 1.
* **[Mission Generation]** Fixed issue where frontline would only search to the right for valid locations.
* **[UI]** Made non-interactive map elements less obstructive.
* **[UI]** Added support for Neutral Dot difficulty label
* **[UI]** Clear skies at night no longer described as "Sunny" by the weather widget.
* **[UI]** Removed ability to buy (useless) ground units at carriers and LHAs.
* **[UI]** Fixed enable/disable of buy/sell buttons.
* **[UI]** EWRs now appear in the custom waypoint list.

# 3.0.0

Saves from 2.5 are not compatible with 3.0.

## Features/Improvements

* **[Campaign]** Ground units can now be transferred by road, airlift, and cargo ship. See https://github.com/dcs-liberation/dcs_liberation/wiki/Unit-Transfers for more information.
* **[Campaign]** Ground units can no longer be sold. To move units to a new location, transfer them.
* **[Campaign]** Ground units must now be recruited at a base with a factory and transferred to their destination. When buying units in the UI, the purchase will automatically be fulfilled at the closest factory, and a transfer will be created on the next turn.
* **[Campaign]** Non-control point FOBs will no longer spawn.
* **[Campaign]** Added squadrons and pilots. See https://github.com/dcs-liberation/dcs_liberation/wiki/Squadrons-and-pilots for more information.
* **[Campaign]** Capturing a base now depopulates all of its attached objectives with units: air defenses, EWRs, ships, armor groups, etc. Buildings are captured.
* **[Campaign]** Ammunition Depots determine how many ground units can be deployed on the frontline by a control point.
* **[Campaign AI]** AI now considers Ju-88s for CAS, strike, and DEAD missions.
* **[Campaign AI]** AI planned AEW&C missions will now be scheduled ASAP.
* **[Campaign AI]** AI now considers the range to the SAM's threat zone rather than the range to the SAM itself when determining target priorities.
* **[Campaign AI]** Auto purchase of ground units will now maintain unit composition instead of buying randomly. The unit composition is predefined.
* **[Campaign AI]** Auto purchase will aim to purchase enough ground units to support the frontline, plus 30% reserve units.
* **[Campaign AI]** Auto purchase will now adjust its air/ground balance to favor whichever is under-funded.
* **[Flight Planner]** Desired mission length is now configurable (defaults to 60 minutes). A BARCAP will be planned every 30 minutes. Other packages will simply have their takeoffs spread out or compressed such that the last flight will take off around the mission end time.
* **[Flight Planner]** Flight plans now include bullseye waypoints.
* **[Flight Planner]** Differentiated SEAD and SEAD escort. SEAD is tasked with suppressing the package target, SEAD escort is tasked with protecting the package from all SAMs along its route.
* **[Flight Planner]** Planned airspeed increased to 0.85 mach for supersonic airframes and 85% of max speed for subsonic.
* **[Flight Planner]** Taxi time estimation for airfields increased from 5 minutes to 8 minutes.
* **[Flight Planner]** Reduce expected error margin for flight plans from 10% to 5%.
* **[Flight Planner]** SEAD flights are scheduled one minute ahead of the package's TOT so that they can suppress the site ahead of the strike.
* **[Flight Planner]** Automatic ATO generation for the player's coalition can now be disabled in the settings.
* **[Payloads]** AI flights for most air to ground mission types (CAS excluded) will have their guns emptied to prevent strafing fully armed and operational battle stations. Gun-reliant airframes like A-10s and warbirds will keep their bullets.
* **[Kneeboard]** ATC table overflow alleviated by wrapping long airfield names and splitting ATC frequency and channel into separate rows.
* **[UI]** Overhauled the map implementation. Now uses satellite imagery instead of low res map images. Display options have moved from the toolbar to panels in the map.
* **[UI]** Campaigns generated for an older or newer version of the game will now be marked as incompatible. They can still be played, but bugs may be present.
* **[UI]** DCS loadouts are now selectable in the loadout setup menu.
* **[UI]** Added global aircraft inventory view under Air Wing dialog.
* **[UI]** Base menu now shows information about ground unit deployment limits.
* **[Modding]** Campaigns now choose locations for factories to spawn.
* **[Modding]** Campaigns now choose locations for ammunition depots to spawn.
* **[Modding]** Campaigns now use map structures as strike targets.
* **[Modding]** Campaigns may now set *any* objective type to be a required spawn rather than random chance. Support for random objective generation was removed.
* **[Modding]** Campaigns may now place AAA objectives.
* **[Modding]** Can now install custom factions to <DCS saved games>/Liberation/Factions instead of the Liberation install directory.
* **[Performance Settings]** Added a settings to lower the number of smoke effects generated on frontlines. Lowered default settings for frontline smoke generators, so less smoke should be generated by default.
* **[Configuration]** Liberation preferences (DCS install and save game location) are now saved to `%LOCALAPPDATA%/DCSLiberation` to prevent needing to reconfigure each new install.
* **[Skynet]** Updated to 2.1.0.

## Fixes

* **[Campaign AI]** Fix purchase of aircraft by priority (the faction's list was being used as the priority list rather than the game's).
* **[Campaign AI]** Fixed bug causing AI to over-purchase cheap aircraft.
* **[Campaign AI]** Auto planner will no longer attempt to plan missions for which the faction has no compatible aircraft.
* **[Campaign AI]** Stop purchasing aircraft after the first unaffordable package to attempt to complete more packages rather than filling airfields with cheap escorts that will never be used.
* **[Campaign]** Fixed bug where offshore strike locations were being used to spawn ship objectives.
* **[Campaign]** EWR sites are now purchasable.
* **[Flight Planner]** AI strike flight plans now include the correct target actions for building groups.
* **[Flight Planner]** AI BAI/DEAD/SEAD flights now have tasks to attack all groups at the target location, not just the primary group (for multi-group SAM sites).
* **[Flight Planner]** Fixed some contexts where damaged runways would be used. Destroying a carrier will no longer break the game.

# 2.5.1

## Features/Improvements

* **[UI]** Engagement ranges are now displayed by default.
* **[UI]** Engagement range display generalized to work for all patrolling flight plans (BARCAP, TARCAP, and CAS).
* **[Flight Planner]** Front lines no longer project threat zones to avoid pushing BARCAPs back so much. TARCAPs will be forcibly planned but strike packages will not route around front lines even if it is reasonable to do so.

## Fixes

* **[Campaigns]** EWRs associated with a base will now only be generated near the base.
* **[Flight Planner]** Fixed error when generating AEW&C flight plans in campaigns with no front lines.

# 2.5.0

Saves from 2.4 are not compatible with 2.5.

## Features/Improvements

* **[Engine]** DCS 2.7 Support
* **[UI]** Improved FOB menu, added a custom banner, and do not display aircraft recruitment menu
* **[Flight Planner]** Added AEW&C missions. (by siKruger)
* **[Kneeboard]** Added dark kneeboard option (by GvonH)
* **[Campaigns]** Multiple EWR sites may now be generated, and EWR sites may be generated outside bases (by SnappyComebacks)
* **[Mission Generation]** Cloudy and rainy (but not thunderstorm) weather will use the cloud presets from DCS 2.7.
* **[Plugins]** Added LotATC export plugin (by drsoran)
* **[Plugins]** Added Splash Damage Plugin (by Wheelijoe)
* **[Loadouts]** Replaced Litening with ATFLIR for all default F/A-18C loadouts.

## Fixes

* **[Flight Planner]** Front lines now project threat zones, so TARCAP/escorts will not be pruned for flights near the front. Packages may also route around the front line when practical.
* **[Flight Planner]** Fixed error when planning BAI at SAMs with dead subgroups.
* **[Flight Planner]** Mig-19 was not allowed for CAS roles fixed
* **[Flight Planner]** Increased size of navigation planning area to avoid plannign failures with distant waypoints.
* **[Flight Planner]** Fixed UI refresh when unchecking the "default loadout" box in the loadout editor.
* **[Objective names]** Fixed typos in objective name : ARMADILLLO -> ARMADILLO (by SnappyComebacks)
* **[Payloads]** F-86 Sabre was missing a custom payload
* **[Payloads]** Added GAR-8 period restrictions (by Mustang-25)
* **[Campaign]** Date now progresses.
* **[Campaign]** Added game over message when a coalition runs out of functioning airbases.
* **[Mission Generation]** Fixed "invalid face handle" error in kneeboard generation that occurred on some machines.

## Regressions

* **[Mod Support]** Stopped support for 2.5.5 Rafale Mode, and removed factions that were using it
* **[Mod Support]** Su-57 mod support might be out of date

# 2.4.3

## Features/Improvements

* **[New Game Wizard]** Added the possibility to setup custom start date

## Fixes

* **[Mods]** Updated C-130J mod data to version 6.4
* **[Mods]** Updated F-22A mod to latest version

# 2.4.2

## Features/Improvements

* **[Factions]** Introduction dates and fallback weapons added for US, Russian, UK, and French weapons. Huge thanks to @TheCandianVendingMachine for the massive amount of data entry!
* **[Campaigns]** Added 1995 start dates.

## Fixes

* **[Economy]** Pending ground unit purchases will also be transferred when a connected base is captured.
* **[UI]** Fixed rounding of budget in recruitment menu.

# 2.4.1

## Fixes

* **[Units]** Fixed syntax error with the SH-60B payload file.
* **[Culling]** Missile sites generate reasonably sized non-cull zones rather than 100km ones.
* **[UI]** Budget display is also now rounded to 2 decimal places.
* **[UI]** Fixed some areas where the old, non-pretty name was displayed to users.

# 2.4.0

Saves from 2.3 are not compatible with 2.4.

## Highlights

* Improved flight plan generation to avoid loitering in or traveling through threatened areas when practical.
* Improved AI aircraft purchasing behavior.
* Era-restricted weapons (work in progress).
* Tons of UI polish.
* Rebalanced economy to keep opfor competitive over the course of the game.

## Features/Improvements

* **[Flight Planner]** Air-to-air and SEAD escorts will no longer be automatically planned for packages that are not in range of threats.
* **[Flight Planner]** Non-custom flight plans will now navigate around threat areas en route to the target area when practical.
* **[Flight Planner]** Flight plans along front lines now ensure that the race track start is closer to the departure airfield than the race track end.
* **[Campaign AI]** Auto-purchase now prefers airfields that are not within range of the enemy.
* **[Campaign AI]** Auto-purchase now prefers the best aircraft for the task, but will attempt to maintain some variety.
* **[Campaign AI]** Opfor now sells off odd aircraft since they're unlikely to be used.
* **[Campaign AI]** Multiple rounds of CAP will be planned (roughly 90 minutes of coverage). Default starting budget has increased to account for the increased need for aircraft.
* **[Mission Generator]** Multiple groups are created for complex SAM sites (SAMs with additional point defense or SHORADS), improving Skynet behavior.
* **[Mission Generator]** Default start type can now be chosen in the settings. This replaces the non-functional "AI Parking Start" option. **Selecting any type other than cold will break OCA/Aircraft missions.**
* **[Cheat Menu]** Added ability to toggle base capture and frontline advance/retreat cheats.
* **[Skynet]** Updated to 2.0.1.
* **[Skynet]** Point defenses are now configured to remain on to protect the site they accompany.
* **[Hercules]** Updated the Hercules Cargo list file.
* **[Balance]** Opfor now gains income using the same rules as the player, significantly increasing their income relative to the player for most campaigns.
* **[Balance]** Units now retreat from captured bases when able. Units with no retreat path will be captured and sold.
* **[Economy]** FOBs generate only $10M per turn (previously $20M like airbases).
* **[Economy]** Carriers and off-map spawns generate no income (previously $20M like airbases).
* **[Economy]** Sales of aircraft and ground vehicles can now be cancelled before the next turn begins.
* **[UI]** Multi-SAM objectives now show threat and detection rings per group.
* **[UI]** New icon for AA sites with no active threat.
* **[UI]** Unit names are now prettier and more accurate, and can now be set per-country for added historical flavour.
* **[UI]** Default loadout is now shown for flights with no custom loadout selected.
* **[UI]** Aircraft for a new flight are now only selectable if they match the task type for that flight.
* **[UI]** WIP - There is now a unit info button for each unit in the recruitment list, that should help newer players learn what each unit does.
* **[UI]** Docs for time-on-target and creating new theaters/factions/loadouts are now linked in the UI at the appropriate places.
* **[UI]** ASAP is now a checkbox rather than a button. Enabling this will disable the TOT selector but changes to the package structure will automatically re-ASAP the package.
* **[UI]** Arrival airfield is now shown in the flight list if it differs from the departure airfield.
* **[UI]** Start type can now be selected when creating a flight.
* **[UI]** Arrival and divert airfields can be edited after the flight is created.
* **[Factions]** Added option for date-based loadout restriction. Active radar homing missiles are handled, patches welcome for the other thousand weapons.
* **[Factions]** Added Poland 2010 faction.
* **[Factions]** Added Greece 2005 faction.
* **[Factions]** Added Iran 1988 faction.
* **[Units]** Support for E-2 Hawkeye, SH-60B Seahawk, S-3B Viking (thanks to awinterquest) and SpGH Dana - these are now being used by appropriate factions.
* **[Culling]** Missile sites are no longer culled.
* **[Campaigns]** Added campaign "Black Sea Lite" by Starfire
* **[Campaigns]** Added campaign "Exercise Vegas Nerve" by Starfire 
* **[New game Wizard]** The theater page is now the first page of the campaign wizard, recommended factions will be selected automatically on the faction selection page
* **[New game Wizard]** Added information text about the selected campaign performance.
* **[Mod Support]** Added support for High Digit SAMs mod 1.4.0
* **[Mod Support]** Added SAMs sites generator : KS19Generator, SA10BGenerator, SA12Generator, SA17Generator, SA20Generator, SA20BGenerator, SA23Generator    

## Fixes

* **[Hercules]** Updated the default Hercules radio frequency.
* **[Economy]** Pending unit orders at captured bases will be refunded.
* **[UI]** Carrier group SAM threat rings now move with the carrier.
* **[UI]** Base intel menu no longer compresses text, and is now scrollable.
* **[UI]** Edit Flight window is now dynamically sized to adapt to the width of waypoint names, so they no longer get truncated.
* **[UI]** Budget income display is now rounded to 2 decimal places.
* **[UI]** Fixed incorrect income per turn displayed for strike target tooltip.
* **[Factions]** USA with C-130 faction now links to the required mod.
* **[Campaign]** Fixed issue where destroyed buildings would sometimes not count as destroyed and thus respawn.
* **[Campaign]** Fixed issue where destroyed runways were not registered.
* **[Units]** J-11A is no longer spawned with empty loadout.
* **[Units]** F-14B is no longer spawned with empty loadout for fighter sweep tasks.
* **[Units]** Pyotr Velikiy cruiser has been removed for now as it's nearly unkillable.
* **[Units]** Submarines have been removed for now as they aren't wholly functional.
* **[Units]** Fixed "FACTION ERROR : Unable to find OliverHazardPerryGroupGenerator in pydcs" error at startup.
* **[Mission Generator]** Fixed a bug where units set to Aggressive stance sometimes did not move.
* **[Mission Generator]** Flyover points for OCA/Aircraft missions are now generated correctly.
* **[Flight Planner]** Fixed not being able to create custom waypoints for buildings.
* **[Flight Planner]** Strike missions will no longer be automatically planned against SAMs.
* **[Flight Planner]** Strike missions will no longer be automatically planned against FOB structures.

# 2.3.4

## Fixes:
[Mission Generator] Mission generator would crash when generating fire missions for destroyed SCUD sites - fixed

# 2.3.3

## Features/Improvements
* **[Campaigns]** Reworked Golan Heights campaign on Syria, (Added FOB and preset locations for SAMS)
* **[Campaigns]** Added a lite version of the Golan Heights campaign
* **[Campaigns]** Reworked Syrian Civil War campaign (Added FOB and preset locations for SAMS)
* **[Campaigns]** Reworked Emirates campaign
* **[Campaigns]** AA units added to frontlines and updated all factions to include some frontline AA units.
* **[Mission Generator]** Infantry will only be generated for APC and IFV groups
* **[Mission Generator]** Infantry squads size is not randomized anymore
* **[Mission Generator]** Infantry squads can have a mortar. 
* **[Mission Generator]** SCUD missiles sites will now fire on enemy controls points in range when possible
* **[Factions]** Updated Nato Desert Storm to include F-14A
* **[Factions]** Updated Iraq 1991 factions to include Zsu-57 and Mig-29A
* **[Factions]** Germany 1944, added Stug III and Stug IV
* **[Factions]** Added factions Insurgents (Hard) with better and more weapons
* **[Plugins]** [The EWRS plugin](https://github.com/Bob7heBuilder/EWRS) is now included.
* **[UI]** Added enemy intelligence summary and details window.

## Fixes:
* **[Factions]** AI would never buy artillery units for the frontline - fixed
* **[Factions]** Removed the F-111 unit from the NATO desert storm faction. (Recruiting it would cause crashes in DCS, since it is not a valid unit)
* **[Campaign]** Automatic redeployment of ground units would sometimes fail - fixed
* **[Mission Generator]** Artillery groups would retreat in the wrong direction - fixed
* **[Units]** Fixed SPG_Stryker_M1128_MGS not being in db
* **[UI]** Fixed and added many missing ground units icons
* **[UI]** Ship groups could be replaced by SAM sites in the UI, which would lead to broken mission being generated - fixed 
* **[New Game Wizard]** Removed the "mid game" campaign generator option which is currently broken
* **[Mission Generator]** Empty navy groups will no longer be generated
* **[Mission Generator]** Fixed BAI, SEAD, and DEAD flights ocassionally being assigned the wrong targets.
* **[Flight Planner]** Fixed not being able to plan packages against opfor carriers
* **[UI]** Repaired SAMs no longer show as dead.
* **[UI]** Fixed not being able to manage a disbanded site after disbanding and closing the base menu.

# 2.3.2

## Features/Improvements
* **[Units]** Support for newly added BTR-82A, T-72B3
* **[Units]** Added ZSU-57 AAA sites
* **[Culling]** BARCAP missions no longer create culling exclusion zones.
* **[Flight Planner]** Improved TOT planning. Negative start times no longer occur with TARCAPs and hold times no longer affect planning for flight plans without hold points.
* **[Factions]** Added Iraq 1991 faction (thanks again to Hawkmoon!)

## Fixes:
* **[Mission Generator]** Fix mission generation error when there are too many radio frequency to setup for the Mig-21
* **[Mission Generator]** Fix ground units not moving forward
* **[Mission Generator]** Fixed assigned radio channels overlapping with beacons.
* **[Flight Planner]** Fix creation of custom waypoints.
* **[Campaigns]** Fixed many cases of SAMs spawning on the runways/taxiways in Syria Full.

# 2.3.1

## Features/Improvements
* **[UX]** Added a warning message when the player is attempting to buy more planes at an already full airbase. 
* **[Campaigns]** Migrated Syria full map to new format. (Thanks to Hawkmoon)
* **[Faction]** Added NATO desert Storm faction (Thanks to Hawkmoon)

## Fixes:
* **[AI]** CAP flights will engage enemies again.
* **[Campaigns]** Fixed a missing path on the Caucasus Full Map campaign

# 2.3.0

## Features/Improvements
* **[Campaign Map]** Overhauled the campaign model
* **[Campaign Map]** Possible to add FOB as control points
* **[Campaign Map]** Added off-map spawn locations
* **[Campaign AI]** Overhauled AI recruiting behaviour
* **[Campaign AI]** Added AI procurement for Blue
* **[Campaign]** New Campaign: "Black Sea"
* **[Mission Planner]** Possible to move carrier and tarawa on the campaign map
* **[Mission Generator]** Infantry squads on frontline can have manpads
* **[Mission Generator]** Unused aircraft now spawned to allow for OCA strikes
* **[Mission Generator]** Opfor now obeys parking limits
* **[Mission Generator]** Support for Anubis C-130 Hercules mod
* **[Flight Planner]** Added fighter sweep missions.
* **[Flight Planner]** Added BAI missions.
* **[Flight Planner]** Added anti-ship missions.
* **[Flight Planner]** Differentiated BARCAP and TARCAP. TARCAP is now for hostile areas and will arrive before the package.
* **[Flight Planner]** Added OCA missions
* **[Flight Planner]** Added Alternate/divert airfields
* **[Culling]** Added possibility to include/exclude carriers from culling zones
* **[QOL]** On liberation startup, your latest save game is loaded automatically
* **[Units]** Reduced starting fuel load for C101
* **[UI]** Inform the user of the weather
* **[UI]** Added toolbar buttons to change map display settings
* **[Game]** Added new Economy options for adjusting income multipliers and starting budgets.

## Fixes :
* **[Map]** Missiles sites now have a proper icon and will not re-use the SAM sites icon
* **[Mission Generator]** Ground unit waypoints improperly set to "On Road" - fixed
* **[Mission Generator]** Target waypoints not at ground level - fixed
* **[Mission Generator]** Selected skill not applied to Helicopters - fixed
* **[Mission Generator]** Ground units do not always spawn - fixed
* **[Kneeboard]** Briefing waypoints off by one - fixed
* **[Game]** Destroyed buildings still granting budget - fixed

# 2.2.1

## Features/Improvements
* **[Factions]** Added factions : Georgia 2008, USN 1985, France 2005 Frenchpack by HerrTom
* **[Factions]** Added map Persian Gulf full by Plob
* **[Flight Planner]** Player flights with start delays under ten minutes will spawn immediately.
* **[UI]** Mission start screen now informs players about delayed flights.
* **[Units]** Added support for F-14A-135-GR
* **[Modding]** Possible to setup liveries overrides in factions definition files

## Fixes :
* **[Flight Planner]** Hold, join, and split points are planned cautiously near enemy airfields. Ascend/descend points are no longer planned.
* **[Flight Planner]** Custom waypoints are usable again. Not that in most cases custom flight plans will revert to the 2.1 flight planning behavior.
* **[Flight Planner]** Fixed UI bug that made it possible to create empty flights which would throw an error.
* **[Flight Planner]** Player flights from carriers will now be delayed correctly according to the player's settings.
* **[Misc]** Spitfire variant with clipped wings was not seen as flyable by DCS Liberation (hence could not be setup as client/player slot)
* **[Misc]** Updated Syria terrain parking slots database, the out-of-date database could end up generating aircraft in wrong slots (We are still experiencing issues with somes airbases, such as Khalkhalah though)

# 2.2.0

## Features/Improvements :
* **[Campaign Generator]** Added early warning radar generation
* **[Campaign Generator]** Added scud launcher sites
* **[Cheat Menu]** Added ability to capture base from mission planner
* **[Cheat Menu]** Added ability to show red ATO
* **[Factions]** Added WW2 factions that do not depend on WW2 asset pack
* **[Factions]** Cold War / Middle eastern factions will use Flak sites
* **[Flight Planner]** Flight planner overhaul, with package and TOT system
* **[Flight Planner]** Pick runways and ascent/descent based on headwind
* **[Map]** Added polygon debug mode display
* **[Map]** Highlight the selected flight path on the map
* **[Map]** Improved SAM display settings
* **[Map]** Improved flight plan display settings
* **[Map]** Caucasus and The Channel map use a new system to generate SAM and strike target location to reduce probability of targets generated in the middle of a forests
* **[Misc]** Flexible Dedicated Hosting Options for Mission Files via environment variables
* **[Moddability]** Custom campaigns can be designed through json files
* **[Moddability]** LUA plugins can now be injected into Liberation missions.
* **[Moddability]** Optional Skynet IADS lua plugin now included
* **[New Game]** Starting budget can be freely selected
* **[New Game]** Exanded information for faction and campaign selection in the new game wizard
* **[UI]** Add double and right click actions to many UI elements.
* **[UI]** Add polygon drawing mode for map background
* **[UI]** Added a warning if you press takeoff with no player enabled flights
* **[UI]** Packages and flights now visible in the main window sidebar
* **[Units/Factions]** Added bombers to some coalitions
* **[Units/Factions]** Added support for SU-57 mod by Cubanace
* **[Units]** Added Freya EWR sites to german WW2 factions
* **[Units]** Added support for many bombers (B-52H, B-1B, Tu-22, Tu-142)
* **[Units]** Added support for new P-47 variants

## Fixes :
* **[Campaign Generator]** Big airbases could end up without any airbase defense.
* **[Campaign generator]** Ship group and offshore buildings should not be generated on land anymore
* **[Flight Planner]** Fix waypoint alitudes for helicopters
* **[Flight Planner]** Fixed CAS aircraft wandering away from frontline
* **[Maps]** Incirlik airbase was missing exclusions zones, so SAMS could end up being generated on the runway
* **[Mission Generator]** Fixed player/client confusion when a flight had only one player slot.
* **[Radios]** Fix A-10C radio
* **[UI]** Many missing unit icons were added
* **[UI]** Missing TER weapons in custom payload now selectable.

# 2.1.5

## Features/Improvements :
* **[Units/Factions]** Enabled EPLRS for ground units that supports it (so they appear on A-10C II TAD and Helmet)

## Fixes :
* **[UI]** Fixed an issue that prevent saving after aborting a mission
* **[Mission Generator]** Fixed aircraft landing point type being wrong

# 2.1.4

## Fixes :
* **[UI]** Fixed an issue that prevented generating the mission (take off button no working) on old savegames.

## Features/Improvements :
* **[Units/Factions]** Added A-10C_2 to USA 2005 and Bluefor modern factions
* **[UI]** Limit number of aircraft that can be bought to the number of available parking slots.
* **[Mission Generator]** Use inline loading of the JSON.lua library, and save to either %LIBERATION_EXPORT_DIR%, or to DCS working directory

## Changes :
* **[Units/Factions]** Bluefor generic factions will now use the new "Combined Joint Task Forces Blue" country in the generated mission instead of "USA"

## Fixes :
* **[UI]** Fixed icon for Viggen
* **[UI]** Added icons for some ground units
* **[Misc]** Fixed issue with Chinese characters in pydcs preventing generating the mission. (Take Off button not working) (thanks to spark135246)
* **[Misc]** Fixed an error causing with ATC frequency preventing generating the mission. (Take Off button not working) (thanks to danalbert)

# 2.1.2

## Fixes :
* **[Mission Generator]** Fix mission generation issues with radio frequencies (Thanks to contributors davidp57 and danalbert)
* **[Mission Generator]** AI should now properly plan flights for Tornados

# 2.1.1

## Features/Improvements :
* **[Other]** Added an installer option (thanks to contributor parithon)
* **[Kneeboards]** Generate mission kneeboards for player flights. Kneeboards include
  airfield/carrier information (ATC frequencies, ILS, TACAN, and runway
  assignments), assigned radio channels, waypoint lists, and AWACS/JTAC/tanker
  information. (Thanks to contributor danalbert)
* **[Radios]** Allocate separate intra-flight channels for most aircraft to reduce global
  chatter. (Thanks to contributor danalbert)
* **[Radios]** Configure radio channel presets for most aircraft. Currently supported are:
  * AJS37
  * AV-8B
  * F-14B
  * F-16C
  * F/A-18C
  * JF-17
  * M-2000C (Thanks to contributor danalbert)
* **[Base Menu]** Added possibility to repair destroyed SAM and base defenses units for the player (Click on a SAM site to fix it)
* **[Base Menu]** Added possibility to buy/sell/replace SAM units
* **[Map]** Added recon images for buildings on strike targets, click on a Strike target to get detailled informations
* **[Units/Factions]** Added F-16C to USA 1990
* **[Units/Factions]** Added MQ-9 Reaper as CAS unit for USA 2005
* **[Units/Factions]** Added Mig-21, Mig-23, SA-342L to Syria 2011
* **[Cheat Menu]** Added buttons to remove money

## Fixed issues :
* **[UI/UX]** Spelling issues (Thanks to contributor steveveepee)
* **[Campaign Generator]** LHA was placed on land in Syrian Civil War campaign
* **[Campaign Generator]** Fixed inverted configuration for Syria full map
* **[Campaign Generator]** Syria "Inherent Resolve" campaign, added Incirlik Air Base
* **[Mission Generator]** AH-1W was not used by AI to generate CAS mission by default
* **[Mission Generator]** Fixed F-16C targeting pod not being added to payload
* **[Mission Generator]** AH-64A and AH-64D payloads fix. 
* **[Units/Factions]** China will use KJ-2000 as awacs instead of A-50

# 2.1.0

## Features/Improvements :

* **[Campaign Generator]** Added Syria map
* **[Campaign Generator]** Added 5 campaigns for the Syria map
* **[Campaign Generator]** Added 2 small scale campaign for Persian Gulf map
* **[Units/Factions]** Added factions for Syria map : Syria 2011, Arab Armies 1982, 1973, 1968, 1948, Israel 1982, 1973, 1948
* **[Base Menu]** Budget is visible in recruitment menu. (Thanks to Github contributor root0fall)
* **[Misc]** Added error message in mission when the state file can not be written
* **[Units/Factions]** China, Pakistan, UAE will now use the new WingLoong drone as JTAC instead of the MQ-9 Reaper
* **[Units/Factions]** Minor changes to Syria 2011 and Turkey 2005 factions
* **[UI]** Version number is shown in about dialog

## Fixed issues :

* **[Mission Generator]** Caucasus terrain improvement on exclusions zone (added forests between Vaziani and Beslan to exclusion zones)
* **[Mission Generator]** The first unit of every base defenses group could not be controlled with Combined Arms.
* **[Mission Generator]** Reduced generated helicopter altitude for CAS missions
* **[Mission Generator]** F-16C default CAS payload was asymmetric, fixed.
* **[Mission Generator]** AH-1W couldn't be bought, and added default payloads.
* **[UI/UX]** Fixed Mi-28N missing thumbnail
* **[UI/UX]** Fixed list of flights not refreshing when changing the mission departure (T+).

# 2.0.11

## Features/Improvements :

* **[Units/Factions]** Added Mig-31, Su-30, Mi-24V, Mi-28N to Russia 2010 faction.
* **[Units/Factions]** Added F-15E to USA 2005 and USA 1990 factions.
* **[Mission Generator]** Added a parameter to choose whether the JTACs should use smoke markers or not

## Fixed issues : 

* **[Units/Factions]** Fixed big performance issue in new release UI that occurred only when running the .exe
* **[Units/Factions]** Fixed mission generation not working with Libya faction
* **[Units/Factions]** Fixed OH-58D not being used by AI
* **[Units/Factions]** Typo in UK 1990 name (fixed by bwRavencl)
* **[Units/Factions]** Fixed Tanker Tacan channel not being the same as the briefing one. (Sorry)
* **[Mission Generator]** Neutral airbases services will now be disabled. (Not possible to refuel or re-arm there)
* **[Mission Generator]** AI will be configured to limit afterburner usage
* **[Mission Generator]** JTAC will not use laser codes above 1688 anymore
* **[Mission Generator]** JTAC units were misconfigured and would not be invisible/immortal. 
* **[Mission Generator]** Increased JTAC status message duration to 25s, so you have more time to enter coordinates;
* **[Mission Generator]** Destroyed units carcass will not appear on airfields to avoid having a destroyed vehicle blocking a runway or taxiway.


# 2.0.10

## Features/Improvements :
* **[Misc]** Now possible to save game in a different file, and to open DCS Liberation savegame files. (You are not restricted to a single save file anymore)
* **[UI/UX]** New dark UI Theme and default theme improvement by Deus
* **[UI/UX]** New "satellite" map backgrounds
* **[UX]** Base menu is opened with a single mouse click
* **[Units/Factions/Mods]** Added Community A-4E-C support for faction Bluefor Cold War
* **[Units/Factions/Mods]** Added MB-339PAN support for faction Bluefor Cold War  
* **[Units/Factions/Mods]** Added Rafale AI mod support
* **[Units/Factions/Mods]** Added faction "France Modded" with units from frenchpack v3.5 mod
* **[Units/Factions/Mods]** Added faction "Insurgent modded" with Insurgent units from frenchpack v3.5 mod (Toyota truck)
* **[Units/Factions/Mods]** Added factions Canada 2005, Australia 2005, Japan 2005, USA Aggressors, PMC
* **[New Game Wizard]** Added the list of required mods for modded factions.
* **[New Game Wizard]** No more RED vs BLUE opposing faction restrictions.
* **[New Game Wizard]** New campaign generation settings added : No aircraft carrier, no lha, no navy, invert map starting positions.
* **[Mission Generator]** Artillery units will start firing mission after a random delay. It should reduces lag spikes induced by artillery strikes by spreading them out.
* **[Mission Generator]** Ground units will retreat after taking too much casualties. Artillery units will retreat if engaged.
* **[Mission Generator]** The briefing will now contain the carrier ATC frequency
* **[Mission Generator]** The briefing contains a small situation update.
* **[Mission Generator]** Previously destroyed units are visible in the mission. (And added a performance settings to disable this behaviour)
* **[Mission Generator]*c* Basic JTAC on Frontlines
* **[Campaign Generator]** Added Tarawa in caucasus campaigns
* **[Campaign Generator]** Tuned the various existing campaign parameters
* **[Campaign Generator]** Added small campaign : "Russia" on Caucasus Theater 

## Fixed issues :
* **[Mission Generator]** Carrier will sail into the wind, not in the same direction
* **[Mission Generator]** Carrier cold start was not working (flight was starting warm even when cold was selected)
* **[Mission Generator]** Carrier group ships are more spread out
* **[Mission Generator]** Fixed wrong radio frequency for german WW2 warbirds
* **[Mission Generator]** Fixed FW-190A8 spawning with bomb rack for CAP missions
* **[Mission Generator]** Fixed A-20G spawning with no payload
* **[Mission Generator]** Fixed Su-33 spawning too heavy to take off from carrier
* **[Mission Generator]** Fixed Harrier AV-8B spawning too heavy to take off from tarawa
* **[Mission Generator]** Base defense units were not controllable with Combined Arms
* **[Mission Generator]** Tanker speed was too low
* **[Mission Generator]** Tanker TACAN settings were wrong
* **[Mission Generator]** AI aircraft should start datalink ON (EPLRS)
* **[Mission Generator]** Base defense units should not spawn on runway and or taxyway. (The chance for this to happen should now be really really low)
* **[Mission Generator]** Fixed all flights starting "In flight" after playing a few missions (parking slot reset issue)
* **[Mission Script/Performance]** Mission lua script will not listen to weapons fired event anymore and register every fired weapons. This should improve performance especially in WW2 scenarios or when rocket artillery is firing. 
* **[Campaign Generator]** Carrier name will now not appear for faction who do not have carriers
* **[Campaign Generator]** SA-10 sites will now have a tracking radar.
* **[Units/Factions]** Remove JF-17 from USA 2005 faction
* **[Units/Factions]** Remove AJS-37 from Russia 2010
* **[Units/Factions]** Removed Oliver Hazard Perry from cold war factions (too powerful sam system for the era)
* **[Bug]** On the persian gulf full map campaign, the two carriers were sharing the same id, this was causing a lot of bugs
* **[Performance]** Tuned the culling setting so that you cannot run into situation where no friendly or enemy AI flights are generated
* **[Other]** Application doesn't gracefully exit.
* **[Other]** Other minor fixes, and multiples factions small changes

# 2.0 RC 9

## Features/Improvements :
* **[UI/UX]** New icons from contributor Deus

## Fixed issues :
* **[Mission Generator]** Carrier TACAN was wrongfully set up as an A/A TACAN
* **[Campaign Generator]** Fixed issue with Russian navy group generator causing a random crash on campaign creation.

# 2.0 RC 8

## Fixed issues :
* **[Mission Generator]** Frequency for P-47D-30 changed to 124Mhz (Generated mission with 251Mhz would not work)
* **[Mission Generator]** Reduced the maximum number of uboat per generated group
* **[Mission Generator]** Fixed an issue with the WW2 LST groups (superposed units).
* **[UI]** Fixed issue with the zoom

# 2.0 RC 7

## Features/Improvements :

* **[Units/Factions]** Added P-47D-30 for factions allies_1944
* **[Units/Factions]** Added factions : Bluefor Coldwar, Germany 1944 Easy

* **[Campaign/Map]** Added a campaign in the Channel map
* **[Campaign/Map]** Changed the Normandy campaign map
* **[Campaign/Map]** Added new campaign Normandy Small

* **[Mission Generator]** AI Flight generator has been reworked
* **[Mission Generator]** Add PP points for JF-17 on STRIKE missions
* **[Mission Generator]** Add ST point for F-14B on STRIKE missions
* **[Mission Generator]** Flights with client slots will never be delayed
* **[Mission Generator]** AI units can start from parking (With a new setting in Settings Window to disable it)
* **[Mission Generator]** Tacan for carrier will only be in Mode X from now
* **[Mission Generator]** RTB waypoints for autogenerated flights

* **[Flight Planner]** Added CAS mission generator
* **[Flight Planner]** Added CAP mission generator
* **[Flight Planner]** Added SEAD mission generator
* **[Flight Planner]** Added STRIKE mission generator
* **[Flight Planner]** Added buttons to add autogenerated waypoints (ASCEND, DESCEND, RTB)
* **[Flight Planner]** Improved waypoint list
* **[Flight Planner]** WW2 factions uses different parameters for flight planning.

* **[Settings]** Added settings to disallow external views
* **[Settings]** Added settings to choose F10 Map mode (All, Allies only, Player only, Fog of War, Map Only)
* **[Settings]** Added settings to choose whether to auto-generate objective marks on the F10 map

* **[Info Panel]** Added information about destroyed buildings in info panel
* **[Info Panel]** Added information about destroyed units at SAM site in info panel
* **[Debriefing]** Added information about units destroyed outside the frontline in the debriefing window
* **[Debriefing]** Added destroyed buildings in the debriefing window

* **[Map]** Tooltip now contains the list of building for Strike targets on the map
* **[Map]** Added "Oil derrick" building
* **[Map]** Added "ww2 bunker" building (WW2)
* **[Map]** Added "ally camp" building (WW2)
* **[Map]** Added "V1 Site" (WW2)

* **[Misc]** Made it possible to setup DCS Saved Games directory and DCS installation directory manually at first start
* **[Misc]** Added culling performance settings 

## Fixed issues :

* **[Units/Factions]** Replaced S3-B Tanker by KC130 for most factions (More fuel)
* **[Units/Factions]** WW2 factions will not have offshore oil station and other modern buildings generated. No more third-reich operated offshore stations will spawn on normandy's coast. 
* **[Units/Factions]** Aircraft carrier will try to move in the wind direction
* **[Units/Factions]** Missing icons added for some aircraft

* **[Mission Generator]** When playing as RED the activation trigger would not be properly generated
* **[Mission Generator]** FW-190A8 is now properly considered as a flyable aircraft
* **[Mission Generator]** Changed "strike" payload for Su-24M that was ineffective
* **[Mission Generator]** Changed "strike" payload for JF-17 to use LS-6 bombs instead of GBU
* **[Mission Generator]** Change power station template. (Buildings could end up superposed).

* **[Maps/Campaign]** Now using Vasiani airbase instead of Soganlung airport in Caucasus campaigns (more parking slot)
* **[Info Panel]** Message displayed on base capture event stated that the enemy captured an airbase, while it was the player who captured it.
* **[Map View]** Graphical glitch on map when one building of an objective was destroyed, but not the others 
* **[Mission Planner]** The list of flights was not updated on departure time change. 


# 2.0 RC 6

Saves file from RC5 are not compatible with the new version. 
Sorry :(

## Features/Improvements :
* **[Units/Factions]** Supercarrier support (You have to go to settings to enable it, if you have the supercarrier module)
* **[Units/Factions]** Added 'Modern Bluefor' factions, containing all most popular DCS flyable units
* **[Units/Factions]** Factions US 2005 / 1990 will now sometimes have Arleigh Burke class ships instead of Perry as carrier escorts 
* **[Units/Factions]** Added support for newest WW2 Units
* **[Campaign logic]** When a base is captured, refill the "base defenses" group with units for the new owner.
* **[Mission Generator]** Carrier ICLS channel will now be configured (check your briefing)
* **[Mission Generator]** SAM units will spawn on RED Alarm state
* **[Mission Generator]** AI Flight planner now creates its own STRIKE flights
* **[Mission Generator]** AI units assigned to Strike flight will now actually engage the buildings they have been assigned.
* **[Mission Generator]** Added performance settings to allow disabling : smoke, artillery strike, moving units, infantry, SAM Red alert mode.
* **[Mission Generator]** Using Late Activation & Trigger in attempt to improve performance & reduce stutter (Previously they were spawned through 'ETA' feature)
* **[UX]** : Improved flight selection behaviour in the Mission Planning Window
 
## Fixed issues :
* **[Mission Generator]** Payloads were not correctly assigned in the release version. 
* **[Mission Generator]** Game generation does not work when "no night mission" settings was selected and the current time was "day"
* **[Mission Generator]** Game generation does not work when the player selected faction has no AWACS
* **[Mission Generator]** Planned flights will spawn even if their home base has been captured or is being contested by enemy ground units. 
* **[Campaign Generator]** Base defenses would not be generated on Normandy map and in some rare cases on others maps as well
* **[Mission Planning]** CAS waypoints created from the "Predefined waypoint selector" would not be at the exact location of the frontline
* **[Naming]** CAP mission flown from airbase are not named BARCAP anymore (CAP from carrier is still named BARCAP)
