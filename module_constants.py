##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_faction_id                = 0
slot_player_spawn_state               = 1 # listed below, starting with player_spawn_state_
slot_player_spawn_invulnerable_time   = 2 # mission time when the player spawned with temporary invlunerability
slot_player_spawn_health_percent      = 3 # saved health percentage to be applied when next spawning
slot_player_spawn_entry_point         = 4 # entry point used at last spawn

player_spawn_state_dead               = 0
player_spawn_state_invulnerable       = 1 # while invlunerable soon after spawning
player_spawn_state_at_marker          = 2 # set before spawning to indicate that the agent should be shifted to the player's marker scene prop
player_spawn_state_alive              = 3

slot_player_inactive_index            = 5 # index in the inactive players array, if stored
slot_player_next_chat_event_type      = 6 # next chat event number that the server expects this player's client to use
slot_player_list_button_id            = 7 # overlay id in the player list presentation
slot_player_outlaw_rating             = 8
slot_player_is_lord                   = 9
slot_player_non_lord_troop_id         = 10 # the last troop used before changing to a lord only troop, to revert after respawning if someone else is voted lord
slot_player_poll_faction_id           = 11 # marks whether the player can vote in the current poll
slot_player_requested_spawn_point     = 12 # the spawn point requested by the player after dying, if any; -1 to indicate a newly connected player that hasn't yet requested to spawn
slot_player_has_faction_door_key      = 13
slot_player_has_faction_money_key     = 14
slot_player_has_faction_item_key      = 15
slot_player_teleport_to_ship_no       = 16 # instance no of the last ship teleported to with the admin tool
slot_player_last_faction_kicked_from  = 17 # stores when kicked from a faction, so subsequent kicks can be free of cost
slot_player_accessing_instance_id     = 18 # stores the instance id of the inventory currently being accessed by the player, for updates if anyone else changes it
slot_player_last_action_time          = 19 # mission time of the last action that should be prevented from quick repetition

slot_player_equip_item_0              = 20 # module equipment slots corresponding to the hard coded ones in header_items starting with ek_
slot_player_equip_item_1              = 21
slot_player_equip_item_2              = 22
slot_player_equip_item_3              = 23
slot_player_equip_head                = 24
slot_player_equip_body                = 25
slot_player_equip_foot                = 26
slot_player_equip_gloves              = 27
slot_player_equip_horse               = 28
slot_player_equip_end                 = 29
slot_player_equip_item_0_ammo         = 30
slot_player_equip_item_1_ammo         = 31
slot_player_equip_item_2_ammo         = 32
slot_player_equip_item_3_ammo         = 33

slot_player_spawn_food_amount         = 34 # saved food for next spawn
slot_player_faction_chat_muted        = 35
slot_player_kick_at_time              = 36 # time to kick a player after the name server has rejected them, to allow time to recieve the message
slot_player_can_faction_announce      = 37
slot_player_next_spawn_health_percent = 38 # spawn health percentage for the troop applied after death, if that server option is enabled
slot_player_accessing_unique_id       = 39 # a unique number identifying an inventory scene prop being accessed that could despawn and the instance id be reused, like corpses

slot_player_admin_no_panel            = 40 # admin permission slots: the default value 0 is permissive so everything works when a name server is not connected
slot_player_admin_no_gold             = 41
slot_player_admin_no_kick             = 42
slot_player_admin_no_temporary_ban    = 43
slot_player_admin_no_permanent_ban    = 44
slot_player_admin_no_kill_fade        = 45
slot_player_admin_no_freeze           = 46
slot_player_admin_no_teleport_self    = 47
slot_player_admin_no_admin_items      = 48
slot_player_admin_no_heal_self        = 49
slot_player_admin_no_godlike_troop    = 50
slot_player_admin_no_ships            = 51
slot_player_admin_no_announce         = 52
slot_player_admin_no_override_poll    = 53
slot_player_admin_no_all_items        = 54
slot_player_admin_no_mute             = 55
slot_player_admin_no_animals          = 56
slot_player_admin_no_factions         = 57
slot_player_admin_end                 = 58
slot_player_character_language        = 59

# PN START *********************************

player_character_language_french = 1
player_character_language_english = 2
player_character_language_austrian = 3
player_character_language_prussian = 4
player_character_language_russian = 5
player_character_language_pirate = 6

voice_type_cry                         = 1
voice_type_surrender                   = 2
voice_type_comm_ready                  = 3
voice_type_comm_present                = 4
voice_type_comm_fire                   = 5
voice_type_comm_charge                 = 6
voice_type_comm_advance                = 7
voice_type_comm_hold                   = 8
voice_type_comm_fire_at_will           = 9
voice_type_comm_on_me                  = 10
voice_type_comm_fall_back              = 11
voice_types_begin                      = voice_type_cry
voice_types_end                        = 12

music_type_start                       = 1
music_type_stop                        = 2
music_type_toggle_together             = 3
music_types_begin                      = music_type_start
music_types_end                        = 4

spyglass_type_start                    = 1
spyglass_type_stop                     = 2

drinking_type_start                    = 1
drinking_type_stop                     = 2

server_action_force_music_selection = 1
server_actions_begin                = server_action_force_music_selection
server_actions_end                  = 2

player_action_change_lang                   = 87
player_action_voice                         = 88
player_action_music                         = 89
player_action_spyglass                      = 90
player_action_place_rocket                  = 91
player_action_toggle_walk                   = 92
player_action_has_cheat                     = 93
player_action_surrender                     = 94
player_action_misc_item_drinking            = 95
player_action_custom_order_menu_interact    = 96
player_action_misc_item_drinking            = 97
player_action_custom_order_menu_interact    = 98
player_actions_begin                        = player_action_voice
player_actions_end                          = 99

instrument_max_tracks = 20 #if adding more than 20 tracks in any list you need to increase this number

