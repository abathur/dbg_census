dbg_census
=======

dbg_census is a minimalist Python wrapper for the Daybreak Games Census API, which provides stats
and other information for DBG titles like Planetside 2, Everquest 2, and DC Universe Online.

The wrapper is "minimalist" because it doesn't hide the (considerable) complexity of the Census APIs
from the end user; you won't be able to use this wrapper without consulting the API docs at:
http://census.daybreakgames.com/

Because this module isn't tightly coupled to the individual APIs it supports, there's a reduced risk
of changes to the API making this module unusable. I chose stability and reliability over usability.
That said, I'll gladly support those who maintain simplified user-friendly interfaces built on dbg_census
for either the entire API, specific games, or even narrow tasks. I'll gladly link to you here, and
I'll be responsive to issues/PRs.

*This project is not maintained, supported by, or affiliated with Daybreak Games or any of its staff.*

##Installation
can install with:

	pip install git+https://github.com/abathur/dbg_census.git

or add to requirements.txt:

	git+https://github.com/abathur/dbg_census.git

##Usage

	>>> from dbg_census import ps2

	>>> api = ps2.Stats() # uses "example" service ID by default, but this is highly throttled

	api.collections()
	[u'single_character_by_id', u'character', u'character_name', u'characters_achievement', u'characters_currency', u'characters_directive', u'characters_directive_objective', u'characters_directive_tier', u'characters_directive_tree', u'characters_skill', u'characters_stat', u'characters_stat_by_faction', u'characters_stat_history', u'characters_weapon_stat', u'characters_weapon_stat_by_faction', u'world_stat_history', u'characters_item', u'ability', u'ability_type', u'achievement', u'currency', u'directive', u'directive_tier', u'directive_tree', u'directive_tree_category', u'effect', u'effect_type', u'empire_scores', u'experience', u'experience_rank', u'facility_link', u'facility_type', u'faction', u'fire_group', u'fire_group_to_fire_mode', u'fire_mode', u'fire_mode_2', u'fire_mode_to_projectile', u'fire_mode_type', u'image', u'image_set', u'image_set_default', u'item', u'item_attachment', u'item_category', u'item_profile', u'item_to_weapon', u'item_type', u'loadout', u'map_hex', u'map_region', u'marketing_bundle', u'marketing_bundle_item', u'marketing_bundle_with_1_item', u'metagame_event', u'metagame_event_state', u'objective', u'objective_set_to_objective', u'objective_type', u'player_state', u'player_state_group', u'player_state_group_2', u'profile', u'projectile', u'projectile_flight_type', u'region', u'resist_type', u'resource_type', u'reward', u'reward_group_to_reward', u'reward_set_to_reward_group', u'reward_type', u'skill', u'skill_category', u'skill_line', u'skill_set', u'target_type', u'title', u'vehicle', u'vehicle_attachment', u'vehicle_faction', u'vehicle_skill_set', u'weapon', u'weapon_ammo_slot', u'weapon_datasheet', u'weapon_to_attachment', u'weapon_to_fire_group', u'zone', u'zone_effect', u'zone_effect_type', u'characters_world', u'world', u'outfit', u'outfit_member', u'outfit_member_extended', u'outfit_rank', u'characters_online_status', u'map', u'characters_friend', u'leaderboard', u'characters_leaderboard', u'characters_event_grouped', u'characters_event', u'event', u'world_event', u'cached_vehicle']

	>>> api.collection('character')
	{u'count': u'?', u'hidden': False, u'resolve_list': [u'item', u'item_full', u'profile', u'faction', u'stat', u'stat_by_faction', u'weapon_stat', u'weapon_stat_by_faction', u'stat_history', u'online_status', u'friends', u'world', u'outfit', u'outfit_member', u'outfit_member_extended', u'currency'], u'name': u'character'}

	>>> fcrw = api("outfit", {"alias":"FCRW", "c:resolve":"member_online_status,member_character(name)"})
	>>> members = fcrw["outfit_list"][0]["members"]
	>>> member_ids = map(lambda x: x['character_id'], members)
	>>> member_ids
	[u'5428010618015208209', u'5428010618015209153', u'5428010618015213777', u'5428010618015228017', u'5428010618015230897', u'5428010618015232161', u'5428010618015255073', u'5428010618015275537', u'5428010618015286209', u'5428010618015297201', u'5428010618015301745', u'5428010618034980305', u'5428010618035005697', u'5428010618035017169', u'5428010618035023761', u'5428010618035457057', u'5428010618035493729', u'5428010618035705265', u'5428010618035717681', u'5428010618036245169', u'5428010618037262881', u'5428010618037744417', u'5428010618037777585', u'5428010618038254881', u'5428010618039111265', u'5428010618040281025', u'5428010618040694241', u'5428010618040699201', u'5428010618041084721', u'5428010618041103809', u'5428010618041341009', u'5428010618041367793', u'5428010618042665809', u'5428010618043524353', u'5428010618043995057', u'5428010917232013873', u'5428011263320303409', u'5428011263339904577', u'5428011263364508001', u'5428011263371789297', u'5428011263375306177', u'5428011263390536977', u'5428011263433450049', u'5428013610385654561', u'5428016459718877265', u'5428016459719767953', u'5428016813493180417', u'5428019223832359665', u'5428021124280549937', u'5428021124280566945', u'5428021124280567409', u'5428021124280656625', u'5428021759076505841', u'5428021759079578753', u'5428031585332962609', u'5428044677947768257', u'5428052273455371601', u'5428054819620325553', u'5428059164951844497', u'5428059164951847633', u'5428059164961558081', u'5428059527738994769', u'5428059527764501905', u'5428059527765244881', u'5428059527811818481', u'5428061686732082129', u'5428064605488651281', u'5428064957327809745', u'5428069961262732113', u'5428069961263076657', u'5428072203500633793', u'5428077644802319393', u'5428077649510812065', u'5428082720373025697', u'5428087454633381313', u'5428095401437254545', u'5428102290040067937', u'5428102290044486129', u'5428105192792626945', u'5428109895939498257', u'5428117870033775521', u'5428130184545531585', u'5428130184555353537', u'5428147970872513585', u'5428163811599438737', u'5428168624813723505', u'5428168624838235793', u'5428168624839069697', u'5428184188516093281', u'5428191068389222321', u'5428197983250395681', u'5428200837430590849', u'5428201940312751137', u'5428201940314275857', u'5428316104355126801']

	>>> filter(lambda x: x['name']['first_lower'] == 'abathur', members)
	[{u'rank_ordinal_merged': u'4', u'character_id': u'5428010618039111265', u'name': {u'first_lower': u'abathur', u'first': u'abathur'}, u'member_since_date_merged': u'2013-07-10 20:31:40.0', u'member_since': u'1373488300', u'online_status': u'0', u'rank': u'Rainbow Warrior', u'character_id_merged': u'5428010618039111265', u'rank_ordinal': u'4', u'rank_merged': u'Rainbow Warrior', u'member_since_merged': u'1373488300', u'member_since_date': u'2013-07-10 20:31:40.0'}]