drum_sounds_britain_begin = "snd_drum_britain_1"
drum_sounds_britain_end   = "snd_drum_france_1"
drum_sounds_france_begin = drum_sounds_britain_end
drum_sounds_france_end   = "snd_drum_prussia_1"
drum_sounds_prussia_begin = drum_sounds_france_end
drum_sounds_prussia_end   = "snd_drum_russia_1"
drum_sounds_russia_begin = drum_sounds_prussia_end
drum_sounds_russia_end   = "snd_drum_austria_1"
drum_sounds_austria_begin = drum_sounds_russia_end
drum_sounds_austria_end   = "snd_drum_highland_1"
drum_sounds_highland_begin = drum_sounds_austria_end
drum_sounds_highland_end   = "snd_drum_signal_1"
drum_sounds_calls_begin = drum_sounds_highland_end
drum_sounds_calls_end   = "snd_fife_britain_1"

fife_sounds_britain_begin = drum_sounds_calls_end
fife_sounds_britain_end   = "snd_fife_france_1"
fife_sounds_france_begin = fife_sounds_britain_end
fife_sounds_france_end   = "snd_fife_prussia_1"
fife_sounds_prussia_begin = fife_sounds_france_end
fife_sounds_prussia_end   = "snd_fife_russia_1"
fife_sounds_russia_begin = fife_sounds_prussia_end
fife_sounds_russia_end   = "snd_fife_austria_1"
fife_sounds_austria_begin = fife_sounds_russia_end
fife_sounds_austria_end   = "snd_bugle_britain_1"

bugle_sounds_britain_begin = fife_sounds_austria_end
bugle_sounds_britain_end   = "snd_bugle_france_1"
bugle_sounds_france_begin = bugle_sounds_britain_end
bugle_sounds_france_end   = "snd_bugle_prussia_1"
bugle_sounds_prussia_begin = bugle_sounds_france_end
bugle_sounds_prussia_end   = "snd_bugle_russia_1"
bugle_sounds_russia_begin = bugle_sounds_prussia_end
bugle_sounds_russia_end   = "snd_bugle_austria_1"
bugle_sounds_austria_begin = bugle_sounds_russia_end
bugle_sounds_austria_end   = "snd_bugle_signal_1"
bugle_sounds_calls_begin = bugle_sounds_austria_end
bugle_sounds_calls_end   = "snd_bagpipes_britain_1"

bagpipes_sounds_britain_begin = bugle_sounds_calls_end
bagpipes_sounds_britain_end   = "snd_bagpipes_extra_1"
bagpipes_sounds_extra_begin = bagpipes_sounds_britain_end
bagpipes_sounds_extra_end   = "snd_piano_loop_1"

piano_sounds_begin = bagpipes_sounds_extra_end
piano_sounds_end   = "snd_organ_loop_1"

organ_sounds_begin = piano_sounds_end
organ_sounds_end   = "snd_instruments_end"

instrument_sounds_begin   = drum_sounds_britain_begin
instruments_sounds_end    = organ_sounds_end

drum_strings_britain_begin = "str_drum_britain_1"
drum_strings_france_begin = "str_drum_france_1"
drum_strings_prussia_begin = "str_drum_prussia_1"
drum_strings_russia_begin = "str_drum_russia_1"
drum_strings_austria_begin = "str_drum_austria_1"
drum_strings_highland_begin = "str_drum_highland_1"
drum_strings_calls_begin = "str_drum_signal_1"

fife_strings_britain_begin = "str_fife_britain_1"
fife_strings_france_begin = "str_fife_france_1"
fife_strings_prussia_begin = "str_fife_prussia_1"
fife_strings_russia_begin = "str_fife_russia_1"
fife_strings_austria_begin = "str_fife_austria_1"

bugle_strings_britain_begin = "str_bugle_britain_1"
bugle_strings_france_begin = "str_bugle_france_1"
bugle_strings_prussia_begin = "str_bugle_prussia_1"
bugle_strings_russia_begin = "str_bugle_russia_1"
bugle_strings_austria_begin = "str_bugle_austria_1"
bugle_strings_calls_begin = "str_bugle_signal_1"
bagpipes_strings_britain_begin = "str_bagpipes_britain_1"
bagpipes_strings_extra_begin = "str_bagpipes_extra_1"

piano_strings_begin   = "str_piano_tune_1"
organ_strings_begin   = "str_organ_tune_1"
mm_cannon_types_begin        = "spr_mm_cannon_12pdr"
mm_cannon_types_end          = "spr_mm_cannonball_6pd"
mm_cannon_wood_types_begin   = "spr_mm_cannon_12pdr_wood"
mm_cannon_wood_types_end     = "spr_mm_cannon_12pdr_wheels"
mm_cannon_wheel_types_begin  = "spr_mm_cannon_12pdr_wheels"
mm_cannon_wheel_types_end    = "spr_mm_cannon_12pdr_barrel"
mm_cannon_barrel_types_begin = "spr_mm_cannon_12pdr_barrel"
mm_cannon_barrel_types_end   = "spr_mm_cannon_12pdr_limber_wheels"
mm_unlimber_button_types_begin = "spr_mm_cannon_12pdr_limber"
mm_unlimber_button_types_end   = "spr_mm_limber_button"
mm_cannon_button_types_begin   = "spr_mm_limber_button"
mm_cannon_button_types_end     = "spr_mm_round_button"
mm_button_types_begin       = "spr_mm_cannon_12pdr_limber"
mm_button_types_end         = "spr_mm_tunnel_wall"
mm_explosive_props_begin       = "spr_crate_explosive_fra"
mm_explosive_props_end         = "spr_mm_bird"

cannon_ammo_type_round      = 1
cannon_ammo_type_shell      = 2
cannon_ammo_type_canister   = 3
cannon_ammo_type_bomb       = 4
cannon_ammo_type_rocket     = 5
cannon_ammo_types_begin     = cannon_ammo_type_round
cannon_ammo_types_end       = 6

cannon_hit_effect_event_type_explosion  = 1
cannon_hit_effect_event_type_ground     = 2
cannon_hit_effect_event_type_water_ball = 3
cannon_hit_effect_event_type_wall       = 4
cannon_hit_effect_event_types_begin = cannon_hit_effect_event_type_explosion
cannon_hit_effect_event_types_end = 5

cannon_command_up           = 1
cannon_command_down         = 2
cannon_command_right        = 3
cannon_command_left         = 4
cannon_command_fire         = 5
cannon_command_stop_aim     = 6
cannon_commands_begin         = cannon_command_up
cannon_commands_end           = 7

command_type_cannon         = 1
command_type_ship           = 2
command_types_begin         = command_type_cannon
command_types_end           = 3

prop_effect_type_sound     = 1
prop_effect_type_particle  = 2
prop_effect_type_stop_all  = 3

prop_effect_types_begin  = prop_effect_type_sound
prop_effect_types_end    = 4

prop_effect_handle_stop    = 0
prop_effect_handle_start   = 1

prop_effect_handles_begin  = prop_effect_handle_stop
prop_effect_handles_end    = 2

mm_destructible_props_begin  = "spr_mm_house_wall_1"
mm_destructible_props_end    = "spr_mm_house_wall_2dd"

mm_destroyed_props_begin     = "spr_mm_house_wall_2dd"
mm_destroyed_props_end       = "spr_mm_wallgate"

construct_costs_offset    = 50
construct_button_offset   = construct_costs_offset + 20
construct_display_offset  = construct_button_offset + 20
construct_offset_end      = construct_display_offset + 20

mm_construct_props_begin       = "spr_mm_stakes_construct"
mm_construct_props_end         = "spr_mm_crator_small"
mm_construct_props_strings     = "str_mm_stakes_construct"
mm_construct_props_meshes     = "mesh_construct_mesh_stakes"

# PN END ***********************************

########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_horse_last_rider           = 0 # if a horse, the agent id of the last (or current) rider, or if stray, negative numbers counting down to when the horse will be removed
slot_agent_drowning_count             = 1 # counts upwards each time an agent is found to be drowning underwater
slot_agent_poison_amount              = 2 # increases each time the agent is attacked with poison, reduced when healed
slot_agent_poisoner_agent_id          = 3 # agent id that last poisoned the agent
slot_agent_poisoner_player_uid        = 4 # player unique id of the poisoner when applicable, to give correct death messages
slot_agent_freeze_instance_id         = 5 # instance id of the invisible scene prop being used to freeze
slot_agent_is_targeted                = 6 # mark that the stored target agent id is correct
slot_agent_food_amount                = 7
slot_agent_fishing_last_school        = 8 # last school fished from, to speed up repetitive check
slot_agent_last_horse_ridden          = 9

slot_agent_money_bag_1_value          = 10 # the values of the money bags picked up, in order
slot_agent_money_bag_2_value          = 11
slot_agent_money_bag_3_value          = 12
slot_agent_money_bag_4_value          = 13

slot_agent_hunting_last_carcass       = 14 # last animal carcass processed, to speed up repetitive checks
slot_agent_died_normally              = 15
slot_agent_animation_end_time_ms      = 16 # mission time in milliseconds
slot_agent_last_animation_string_id   = 17
slot_agent_recent_animations_delay_ms = 18 # interval in milliseconds
slot_agent_storage_corpse_instance_id = 19 # saved when discarding armor

slot_agent_animal_herd_manager        = 20 # instance id of the herd manager item attached to
slot_agent_animal_birth_time          = 21 # mission time when the animal was spawned as a child, or extrapolated if spawned as an adult
slot_agent_animal_grow_time           = 22 # mission time after which the animal will grow to an adult or birth a child
slot_agent_animal_move_time           = 23 # mission time after which to move
slot_agent_animal_last_damage_time    = 24
slot_agent_animal_food                = 25
slot_agent_animal_carcass_instance_id = 26
slot_agent_animal_times_stuck         = 27
slot_agent_animal_end                 = 28
slot_agent_last_voice_at              = 29
slot_agent_last_sound_at              = 30
slot_agent_used_prop_instance         = 31
slot_agent_music_play_together        = 32
slot_agent_base_speed_mod             = 33
slot_agent_started_playing_music_at   = 34

slot_agent_head_damage_factor         = 40 # agent modifier factors for armor slots
slot_agent_head_speed_factor          = 41
slot_agent_head_accuracy_factor       = 42
slot_agent_head_reload_factor         = 43
slot_agent_body_damage_factor         = 44
slot_agent_body_speed_factor          = 45
slot_agent_body_accuracy_factor       = 46
slot_agent_body_reload_factor         = 47
slot_agent_foot_damage_factor         = 48
slot_agent_foot_speed_factor          = 49
slot_agent_foot_accuracy_factor       = 50
slot_agent_foot_reload_factor         = 51
slot_agent_hand_damage_factor         = 52
slot_agent_hand_speed_factor          = 53
slot_agent_hand_accuracy_factor       = 54
slot_agent_hand_reload_factor         = 55
slot_agent_armor_damage_factor        = 56 # total agent modifier factors for armor
slot_agent_armor_speed_factor         = 57
slot_agent_armor_accuracy_factor      = 58
slot_agent_armor_reload_factor        = 59
slot_agent_weapon_damage_factor       = 60 # agent modifier factors for the wielded weapon
slot_agent_weapon_speed_factor        = 61
slot_agent_weapon_accuracy_factor     = 62
slot_agent_weapon_reload_factor       = 63
slot_agent_cannot_attack              = 64 # marks that any attack should be canceled
slot_agent_armor_damage_through       = 65 # factor of letting damage received bleed through the armor
slot_agent_last_apply_factors_item_id = 66 # last item id that modifier factors were last checked for, to avoid duplicating calculations due to trigger activation quirks
slot_agent_frizzle_times              = 67
slot_agent_current_control_prop       = 68
slot_agent_last_build_at              = 69
slot_agent_has_fallen_off_horse       = 70
slot_agent_last_rotz                  = 71
slot_agent_last_speed_same_count      = 72
slot_agent_current_command            = 73
slot_agent_character_language         = 74

########################################################
##  SCENE PROP SLOTS       #############################
########################################################

slot_scene_prop_item_id               = 0 # main associated item id, for stockpiles and similar
slot_scene_prop_gold_value            = 1 # preset gold value, or cached value of the associated item
slot_scene_prop_gold_multiplier       = 2 # cached price multiplier of the associated item
slot_scene_prop_use_string            = 3 # string id displayed when players look at the scene prop
slot_scene_prop_troop_id              = 4 # for troop training stations
slot_scene_prop_full_hit_points       = 5
slot_scene_prop_is_mercenary          = 6 # 1 = stay associated with the faction that owned the castle at mission start, rather than changing with capture
slot_scene_prop_required_horse        = 7 # horse item required for attaching to a cart
slot_scene_prop_average_craft_skill   = 8
slot_scene_prop_is_resource_stockpile = 9 # marks stockpiles for raw resources, which have different sell price calculations

slot_scene_prop_linked_scene_prop     = 10 # instance ids of linked scene props
slot_scene_prop_linked_scene_prop_1   = 10
slot_scene_prop_linked_scene_prop_2   = 11
slot_scene_prop_linked_scene_prop_3   = 12
slot_scene_prop_linked_scene_prop_4   = 13
linked_scene_prop_slot_count          = 4

slot_scene_prop_linked_sail           = slot_scene_prop_linked_scene_prop_1
slot_scene_prop_linked_sail_off       = slot_scene_prop_linked_scene_prop_2
slot_scene_prop_linked_ramp           = slot_scene_prop_linked_scene_prop_3
slot_scene_prop_linked_hold           = slot_scene_prop_linked_scene_prop_4

slot_scene_prop_linked_platform_1     = slot_scene_prop_linked_scene_prop_1
slot_scene_prop_linked_platform_2     = slot_scene_prop_linked_scene_prop_2
slot_scene_prop_linked_ferry_winch    = slot_scene_prop_linked_scene_prop_3

slot_scene_prop_position              = 15 # multiple meanings, mostly ships and carts - use with care
slot_scene_prop_target_position       = 16 # used for ships
slot_scene_prop_rotation              = 17 # multiple meanings, for ships, carts, and doors - use with care
slot_scene_prop_target_rotation       = 18 # used for ships
slot_scene_prop_max_position          = slot_scene_prop_rotation
slot_scene_prop_max_distance          = slot_scene_prop_target_rotation

slot_scene_prop_attached_to_agent     = 19 # store agent id attached to
slot_scene_prop_controlling_agent     = 20 # agent id steering the ship
slot_scene_prop_length                = 21 # multiple meanings - use with care
slot_scene_prop_width                 = 22 # multiple meanings - use with care
slot_scene_prop_height                = 23 # multiple meanings - use with care
slot_scene_prop_collision_kind        = 24 # collision testing scene prop kind for ships; set to -1 for scene props that should never be checked for collision with ships
slot_scene_prop_speed_limit           = 25 # used for ships
slot_scene_prop_no_move_physics       = 26 # whether to disable physics when moving, so agents can't ride on the prop
slot_scene_prop_capture_faction_id    = 27 # faction that has captured this prop individually, rather than the castle it belongs to

slot_scene_prop_next_resource_hp      = 30 # hit points when the next resource item should be produced
slot_scene_prop_state                 = 31 # constants below starting with scene_prop_state_
slot_scene_prop_state_time            = 32 # mission time involved with changing state, if appropriate
slot_scene_prop_stock_count           = 33
slot_scene_prop_stock_count_update_time = 34 # on clients, time of the last stock count update, to prevent quickly repeated requests
slot_scene_prop_unlocked              = 35
slot_scene_prop_regrow_script         = 36 # script id to call when finished regrowing
slot_scene_prop_resource_item_id      = 37
slot_scene_prop_prune_time            = 38 # mission time when a spawned item scene prop will be pruned
slot_scene_prop_resources_default_cost = 39

slot_scene_prop_water                 = 40
slot_scene_prop_seeds                 = 41
slot_scene_prop_fruiting_interval     = slot_scene_prop_water
slot_scene_prop_fruit_count           = slot_scene_prop_seeds

slot_scene_prop_show_linked_hit_points = 45
slot_scene_prop_disabled              = 46

slot_scene_prop_resource_refund_cost  = 50
slot_scene_prop_crafting_resource_1   = 51
slot_scene_prop_crafting_resource_2   = 52
slot_scene_prop_crafting_resource_3   = 53
slot_scene_prop_crafting_resource_4   = 54

scene_prop_state_active               = 0
scene_prop_state_destroyed            = 1
scene_prop_state_hidden               = 2
scene_prop_state_regenerating         = 3

slot_scene_prop_inventory_targeted    = 196 # instance id of targeted inventory, used with item scene props
slot_scene_prop_inventory_unique_id   = 197 # unique number identifying spawned item scene props
slot_scene_prop_inventory_max_length  = 198 # maximum length of items inside the container
slot_scene_prop_inventory_count       = 199 # number of inventory slots for this container
slot_scene_prop_inventory_begin       = 200 # item ids in container
slot_scene_prop_inventory_item_0      = 290 # item ids in player equipment
slot_scene_prop_inventory_ammo_begin  = 300 # ammo counts in container
slot_scene_prop_inventory_mod_begin   = 400 # item changes in container needing presentation updates
slot_scene_prop_inventory_mod_item_0  = 490 # item changes in player equipment needing presentation updates
slot_scene_prop_inventory_obj_begin   = 500 # container slot overlay ids
slot_scene_prop_inventory_obj_item_0  = 590 # player equipment overlay ids
slot_scene_prop_inventory_mesh_begin  = 600 # container item mesh overlay ids
slot_scene_prop_inventory_mesh_item_0 = 690 # player equipment item mesh overlay ids
slot_scene_prop_inventory_end         = slot_scene_prop_inventory_ammo_begin
slot_scene_prop_inventory_mod_end     = slot_scene_prop_inventory_obj_begin
slot_scene_prop_inventory_obj_end     = slot_scene_prop_inventory_mesh_begin
inventory_count_maximum               = slot_scene_prop_inventory_item_0 - slot_scene_prop_inventory_begin

corpse_inventory_slots                = 5 # coded into the module so values are the same on the server and clients
corpse_inventory_max_length           = 100

slot_animal_herd_manager_adult_item_id= 100
slot_animal_herd_manager_starving     = 101

slot_animal_carcass_meat_count        = 100
slot_animal_carcass_hide_count        = 101

########################################################
##  SCENE PROP SLOTS  *PN*     #########################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_slot_is_spawned          = 3
scene_prop_slot_in_use              = 4
scene_prop_slot_x_value             = 5
scene_prop_slot_y_value             = 6
scene_prop_slot_z_value             = 7
scene_prop_slot_x_rot               = 8
scene_prop_slot_y_rot               = 9
scene_prop_slot_z_rot               = 10
scene_prop_slot_z_rotation_limit    = 11
scene_prop_slot_x_scale             = 12
scene_prop_slot_y_scale             = 13
scene_prop_slot_z_scale             = 14
scene_prop_slot_is_scaled           = 15
scene_prop_slot_x_extra             = 16
scene_prop_slot_y_extra             = 17
scene_prop_slot_z_extra             = 18
scene_prop_slot_time                = 19
scene_prop_slot_bounces             = 20
scene_prop_slot_times_hit           = 21
scene_prop_slot_owner_team          = 22
scene_prop_slot_time_left           = 23
scene_prop_slot_has_ball            = 24
scene_prop_slot_is_loaded           = 25
scene_prop_slot_is_active           = 26
scene_prop_slot_just_fired          = 27
scene_prop_slot_health              = 28
scene_prop_slot_max_health          = 29
scene_prop_slot_displayed_particle  = 30
scene_prop_slot_ammo_type           = 31
scene_prop_slot_ignore_inherit_movement = 32
scene_prop_slot_float_ground        = 33
scene_prop_slot_ground_offset       = 34
scene_prop_slot_spawned_at          = 35
scene_prop_slot_is_not_pushed_back  = 36
scene_prop_slot_just_pushed_back    = 37

# under here slots that need -1 as default
scene_prop_slot_replaced_by         = 52
scene_prop_slot_replacing           = 53
scene_prop_slot_last_hit_by         = 54
scene_prop_slot_user_agent          = 55
scene_prop_slot_controller_agent    = 56
scene_prop_slot_carrier_agent       = 57
scene_prop_slot_linked_prop         = 58

scene_prop_slot_sound_effect        = 59
scene_prop_slot_particle_effect1    = 60
scene_prop_slot_particle_effect2    = 61
scene_prop_slot_particle_effect3    = 62
scene_prop_slot_particle_effect4    = 63

scene_prop_slot_parent_prop         = 80
scene_prop_slot_child_prop1         = 81
scene_prop_slot_child_prop2         = 82
scene_prop_slot_child_prop3         = 83
scene_prop_slot_child_prop4         = 84
scene_prop_slot_child_prop5         = 85
scene_prop_slot_child_prop6         = 86
scene_prop_slot_child_prop7         = 88
scene_prop_slot_child_prop8         = 89
scene_prop_slot_child_prop9         = 90
scene_prop_slot_child_prop10        = 91
scene_prop_slot_child_prop11        = 92
scene_prop_slot_child_prop12        = 93
scene_prop_slot_child_prop13        = 94
scene_prop_slot_child_prop14        = 95
scene_prop_slot_child_prop15        = 96
scene_prop_slot_child_prop16        = 97

scene_prop_slots_begin              = scene_prop_open_or_close_slot
scene_prop_slots_end                = 98

scene_prop_slots_defmin_begin       = scene_prop_slot_replaced_by

scene_prop_slot_destruct_wall_height            = 99
scene_prop_slot_destruct_wall_width             = 100
scene_prop_slot_destruct_wall_length            = 101
scene_prop_slot_destruct_move_height_to_center  = 102
scene_prop_slot_destruct_move_width_to_center   = 103
scene_prop_slot_destruct_move_length_to_center  = 104
scene_prop_slot_destruct_rotate_z_90            = 105
scene_prop_slot_destruct_wall_height_offset     = 106
scene_prop_slot_destruct_wall_width_offset      = 107
scene_prop_slot_destruct_wall_length_offset     = 108
scene_prop_slot_destruct_inverse_width_movement = 109
scene_prop_slot_destruct_max_length             = 110
scene_prop_slot_destruct_smoke_strength         = 111

scene_prop_slot_destruct_smoke_type             = 112
scene_prop_slot_destruct_smoke_type2            = 113
scene_prop_slot_destruct_particles_type         = 114
scene_prop_slot_destruct_sound_id               = 115
scene_prop_slot_destruct_pile_prop_begin        = 116
scene_prop_slot_destruct_pile_prop_end          = 117

scene_prop_slot_destruct_next_stage_1           = 118
scene_prop_slot_destruct_next_stage_2           = 119
scene_prop_slot_destruct_next_stage_3           = 120
scene_prop_slot_destruct_next_stage_4           = 121
scene_prop_slot_destruct_next_stage_5           = 122
scene_prop_slot_destruct_next_stage_6           = 123
scene_prop_slot_destruct_next_stage_7           = 124
scene_prop_slot_destruct_next_stage_8           = 125
scene_prop_slot_destruct_next_stage_9           = 126
scene_prop_slot_destruct_next_stage_10          = 127

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_difficulty                  = 0
slot_item_length                      = 1
slot_item_class                       = 2 # listed below, starting with item_class_
slot_item_resource_amount             = 3 # resource amount of the item class
slot_item_gender                      = 4 # 0 = male or anyone, 1 = female only
slot_item_max_ammo                    = 5
slot_item_bonus_against_wood          = 6
slot_item_couchable                   = 7
slot_item_has_attack_requirements     = 8
slot_item_max_raw_damage              = 9 # maximum out of swing and thrust damage

item_class_none                       = 0
item_class_repair                     = 1
item_class_wood_cutting               = 2
item_class_wood                       = 3
item_class_mining                     = 4
item_class_iron                       = 5
item_class_lock_pick                  = 6
item_class_heraldic                   = 7 # marks the item to be redrawn when the banner changes
item_class_precious                   = 8
item_class_food                       = 9
item_class_grain_harvesting           = 10
item_class_knife                      = 11
item_class_cloth                      = 12
item_class_leather                    = 13
item_class_herding_calm               = 14
item_class_herding_rouse              = 15

slot_item_animal_adult_item_id        = 20
slot_item_animal_child_item_id        = 21
slot_item_animal_grow_time            = 22
slot_item_animal_max_in_herd          = 23
slot_item_animal_attack_reaction      = 24 # listed below, starting with animal_reaction_
slot_item_animal_death_sound          = 25
slot_item_animal_meat_count           = 26
slot_item_animal_hide_count           = 27
slot_item_animal_wildness             = 28 # higher values have greater unpredictability when herded or attacked

slot_item_multiplayer_item_class                     = 29
slot_item_multiplayer_item_class2                    = 30
slot_item_multiplayer_gf                             = 31
slot_item_multiplayer_availability_linked_list_begin = 32 #temporary, can be moved to higher values

animal_reaction_flee                  = 0
animal_reaction_charge                = 1

########################################################
##  FACTION SLOTS          #############################
########################################################

slot_faction_banner_mesh              = 0
slot_faction_name_is_custom           = 1 # 1 if the name has been changed from the default
slot_faction_is_active                = 2 # 1 if the faction has at least one capture point associated with their castle at mission start
slot_faction_lord_player_uid          = 3 # player unique id of the faction lord
slot_faction_lord_last_seen_time      = 4
slot_faction_castle_banner_variant    = 5 # work around an unwanted engine optimization: change tableau id used when changing faction banners to force them to update
slot_faction_list_button_id           = 6 # overlay id in the faction list presentation
slot_faction_is_locked                = 7 # 1 if an adminstrator locked the faction to prevent lord polls

slot_faction_poll_end_time            = 20
slot_faction_poll_voter_count         = 21
slot_faction_poll_yes_votes           = 22
slot_faction_poll_no_votes            = 23
slot_faction_poll_type                = 24 # listed below, starting with poll_type_
slot_faction_poll_value_1             = 25
slot_faction_poll_value_2             = 26
slot_faction_poll_target_unique_id    = 27 # when targeting a player, store their unique id to prevent accidentally harming another player reusing their id after they quit

poll_type_change_scene                = 0
poll_type_kick_player                 = 1
poll_type_ban_player                  = 2
poll_type_faction_lord                = 10

poll_cost_change_scene                = 1000
poll_cost_kick_player                 = 500
poll_cost_ban_player                  = 700
poll_cost_faction_lord                = 1000

poll_vote_no                          = 0
poll_vote_yes                         = 1
poll_vote_admin_no                    = 2
poll_vote_admin_yes                   = 3
poll_vote_abstain                     = 4
poll_result_no                        = -1
poll_result_yes                       = -2
poll_result_admin_no                  = -3
poll_result_admin_yes                 = -4
poll_result_existing                  = -5
poll_result_invalid                   = -6
poll_result_color                     = 0xFF0000

slot_faction_relations_begin          = 30

faction_cost_change_banner            = 500
faction_cost_change_name              = 500
faction_cost_kick_player              = 500
faction_cost_outlaw_player            = 1000

########################################################
##  SCENE SLOTS            #############################
########################################################


########################################################
##  TROOP SLOTS            #############################
########################################################

troop_slot_count_per_equipment_type   = 5
slot_troop_equipment_one_hand_begin   = 0
slot_troop_equipment_two_hand_begin   = 1 * troop_slot_count_per_equipment_type
slot_troop_equipment_ranged_begin     = 2 * troop_slot_count_per_equipment_type
slot_troop_equipment_ammo_begin       = 3 * troop_slot_count_per_equipment_type
slot_troop_equipment_shield_begin     = 4 * troop_slot_count_per_equipment_type
slot_troop_equipment_head_begin       = 5 * troop_slot_count_per_equipment_type
slot_troop_equipment_body_begin       = 6 * troop_slot_count_per_equipment_type
slot_troop_equipment_foot_begin       = 7 * troop_slot_count_per_equipment_type
slot_troop_equipment_hand_begin       = 8 * troop_slot_count_per_equipment_type
slot_troop_equipment_horse_begin      = 9 * troop_slot_count_per_equipment_type

slot_troop_ranking                    = 50 # used for sorting troop types in the player stats chart
slot_troop_spawn_health_percent       = 51 # respawn health percentage when dying as this troop
slot_troop_class                      = 52
slot_troop_class_type                 = 53
slot_troop_rank                       = 54
slot_troop_rank_type                  = 55

slot_player_array_size                = 0
slot_player_array_begin               = 1

player_array_unique_id                = 0
player_array_troop_id                 = 1
player_array_faction_id               = 2
player_array_gold_value               = 3
player_array_outlaw_rating            = 4
player_array_entry_size               = 5 # number of values stored in the disconnected players array

max_castle_count = 8
slot_mission_data_castle_owner_faction_begin    = 0 # owner factions of all castles
slot_mission_data_castle_owner_faction_end      = 8
slot_mission_data_castle_is_active_begin        = 10 # flags of which castles are active, with at least 1 capture point
slot_mission_data_castle_is_active_end          = 18
slot_mission_data_castle_name_string_begin      = 20 # string ids for castle names
slot_mission_data_castle_name_string_end        = 28
slot_mission_data_castle_money_chest_begin      = 30 # instance ids of the main money chest linked to each castle
slot_mission_data_castle_money_chest_end        = 38
slot_mission_data_castle_allows_training_begin  = 40 # flags of which active castles have at least one linked training station
slot_mission_data_castle_allows_training_end    = 48
slot_mission_data_faction_to_change_name_of     = 100 # store the faction id for the next faction name change message

slot_last_chat_message_event_type     = 0 # for the last chat message sent: network event number, combined with a type from the list below starting with chat_event_type_
slot_last_chat_message_not_recieved   = 1 # mark that the server has not notified of receiving the last chat message

chat_event_type_local                 = 0 # for each chat type, holding shift while pressing enter will add 1 to the type
chat_event_type_local_shout           = 1
chat_event_type_set_faction_name      = 2
chat_event_type_faction               = 4
chat_event_type_faction_announce      = 5
chat_event_type_admin                 = 6
chat_event_type_admin_announce        = 7

slot_chat_overlay_local_color         = 0
slot_chat_overlay_faction_color       = 1

slot_ship_array_count                 = 0 # count of ship instance ids in the scene
slot_ship_array_begin                 = 1 # array of ship instance ids
slot_ship_array_collision_props_count = 100 # stored instance ids of scene props near water level, for checking collision with ships
slot_ship_array_collision_props_begin = 101

slot_array_count                      = 0
slot_array_begin                      = 1

########################################################
##  TEAM SLOTS             #############################
########################################################


########################################################

spawn_invulnerable_time               = 10 # time agents are invlunerable after freshly spawning
loop_player_check_outlaw_interval     = 60
loop_agent_check_interval             = 2
loop_horse_check_interval             = 30
loop_health_check_interval            = 29
loop_weather_adjust_interval          = 32
stock_count_check_interval            = 5 # don't request stock count updates of the scene prop aimed at more often than this
repeat_action_min_interval            = 5 # prevent players from repeating certain potentially expensive actions more often than this
carcass_search_min_interval           = 5 # only search for a different animal carcass to process after this interval from the last
poll_time_duration                    = 60
name_server_kick_delay_interval       = 5 # delay before kicking from the server to allow the rejection message to be received

def sq(distance):
  return distance * distance / 100 # get_sq_distance_between_positions always uses fixed point multiplier 100

max_distance_to_play_sound            = 10000
max_distance_to_see_labels            = 1500
max_distance_horse_rider              = 5000
max_distance_local_chat               = 3000
max_distance_local_chat_shout         = 5000
ambient_distance_local_chat           = 1000
ambient_distance_local_chat_shout     = 2000
max_distance_local_animation          = 2500
z_position_to_hide_object             = -4999 # lower values might cause the position to "wrap around" up into the sky
z_position_water_level                = -30 # approximate visible water level based on tests
max_distance_to_use                   = 300
max_distance_to_loot                  = 100
max_distance_admin_cart               = 2000 # allow admins in their armor to attach carts from greater distances
max_distance_to_catch_fish            = 2000
fish_school_max_move_distance         = 500
fish_school_min_move_distance         = 200
fish_school_minimum_depth             = 200 # minimum water depth that a fish school will move into
fish_spawn_time                       = 300 # time before pruning fish items spawned
max_distance_to_include_in_herd       = 5000 # when searching for a herd for an animal

castle_tax_gold_percentage            = 20 # percentage of item price subtracted for selling price and added to the linked castle chest when bought
castle_training_gold_percentage       = 50 # percentage of training cost added to the linked castle chest
craft_price_gold_reward_percentage    = 20 # percentage of item price given to the crafter proportional to difference from target stock count
craft_skill_gold_reward_multiplier    = 300 # multiplier of crafting skill required given to the crafter proportional to difference from target stock count
base_export_percentage                = 100 # default percentage of item price for export stations

reduction_factor_base                 = 90
armor_damage_reduction_factor         = 10
head_armor_speed_reduction_factor     = 10
head_armor_accuracy_reduction_factor  = 50
head_armor_reload_reduction_factor    = 20
body_armor_speed_reduction_factor     = 20
body_armor_accuracy_reduction_factor  = 30
body_armor_reload_reduction_factor    = 10
foot_armor_speed_reduction_factor     = 30
foot_armor_accuracy_reduction_factor  = 5
foot_armor_reload_reduction_factor    = 5
hand_armor_speed_reduction_factor     = 5
hand_armor_accuracy_reduction_factor  = 30
hand_armor_reload_reduction_factor    = 10
melee_damage_reduction_factor         = 25
melee_speed_reduction_factor          = 5
crossbow_damage_reduction_factor      = 15
crossbow_speed_reduction_factor       = 5
crossbow_accuracy_reduction_factor    = 30
crossbow_reload_reduction_factor      = 30
bow_thrown_damage_reduction_factor    = 30
bow_thrown_speed_reduction_factor     = 5
bow_thrown_accuracy_reduction_factor  = 20
melee_max_level_difference            = 3 # max strength difference to be able to swing a melee weapon
crossbow_max_level_difference         = 4 # max strength difference to be able to shoot a crossbow
bow_ranged_max_level_difference       = 3 # max power draw or power throw difference to be able to shoot a bow or throw a weapon

winch_type_drawbridge                 = 0
winch_type_portcullis                 = 1
winch_type_platform                   = 2
winch_type_sliding_door               = 3

repairable_hit                        = 0
repairable_destroyed                  = 1
repairable_hit_destroyed              = 2
repairable_repairing                  = 3
repairable_resource_required          = 4
repairable_repaired                   = 5

ship_station_not_on_ship              = 0
ship_station_none                     = 1
ship_station_mast                     = 2
ship_station_rudder                   = 3

ship_forwards_maximum                 = 9 # maximum forwards speed - also limited by ship type and agent skill
ship_rotation_maximum                 = 5 # maximum turning speed
ship_forwards_multiplier              = 100
ship_rotation_multiplier              = 3

player_list_item_height               = 20
escape_menu_item_height               = 35
admin_panel_item_height               = 40
action_menu_item_height               = 23
faction_menu_item_height              = 120
animation_menu_item_height            = 32
chat_overlay_item_height              = 17
chat_overlay_ring_buffer_begin        = "trp_chat_overlay_ring_buffer_0"
chat_overlay_ring_buffer_end          = "trp_chat_overlay_ring_buffer_end"
chat_overlay_ring_buffer_size         = 11
local_chat_color                      = 0xFFFFDD8A
local_chat_shout_color                = 0xFFFF8C27
local_animation_color                 = 0xFFFFBBAA
admin_chat_color                      = 0xFFFF00FF
invalid_faction_color                 = 0xFF888888

outlaw_rating_for_kill                = 2
outlaw_rating_for_team_kill           = 5
outlaw_rating_for_lord_outlawed       = 4
outlaw_rating_outlawed                = 15 # outlaw players when they get this rating
outlaw_rating_maximum                 = 30 # don't add increase the rating more than this

change_faction_type_respawn           = 0 # changing faction when training
change_faction_type_no_respawn        = 1 # changing faction by clicking the use control, to the same troop type or one that allows it
change_faction_type_outlawed          = 2 # being forced to change when outlawed, without respawning

capture_point_type_primary            = 0 # after the required secondary points are captured, take over the castle
capture_point_type_secondary_all      = 1 # require taking all secondary capture points of this type
capture_point_type_secondary_one      = 2 # require taking at least one secondary capture point of this type

redraw_all_banners                    = 0 # at mission start on the server
redraw_castle_banners                 = 1 # when a castle is captured
redraw_faction_banners                = 2 # when a faction lord changes their banner
redraw_client_banner_positions        = 3 # at mission start on a client, to work around engine quirks with spawned items
redraw_single_capture_point_banner    = 4 # when a secondary point is captured

inventory_slots_per_row               = 6
inventory_slot_spacing                = 100
inventory_mesh_offset                 = 50
inventory_container_x_offset          = 190
inventory_container_y_offset          = 175

scene_prop_hit_points_bar_scale_x     = 6230
scene_prop_hit_points_bar_scale_y     = 15000

select_agent_max_x                    = 300
select_agent_max_y                    = 200
presentation_max_x                    = 1000 # at fixed point multiplier 1000
presentation_max_y                    = 750 # at fixed point multiplier 1000

animation_menu_end_offset             = 11

max_scene_prop_instance_id            = 10000 # when trying to loop over all props in a scene, stop at this limit

max_food_amount                       = 100
max_hit_points_percent                = 200

all_items_begin = "itm_tattered_headcloth"
all_items_end = "itm_all_items_end"

all_pn_items_begin = "itm_flag_france_45e"
all_pn_items_end = "itm_arty_horse_howitzer_prussian"

wielded_items_begin = "itm_club"
wielded_items_end = "itm_all_items_end"

scripted_items_begin = "itm_surgeon_scalpel" # items outside this range are not checked from the ti_on_agent_hit trigger
scripted_items_end = "itm_money_bag"

herd_animal_items_begin = "itm_deer" # item range used for herd animal spawners
herd_animal_items_end = "itm_stick"

playable_troops_begin = "trp_peasant" # troops outside this range are treated as storage objects unusable by players
playable_troops_end = "trp_playable_troops_end"

factions_begin = "fac_commoners"
castle_factions_begin = "fac_1"
factions_end = "fac_factions_end"

castle_names_begin = "str_castle_name_0"
castle_names_end = "str_castle_names_end"

scenes_begin = "scn_scene_1"
scenes_end = "scn_scenes_end"

scene_names_begin = "str_scene_name_1" # this range of strings must correspond to the available scene slots
scene_names_end = "str_scene_names_end"

game_type_mission_templates_begin = "mt_conquest"
game_type_mission_templates_end = "mt_edit_scene"

game_type_names_begin = "str_game_type_1"
game_type_names_end = "str_game_types_end"

game_type_info_strings_begin = "str_game_type_1_info"

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end = "mesh_banners_default_a"

banner_items_begin = "itm_pw_banner_pole_a01" # range of items associated with banner mesh ids
banner_items_end = "itm_admin_horse"

commands_module_system_names_begin = "str_bot_count" # range of strings associated with hard coded server commands
commands_napoleonic_wars_names_begin = "str_use_class_limits"
admin_action_log_strings_begin = "str_log_admin_kick" # range of strings associated with admin actions, for the server log

ambient_sounds_begin = "snd_fire_loop" # for ambient sound emitter scene props
ambient_sounds_end = "snd_sounds_end"

action_menu_strings_begin = "str_toggle_name_labels" # range of strings associated with the action menu
action_menu_strings_end = "str_action_menu_end"

animation_strings_begin = "str_anim_cheer" # range of strings associated with the animation menu
animation_strings_end = "str_log_animation"

profile_option_strings_begin = "str_display_name_labels" # range of strings for options stored in a player profile

colour_white      = 0
colour_red        = 1
colour_green      = 2
colour_blue       = 3
colour_yellow     = 4
colour_purple     = 5
colour_pink       = 6
colour_magenta    = 7
colour_invisible  = 8

from header_common import *

profile_options = [ # global flag variables for options stored in a player profile
  "$g_display_agent_labels",
  "$g_hide_faction_in_name_labels",
  "$g_display_chat_overlay",
  "$g_chat_overlay_type_selected",
  "$g_disable_automatic_shadow_recalculation",
  "$g_animation_menu_no_mouse_grab",
  "$g_mute_global_chat",
  "$g_disable_rain_snow_particles",
  ]
if len(profile_options) >= profile_banner_id_option_bits_end - profile_banner_id_option_bits_begin:
  raise Exception("Too many profile options: %d, maximum %d" % (len(profile_options), profile_banner_id_option_bits_end - profile_banner_id_option_bits_begin))
