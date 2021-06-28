from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *
from module_animations import *
import header_debug as dbg
import header_lazy_evaluation as lazy

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id.
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags.
#  3) Mission-type (int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#  4) Mission description text (string).
#
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) Entry point number: Troops spawned from this spawn record will use this entry.
#    5.2) Spawn flags.
#    5.3) Alter flags: which equipment will be overriden.
#    5.4) AI flags.
#    5.5) Number of troops to spawn.
#    5.6) List of equipment to add to troops spawned from here (maximum 8).
#
#  6) List of triggers (list): Each trigger contains the following fields:
#    6.1) Check interval: How frequently this trigger will be checked. Also used for special triggers listed in header_triggers.py.
#    6.2) Delay interval: Time to wait before applying the consequences of the trigger after its conditions have been evaluated as true.
#    6.3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
#    6.4) Conditions block (list), must be a valid operation block. Every time the trigger is checked, this block will be executed.
#    If the conditions block returns true or is empty, the consequences block will be executed.
#    6.5) Consequences block (list), must be a valid operation block. Executed only if the conditions block succeeded.
####################################################################################################################

spawn_points_0_99 = [
  (0,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (1,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (2,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (3,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (4,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (5,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (6,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (7,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (8,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (9,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (10,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (11,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (12,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (13,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (14,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (15,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (16,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (17,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (18,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (19,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (20,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (21,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (22,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (23,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (24,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (25,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (26,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (27,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (28,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (29,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (30,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (31,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (32,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (33,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (34,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (35,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (36,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (37,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (38,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (39,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (40,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (41,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (42,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (43,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (44,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (45,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (46,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (47,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (48,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (49,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (50,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (51,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (52,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (53,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (54,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (55,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (56,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (57,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (58,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (59,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (60,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (61,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (62,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (63,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (64,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (65,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (66,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (67,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (68,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (69,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (70,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (71,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (72,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (73,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (74,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (75,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (76,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (77,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (78,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (79,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (80,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (81,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (82,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (83,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (84,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (85,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (86,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (87,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (88,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (89,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (90,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (91,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (92,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (93,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (94,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (95,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (96,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (97,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (98,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (99,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  ]

before_mission_start_setup = (ti_before_mission_start, 0, 0, [], # set up basic mission and scene values
   [(server_set_friendly_fire, 1),
    (server_set_melee_friendly_fire, 1),
    (server_set_friendly_fire_damage_self_ratio, 0),
    (server_set_friendly_fire_damage_friend_ratio, 100),
    (team_set_relation, team_default, team_default, -1),
    (team_set_relation, team_default, team_spawn_invulnerable, 0),
    (team_set_relation, team_spawn_invulnerable, team_default, 0),
    (team_set_relation, team_spawn_invulnerable, team_spawn_invulnerable, 0),
    (call_script, "script_initialize_scene_globals"),
    (call_script, "script_scene_set_day_time"),
    (call_script, "script_scene_setup_factions_castles"),
    (call_script, "script_setup_all_linked_scene_props"),
    (try_begin),
      (multiplayer_is_server),
      (call_script, "script_setup_castle_money_chests"),
    (else_try),
      (call_script, "script_load_profile_options"),
    (try_end),
    ])

after_mission_start_setup = (ti_after_mission_start, 0, 0, [], # spawn and move certain things after most other set up is done
   [(set_spawn_effector_scene_prop_kind, 0, -1),
    (set_spawn_effector_scene_prop_kind, 1, -1),
    (assign, "$g_preset_message_display_enabled", 0),
    (multiplayer_is_server),
    (assign, "$g_next_scene", -1),
    (call_script, "script_setup_ship_collision_props"),
    (call_script, "script_setup_scene_props_after_mission_start"),
    (init_position, pos1),
    (set_spawn_position, pos1), # spawn a respawn position marker scene prop for each possible player
    (server_get_max_num_players, "$g_spawn_marker_count"),
    (val_add, "$g_spawn_marker_count", 1),
    (try_for_range, ":unused", 0, "$g_spawn_marker_count"),
      (spawn_scene_prop, "spr_code_spawn_marker"),
    (try_end),
    (assign, "$g_spawned_bot_count", 0),
    (call_script, "script_check_name_server"),
    ])

player_joined = (ti_server_player_joined, 0, 0, [], # server: handle connecting players
   [(store_trigger_param_1, ":player_id"),
    (call_script, "script_setup_player_joined", ":player_id"),
    (call_script, "script_player_check_name", ":player_id"),
    ])

player_exit = (ti_on_player_exit, 0, 0, [], # server: save player values on exit
   [(store_trigger_param_1, ":player_id"),
    (call_script, "script_cf_save_player_exit", ":player_id"),
    ])

agent_spawn = (ti_on_agent_spawn, 0, 0, [], # server and clients: set up new agents after they spawn
   [(store_trigger_param_1, ":agent_id"),
    (call_script, "script_on_agent_spawned", ":agent_id"),
    ])

agent_killed = (ti_on_agent_killed_or_wounded, 0, 0, [], # server and clients: handle messages, score, loot, and more after agents die
   [(store_trigger_param_1, ":dead_agent_id"),
    (store_trigger_param_2, ":killer_agent_id"),
    (call_script, "script_client_check_show_respawn_time_counter", ":dead_agent_id"),
    (call_script, "script_apply_consequences_for_agent_death", ":dead_agent_id", ":killer_agent_id"),
    (multiplayer_is_server),
    (call_script, "script_setup_agent_for_respawn", ":dead_agent_id"),
    (call_script, "script_check_animal_killed", ":dead_agent_id", ":killer_agent_id"),
    (call_script, "script_check_spawn_bots", ":dead_agent_id"),
    ])

agent_hit = (ti_on_agent_hit, 0, 0, [], # server: apply extra scripted effects for special weapons, hitting animals, and when overloaded by armor
   [(store_trigger_param_1, ":attacked_agent_id"),
    (store_trigger_param_2, ":attacker_agent_id"),
    (store_trigger_param_3, ":damage_dealt"),
    (try_begin), # check if damage should bleed through the armor due to unmet requirements
      (agent_slot_ge, ":attacked_agent_id", slot_agent_armor_damage_through, 5),
      (agent_get_slot, ":damage_through_multiplier", ":attacked_agent_id", slot_agent_armor_damage_through),
      (gt, reg0, -1),
      (item_get_slot, ":damage_through", reg0, slot_item_max_raw_damage),
      (val_mul, ":damage_through", ":damage_through_multiplier"),
      (val_div, ":damage_through", 100),
      (gt, ":damage_through", ":damage_dealt"),
      (store_random_in_range, ":damage_through", ":damage_dealt", ":damage_through"),
      (set_trigger_result, ":damage_through"),
    (try_end),
    (try_begin),
      (agent_slot_ge, ":attacked_agent_id", slot_agent_animal_birth_time, 1),
      (call_script, "script_animal_hit", ":attacked_agent_id", ":attacker_agent_id", ":damage_dealt", reg0),
    (try_end),
    (try_begin),
      (is_between, reg0, scripted_items_begin, scripted_items_end),
      (call_script, "script_agent_hit_with_scripted_item", ":attacked_agent_id", ":attacker_agent_id", ":damage_dealt", reg0),
    (try_end),
    ])

item_picked_up = (ti_on_item_picked_up, 0, 0, [], # handle agents picking up an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (store_trigger_param_3, ":instance_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 1, 1),
    (multiplayer_is_server),
    (call_script, "script_check_on_item_picked_up", ":agent_id", ":item_id", ":instance_id"),
    ])

item_dropped = (ti_on_item_dropped, 0, 0, [], # handle agents dropping an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (store_trigger_param_3, ":instance_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 0, 1),
    (multiplayer_is_server),
    (call_script, "script_check_on_item_dropped", ":agent_id", ":item_id", ":instance_id", 0),
    ])

item_wielded = (ti_on_item_wielded, 0, 0, [], # handle agents wielding an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 1, 1),
    ])

item_unwielded = (ti_on_item_unwielded, 0, 0, [], # handle agents un-wielding an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 0, 1),
    ])

agent_mount = (ti_on_agent_mount, 0, 0, [], # server: check speed factor and attached carts when agents mount a horse
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":horse_agent_id"),
    (agent_set_slot, ":horse_agent_id", slot_agent_horse_last_rider, ":agent_id"),
    (agent_set_slot, ":agent_id", slot_agent_last_horse_ridden, ":horse_agent_id"),
    (multiplayer_is_server),
    (call_script, "script_check_agent_horse_speed_factor", ":agent_id", ":horse_agent_id", 0),
    (try_begin),
      (call_script, "script_cf_attach_cart", ":agent_id", -1, ":agent_id"),
    (try_end),
    ])

agent_dismount = (ti_on_agent_dismount, 0, 0, [], # server: make horses stand still after being dismounted from
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":horse_agent_id"),
    (agent_set_slot, ":horse_agent_id", slot_agent_horse_last_rider, ":agent_id"),
    (agent_set_slot, ":agent_id", slot_agent_last_horse_ridden, ":horse_agent_id"),
    (multiplayer_is_server),
    (agent_get_position, pos1, ":horse_agent_id"),
    (agent_set_scripted_destination, ":horse_agent_id", pos1, 0),
    ])

player_check_loop = (0, 0, 0.5, # server: check all players to see if any need agents spawned, also periodically lowering outlaw ratings
   [(multiplayer_is_server),
    (store_mission_timer_a, ":time"),
    (get_max_players, ":max_players"),
    (assign, ":loop_end", ":max_players"),
    (try_for_range, ":player_id", "$g_loop_player_id", ":loop_end"), # continue from the last player id checked
      (player_is_active, ":player_id"),
      (player_get_slot, ":kick_at_time", ":player_id", slot_player_kick_at_time),
      (try_begin), # kick after an interval if rejected by the name server
        (gt, ":kick_at_time", 0),
        (try_begin),
          (ge, ":time", ":kick_at_time"),
          (kick_player, ":player_id"),
        (try_end),
      (else_try),
        (try_begin),
          (this_or_next|player_slot_eq, ":player_id", slot_player_spawn_state, player_spawn_state_dead),
          (player_slot_eq, ":player_id", slot_player_spawn_state, player_spawn_state_invulnerable),
          (call_script, "script_cf_player_check_spawn_agent", ":player_id"),
          (assign, ":loop_end", -1), # if the spawn checks were run, end the loop to give other triggers a chance to run, then immediately continue
          (store_add, "$g_loop_player_id", ":player_id", 1),
        (try_end),
        (try_begin),
          (eq, "$g_loop_player_check_outlaw", 1),
          (player_get_slot, ":outlaw_rating", ":player_id", slot_player_outlaw_rating),
          (try_begin),
            (gt, ":outlaw_rating", 0),
            (val_sub, ":outlaw_rating", 1),
            (player_set_slot, ":player_id", slot_player_outlaw_rating, ":outlaw_rating"),
            (multiplayer_send_3_int_to_player, ":player_id", server_event_player_set_slot, ":player_id", slot_player_outlaw_rating, ":outlaw_rating"),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
    (eq, ":loop_end", ":max_players"), # if all players were checked, the trigger will succeed and wait the rearm interval before checking again
    (assign, "$g_loop_player_id", 1), # go back to the start (player id 0 is the server)
    (try_begin), # only decrease outlaw ratings at certain intervals, not every time
      (ge, ":time", "$g_loop_player_check_outlaw_time"),
      (val_add, "$g_loop_player_check_outlaw_time", loop_player_check_outlaw_interval),
      (assign, "$g_loop_player_check_outlaw", 1),
    (else_try),
      (assign, "$g_loop_player_check_outlaw", 0),
    (try_end),
    ], [])

agent_check_loop = (0, 0, 0.5, # server: loop over all agents, doing all common repetitive checks together for each agent, to minimize the penalty of using try_for_agents
   [(multiplayer_is_server),
    (try_begin), # if the loop was not restarted
      (gt, "$g_loop_agent_last_checked", -2),
      (assign, ":agent_id", -1),
      (try_for_agents, ":loop_agent_id"), # find the next agent id greater than the previous checked
        (eq, ":agent_id", -1),
        (gt, ":loop_agent_id", "$g_loop_agent_last_checked"),
        (assign, ":agent_id", ":loop_agent_id"),
      (try_end),
      (try_begin),
        (gt, ":agent_id", -1), # if a next agent id was found
        (assign, "$g_loop_agent_last_checked", ":agent_id"),
        (call_script, "script_check_agent_drowning", ":agent_id"),
        (try_begin),
          (eq, "$g_loop_horse_check", 1),
          (try_begin),
            (neg|agent_is_human, ":agent_id"),
            (call_script, "script_check_remove_lost_horse", ":agent_id"),
          (else_try),
            (call_script, "script_agent_remove_empty_ammo_stacks", ":agent_id"),
          (try_end),
        (try_end),
        (try_begin),
          (eq, "$g_loop_health_check", 1),
          (call_script, "script_check_agent_health", ":agent_id"),
        (try_end),
      (else_try),
        (assign, "$g_loop_agent_last_checked", -2),
      (try_end),
    (else_try), # setting up to restart the loop
      (store_mission_timer_a, ":time"),
      (try_begin),
        (ge, ":time", "$g_loop_agent_check_time"),
        (val_add, "$g_loop_agent_check_time", loop_agent_check_interval),
        (assign, "$g_loop_agent_last_checked", -1), # set to an invalid low agent id to start
        (try_begin),
          (ge, ":time", "$g_loop_horse_check_time"),
          (val_add, "$g_loop_horse_check_time", loop_horse_check_interval),
          (assign, "$g_loop_horse_check", 1),
        (else_try),
          (assign, "$g_loop_horse_check", 0),
        (try_end),
        (try_begin),
          (ge, ":time", "$g_loop_health_check_time"),
          (val_add, "$g_loop_health_check_time", loop_health_check_interval),
          (assign, "$g_loop_health_check", 1),
        (else_try),
          (assign, "$g_loop_health_check", 0),
        (try_end),
      (try_end),
    (try_end),
    (eq, "$g_loop_agent_last_checked", -2), # at the end of the loop, the trigger succeeds to wait the rearm interval before restarting
    ], [])

agent_check_attack_loop = (0, 0, 0.2, [], # server: repeatedly check all agents for attacking with a weapon they can't use - should be kept as simple as possible
   [(multiplayer_is_server),
    (try_for_agents, ":agent_id"),
      (agent_slot_eq, ":agent_id", slot_agent_cannot_attack, 1),
      (agent_get_attack_action, ":action", ":agent_id"),
      (is_between, ":action", 1, 7), # if the agent attack action is anything except "free" or "cancelling attack", unwield the weapon
      (agent_set_wielded_item, ":agent_id", -1),
    (try_end),
    ])

ship_movement_loop = (0, 0, 0.1, # server: update ship movement animations approximately every second
   [(try_begin),
      (multiplayer_is_server),
      (troop_get_slot, ":ship_array_end", "trp_ship_array", slot_ship_array_count),
      (gt, ":ship_array_end", 0),
      (try_begin), # after running the script for a moving ship, end the loop to allow other triggers to run, then immediately continue the loop
        (ge, "$g_loop_ship_to_check", slot_ship_array_begin),
        (val_add, ":ship_array_end", slot_ship_array_begin),
        (assign, ":loop_end", ":ship_array_end"),
        (try_for_range, ":ship_slot", "$g_loop_ship_to_check", ":loop_end"),
          (troop_get_slot, ":hull_instance_id", "trp_ship_array", ":ship_slot"),
          (scene_prop_slot_eq, ":hull_instance_id", slot_scene_prop_state, scene_prop_state_active),
          (try_begin), # if all possible movement slots make the ship stationary, skip
            (scene_prop_slot_eq, ":hull_instance_id", slot_scene_prop_position, 0),
            (scene_prop_slot_eq, ":hull_instance_id", slot_scene_prop_target_position, 0),
            (scene_prop_get_slot, ":ramp_instance_id", ":hull_instance_id", slot_scene_prop_linked_ramp),
            (try_begin),
              (neq, ":ramp_instance_id", -1),
              (scene_prop_get_slot, ":ramp_position", ":ramp_instance_id", slot_scene_prop_position),
              (scene_prop_slot_eq, ":ramp_instance_id", slot_scene_prop_target_position, ":ramp_position"),
              (assign, ":ramp_instance_id", -1),
            (try_end),
            (eq, ":ramp_instance_id", -1),
          (else_try), # otherwise, move the ship
            (call_script, "script_move_ship", ":hull_instance_id"),
            (assign, ":loop_end", -1),
          (try_end),
        (try_end),
        (store_add, "$g_loop_ship_to_check", ":ship_slot", 1),
        (try_begin),
          (ge, "$g_loop_ship_to_check", ":ship_array_end"),
          (assign, "$g_loop_ship_to_check", -1),
        (try_end),
      (else_try),
        (store_mission_timer_a, ":time"),
        (try_begin), # recheck the time every 0.1 seconds, but only move the ships every 1 second, so small extra delays in the trigger timer don't accumulate
          (ge, ":time", "$g_loop_ship_check_time"),
          (val_add, "$g_loop_ship_check_time", 1),
          (val_sub, ":time", 1),
          (val_max, "$g_loop_ship_check_time", ":time"),
          (assign, "$g_loop_ship_to_check", slot_ship_array_begin),
        (try_end),
      (try_end),
    (try_end),
    (this_or_next|eq, "$g_loop_ship_to_check", -1),
    (this_or_next|neg|multiplayer_is_server),
    (eq, ":ship_array_end", 0),
    ], [])

resource_regrow_check = (10, 0, 0, [], # server: call the script to regrow a removed scene prop after the required time
   [(multiplayer_is_server),
    (troop_get_slot, ":resources_count", "trp_removed_scene_props", slot_array_count),
    (gt, ":resources_count", 0),
    (val_add, ":resources_count", slot_array_begin),
    (try_for_range, ":resource_slot", slot_array_begin, ":resources_count"), # loop over all scene props added to the removed list
      (troop_get_slot, ":instance_id", "trp_removed_scene_props", ":resource_slot"),
      (le, ":instance_id", 0),
    (else_try),
      (scene_prop_get_slot, ":regrow_script", ":instance_id", slot_scene_prop_regrow_script),
      (eq, ":regrow_script", 0),
      (neg|scene_prop_slot_eq, ":instance_id", slot_scene_prop_state, scene_prop_state_hidden),
      (troop_set_slot, "trp_removed_scene_props", ":resource_slot", -1),
    (else_try),
      (scene_prop_get_slot, ":regen_time", ":instance_id", slot_scene_prop_state_time),
      (store_mission_timer_a, ":time"),
      (ge, ":time", ":regen_time"), # if the regeneration time is passed, remove from the list and call the stored script
      (troop_set_slot, "trp_removed_scene_props", ":resource_slot", -1),
      (try_begin),
        (eq, ":regrow_script", 0),
        (call_script, "script_regrow_resource", ":instance_id"),
      (else_try),
        (call_script, ":regrow_script", ":instance_id"),
      (try_end),
    (try_end),
    ])

polls_check = (2, 0, 0, [], # server: regularly check to see if any polls have ended
   [(multiplayer_is_server),
    (call_script, "script_check_polls_ended"),
    ])

game_ended_check = (1, 5, 0, # server: check for game end from victory or an admin scene change
   [(multiplayer_is_server),
    (eq, "$g_game_ended", 0),
    (store_mission_timer_a, ":current_time"),
    (store_mul, ":game_end_time", "$g_game_time_limit", 60),
    (try_begin), # check for the victory condition
      (call_script, "script_cf_victory_condition_met"),
      (assign, ":faction_id", reg0),
      (try_begin), # if only just met, store the time when the game could end
        (le, "$g_victory_condition_time", 0),
        (store_mul, "$g_victory_condition_time", "$g_victory_condition", 60),
        (val_add, "$g_victory_condition_time", ":current_time"),
      (else_try),
        (gt, "$g_victory_condition_time", 0),
        (this_or_next|ge, ":current_time", "$g_victory_condition_time"), # if the victory condition has held for the required time, end the game
        (ge, ":current_time", ":game_end_time"),
        (get_max_players, ":max_players"),
        (try_for_range, ":player_id", 1, ":max_players"),
          (player_is_active, ":player_id"),
          (multiplayer_send_3_int_to_player, ":player_id", server_event_preset_message, "str_s1_reign_supreme", preset_message_faction|preset_message_big|preset_message_log, ":faction_id"),
        (try_end),
        (assign, "$g_game_ended", 1),
      (try_end),
    (else_try), # reset the victory condition timer
      (assign, "$g_victory_condition_time", 0),
    (try_end),
    (this_or_next|eq, "$g_game_ended", 1),
    (this_or_next|is_between, "$g_next_scene", scenes_begin, scenes_end), # end the mission if an admin changes the scene
    (ge, ":current_time", ":game_end_time"),
    (assign, "$g_game_ended", 1),
    ],
   [(try_begin), # after the delay, start the next mission
      (neg|is_between, "$g_next_game_type", game_type_mission_templates_begin, game_type_mission_templates_end),
      (assign, "$g_next_game_type", game_type_mission_templates_begin),
    (try_end),
    (assign, ":started_manually", 1),
    (try_begin),
      (neg|is_between, "$g_next_scene", scenes_begin, scenes_end),
      (assign, "$g_next_scene", scenes_begin),
      (assign, ":started_manually", 0),
    (try_end),
    (start_multiplayer_mission, "$g_next_game_type", "$g_next_scene", ":started_manually"),
    (call_script, "script_game_set_multiplayer_mission_end"),
    ])

draw_initial_banners = (0, 0, ti_once, [], # server: calculate and draw all castle banners at mission start
   [(multiplayer_is_server),
    (call_script, "script_redraw_castle_banners", redraw_all_banners, -1),
    ])

fill_chests_starting_inventory = (8, 0, ti_once, [], # server: wait so the pseudo random number generator can get some entropy
   [(multiplayer_is_server),
    (call_script, "script_scene_fill_chests_starting_inventory"),
    ])

fire_place_check = (1, 0, 60, # server: wait 1 second between checks of fire heaps, then 60 seconds after all have been checked
   [(multiplayer_is_server),
    (scene_prop_get_instance, ":instance_id", "spr_pw_fire_wood_heap", "$g_fire_place_instance_no"),
    (call_script, "script_fire_place_burn", ":instance_id"),
    (val_add, "$g_fire_place_instance_no", 1),
    (scene_prop_get_num_instances, ":num_instances", "spr_pw_fire_wood_heap"),
    (try_begin),
      (ge, "$g_fire_place_instance_no", ":num_instances"),
      (assign, "$g_fire_place_instance_no", 0),
    (try_end),
    (eq, "$g_fire_place_instance_no", 0),
    ], [])

fish_school_loop = (0.1, 0, 30, # server: wait 0.1 seconds between checks of fish schools, then 30 seconds after all have been checked
   [(multiplayer_is_server),
    (try_begin),
      (scene_prop_get_instance, ":instance_id", "spr_pw_fish_school", "$g_fish_school_instance_no"),
      (call_script, "script_move_fish_school", ":instance_id"),
      (val_add, "$g_fish_school_instance_no", 1),
    (else_try), # at the loop end, check all nets as well
      (assign, "$g_fish_school_instance_no", 0),
      (call_script, "script_check_fishing_nets"),
    (try_end),
    (eq, "$g_fish_school_instance_no", 0),
    ], [])

herd_leader_movement_loop = (5, 0, 0, [], # server: check all animal herd leaders to see if any are ready to move
   [(multiplayer_is_server),
    (le, "$g_loop_animal_herd_begin", 0), # not currently moving a herd
    (scene_spawned_item_get_num_instances, ":herds_end", "itm_animal_herd_manager"),
    (try_begin),
      (ge, "$g_loop_animal_herd_to_move", ":herds_end"),
      (assign, "$g_loop_animal_herd_to_move", 0),
    (try_end),
    (store_mission_timer_a, ":time"), # loop over next herd managers to check if any are ready to move
    (try_for_range, "$g_loop_animal_herd_to_move", "$g_loop_animal_herd_to_move", ":herds_end"),
      (scene_spawned_item_get_instance, ":herd_manager", "itm_animal_herd_manager", "$g_loop_animal_herd_to_move"),
      (assign, "$g_loop_animal_herd_leader", -1),
      (scene_prop_get_slot, ":adult_item_id", ":herd_manager", slot_animal_herd_manager_adult_item_id),
      (item_get_slot, ":loop_end", ":adult_item_id", slot_item_animal_max_in_herd),
      (try_for_range, ":herd_slot", 0, ":loop_end"), # loop over animals in the herd
        (scene_prop_get_slot, ":herd_agent_id", ":herd_manager", ":herd_slot"),
        (gt, ":herd_agent_id", -1),
        (try_begin),
          (agent_is_active, ":herd_agent_id"),
          (agent_get_item_id, ":herd_item_id", ":herd_agent_id"),
          (agent_slot_eq, ":herd_agent_id", slot_agent_animal_herd_manager, ":herd_manager"),
          (gt, ":herd_item_id", -1),
          (item_slot_eq, ":herd_item_id", slot_item_animal_adult_item_id, ":adult_item_id"),
          (try_begin), # if the leader has been found, set the times for the followers to move
            (neq, "$g_loop_animal_herd_leader", -1),
            (store_random_in_range, ":move_time", 0, 6),
            (val_add, ":move_time", ":time"),
            (agent_set_slot, ":herd_agent_id", slot_agent_animal_move_time, ":move_time"),
          (else_try), # the first valid animal found is the leader: start the movement if the set time is met
            (assign, "$g_loop_animal_herd_leader", ":herd_agent_id"),
            (neg|agent_slot_ge, ":herd_agent_id", slot_agent_animal_move_time, ":time"),
            (assign, ":herds_end", -1), # break out of the herd manager checking loop after the animal loop is finished
            (store_add, "$g_loop_animal_herd_begin", ":herd_slot", 1),
            (store_random_in_range, ":move_time", 5, 31), # set the next move time
            (val_add, ":move_time", ":time"),
            (agent_set_slot, "$g_loop_animal_herd_leader", slot_agent_animal_move_time, ":move_time"),
            (call_script, "script_animal_move", "$g_loop_animal_herd_leader", "$g_loop_animal_herd_leader"), # move the leader
          (else_try), # if the leader movement time is not met, skip to the next herd manager to check
            (assign, ":loop_end", -1),
          (try_end),
        (else_try), # if the animal or agent id is not valid, remove it from the herd manager
          (scene_prop_set_slot, ":herd_manager", ":herd_slot", -1),
          (agent_is_active, ":herd_agent_id"),
          (le, ":herd_item_id", -1),
          (agent_set_slot, ":herd_agent_id", slot_agent_animal_herd_manager, -1),
        (try_end),
      (try_end),
      (try_begin), # if no valid animals are found, remove the herd manager
        (eq, "$g_loop_animal_herd_leader", -1),
        (scene_prop_set_prune_time, ":herd_manager", 1),
      (try_end),
    (try_end),
    ])

herd_follower_movement_loop = (0.5, 0, 0, [], # server: when currently moving a herd, check the follower animals for any ready to move
   [(multiplayer_is_server),
    (gt, "$g_loop_animal_herd_begin", 0), # currently moving a herd
    (try_begin), # if the herd leader and manager are valid
      (agent_is_active, "$g_loop_animal_herd_leader"),
      (scene_spawned_item_get_instance, ":herd_manager", "itm_animal_herd_manager", "$g_loop_animal_herd_to_move"),
      (store_mission_timer_a, ":time"),
      (scene_prop_get_slot, ":adult_item_id", ":herd_manager", slot_animal_herd_manager_adult_item_id),
      (item_get_slot, ":loop_end", ":adult_item_id", slot_item_animal_max_in_herd),
      (assign, ":remaining_to_move", 0),
      (try_for_range, ":herd_slot", "$g_loop_animal_herd_begin", ":loop_end"), # loop over the followers to check if any are ready to move
        (scene_prop_get_slot, ":herd_agent_id", ":herd_manager", ":herd_slot"),
        (agent_is_active, ":herd_agent_id"),
        (agent_get_slot, ":move_time", ":herd_agent_id", slot_agent_animal_move_time),
        (gt, ":move_time", 0),
        (try_begin),
          (ge, ":time", ":move_time"),
          (agent_set_slot, ":herd_agent_id", slot_agent_animal_move_time, 0),
          (call_script, "script_animal_move", ":herd_agent_id", "$g_loop_animal_herd_leader"),
        (else_try),
          (val_add, ":remaining_to_move", 1),
        (try_end),
      (try_end),
      (gt, ":remaining_to_move", 0), # if any followers are still waiting
    (else_try), # otherwise, go back to the herd manager checking loop
      (assign, "$g_loop_animal_herd_begin", 0),
      (val_add, "$g_loop_animal_herd_to_move", 1),
    (try_end),
    ])

herd_animal_count_check = (300, 0, 0, [], # server: periodically update the global count of herd animals - rare conditions seemed to make this value incorrect over time
   [(multiplayer_is_server),
    (assign, "$g_herd_animal_count", 0),
    (try_for_agents, ":agent_id"),
      (agent_slot_ge, ":agent_id", slot_agent_animal_birth_time, 1),
      (val_add, "$g_herd_animal_count", 1),
    (try_end),
    ])

herd_animal_spawn_check = (60, 0, 0, [], # server: check all herd animal spawners to see if any are ready to activate
   [(multiplayer_is_server),
    (try_begin), # if the maximum number of herd animals in the server is not reached, check the spawners
      (lt, "$g_herd_animal_count", "$g_max_herd_animal_count"),
      (scene_prop_get_instance, ":instance_id", "spr_pw_herd_animal_spawn", "$g_herd_animal_spawn_instance_no"),
      (val_add, "$g_herd_animal_spawn_instance_no", 1),
      (scene_prop_get_slot, ":spawn_time", ":instance_id", slot_scene_prop_state_time),
      (store_mission_timer_a, ":time"),
      (try_begin), # if the spawning time has been reached
        (gt, ":time", ":spawn_time"),
        (prop_instance_get_variation_id_2, ":next_spawn_time", ":instance_id"),
        (try_begin), # if the spawn interval value is not set, get a random time between 1 and 4 hours
          (lt, ":next_spawn_time", 1),
          (store_random_in_range, ":next_spawn_time", 3600, 24001),
        (else_try), # otherwise, convert it to hours and apply a random adjustment between +/- 20%
          (val_mul, ":next_spawn_time", 3600),
          (store_random_in_range, ":random_adjustment", 80, 121),
          (val_mul, ":next_spawn_time", ":random_adjustment"),
          (val_div, ":next_spawn_time", 100),
        (try_end),
        (scene_prop_set_slot, ":instance_id", slot_scene_prop_state_time, ":next_spawn_time"),
        (gt, ":spawn_time", 0), # if not mission start
        (prop_instance_get_variation_id, ":animal_item_id", ":instance_id"),
        (try_begin), # use the animal type if set
          (val_add, ":animal_item_id", herd_animal_items_begin),
          (val_sub, ":animal_item_id", 1),
          (is_between, ":animal_item_id", herd_animal_items_begin, herd_animal_items_end),
        (else_try), # otherwise get a random herd animal
          (store_random_in_range, ":animal_item_id", herd_animal_items_begin, herd_animal_items_end),
        (try_end),
        (prop_instance_get_position, pos1, ":instance_id"),
        (call_script, "script_cf_spawn_herd_animal", ":animal_item_id", -1),
      (try_end),
    (else_try),
      (assign, "$g_herd_animal_spawn_instance_no", 0),
    (try_end),
    ])

weather_situation_check = (loop_weather_adjust_interval, 0, 0, [], # server: adjust the weather systems in the scene
   [(multiplayer_is_server),
    (call_script, "script_scene_adjust_weather_situation"),
    ])

escape_pressed = (ti_escape_pressed, 0, 0, [], # clients: show escape menu
   [(call_script, "script_cf_no_input_presentation_active"),
    (start_presentation, "prsnt_escape_menu"),
    ])

tab_pressed = (ti_tab_pressed, 0, 0, [], # clients: show player stats chart when that control is pressed (not necessarily tab)
   [(call_script, "script_cf_no_input_presentation_active"),
    (neg|is_presentation_active, "prsnt_tabbed_stats_chart"),
    (assign, "$g_stats_chart_opened_manually", 1),
    (start_presentation, "prsnt_tabbed_stats_chart"),
    ])

static_presentations_setup = (ti_battle_window_opened, 0, 0, [], # clients: called after connecting and when returning from the log window (which clears all presentations)
   [(try_begin),
      (eq, "$g_display_agent_labels", 1),
      (start_presentation, "prsnt_display_agent_labels"),
    (try_end),
    (try_begin),
      (eq, "$g_display_chat_overlay", 1),
      (start_presentation, "prsnt_chat_overlay"),
    (try_end),
    (try_begin),
      (gt, "$g_respawn_start_time", 0),
      (start_presentation, "prsnt_respawn_time_counter"),
    (try_end),
    (try_begin),
      (neq, "$g_game_type", "mt_no_money"),
      (start_presentation, "prsnt_gold"),
    (try_end),
    (start_presentation, "prsnt_food_bar"),
    (start_presentation, "prsnt_scene_prop_hit_points_bar"),
    (start_presentation, "prsnt_multiplayer_artillery_icons"),
    (try_begin), # if an inventory was being accessed before the presentations were cleared, notify the server to stop sending updates
      (gt, "$g_show_inventory_instance_id", 0),
      (assign, "$g_show_inventory_instance_id", 0),
      (multiplayer_send_message_to_server, client_event_transfer_inventory),
    (try_end),
    ])

action_menu_pressed = (0, 0, 0, [], # clients: show action menu while that control is held down
   [(game_key_clicked, gk_action_menu),
    (call_script, "script_cf_no_input_presentation_active"),
    (neg|is_presentation_active, "prsnt_action_menu"),
    (start_presentation, "prsnt_action_menu"),
    ])

target_agent_pressed = (0, 0.3, 0, # clients: allow aiming at other agents or corpses to select them
   [(game_key_is_down, gk_target_agent),
    (call_script, "script_cf_no_input_presentation_active"),
    (multiplayer_get_my_player, ":player_id"),
    (player_is_active, ":player_id"),
    (try_begin), # if shift is down, select live agents while the control is held down
      (this_or_next|key_is_down, key_left_shift),
      (key_is_down, key_right_shift),
      (call_script, "script_select_target_agent"),
      (assign, "$g_targeting_corpses", 0),
    (else_try), # otherwise select corpses, running the loot script when the control is released
      (call_script, "script_select_target_corpse"),
      (assign, "$g_targeting_corpses", 1),
    (try_end),
    ],
   [(eq, "$g_targeting_corpses", 1),
    (neg|game_key_is_down, gk_target_agent),
    (call_script, "script_loot_target_corpse"),
    ])

chat_overlay_toggled = (0, 0, 0, [], # clients: toggle the overlay for local or faction chat
   [(key_clicked, key_f10),
    (call_script, "script_cf_no_input_presentation_active"),
    (try_begin),
      (neg|is_presentation_active, "prsnt_chat_overlay"),
      (assign, "$g_display_chat_overlay", 1),
      (start_presentation, "prsnt_chat_overlay"),
    (else_try),
      (assign, "$g_display_chat_overlay", 0),
    (try_end),
    ])

chat_resend_check = (0.3, 0.3, 0, [(troop_slot_eq, "trp_last_chat_message", slot_last_chat_message_not_recieved, 1)], # clients: try to resend lost chat mesages
   [(troop_slot_eq, "trp_last_chat_message", slot_last_chat_message_not_recieved, 1), # if the server has not confirmed receiving the last chat message for at least 0.3 seconds
    (troop_get_slot, ":event", "trp_last_chat_message", slot_last_chat_message_event_type), # resend the chat type and string
    (try_begin),
      (gt, ":event", net_chat_event_mask),
      (multiplayer_send_int_to_server, client_event_chat_message_type, ":event"),
    (try_end),
    (val_and, ":event", net_chat_event_mask),
    (str_store_troop_name, s0, "trp_last_chat_message"),
    (multiplayer_send_string_to_server, ":event", s0),
    ])

# PN START *******************************************************************************************************************

multiplayer_client_surrender = (
  0, 0.5, 0.1, [
  (neg|multiplayer_is_dedicated_server),
  (key_clicked, key_b),
  (try_begin),
    (call_script,"script_client_get_my_agent"),
    (assign,":agent_id",reg0),
    (agent_is_active,":agent_id"),
    (agent_is_alive,":agent_id"),
    (multiplayer_send_2_int_to_server, multiplayer_event_send_player_action, player_action_surrender,music_type_start),
    (multiplayer_send_2_int_to_server,multiplayer_event_send_player_action,player_action_voice,voice_type_surrender),
  (try_end),
  ],
  [
    (try_begin),
      (call_script,"script_client_get_my_agent"),
      (assign,":agent_id",reg0),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (multiplayer_send_2_int_to_server, multiplayer_event_send_player_action, player_action_surrender,music_type_start),
    (try_end),
  ])

multiplayer_client_walking = (
  0, 0, 0.1, [
  (game_key_clicked, gk_zoom),
  ],
  [
    (try_begin),
      (neg|is_zoom_disabled),
      (multiplayer_get_my_player, ":player_id"),
      (player_is_active, ":player_id"),
      (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
    (else_try),
      (call_script,"script_client_get_my_agent"),
      (assign,":agent_id",reg0),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_toggle_walk),
    (try_end),
])

multiplayer_client_spyglass = (
  0, 0, 1, [
  (neg|multiplayer_is_dedicated_server),
  (game_key_is_down,gk_defend),
  ],
  [
    (neg|is_presentation_active,"prsnt_spyglass_dummy"),
    (neg|is_presentation_active,"prsnt_drinking"),
    (call_script,"script_client_get_my_agent"),
    (assign,":agent_id",reg0),
    (agent_is_active,":agent_id"),
    (agent_is_alive,":agent_id"),
    (agent_get_wielded_item,":item_id",":agent_id",0),
    (try_begin),
      (eq,":item_id","itm_spyglass"),
      (start_presentation,"prsnt_spyglass_dummy"),
    (else_try),
      #drinking
      (call_script, "script_multiplayer_agent_drinking_get_animation", ":item_id"),
      (this_or_next|eq, ":item_id", "itm_drinking_cup"),
      (this_or_next|eq, ":item_id", "itm_drinking_tea_cup"),
      (this_or_next|eq, ":item_id", "itm_drinking_tea_cup_plate"),
      (eq, ":item_id", "itm_drinking_bottle"),
      (start_presentation, "prsnt_drinking"),
      #end drinking
    (try_end),
  ])

# Trigger Param 1: damage inflicted agent_id
# Trigger Param 2: damage dealer agent_id
# Trigger Param 3: inflicted damage
# Register 0: damage dealer item_id
# Position Register 0: position of the blow
#                      rotation gives the direction of the blow
# Trigger result: if returned result is greater than or equal to zero, inflicted damage is set to the value specified by the module.
# this trigger is called server only apparently after testing lol.. just added checks to make sure. ( you know warband patches.. :P )
multiplayer_server_agent_hit_common = (ti_on_agent_hit, 0, 0, [],
  [
    (store_trigger_param_1,":hit_agent_no"),
    (assign,":item_id",reg0),

    (try_begin),
       (try_begin), 
        (agent_is_active,":hit_agent_no"),
        (gt,"$g_chance_of_falling_off_horse",0),
        (agent_get_horse,":horse",":hit_agent_no"),
        (agent_is_active,":horse"),
        (agent_is_alive,":hit_agent_no"),

        (store_trigger_param_3,":damage"),
        (ge,":damage",10),
           
        (neg|agent_is_non_player,":hit_agent_no"), #Only do this to players
        (neg|agent_slot_eq,":hit_agent_no",slot_agent_has_fallen_off_horse,1), #Apparently there's some bug if you fall off twice

        (store_random_in_range,":random",0,100),
        (lt,":random","$g_chance_of_falling_off_horse"),
           
        (store_random_in_range,":anim",0,2),
        (val_add,":anim","anim_rider_fall_right_2"),
        (agent_set_animation,":hit_agent_no",":anim"),
        (agent_set_slot,":hit_agent_no",slot_agent_has_fallen_off_horse,1), #Apparently there's some bug if you fall off twice
        (agent_clear_scripted_mode,":horse"),
        (agent_start_running_away,":horse"),
        
      (try_begin),
        (gt,"$g_damage_from_horse_dying",0),
        (neg|agent_is_human,":hit_agent_no"), #Horse
        (agent_get_rider,":rider",":hit_agent_no"),
          
        (agent_is_active,":rider"),
        (agent_is_alive,":rider"),
          
        (store_trigger_param_3,":damage"),
        (store_agent_hit_points,":hit_points",":hit_agent_no",1),
        (val_sub,":hit_points",":damage"),
        (le,":hit_points",0),
          
        (store_trigger_param_2,":attacker_agent_no"),
        (store_random_in_range,":damage_to_rider",10,20),
        (val_mul,":damage_to_rider","$g_damage_from_horse_dying"),
        (val_div,":damage_to_rider",100),
          
        (try_begin),
          (eq,":item_id",-1),
          (assign,":item_id","itm_russian_peasant_knife"),
        (try_end),
        (agent_deliver_damage_to_agent_advanced,":damage", ":attacker_agent_no", ":rider", ":damage_to_rider", ":item_id"),
        (try_end),
        
        (try_begin),
          (agent_slot_ge,":hit_agent_no",slot_agent_current_control_prop,0), # we are controlling a prop.
          (try_begin),
            (agent_get_slot,":prop_instance",":hit_agent_no",slot_agent_current_control_prop),
            (prop_instance_is_valid,":prop_instance"),
            (prop_instance_get_scene_prop_kind,":prop_kind",":prop_instance"),
            (try_begin),
              (is_between,":prop_kind",mm_cannon_wood_types_begin,mm_cannon_wood_types_end),
              (call_script,"script_stop_agent_controlling_cannon",":prop_instance",":hit_agent_no"),
            (else_try),
              (call_script,"script_set_agent_controlling_prop",":prop_instance",":hit_agent_no",0),
            (try_end),
          (try_end),
        (else_try),
          (agent_slot_ge,":hit_agent_no",slot_agent_used_prop_instance,0), #CONTINUAR
          
          (call_script,"script_multiplayer_server_agent_stop_music",":hit_agent_no"),
        (else_try),
          #(call_script, "script_cf_agent_is_playing_music", ":hit_agent_no"), # is playing
          # if we have a musician just to be sure call stop music.
          (agent_get_troop_id,":troop_no",":hit_agent_no"),
          (this_or_next|eq,":troop_no", "trp_military_musician"),
          (eq, ":troop_no", "trp_godlike_hero"),
          (call_script,"script_multiplayer_server_agent_stop_music",":hit_agent_no"),
        (try_end),

        # horsies. clear their scripted mode.
        (try_begin),
          (neg|agent_is_human,":hit_agent_no"),
          
          (agent_get_rider, ":rider_agent_id", ":hit_agent_no"),
          (lt, ":rider_agent_id", 0),
          (agent_get_item_id,":horse_kind", ":hit_agent_no"),
          
          (neg|item_slot_eq,":horse_kind",slot_item_multiplayer_item_class, multi_item_class_type_horse_cannon),
          (neg|item_slot_eq,":horse_kind",slot_item_multiplayer_item_class, multi_item_class_type_horse_howitzer),
          
          (agent_clear_scripted_mode,":hit_agent_no"),
        (try_end),
      (try_end),
    (try_end),

    ##drinking bottle break script
    (try_begin),
      (eq, ":item_id", "itm_drinking_bottle_melee"),
      (store_trigger_param_2, ":attacker_agent_no"),
      (assign, ":end_cond", ek_head),
      (try_for_range, ":equipment_slot", ek_item_0, ":end_cond"),
        (agent_get_item_slot, ":cur_item_id", ":attacker_agent_no", ":equipment_slot"),
        (this_or_next|eq, ":cur_item_id", "itm_drinking_bottle_melee"),
        (eq, ":cur_item_id", "itm_drinking_bottle"),
        (val_add, ":equipment_slot", 1),
        (agent_unequip_item, ":attacker_agent_no", ":cur_item_id", ":equipment_slot"),
        (agent_equip_item, ":attacker_agent_no", "itm_brokenbottle", ":equipment_slot"),
        (agent_set_wielded_item, ":attacker_agent_no", "itm_brokenbottle"),
        (call_script, "script_multiplayer_server_play_sound_at_agent", "snd_glass_break", ":attacker_agent_no"),
        (assign, ":end_cond", 0),
      (try_end),
    (try_end),
    ##end drinking bottle break script
  ])

# This is the taunt:
multiplayer_client_voice_warcry = (
  0, 0, 1, [(key_clicked, key_v),],
  [
    (store_mission_timer_a, ":current_time"),
    (store_sub, ":elapsed_time", ":current_time", "$g_last_voice_command_at"),
    
    (call_script, "script_client_get_my_agent"),
    (assign, ":player_agent", reg0),
    
    (agent_is_active,":player_agent"),
    (agent_is_alive, ":player_agent"), # Still alive?
    
    (try_begin),
      (call_script,"script_cf_agent_is_playing_music",":player_agent"), # when playing music dont do anything.
    (else_try),
      (call_script,"script_cf_agent_is_playing_piano",":player_agent"), # when playing music dont do anything.
    (else_try),
      (assign, ":wait_time", "$g_time_between_voice_commands"),
      
      (val_add,":wait_time",5), # add two due to lag...  changed to 5.
      (gt, ":elapsed_time", ":wait_time"), # last command more then x seconds ago. 

      # not in some presentation?
      (neg|is_presentation_active, "prsnt_escape_menu"),
      (neg|is_presentation_active, "prsnt_game_multiplayer_admin_panel"),
      (neg|is_presentation_active, "prsnt_admin_message"),
      (neg|is_presentation_active, "prsnt_chat_box"), #custom_chat:
      
      (assign, ":voice_type", -1),
      (try_begin),
        (key_clicked, key_v),
        (assign, ":voice_type", voice_type_cry),
      (try_end),

      (try_begin),
        (gt, ":voice_type", -1),
        (multiplayer_send_2_int_to_server, multiplayer_event_send_player_action, player_action_voice, ":voice_type"),
        (store_mission_timer_a, "$g_last_voice_command_at"),
      (try_end),
    (try_end),
])

multiplayer_client_voice_orders = (
  0, 0.5, 0.1,[(key_clicked, key_o)],
  [
    (neg|multiplayer_is_dedicated_server),
    (try_begin),
      (call_script,"script_client_get_my_agent"),
      (assign,":agent_id",reg0),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (start_presentation,"prsnt_orders_menu"),
    (try_end),
])

multiplayer_client_music_and_sapper = (
  0, 0, 0, [(neg|multiplayer_is_dedicated_server),(game_key_clicked, gk_defend),],
  [
    (try_begin),
      (call_script, "script_client_get_my_agent"),
      (assign, ":player_agent", reg0),

      (agent_is_active,":player_agent"),
      (agent_is_alive, ":player_agent"), # Still alive?
      (try_begin), # stop playing piano
        (call_script,"script_cf_agent_is_playing_piano",":player_agent"),
        (multiplayer_send_2_int_to_server, multiplayer_event_send_player_action, player_action_music, music_type_stop),

      (else_try),
        (call_script,"script_cf_agent_is_taking_a_shit",":player_agent"),
        (multiplayer_send_2_int_to_server, multiplayer_event_send_player_action, player_action_music, music_type_stop),

      (else_try),
        (call_script,"script_cf_agent_is_surrendering",":player_agent"),
        (multiplayer_send_2_int_to_server, multiplayer_event_send_player_action, player_action_surrender, music_type_stop),

      (else_try),
        (agent_get_troop_id,":player_troop",":player_agent"),
        (agent_get_wielded_item,":item_id",":player_agent",0),
        (ge, ":item_id", 0),
        (try_begin),
          (eq,":player_troop","trp_sapper"),
          (is_between,":item_id","itm_construction_hammer","itm_shovel"), #Hammer
          #(neg|is_presentation_active, "prsnt_multiplayer_construct"),
          #(start_presentation,"prsnt_multiplayer_construct"),
        (else_try),
          (this_or_next|eq,":player_troop","trp_military_musician"),
          (eq, ":player_troop", "trp_godlike_hero"),
          (is_between, ":item_id", "itm_drumstick_right", "itm_bullets"), # an instrument
          (try_begin),
            (call_script,"script_cf_agent_is_playing_music",":player_agent"),
            (neg|is_presentation_active, "prsnt_multiplayer_music"),
            (try_begin),
              (store_mission_timer_a,":cur_time"),
              (store_sub, ":elapsed_time", ":cur_time", "$g_started_playing_music_at"),
              (lt,":elapsed_time",2),
            (else_try),
              (multiplayer_send_2_int_to_server, multiplayer_event_send_player_action, player_action_music, music_type_stop),
            (try_end),
          (else_try),
            (neg|is_presentation_active, "prsnt_multiplayer_music"),
            (start_presentation,"prsnt_multiplayer_music"),
          (try_end),
        (else_try),
          (this_or_next|eq,":player_troop","trp_artillerist"),
          (this_or_next|eq,":player_troop","trp_artillerist_officer"),
          (eq, ":player_troop", "trp_godlike_hero"),
          (eq,":item_id", "itm_rocket_placement"),
          (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_place_rocket),
        (try_end),
      (try_end),
    (try_end)
])

multiplayer_agent_wield_item_common = (
  ti_on_item_wielded, 0, 0, [
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode)],
  [
    (store_trigger_param_1,":agent_id"),
    (store_trigger_param_2,":item_id"),
    
    (try_begin),
      (gt,":item_id",-1),
      (try_begin),
        (call_script,"script_cf_agent_is_playing_piano",":agent_id"),
        (call_script,"script_multiplayer_server_agent_stop_music", ":agent_id"),
      (else_try),
        (call_script,"script_cf_agent_is_taking_a_shit",":agent_id"),
        (call_script,"script_multiplayer_server_agent_stop_music", ":agent_id"),

      (else_try),
        (call_script,"script_cf_agent_is_surrendering",":agent_id"),
        (set_fixed_point_multiplier,100),
        (agent_set_speed_modifier,":agent_id", 100),
        (agent_set_slot,":agent_id",slot_agent_base_speed_mod,100),
        (agent_set_horse_speed_factor, ":agent_id", 100),
      (try_end),
    (try_end),
])

multiplayer_agent_unwield_item_common = (
  ti_on_item_unwielded, 0.1, 0, [
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode)],
  [
    (store_trigger_param_1,":agent_no"),
    (store_trigger_param_2,":item_id"),
      
    (try_begin),
      (gt,":item_id",-1),
      #(this_or_next|item_slot_eq,":item_id",slot_item_multiplayer_item_class, multi_item_class_type_flag), #always use item classes!!!
      (eq,":item_id","itm_rocket_placement"),
      
      (agent_is_active,":agent_no"),
      (neg|agent_is_non_player, ":agent_no"),  #patch1115 fix43/11
      (agent_get_position,pos25,":agent_no"),
      (position_move_y,pos25,30),
      (try_begin),
        (neq,":item_id","itm_rocket_placement"), # dont rotate up for the rocketplacement
        
        (agent_get_horse, ":agent_horse", ":agent_no"),
        (try_begin),
          (gt, ":agent_horse", -1),
          (position_move_x,pos25,50),
        (else_try),
          (position_move_z,pos25,36),
        (try_end),
        
        (position_rotate_x,pos25,90),
      (try_end),
      (set_spawn_position,pos25),
      (spawn_item,":item_id",0,300), # remove after 5 minutes
      
      (assign, ":end_cond", ek_head),
      (try_for_range,":equipment_slot",ek_item_0,":end_cond"),
        (agent_get_item_slot, ":cur_item_id", ":agent_no", ":equipment_slot"),
        (eq,":cur_item_id",":item_id"),
        (val_add,":equipment_slot",1),
        (agent_unequip_item, ":agent_no", ":item_id", ":equipment_slot"),
        (assign,":end_cond",0),
      (try_end),
      
      #(agent_unequip_item,":agent_no",":item_id"),
    (else_try),
      (call_script, "script_cf_agent_is_playing_music", ":agent_no"), # is playing
      
      (call_script,"script_multiplayer_server_agent_stop_music",":agent_no"),
    (try_end),
])

multiplayer_server_bird_spawn_common = (
  ti_after_mission_start, 0, 0, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode),],
  [
    (store_random_in_range,":num_birds_to_spawn",0,4),
    (try_for_range,":unused",0,":num_birds_to_spawn"),
      (store_random_in_range,":entry",0,64),
      (entry_point_get_position,pos49,":entry"),
      (set_fixed_point_multiplier,100),
      (position_set_z,pos49,9000),
      
      (call_script, "script_find_or_create_scene_prop_instance", "spr_mm_bird", 0, 0, 0),
    (try_end),
])

multiplayer_server_move_bird_common = (
  5.55, 0, 0, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode),],
  [
    (set_fixed_point_multiplier,100),
    
    (scene_prop_get_num_instances, ":num_instances", "spr_mm_bird"),
    (try_for_range,":prop_no",0,":num_instances"),
      (scene_prop_get_instance,":bird_id","spr_mm_bird",":prop_no"),
      (scene_prop_slot_eq,":bird_id", scene_prop_slot_in_use, 1),
      
      (prop_instance_get_position, pos23, ":bird_id"),
      
      (try_begin),
        (store_random_in_range,":play_sound",0,100),
        (lt,":play_sound",5),
        (copy_position,pos56,pos23),
        (call_script, "script_multiplayer_server_play_sound_at_position", "snd_ambient_buzzard"),
      (try_end),
      
      (store_random_in_range,":rotation_angle",-50,51),
      (position_rotate_z,pos23,":rotation_angle"),
      (position_move_y,pos23,500,0),#2500
      (prop_instance_animate_to_position, ":bird_id", pos23, 560),#2000
    (try_end),
])

multiplayer_server_drag_limber = (
0.25, 0, 0, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode),],
  [  
    (try_for_prop_instances, ":instance_id", "spr_mm_limber_wood", somt_temporary_object),
      (scene_prop_get_slot,":cur_control_agent",":instance_id",scene_prop_slot_carrier_agent),
      (ge, ":cur_control_agent", 0),
      
      (assign,":agent_is_ok",0),
      (try_begin),
        (agent_is_active, ":cur_control_agent"),
        (agent_is_alive, ":cur_control_agent"),
        (assign,":agent_is_ok",1),
      (else_try), # The agent died... lets set some vars on this one.
        (scene_prop_set_slot,":instance_id",scene_prop_slot_carrier_agent,-1),
        
        (store_mission_timer_a,":cur_time"),
        (scene_prop_set_slot,":instance_id",scene_prop_slot_spawned_at,":cur_time"),
        
        (prop_instance_get_animation_target_position,pos12,":instance_id"),
        (position_set_z_to_ground_level,pos12),
        (position_move_z,pos12,-30),
        (position_move_y,pos12,-18),
        (position_rotate_x,pos12,-22),
        (prop_instance_animate_to_position,":instance_id",pos12,100),
      (try_end),
      (eq,":agent_is_ok",1),
      
      (scene_prop_get_slot,":wheels_instance",":instance_id",scene_prop_slot_child_prop1),
      (scene_prop_get_slot,":cannon_instance",":instance_id",scene_prop_slot_child_prop2),
      (try_begin),
        (prop_instance_is_valid,":cannon_instance"),
        (scene_prop_get_slot,":cannon_wheels_instance",":cannon_instance",scene_prop_slot_child_prop1),
      (try_end),
      
      # if this limber has wheels
      (prop_instance_is_valid,":wheels_instance"),
      
      (set_fixed_point_multiplier, 1000),
      (agent_get_position, pos11, ":cur_control_agent"),
      (position_get_rotation_around_z,":z_rot_temp",pos11),
      
      (agent_get_speed, pos14, ":cur_control_agent"),
      (position_get_y,":agent_speed",pos14),
      
      (assign,":continue",1),
      (try_begin),
        (agent_get_slot,":old_zrot",":cur_control_agent",slot_agent_last_rotz),
        
        (try_begin),
          (eq,":agent_speed",0), # same speed now
          (eq,":z_rot_temp",":old_zrot"), # same rot.
          (agent_get_slot,":samecount",":cur_control_agent",slot_agent_last_speed_same_count),
          (try_begin),
            (gt,":samecount",2), # 2 times same shit.
            (assign,":continue",0),
          (else_try),
            (val_add,":samecount",1),
            (agent_set_slot, ":cur_control_agent", slot_agent_last_speed_same_count, ":samecount"),
          (try_end),
        (else_try),
          (agent_set_slot, ":cur_control_agent", slot_agent_last_speed_same_count, 0),
        (try_end),
        
        (agent_set_slot, ":cur_control_agent", slot_agent_last_rotz, ":z_rot_temp"),
      (try_end),
      (eq,":continue",1),
      
      # (try_begin),
        # (eq,":agent_speed",0), # no movement...
        # (position_get_rotation_around_z,":z_rot_temp",pos11),
        # (prop_instance_get_position, pos13, ":instance_id"),
        # (position_get_rotation_around_z,":prop_z_rot_temp",pos13),
        # (eq,":prop_z_rot_temp",":z_rot_temp"),
        # (assign,":continue",0),
      # (try_end),
       
      
      # max speed 2907  old:  2766
        # (assign, reg0, ":agent_speed"),
        # (str_store_string, s4, "@agent_speed: {reg0}"),
        # (call_script, "script_multiplayer_broadcast_message"),
      
      (store_mul,":agent_speed_wheel",":agent_speed",-1), # inverse
      (store_div,":limber_wheel_speed",":agent_speed_wheel",64), # make it realistic for front wheels
      (store_div,":cannon_wheel_speed",":agent_speed_wheel",76), # make it realistic for cannon wheels
      
      # From the agent position (flat on ground middle of horse) only save the Z rot and origin.
      (position_get_rotation_around_z,":z_rot",pos11),
      (init_position,pos12),
      (position_copy_origin,pos12,pos11),
      (position_rotate_z,pos12,":z_rot"),
      
      # move above ground. (for proper get_distance_to_ground checks)
      (scene_prop_get_slot,":z_offset",":instance_id",scene_prop_slot_z_value),
      (position_move_z,pos12,":z_offset"),
      
      # copy it over to 14 for later use, now just use 12 for getting rotations.
      (copy_position,pos14,pos12),
      
      # move from middle of horse to center where wheels should be.
      (scene_prop_get_slot,":y_offset",":wheels_instance",scene_prop_slot_y_value),
      (position_move_y, pos12,":y_offset"),
      
      # march to left wheel and get height there.
      (position_move_x,pos12,-60),
      (position_get_distance_to_ground_level, ":left_height_to_terrain", pos12),
      (val_div,":left_height_to_terrain",10), # due to fixed point at 1000
      
      # march to right wheel and get height there.
      (position_move_x,pos12,120),
      (position_get_distance_to_ground_level, ":right_height_to_terrain", pos12),
      (val_div,":right_height_to_terrain",10), # due to fixed point at 1000
      
      # march back to center
      # (position_rotate_z,pos12,180),
      # (position_move_y,pos12,60),
      # (position_rotate_z,pos12,-90),
      
      # calculate
      (store_sub,":height_difference",":left_height_to_terrain",":right_height_to_terrain"),
     
      (store_div,":combined_height",":height_difference",2),
      (try_begin),
        (gt,":combined_height",0),
        (val_mul,":combined_height",-1),
      (try_end),      

      (val_mul,":height_difference",1000), # make it fixed point
      (store_div,":deg_value2",":height_difference",120),  # 120 is distance between the two wheels.
      (store_atan,":deg_value2",":deg_value2"), # get the angle
      (val_div,":deg_value2",1000),
      (val_mul,":deg_value2",-1),

      
      # combine the two heights and get the angle between them combined and the horse position.
      (store_add,":height_to_terrain",":left_height_to_terrain",":right_height_to_terrain"),
      (val_div,":height_to_terrain",2), 
      
      # some weird fix i forgot why.      
      (val_mul,":combined_height",46),
      (val_div,":combined_height",100),
      (val_add,":height_to_terrain",":combined_height"),
      
      (store_sub,":height_difference",":height_to_terrain",":z_offset"),
      (val_mul,":height_difference",1000), # make it fixed point
      (store_div,":deg_value",":height_difference",":y_offset"),
      (store_atan,":deg_value",":deg_value"), # get the angle
      (val_div,":deg_value",1000),
      (val_mul,":deg_value",-1),
      
      # Tweaking for slope, (wheels are round so should "float" a bit when on angle so their not into ground)
      (try_begin),
        (lt,":deg_value",0),
        (val_mul,":deg_value",108), # 108 %
        (val_div,":deg_value",100),
      (else_try),
        (gt,":deg_value",0),
        (val_mul,":deg_value",92), # 92 %
        (val_div,":deg_value",100),
      (try_end),
      
      # move it up, rotate it, move it down (or a bit sideways that is...)
      # 50 cm is the bars height above the center of liberwood.
      (position_move_z,pos14,50),
      (position_rotate_y,pos14,":deg_value2"),
      (position_move_z,pos14,-50),
      
      # Do a slight Z change due to the bars otherwise sticking into the horse.
      # (try_begin),
        # (neq,":deg_value2",0),

        # (store_div,":deg_value2_div",":deg_value2",8),
        # (position_rotate_z,pos14,":deg_value2_div"),
        
        # (val_add,":z_rot",":deg_value2_div"),
      # (try_end),
      (scene_prop_get_slot,":previous_z_rot",":instance_id",scene_prop_slot_z_extra),
      (scene_prop_set_slot,":instance_id",scene_prop_slot_z_extra,":z_rot"),
      
      (position_rotate_x,pos14,":deg_value"),
      
      # And finally move the wood to this rotated position.
      (prop_instance_animate_to_position, ":instance_id", pos14, 28),
      
      # move from middle of horse to center where wheels should be.
      (position_move_y, pos14,":y_offset"),
      
      # overwrite the 12 we temporary used.
      (copy_position,pos12,pos14),
      
      # reset pos14 its X rotation for the weels (they store their own rotation and rotate with it.)
      (position_get_rotation_around_x,":parent_x_rot",pos14),
      (val_mul,":parent_x_rot",-1),
      (position_rotate_x,pos14,":parent_x_rot"),
      
      (scene_prop_get_slot,":x_rot",":wheels_instance",scene_prop_slot_x_extra),
      (val_add,":x_rot",":limber_wheel_speed"),
      (try_begin),
        (gt,":x_rot",360),
        (val_sub,":x_rot",360),
      (try_end),
      (scene_prop_set_slot,":wheels_instance",scene_prop_slot_x_extra,":x_rot"),
      (position_rotate_x,pos14,":x_rot"),
      
      (prop_instance_animate_to_position, ":wheels_instance", pos14, 28),
      
      
      # if we have a cannon and wheels, go on.
      (prop_instance_is_valid,":cannon_instance"),
      (prop_instance_is_valid,":cannon_wheels_instance"),
      
      (store_sub,":diffirence_z_old_new",":previous_z_rot",":z_rot"),
      
      (try_begin),
        (gt,":diffirence_z_old_new",300),
        (val_sub,":diffirence_z_old_new",360),
      (else_try),
        (lt,":diffirence_z_old_new",-300),
        (val_add,":diffirence_z_old_new",360),
      (try_end),
      
      # calculate percent speed
      (val_mul,":agent_speed",100),
      (val_div,":agent_speed",2907), # speed/max speed
      
      # calc difirence * percent speed
      (val_mul,":diffirence_z_old_new",":agent_speed"),
      (val_div,":diffirence_z_old_new",100),
      
      (scene_prop_get_slot,":previous_z_rot",":cannon_instance",scene_prop_slot_z_extra),
      (store_sub,":diffirence_z_object",":previous_z_rot",":z_rot"),
      
      (try_begin),
        (gt,":diffirence_z_object",300),
        (val_sub,":diffirence_z_object",360),
      (else_try),
        (lt,":diffirence_z_object",-300),
        (val_add,":diffirence_z_object",360),
      (try_end),
       
      (try_begin),
        (neq,":agent_speed",0),
        (val_mul, ":agent_speed", 40), 
        (val_div, ":agent_speed", 100), # value * 40 / 100 = - 40% of the speed
        (store_mul,":sub_dif",":diffirence_z_object",":agent_speed"),

        (try_begin),
          (is_between, ":sub_dif", -100, 101),
          (eq,":diffirence_z_old_new",0),
          (assign,":diffirence_z_object",0),
        (else_try),
          (val_div,":sub_dif",100),
          (val_sub,":diffirence_z_object",":sub_dif"),
        (try_end),
      (try_end),

      (val_add,":diffirence_z_object",":diffirence_z_old_new"),
       
      (try_begin),
        (gt,":diffirence_z_object",40),
        (assign,":diffirence_z_object",40),
      (else_try),
        (lt,":diffirence_z_object",-40),
        (assign,":diffirence_z_object",-40),
      (try_end),
      
      # move a bit up so the wedge is on the spike of the limber.
      (scene_prop_get_slot,":cannon_z_offset",":cannon_instance",scene_prop_slot_z_value),
      (position_move_z,pos12,":cannon_z_offset"),
      (store_add,":total_z_offset",":z_offset",6),
      
      # Reset pos12 rotations except Z, so we have a fresh pos12 to use.
      (store_mul,":deg_value2_min",":deg_value2",-1),
      (store_mul,":deg_value_min",":deg_value",-1),
      (position_rotate_x,pos12,":deg_value_min"),
      (position_rotate_y,pos12,":deg_value2_min"),
      
      # Rotate to the difirence calculated.
      (position_rotate_z,pos12,":diffirence_z_object"),
      (val_add,":diffirence_z_object",":z_rot"),
      (scene_prop_set_slot,":cannon_instance",scene_prop_slot_z_extra,":diffirence_z_object"),
      
      (copy_position,pos14,pos12),
      
      # move to wheels position.
      (scene_prop_get_slot,":y_offset",":cannon_wheels_instance",scene_prop_slot_y_value),
      (position_move_y, pos12,":y_offset"),
      
      # march to left wheel and get height there.
      (position_move_x,pos12,-72),
      (position_get_distance_to_ground_level, ":left_height_to_terrain", pos12),
      (val_div,":left_height_to_terrain",10), # due to fixed point at 1000
      
      # march to right wheel and get height there.
      (position_move_x,pos12,144),
      (position_get_distance_to_ground_level, ":right_height_to_terrain", pos12),
      (val_div,":right_height_to_terrain",10), # due to fixed point at 1000
      

      # calculate
      (store_sub,":height_difference",":left_height_to_terrain",":right_height_to_terrain"),
     
      (store_div,":combined_height",":height_difference",2),
      (try_begin),
        (gt,":combined_height",0),
        (val_mul,":combined_height",-1),
      (try_end),      

      (val_mul,":height_difference",1000), # make it fixed point
      (store_div,":deg_value2",":height_difference",120),  # 120 is distance between the two wheels.
      (store_atan,":deg_value2",":deg_value2"), # get the angle
      (val_div,":deg_value2",1000),
      (val_mul,":deg_value2",-1),

      
      # combine the two heights and get the angle between them combined and the horse position.
      (store_add,":height_to_terrain",":left_height_to_terrain",":right_height_to_terrain"),
      (val_div,":height_to_terrain",2), 
      
      # some weird fix i forgot why.
      (val_mul,":combined_height",44),
      (val_div,":combined_height",100),
      (val_add,":height_to_terrain",":combined_height"),
      
      (store_sub,":height_difference",":height_to_terrain",":total_z_offset"),
      (val_mul,":height_difference",1000), # make it fixed point
      (store_div,":deg_value",":height_difference",":y_offset"),
      (store_atan,":deg_value",":deg_value"), # get the angle
      (val_div,":deg_value",1000),
      (val_mul,":deg_value",-1),
      
      # Tweaking for slope, (wheels are round so should "float" a bit when on angle so their not into ground)
      (try_begin),
        (lt,":deg_value",0),
        (val_mul,":deg_value",108), # 108 %
        (val_div,":deg_value",100),
      (else_try),
        (gt,":deg_value",0),
        (val_mul,":deg_value",92), # 92 %
        (val_div,":deg_value",100),
      (try_end),
      
      (position_rotate_y,pos14,":deg_value2"),
      (position_rotate_x,pos14,":deg_value"),

      (prop_instance_animate_to_position, ":cannon_instance", pos14, 28),

      # Wheels.
      # move from middle of spike to the wheel position on limber.
      (position_move_y, pos14,":y_offset"),
      
      # reset pos14 its X rotation for the weels (they store their own rotation and rotate with it.)
      (position_get_rotation_around_x,":parent_x_rot",pos14),
      (val_mul,":parent_x_rot",-1),
      (position_rotate_x,pos14,":parent_x_rot"),

      (scene_prop_get_slot,":x_rot",":cannon_wheels_instance",scene_prop_slot_x_extra),
      (val_add,":x_rot",":cannon_wheel_speed"),
      (try_begin),
        (gt,":x_rot",360),
        (val_sub,":x_rot",360),
      (try_end),
      (scene_prop_set_slot,":cannon_wheels_instance",scene_prop_slot_x_extra,":x_rot"),
      (position_rotate_x,pos14,":x_rot"),
      
      (prop_instance_animate_to_position, ":cannon_wheels_instance", pos14, 28),
    (try_end),
])

multiplayer_server_on_item_dropped = (
  ti_on_item_dropped, 0, 0, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode)],
  [
    (store_trigger_param_2, ":item_id"),
    
    (try_begin),
      (gt,":item_id",-1),
      
      (store_trigger_param_1, ":agent_no"),
      (agent_is_active,":agent_no"),
      
      (try_begin),
        (item_slot_eq,":item_id",slot_item_multiplayer_item_class, multi_item_class_type_flag), #always use item classes!!!
        (store_trigger_param_3, ":dropped_prop"),
        (prop_instance_get_position, pos25, ":dropped_prop"),
        
        (agent_get_horse, ":agent_horse", ":agent_no"),
        (try_begin),
          (gt, ":agent_horse", -1), #PATCH1115 fix 5/4
          (position_move_x,pos25,50),
        (else_try),
          (position_move_y,pos25,36),
        (try_end),
        (position_rotate_x, pos25, 90),
        (prop_instance_set_position, ":dropped_prop", pos25),
        (scene_prop_set_prune_time, ":dropped_prop", 300), # 5 minutes
      (else_try),
        (eq, ":item_id", "itm_cannon_lighter"),
        (agent_slot_ge,":agent_no",slot_agent_current_control_prop,0), # we are controlling a prop.
        (try_begin),
          (agent_get_slot,":prop_instance",":agent_no",slot_agent_current_control_prop),
          (prop_instance_is_valid,":prop_instance"),
          (prop_instance_get_scene_prop_kind,":prop_kind",":prop_instance"),
          (try_begin),
            (is_between,":prop_kind",mm_cannon_wood_types_begin,mm_cannon_wood_types_end),
            (call_script,"script_stop_agent_controlling_cannon",":prop_instance",":agent_no"),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
  ])

multiplayer_client_control_cannon = (
  0, 0, 1, [ # Execute conditions.
             (neg|multiplayer_is_dedicated_server),
             (eq, "$g_currently_controlling_object", 1),
             (this_or_next|game_key_clicked, gk_attack),
             (game_key_clicked, gk_defend),
             (is_between,"$g_cur_control_prop_kind", mm_cannon_wood_types_begin,mm_cannon_wood_types_end),
           ],
  [
    (assign,":command",-1),
    (try_begin),
      (game_key_clicked, gk_defend),
      (assign,":command",cannon_command_stop_aim),
    (else_try),
      (game_key_clicked, gk_attack),
      (assign,":command",cannon_command_fire),
    (try_end),
  
    (gt,":command",-1),
    (try_begin),
      (game_in_multiplayer_mode),
      (multiplayer_send_2_int_to_server,multiplayer_event_send_control_command,command_type_cannon,":command"),
    (else_try),
      (call_script,"script_client_get_my_agent"),
      (call_script,"script_handle_agent_control_command",reg0,command_type_cannon,":command"),
    (try_end),
  ])

multiplayer_server_aim_cannon  = (
  0.5, 0, 0, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode)],
  [  
    (set_fixed_point_multiplier, 100),
    (try_for_range,":cannon_type", mm_cannon_wood_types_begin, mm_cannon_wood_types_end),
      (try_for_prop_instances, ":instance_id", ":cannon_type", somt_temporary_object),
        (scene_prop_get_slot,":cur_control_agent",":instance_id",scene_prop_slot_controller_agent),
        
        (agent_is_active, ":cur_control_agent"),
        
        (prop_instance_get_position, pos10, ":instance_id"),
        
        (assign,":agent_is_ok",0),
        (try_begin),
          (agent_is_alive, ":cur_control_agent"),
        
          (agent_get_horse,":horse",":cur_control_agent"),
          (eq,":horse",-1),          
          
          (agent_get_position, pos11, ":cur_control_agent"),
          
          (get_distance_between_positions,":dist",pos10,pos11),
          (le, ":dist", 600),
          
          (assign,":agent_is_ok",1),
        (else_try),
          (call_script,"script_stop_agent_controlling_cannon",":instance_id",":cur_control_agent"),
        (try_end),
        
        (eq,":agent_is_ok",1),
        
        (store_mission_timer_a,":cur_time"),
        (scene_prop_set_slot,":instance_id",scene_prop_slot_spawned_at,":cur_time"),
        
        # (try_begin),
          # (call_script, "script_prop_instance_find_first_child_of_type", ":instance_id", "spr_mm_cannon_aim_platform"),
          # (prop_instance_is_valid,reg0),
          # (neg|scene_prop_has_agent_on_it, reg0, ":cur_control_agent"),
          ####(call_script,"script_stop_agent_controlling_cannon",":instance_id",":cur_control_agent"),
          # (prop_instance_get_position,pos9,reg0),
          # (agent_set_position,":cur_control_agent",pos9),
        # (try_end),
        
        # Handle firing first, else handle aiming.
        (agent_get_slot,":cur_command",":cur_control_agent",slot_agent_current_command),
        (try_begin),
          (eq,":cur_command",cannon_command_fire),
          
          (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
          (try_begin),
            (eq,":cur_time",1), # already been once then fire it! :)
            
            (call_script,"script_fire_cannon",":instance_id",":cur_control_agent"),
            
            (agent_set_slot, ":cur_control_agent", slot_agent_current_command, 0),
            (assign,":cur_time",0),
          (else_try),
            (val_add,":cur_time",1),
          (try_end),
          
          (scene_prop_set_slot,":instance_id", scene_prop_slot_time, ":cur_time"),
        (else_try),
          
          (copy_position,pos19,pos10),
          (agent_get_look_position, pos11, ":cur_control_agent"),
          (copy_position,pos23,pos11),
          (position_rotate_z, pos11, 90),
          
          (try_begin),
            (eq,":cannon_type","spr_mm_cannon_mortar_wood"),
            
            (call_script,"script_search_for_first_ground_from_direction_to_angle"),
            (assign,":agent_y_rot",reg0),
          (else_try),
            (position_get_rotation_around_y,":agent_y_rot",pos11),
          (try_end),
          
          #(get_distance_between_positions,":dist",pos10,pos11),
          (try_begin),
            # (gt, ":dist", 500),
            
            # (call_script,"script_stop_agent_controlling_cannon",":instance_id",":cur_control_agent"),
          # (else_try),
            (call_script,"script_cannon_instance_get_barrel",":instance_id"),
            (assign,":barrel_instance",reg0),

           # (position_rotate_z, pos11, 90), # Rotate because the agent front is Y axis but for cannons it is the X axis.. lol..
           # 
            (position_get_rotation_around_z,":agent_z_rot",pos11),
          #   (position_get_rotation_around_y,":agent_y_rot",pos11),
            (position_get_rotation_around_z,":prop_z_rot",pos10),
            
                        
            (assign,":prop_y_rot",0),
            (assign,":can_y_rot",0),
            (try_begin),
              (prop_instance_is_valid,":barrel_instance"), # patch1115 18/23
              
              (prop_instance_get_position,pos12,":barrel_instance"),
              (position_get_rotation_around_y,":prop_y_rot",pos12),
              
              (position_get_rotation_around_y,":can_y_rot",pos10),
            (else_try),
              (position_get_rotation_around_y,":prop_y_rot",pos10),
            (try_end),
            
            (store_sub,":diffirence_z",":agent_z_rot",":prop_z_rot"),
            (store_sub,":diffirence_y",":agent_y_rot",":prop_y_rot"),
            
            (try_begin),
              (gt,":diffirence_z",180),
              (val_sub,":diffirence_z",360),
            (else_try),
              (lt,":diffirence_z",-180),
              (val_add,":diffirence_z",360),
            (try_end),
            
            (try_begin),
              (gt,":diffirence_y",180),
              (val_sub,":diffirence_y",360),
            (else_try),
              (lt,":diffirence_y",-180),
              (val_add,":diffirence_y",360),
            (try_end),
            
            (try_begin),
              (gt,":diffirence_z",4),
              (assign,":diffirence_z",4),
            (else_try),
              (lt,":diffirence_z",-4),
              (assign,":diffirence_z",-4),
            (try_end),
            
            (try_begin),
              (gt,":diffirence_y",2),
              (assign,":diffirence_y",2),
            (else_try),
              (lt,":diffirence_y",-2),
              (assign,":diffirence_y",-2),
            (try_end),
            
            # Limit cannon Z rot if applicable
            (scene_prop_get_slot,":z_rotation_limit",":instance_id",scene_prop_slot_z_rotation_limit),
            (try_begin),
              (gt, ":z_rotation_limit", 0),

              (scene_prop_get_slot,":prop_z_rot_offset",":instance_id",scene_prop_slot_z_rot),
              
              (store_add,":new_prop_z_rot_offset",":prop_z_rot_offset",":diffirence_z"),# Add the change towards the current rotation.
              (store_mul,":z_rotation_limit_min",":z_rotation_limit",-1),
              
              (try_begin),
                (gt,":new_prop_z_rot_offset",":z_rotation_limit"),
                (assign,":prop_z_rot_offset",":z_rotation_limit"),
                (store_sub,":res_diffirence_z",":new_prop_z_rot_offset",":prop_z_rot_offset"),
                (val_sub,":diffirence_z",":res_diffirence_z"),
              (else_try),
                (lt,":new_prop_z_rot_offset",":z_rotation_limit_min"),
                (assign,":prop_z_rot_offset",":z_rotation_limit_min"),
                (store_sub,":res_diffirence_z",":new_prop_z_rot_offset",":prop_z_rot_offset"),
                (val_sub,":diffirence_z",":res_diffirence_z"),
              (else_try),
                (assign,":prop_z_rot_offset",":new_prop_z_rot_offset"),
              (try_end),
              
              (scene_prop_set_slot,":instance_id",scene_prop_slot_z_rot,":prop_z_rot_offset"), 
            (try_end),

            (position_rotate_z,pos10,":diffirence_z"),
            (copy_position,pos57,pos10),

            (try_begin),
              (prop_instance_is_valid,":barrel_instance"), #patch1115 18/24
              
              (call_script, "script_prop_instance_animate_to_position_with_childs", ":instance_id", 53,":barrel_instance",0),
   
              (scene_prop_get_slot,":xvalue",":barrel_instance",scene_prop_slot_x_value),
              (scene_prop_get_slot,":yvalue",":barrel_instance",scene_prop_slot_y_value),
              (scene_prop_get_slot,":zvalue",":barrel_instance",scene_prop_slot_z_value),
              (position_move_x, pos57,":xvalue"),
              (position_move_y, pos57,":yvalue"),
              (position_move_z, pos57,":zvalue"),
                           
              (val_sub,":prop_y_rot",":can_y_rot"), 
              (try_begin),
                (lt,":prop_y_rot",0),
                (val_add,":prop_y_rot",360),
              (try_end),
              (val_add,":prop_y_rot",":diffirence_y"),# Add the change towards the current rotation.

              (try_begin),
                (neq,":cannon_type","spr_mm_cannon_mortar_wood"),
                (try_begin), # limit barrel rotations
                  (is_between,":prop_y_rot",180,340), # upper limit
                  (assign,":prop_y_rot",340),
                (else_try),
                  (is_between,":prop_y_rot",19,180), # down limit
                  (assign,":prop_y_rot",18),
                (try_end),
              (try_end),
              
              (position_rotate_y,pos57,":prop_y_rot"),
              
              (scene_prop_set_slot,":barrel_instance",scene_prop_slot_y_rot,":prop_y_rot"), # store rotation to keep barrel in same direction :3
              
              (call_script, "script_prop_instance_animate_to_position_with_childs", ":barrel_instance", 53,0,0),
            (else_try),
              (position_rotate_y,pos57,":diffirence_y"),
              (call_script, "script_prop_instance_animate_to_position_with_childs", ":instance_id", 53,0,0),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
  ])

multiplayer_server_cannonball_flight = (
  0.125, 0, 0, [ (this_or_next|multiplayer_is_server),
                (neg|game_in_multiplayer_mode),
              ],
  [
    (set_fixed_point_multiplier, 100),
    
    (try_for_range,":cannonball_type", "spr_mm_cannonball_code_only_6pd", "spr_mm_cannon_12pdr_wood"),
      (try_for_prop_instances, ":ball_instance_id", ":cannonball_type", somt_temporary_object),
        (scene_prop_slot_eq, ":ball_instance_id", scene_prop_slot_in_use, 1), # ball is in use.

        (scene_prop_get_slot,":cur_x_vel",":ball_instance_id", scene_prop_slot_x_value),
        (scene_prop_get_slot,":cur_y_vel",":ball_instance_id", scene_prop_slot_y_value),
        (scene_prop_get_slot,":cur_z_vel",":ball_instance_id", scene_prop_slot_z_value),
        (scene_prop_get_slot,":time",":ball_instance_id", scene_prop_slot_time),
        (scene_prop_get_slot,":ammo_type",":ball_instance_id", scene_prop_slot_ammo_type),
        (scene_prop_get_slot,":user_agent",":ball_instance_id", scene_prop_slot_user_agent),
        
        (prop_instance_get_position, pos33, ":ball_instance_id"),
        (position_get_z, ":ball_z",pos33),
        
        # (assign,reg22,":cur_x_vel"),
        # (assign,reg23,":cur_y_vel"),
        # (assign,reg24,":cur_z_vel"),
        # (display_message,"@cur_x_vel: {reg22}  cur_y_vel: {reg23}  cur_z_vel: {reg24}"),
        
        (assign,":move",1),
        (assign,":check_walls",1),
        (assign,":check_agents",1),
        (copy_position,pos35,pos33),
        (copy_position,pos26,pos35),


        (try_begin),
          (gt,":time",0),
          
          (copy_position,pos34,pos33),
          (position_set_z_to_ground_level,pos34),
          (position_get_z,":ground_z",pos34),
          (val_add, ":ground_z", 10), 
          
          (this_or_next|lt,":ball_z", "$g_scene_water_level"),
          (lt,":ball_z", ":ground_z"),
          
          # Reset all rotations on pos34 except z
          (position_get_rotation_around_z, ":z_rot", pos34),
          (position_copy_origin,pos47,pos34),
          (init_position,pos34),
          (position_copy_origin,pos34,pos47),
          (position_rotate_z,pos34,":z_rot"),
          
          (try_begin), # Hitting the water?
            (lt,":ball_z", "$g_scene_water_level"), # we are underwater
            
            (gt,":ball_z", ":ground_z"), # we are undrerwater and not underground
            
            (scene_prop_slot_eq, ":ball_instance_id", scene_prop_slot_displayed_particle, 0), # shown the water effect already?
            (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_displayed_particle, 1),
            (copy_position,pos60,pos34), # pos60 is particle pos
            (position_set_z,pos60,"$g_scene_water_level"), # 0 = water level.
            
            (call_script,"script_multiplayer_server_play_hit_effect",cannon_hit_effect_event_type_water_ball, 0),
          (try_end),
         
          (lt,":ball_z", ":ground_z"),
          
          (assign,":clean_it_up",0),
          (try_begin),
            (this_or_next|eq,":ammo_type",cannon_ammo_type_shell),
            (this_or_next|eq,":ammo_type",cannon_ammo_type_bomb),
            (eq,":ammo_type",cannon_ammo_type_rocket),
            
            (copy_position,pos47,pos34),
            (call_script,"script_cannon_explosion_on_position",1,":ammo_type",":user_agent"),
            
            (assign,":clean_it_up",1),
          (else_try),
            (eq,":ammo_type",cannon_ammo_type_round),
            
            (call_script, "script_cannon_ball_hit_ground", ":ball_instance_id", ":cur_x_vel",":cur_z_vel"),
            (assign, ":cur_x_vel", reg0),
            (assign, ":cur_z_vel", reg1),
            (assign, ":clean_it_up", reg2),
          (try_end),
          
          (try_begin),
            (eq,":clean_it_up",1),
            
            (call_script, "script_clean_up_prop_instance", ":ball_instance_id"),
            
            (assign,":time",-1),
            (assign,":move",0),
            (assign,":check_walls",0),
            (assign,":check_agents",0),
          (try_end),
          
        (else_try),
          (assign, ":modulus", ":time"),
          
          (try_begin),
            (eq,":ammo_type",cannon_ammo_type_rocket),
            
            (val_mod, ":modulus", 2), # move and check once in 2 times (0.25 seconds)
          (else_try),
            (val_mod, ":modulus", 4), # move and check once in 4 times (0.5 seconds)
          (try_end),
          
          (gt, ":modulus", 0), # If not right mod result dont move. (1 == second value it will return so always move first pass :) )
          (assign,":move",0), # Dont move/check stuff just for ground detection...
        (try_end),

        # Copy ball pos when needed
        (store_mul,":z_offset_calc",":cur_z_vel",10000),
        (try_begin),
          (neq,":cur_x_vel",0),
          (val_div,":z_offset_calc",":cur_x_vel"),       
        (else_try),
          (val_div,":z_offset_calc",10000),      
        (try_end),
        
        (store_div,":x_movement",":cur_x_vel",2),
        (store_div,":y_movement",":cur_y_vel",2),
        (store_div,":z_movement",":cur_z_vel",2),
        
        (position_move_x,pos35,":x_movement"),
        (position_move_y,pos35,":y_movement"),
        (position_move_z,pos35,":z_movement"),
        
          
        (try_begin),
          (eq,":move",1),
          (set_fixed_point_multiplier, 100),
          
          (position_get_x,":ball_x",pos33),
          (position_get_y,":ball_y",pos33),
          
          (try_begin),
            (this_or_next|lt,":ball_x","$g_scene_min_x"),
            (this_or_next|gt,":ball_x","$g_scene_max_x"),
            (this_or_next|lt,":ball_y","$g_scene_min_y"),
            (gt,":ball_y","$g_scene_max_y"),
            
            (call_script, "script_clean_up_prop_instance", ":ball_instance_id"),
            (assign,":time",-1),
            (assign,":move",0),
            (assign,":check_walls",0),
            (assign,":check_agents",0),
          (else_try),
            # Animate first
            
            # (assign,reg29,":cur_x_vel"),
            # (assign,reg30,":cur_z_vel"),
            # (assign,reg31,":cur_y_vel"),
            # (display_message,"@at move;  cur_x_vel: {reg29}  cur_z_vel: {reg30}  cur_y_vel: {reg31}"),
            
            (position_move_x,pos33,":cur_x_vel"),
            (position_move_y,pos33,":cur_y_vel"),
            (position_move_z,pos33,":cur_z_vel"),
            
            (try_begin),
              (eq,":ammo_type",cannon_ammo_type_rocket),
              (try_begin),
                (ge,":time", 4),
                (store_random_in_range,":rand_z",-4,4),
                (position_rotate_z,pos33,":rand_z"),
                (store_random_in_range,":rand_y",-4,4),
                (position_rotate_y,pos33,":rand_y"),
              (try_end),
              (prop_instance_animate_to_position, ":ball_instance_id", pos33, 28),
            (else_try),
              (prop_instance_animate_to_position, ":ball_instance_id", pos33, 53),
            (try_end),
            
            (try_begin),
              (eq,":ammo_type",cannon_ammo_type_rocket),
              (try_begin),
                (le,":time", 28),
                (val_add, ":cur_x_vel", 150),
              (else_try),
                (val_mul, ":cur_x_vel", 99), 
                (val_div, ":cur_x_vel", 100), # value * 99 / 100 = - 99% of speed due to friction per 0.5 sec so 2% friction per second
              (try_end),
              (try_begin),
                (gt,":time",4),
                (val_sub,":cur_z_vel", 59), 
              (try_end),
            (else_try),
              # Then apply gravity and friction
              ## -196 cm per second so # 0.981 per half
              (val_sub,":cur_z_vel", 118), 
              (val_max,":cur_z_vel",-1700),
              (val_mul, ":cur_x_vel", 99), 
              (val_div, ":cur_x_vel", 100), # value * 99 / 100 = - 99% of speed due to friction per 0.5 sec so 2% friction per second
            (try_end),
            
            (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_x_value, ":cur_x_vel"),
            (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_y_value, ":cur_y_vel"),
            (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_z_value, ":cur_z_vel"),
          (try_end),
        (try_end),
        
        (val_add,":time",1),
        (scene_prop_set_slot, ":ball_instance_id", scene_prop_slot_time, ":time"),
        
        (eq,":move",1), # Only check stuff when just moved.
        
        
        (assign,":hitted_wall_x_dist",":cur_x_vel"),
                
        (try_begin), # destroy those bloody walls bitch..
          #(gt,":time",0),
          (eq,":check_walls",1), # not the first time so dont destroy your defence walls..
          (assign,":min_dist",9999999999),
          (assign,":hitted_wall_instance",-1),
          #(assign,":hitted_length_div2",0),
          (assign,":hitted_wall_kind",-1),
          (assign,":hitted_wall_power",3),
          (assign,":hitted_distance_ball_wall",0),
          (store_mul,":cur_x_vel_min",":cur_x_vel",-1),
          (try_for_range,":wall_type",mm_destructible_props_begin,mm_destructible_props_end),
            
            (assign,":wall_power", 3),
            #(try_begin),
             # (this_or_next|is_between, ":wall_type", "spr_mm_stakes","spr_mm_destructible_pioneer_builds_end"), #patch1115 fix 35/1 removed
             # (eq,":wall_type","spr_mm_dummy"),
            #  (assign,":wall_power",1),
           # (try_end),
            
            (try_for_prop_instances, ":wall_id", ":wall_type"),
              (prop_instance_get_position, pos40, ":wall_id"),
              
              (scene_prop_get_slot,":max_length",":wall_id", scene_prop_slot_destruct_max_length),
              (store_add,":cur_x_vel_awall", ":x_movement", ":max_length"),
              
              # only get shit that is close to this ball middle position.
              (get_distance_between_positions, ":distance_ball_wall", pos35, pos40),
              (le, ":distance_ball_wall", ":cur_x_vel_awall"),
              
              # We are close enough, optimization done, lets get the real stuff about this prop.
              (call_script,"script_get_prop_center",":wall_id"),
              (eq,reg1,1), # is ok :)
              (scene_prop_get_slot,":cur_wall_height",":wall_id",scene_prop_slot_destruct_wall_height),
              (scene_prop_get_slot,":cur_wall_width",":wall_id",scene_prop_slot_destruct_wall_width),
              (scene_prop_get_slot,":cur_wall_length",":wall_id",scene_prop_slot_destruct_wall_length),

              (assign,":cur_wall_width_usa",":cur_wall_width"),
              
              (copy_position,pos40,pos42), 
              
              (set_fixed_point_multiplier, 1000),
              # resize for the angle of wall
              (get_angle_between_positions, ":rotation", pos33, pos40),
              # get length
              (store_cos, ":cos_of_rotation", ":rotation"),
              (try_begin), # make it positive if needed
                (lt, ":cos_of_rotation", 0),
                (val_mul, ":cos_of_rotation", -1),
              (try_end),
              (val_mul,":cur_wall_length",":cos_of_rotation"),
              (val_div, ":cur_wall_length", 1000),
              # get width
              (store_sub, ":cos_of_rotation", 1000, ":cos_of_rotation"), # get remainder
              (val_mul,":cur_wall_width",":cos_of_rotation"),
              (val_div, ":cur_wall_width", 1000),
              
              # Put length + width together
              (val_add, ":cur_wall_length", ":cur_wall_width"),
              
              
              # prepare vars for compare against ball pos
              (set_fixed_point_multiplier, 100),
              (store_div, ":length_div2", ":cur_wall_length", 2),
              (store_div, ":height_div2", ":cur_wall_height", 2),
              (store_mul, ":length_div2_min", ":length_div2", -1),
              (store_mul, ":height_div2_min", ":height_div2", -1),              
              
              (position_transform_position_to_local,pos45,pos26,pos40),
              (position_get_x,":x_value",pos45),
              (position_get_y,":y_value",pos45),
              (position_get_z,":z_value",pos45),
              
              (is_between,":y_value",":length_div2_min",":length_div2"), # Length 
              (is_between,":x_value",-50,":cur_x_vel"), #  50 cm before and speed after the path of the ball. (due to lag..)
              
              (store_mul,":z_offset",":z_offset_calc",":x_value"),
              (val_div,":z_offset",10000), # zoffset is clear.
              (val_add,":height_div2",":z_offset"),
              (val_add,":height_div2_min",":z_offset"),
              
              (is_between,":z_value",":height_div2_min",":height_div2"), # height
              
              # is hit.
              # then, check if its the closest one, using agent position due to you want to hit the first thing comming from x direction.
              (try_begin),
                (agent_is_active,":user_agent"),
                (agent_get_position,pos56,":user_agent"),
                (get_distance_between_positions, ":distance_ball_wall", pos56, pos40),
              (try_end),
              (this_or_next|eq,":hitted_wall_instance",-1),
              (lt,":distance_ball_wall",":min_dist"),
              (assign,":min_dist",":distance_ball_wall"),
              (assign,":hitted_wall_instance",":wall_id"),
              (assign,":hitted_wall_x_dist",":x_value"),
              #(assign,":hitted_length_div2",":length_div2"),
              (store_div,":hitted_width_div2", ":cur_wall_width_usa", 2),
              (assign,":hitted_wall_kind",":wall_type"),
              (assign,":hitted_wall_power",":wall_power"),
              
              (copy_position,pos45,pos33),
              (position_move_x,pos45,":cur_x_vel_min"),
              (get_distance_between_positions, ":hitted_distance_ball_wall", pos45, pos40),
              (copy_position,pos47,pos40),
            (try_end),
          (try_end),
          

          (try_begin), # we have something hit.
           # (gt,":hitted_wall_instance", -1),
            (prop_instance_is_valid,":hitted_wall_instance"), #patch1115 18/25
            
            (copy_position,pos45,pos33),
            (position_move_x,pos45,":cur_x_vel_min"),
            
            
            # copy ball to a temp pos. (for its rotations.
            
            #            85%
            # (val_mul,":hitted_length_div2",85),
            # (val_div,":hitted_length_div2",100),
            
            (val_sub,":hitted_distance_ball_wall",":hitted_width_div2"),
            (position_move_x,pos45,":hitted_distance_ball_wall"),
            
            (position_get_z,":wall_middle_z",pos47),
            
            (store_random_in_range,":random_z_add",-100,101),
            (val_add,":wall_middle_z",":random_z_add"),
            
            (position_set_z,pos45,":wall_middle_z"),
            #(position_rotate_y,pos45,90),
            
            
            # place wall xyz into the rotation of ball.
            #(position_copy_origin,pos45,pos47),
            # flip the position
            # (position_rotate_x,pos45,180),
            # (position_move_x,pos45,":hitted_length_div2"),
            (copy_position,pos47,pos45),
            
            (try_begin),
              (this_or_next|eq,":ammo_type",cannon_ammo_type_shell),
              (this_or_next|eq,":ammo_type",cannon_ammo_type_bomb),
              (eq,":ammo_type",cannon_ammo_type_rocket),
              
              (call_script,"script_cannon_explosion_on_position",0,":ammo_type",":user_agent"),
              
              (call_script, "script_clean_up_prop_instance", ":ball_instance_id"), # clean up ball
              (assign,":check_agents",0),
            (else_try),
              (eq,":ammo_type",cannon_ammo_type_round),
              
              (try_begin),
                (is_between, ":hitted_wall_kind", "spr_fortnew", "spr_mm_new_wall_1_1"), #patch1115 fix 38/1
                (call_script,"script_deliver_damage_to_prop",":hitted_wall_instance",201, 1, ":user_agent"),
              (else_try),
                (call_script,"script_deliver_damage_to_prop",":hitted_wall_instance",201, 0, ":user_agent"),
              (try_end),
              
              (scene_prop_get_slot,":ball_times_hit",":ball_instance_id", scene_prop_slot_times_hit),
              (val_add, ":ball_times_hit", ":hitted_wall_power"),
              
              (try_begin),
                (ge, ":ball_times_hit", 3),
                #Clean up ball
                (call_script, "script_clean_up_prop_instance", ":ball_instance_id"),
               # (assign,":check_agents",0),
              (else_try),
                # hit something, loosing speed.
                (val_mul, ":cur_x_vel", 90), 
                (val_div, ":cur_x_vel", 100), # value * 90 / 100 = - 90% speed left
                (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_x_value, ":cur_x_vel"),
                (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_times_hit, ":ball_times_hit"),
              (try_end),
            (try_end),
          (try_end),
        (try_end), 
        #(gt,":time",1),
        (eq, ":check_agents", 1),
	    	(neq,":ammo_type",cannon_ammo_type_bomb),
        (set_fixed_point_multiplier, 100),
        
        
        # get the Z offset by knowing the Z mov per x mov. (fixed point * 10000)
        
        (assign,":myhorseid",-1),
        (try_begin),
          (agent_is_active, ":user_agent"),
          (agent_get_horse,":myhorseid",":user_agent"),
        (try_end),
        
        

        (store_add,":check_range",":x_movement",120),
        

        
        (try_for_agents, ":cur_agent",pos35,":check_range"),
          (eq, ":check_agents", 1),
          (agent_is_active, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_get_position, pos40, ":cur_agent"),
          
          (assign,":z_mov",90),
          (assign,":z_size",90),
          (assign,":y_width",70),
          (assign,":whores",-1),
          (try_begin),
            (agent_is_human,":cur_agent"),
            (try_begin),
              (agent_get_horse,":whores",":cur_agent"),
              (gt,":whores",-1),
              (assign,":z_mov",130),
              (assign,":z_size",80),
            (else_try),
              (agent_get_animation,":cur_anim",":cur_agent",0),
              (eq,":cur_anim","anim_stand_to_crouch"),
              (assign,":z_mov",50),
              (assign,":z_size",50),
            (try_end),
          (else_try), # horse.
          
            (assign,":y_width",150),
            (assign,":cur_wall_width",70),
            
            # resize for the angle of horse
            (set_fixed_point_multiplier, 1000),
            (get_angle_between_positions, ":rotation", pos33, pos40),
            (store_cos, ":cos_of_rotation", ":rotation"),
            (try_begin), # make it positive if needed
              (lt, ":cos_of_rotation", 0),
              (val_mul, ":cos_of_rotation", -1),
            (try_end),
            (val_mul,":y_width",":cos_of_rotation"),
            (val_div, ":y_width", 1000),
            
            (store_sub, ":sin_of_rotation", 1000, ":cos_of_rotation"), # get remainder
            (val_mul,":cur_wall_width",":sin_of_rotation"),
            (val_div, ":cur_wall_width", 1000),

            # Put length + width together
            (val_add, ":y_width", ":cur_wall_width"),
            (set_fixed_point_multiplier, 100),
            
            (assign,":z_mov",110),
            (assign,":z_size",110),
          (try_end),
          
          (position_move_z,pos40,":z_mov"),
          
          (position_transform_position_to_local,pos45,pos26,pos40),
          (position_get_x,":x_value",pos45),
          (position_get_y,":y_value",pos45),
          (position_get_z,":z_value",pos45),
          
          (assign,":x_min",-50),
          (try_begin),
            (le,":time",1),
            (this_or_next|eq,":cur_agent",":user_agent"),
            (eq,":myhorseid",":user_agent"),
            (assign,":x_min",":hitted_wall_x_dist"),
          (try_end),
          
          (is_between,":x_value",":x_min",":hitted_wall_x_dist"), # 0.5 meters after + speed before the path of the ball.
          
          (store_add,":y_test",":y_width",1),
          (store_mul,":min_y_test",":y_test",-1),
          
          (is_between,":y_value",":min_y_test",":y_test"), # width 50 cm each side so a meter wide we hit him
          
         
          
          (store_add,":z_test",":z_size",15),
          (store_mul,":min_z_test",":z_test",-1),
          (val_add,":z_test",20),
          (store_mul,":z_offset",":z_offset_calc",":x_value"),
          (val_div,":z_offset",10000), # zoffset is clear.
          (val_add,":z_test",":z_offset"),
          (val_add,":min_z_test",":z_offset"),
          
          
          # (assign,reg21,":cur_agent"),
           # (assign,reg22,":x_value"),
           # (assign,reg24,":z_value"),
           # (assign,reg25,":cur_x_vel"),
           # (assign,reg27,":cur_z_vel"),
           # (assign,reg28,":z_offset"),
           
           # (display_message,"@cur_agent:{reg21}  x_value: {reg22}  z_value: {reg24}  ball_x_vel: {reg25}  ball_z_vel: {reg27}  z_offset: {reg28}"),
          
          
          (is_between,":z_value",":min_z_test",":z_test"),#,-110,121), # height 2 meter man + 20 for correction
          
          
          (try_begin),
            (this_or_next|eq,":ammo_type",cannon_ammo_type_shell),
            (eq,":ammo_type",cannon_ammo_type_rocket),
            (copy_position,pos47,pos40),
            
            (call_script,"script_cannon_explosion_on_position",0,":ammo_type",":user_agent"),
            
            (call_script, "script_clean_up_prop_instance", ":ball_instance_id"), # clean up ball
            (assign, ":check_agents", 0),
          (else_try),
            (eq,":ammo_type",cannon_ammo_type_round),
          
            (assign, ":killer_agent", 0),
            (try_begin),
              (agent_is_active,":user_agent"),
              (assign, ":killer_agent", ":user_agent"),
            (else_try),
              (assign, ":killer_agent", ":cur_agent"),
            (try_end),
            #(agent_set_hit_points, ":cur_agent", 0, 1),
            #(agent_deliver_damage_to_agent, ":killer_agent", ":cur_agent", 1),
            (agent_deliver_damage_to_agent_advanced, ":unused", ":killer_agent", ":cur_agent", 200,"itm_cannon_ball_dummy"),
            (particle_system_burst,"psys_cannon_blood",pos40,100),
            (particle_system_burst,"psys_cannon_blood_2",pos40,100),
                                 
            # Play hitsound
            (copy_position,pos56,pos40),
            (call_script,"script_multiplayer_server_play_sound_at_position","snd_cannon_hit"),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
  ])

multiplayer_server_explosives  = (
  1, 0, 0, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode),],
  [
    (try_for_range,":explosive_type", mm_explosive_props_begin, mm_explosive_props_end),
      (try_for_prop_instances, ":instance_id", ":explosive_type"),
        
        (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
        (gt,":cur_time",0),
        (val_sub,":cur_time",1),
        
        (prop_instance_get_position, pos47, ":instance_id"), 
        (try_begin),
          (le,":cur_time",0),
          
          (scene_prop_get_slot,":agent_id",":instance_id",scene_prop_slot_user_agent),
          
          (call_script, "script_clean_up_prop_instance", ":instance_id"),
          
          (call_script,"script_explosion_at_position",":agent_id",270,370), # Input: shooter_agent_no, max_damage points, range in cm
        (else_try),
          (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
          (set_fixed_point_multiplier,100),
          (position_move_z,pos47,80),
          (particle_system_burst, "psys_explosives_fuse_smoke", pos47, 60),
        (try_end),
      (try_end),
    (try_end),
])

multiplayer_play_sounds_and_particles  = (
  1, 0, 0, [(neg|multiplayer_is_dedicated_server)],
  [
    (try_for_prop_instances, ":instance_id", "spr_mm_watersplash", somt_object), #Name of prop
      (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
      (val_sub,":cur_time",1),
      (try_begin),
        (le,":cur_time",0),
        (prop_instance_get_position, pos47, ":instance_id"),
        (particle_system_burst_no_sync, "psys_game_water_splash_2", pos47, 100), #particle name
        (store_random_in_range,":cur_time",2,3), #Seconds until next particle
      (try_end),
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    (try_end),
    
    (try_for_prop_instances, ":instance_id", "spr_mm_ambient_insects", somt_object),  #Name of prop
      (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
      (val_sub,":cur_time",1),
      (try_begin),
        (le,":cur_time",0),
        (prop_instance_get_position, pos47, ":instance_id"),
        (particle_system_burst_no_sync, "psys_mm_bug_fly_1", pos47, 100), #particle name
        (store_random_in_range,":cur_time",8,14), #Seconds until next particle
      (try_end),
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    (try_end),
    
    (try_for_prop_instances, ":instance_id", "spr_mm_ambient_insects1", somt_object),  #Name of prop
      (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
      (val_sub,":cur_time",1),
      (try_begin),
        (le,":cur_time",0),
        (prop_instance_get_position, pos47, ":instance_id"),
        (particle_system_burst_no_sync, "psys_mm_bug_fly_2", pos47, 100), #particle name
        (store_random_in_range,":cur_time",8,14), #Seconds until next particle
      (try_end),
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    (try_end),
    
    (try_for_prop_instances, ":instance_id", "spr_mm_ambient_insects2", somt_object),  #Name of prop
      (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
      (val_sub,":cur_time",1),
      (try_begin),
        (le,":cur_time",0),
        (prop_instance_get_position, pos47, ":instance_id"),
        (particle_system_burst_no_sync, "psys_mm_bug_fly_3", pos47, 100), #particle name
        (store_random_in_range,":cur_time",8,14), #Seconds until next particle
      (try_end),
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    (try_end),
    #end
    (try_for_prop_instances, ":instance_id", "spr_mm_ambience_sound_local_crow", somt_object),  #Name of prop
      (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
      (val_sub,":cur_time",1),
      (try_begin),
        (le,":cur_time",0),
        (prop_instance_get_position, pos56, ":instance_id"),
        (play_sound_at_position, "snd_ambient_crow", pos56),#sound name
        (store_random_in_range,":cur_time",10,61), #Seconds until next sound
      (try_end),
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    (try_end),
])

# PN END *******************************************************************************************************************

local_chat_pressed = (0, 0.05, 0, [(game_key_clicked, gk_local_chat),(call_script, "script_cf_no_input_presentation_active")], # clients: local chat entry box
   [(assign, "$g_chat_box_string_id", "str_send_message_to_players_nearby"),
    (assign, "$g_chat_box_event_type", chat_event_type_local),
    (start_presentation, "prsnt_chat_box"),
    ])

faction_chat_pressed = (0, 0.05, 0, [(game_key_clicked, gk_faction_chat),(call_script, "script_cf_no_input_presentation_active")], # clients: faction chat entry box
   [(multiplayer_get_my_player, ":player_id"),
    (player_get_slot, ":faction_id", ":player_id", slot_player_faction_id),
    (is_between, ":faction_id", castle_factions_begin, factions_end),
    (str_store_faction_name, s11, ":faction_id"),
    (assign, "$g_chat_box_string_id", "str_send_message_to_the_s11"),
    (assign, "$g_chat_box_event_type", chat_event_type_faction),
    (start_presentation, "prsnt_chat_box"),
    ])

admin_chat_pressed = (0, 0.05, 0, [(game_key_clicked, gk_admin_chat),(call_script, "script_cf_no_input_presentation_active")], # clients: admin chat entry box
   [(try_begin), # for admins, allow sending only to a targeted player
      (multiplayer_get_my_player, ":player_id"),
      (player_is_admin, ":player_id"),
      (assign, "$g_chat_box_player_string_id", "str_send_admin_message_to_s1"),
    (else_try),
      (assign, "$g_chat_box_player_string_id", 0),
    (try_end),
    (assign, "$g_chat_box_string_id", "str_send_admin_message"),
    (assign, "$g_chat_box_event_type", chat_event_type_admin),
    (start_presentation, "prsnt_chat_box"),
    ])

ship_control_pressed = (0, 0, 0, [], # clients: check if the player agent is at a valid position on a ship, then send control requests the server
   [(this_or_next|key_clicked, key_up),
    (this_or_next|key_clicked, key_down),
    (this_or_next|key_clicked, key_left),
    (key_clicked, key_right),
    (call_script, "script_cf_no_input_presentation_active"),
    (call_script, "script_cf_client_check_control_ship"),
    ])

money_bag_pressed = (0, 0, 0, [], # clients: show presentation to drop money bags or interact with money chests
   [(game_key_clicked, gk_money_bag),
    (call_script, "script_cf_no_input_presentation_active"),
    (start_presentation, "prsnt_money_bag"),
    ])

animation_menu_pressed = (0, 0.05, 0, [(game_key_clicked, gk_animation_menu),(call_script, "script_cf_no_input_presentation_active")], # clients: show animation menu
   [(try_begin),
      (eq, "$g_animation_menu_no_mouse_grab", 1),
      (start_presentation, "prsnt_animation_menu_no_mouse_grab"),
    (else_try),
      (start_presentation, "prsnt_animation_menu"),
    (try_end),
    ])

welcome_message = (0, 0, ti_once, [], # clients: show a welcome message when connecting to a server
   [(neg|multiplayer_is_server),
    (call_script, "script_show_welcome_message"),
    ])

turn_windmill_fans = (0, 0, 4.0, [], # clients: make windmill fans in the scene turn visually (not affecting collision detection)
   [(neg|multiplayer_is_server),
    (call_script, "script_cf_turn_windmill_fans", 0),
    ])

ambient_sounds_check = (1, 0, 10, # clients: check for nearby ambient sound emitters to activate
   [(neg|multiplayer_is_server),
    (scene_prop_get_num_instances, ":num_instances", "spr_pw_scene_ambient_sound"),
    (try_begin),
      (ge, "$g_ambient_sound_instance_no", ":num_instances"),
      (assign, "$g_ambient_sound_instance_no", 0),
    (try_end),
    (scene_prop_get_instance, ":instance_id", "spr_pw_scene_ambient_sound", "$g_ambient_sound_instance_no"),
    (val_add, "$g_ambient_sound_instance_no", 1),
    (call_script, "script_cf_play_scene_ambient_sound", ":instance_id"),
    ], [])

music_situation_check = (25, 0, 0, [], # clients: try adjust the music for the current situation
   [(neg|multiplayer_is_server),
    (call_script, "script_music_set_situation"),
    ])

shadow_recalculation = (15, 1, 0, # clients: periodically recalculate environment shadows to fix them for moveable scene props
   [(neg|multiplayer_is_server),
    (eq, "$g_disable_automatic_shadow_recalculation", 0),
    (call_script, "script_cf_client_agent_is_inactive"),
    ],
   [(call_script, "script_cf_client_agent_is_inactive"),
    (rebuild_shadow_map),
    ])

adjust_weather_effects = (0, 0, 0.9, [], # clients: calculate weather effects based on server updates
   [(neg|multiplayer_is_server),
    (call_script, "script_cf_adjust_weather_effects"),
    ])

render_weather_effects = (0.1, 0, 0, [], # clients: regularly display weather effects
   [(neg|multiplayer_is_server),
    (call_script, "script_cf_render_weather_effects"),
    ])

def common_triggers(self):
  return [(ti_before_mission_start, 0, 0, [(assign, "$g_game_type", "mt_" + self)], []),
    before_mission_start_setup,
    after_mission_start_setup,

    player_joined,
    player_exit,

    agent_spawn,
    agent_killed,
    agent_hit,

    item_picked_up,
    item_dropped,
    item_wielded,
    item_unwielded,

    agent_mount,
    agent_dismount,

    player_check_loop,
    agent_check_loop,
    agent_check_attack_loop,
    ship_movement_loop,

    resource_regrow_check,
    polls_check,
    game_ended_check,
    draw_initial_banners,
    fill_chests_starting_inventory,
    fire_place_check,
    fish_school_loop,
    herd_leader_movement_loop,
    herd_follower_movement_loop,
    herd_animal_count_check,
    herd_animal_spawn_check,
    weather_situation_check,

    escape_pressed,
    tab_pressed,
    static_presentations_setup,
    action_menu_pressed,
    target_agent_pressed,
    chat_overlay_toggled,
    chat_resend_check,

    multiplayer_client_surrender,
    multiplayer_client_walking,
    multiplayer_client_spyglass,
    multiplayer_server_agent_hit_common,
    multiplayer_client_voice_warcry,
    multiplayer_client_voice_orders,
    multiplayer_client_music_and_sapper,
    multiplayer_agent_unwield_item_common,
    multiplayer_server_bird_spawn_common,
    multiplayer_server_move_bird_common,
    multiplayer_server_drag_limber,
    multiplayer_client_control_cannon,
    multiplayer_server_aim_cannon,
    multiplayer_server_cannonball_flight,
    multiplayer_agent_wield_item_common,
    multiplayer_server_explosives,
    multiplayer_play_sounds_and_particles,
    multiplayer_server_on_item_dropped,

    local_chat_pressed,
    faction_chat_pressed,
    admin_chat_pressed,
    ship_control_pressed,
    animation_menu_pressed,

    welcome_message,
    turn_windmill_fans,
    ambient_sounds_check,
    music_situation_check,
    shadow_recalculation,
    adjust_weather_effects,
    render_weather_effects,
]

mission_templates = [
  ("conquest", mtf_battle_mode, -1, "Conquest.", spawn_points_0_99,
    common_triggers("conquest") + [
    money_bag_pressed,
    ]),

  ("quick_battle", mtf_battle_mode, -1, "Quick battle.", spawn_points_0_99,
    common_triggers("quick_battle") + [
    money_bag_pressed,
    ]),

  ("no_money", mtf_battle_mode, -1, "No money.", spawn_points_0_99,
    common_triggers("no_money")
    ),

  ("feudalism", mtf_battle_mode, -1, "Feudalism.", spawn_points_0_99,
    common_triggers("feudalism") + [
    money_bag_pressed,
    ]),

  ("permanent_death", mtf_battle_mode, -1, "Permanent death.", spawn_points_0_99,
    common_triggers("permanent_death") + [
    money_bag_pressed,
    ]),

  ("edit_scene", 0, -1, "edit_scene", [(0,mtef_visitor_source,0,aif_start_alarmed,1,[])],
   [
    (ti_before_mission_start, 0, 0, [], # set up some basic values for scene editing features
     [(server_set_add_to_game_servers_list, 0),
      (assign, "$g_edit_scene", 1),
      (call_script, "script_scene_set_day_time"),
      (call_script, "script_setup_castle_names"),
      (troop_set_slot, "trp_removed_scene_props", 0),
      (call_script, "script_setup_all_linked_scene_props"),
      ]),

    (ti_after_mission_start, 0, 0, [], # set up more values and perform some scene checks
     [(set_spawn_effector_scene_prop_kind, team_default, -1),
      (team_set_relation, team_default, team_default, -1),
      (call_script, "script_initialize_troop_equipment_slots"),
      (call_script, "script_initialize_item_slots"),
      (call_script, "script_setup_ship_collision_props"),
      (try_begin),
        (neg|is_edit_mode_enabled),
        (display_message, "str_error_edit_mode_not_enabled"),
      (try_end),
      (display_message, "str_pw_editor_welcome"),
      (try_begin),
        (prop_instance_is_valid, 0),
        (prop_instance_get_scene_prop_kind, reg0, 0),
        (ge, reg0, "spr_pw_tree_a1"),
        (display_message, "str_error_scene_prop_0_pw"),
      (try_end),
      ]),

    (ti_server_player_joined, 0, 0, [], # spawn an agent to walk or ride around with
     [(store_trigger_param_1, ":player_id"),
      (player_set_team_no, ":player_id", team_default),
      (player_set_troop_id, ":player_id", "trp_player"),
      (entry_point_get_position, pos10, 0),
      (player_spawn_new_agent, ":player_id", 0),
      ]),

    (ti_on_agent_spawn, 0, 0, [], # move new agents near the position of previous ones
     [(store_trigger_param_1, ":agent_id"),
      (neg|agent_is_non_player, ":agent_id"),
      (agent_set_position, ":agent_id", pos10),
      ]),

    (ti_escape_pressed, 0, 0, [], # confirm leaving edit mode
     [(question_box, "str_leave_edit_mode"),
      ]),

    (ti_question_answered, 0, 0, [], # handle the leaving confirmation dialog
     [(store_trigger_param_1, ":answer"),
      (eq, ":answer", 0),
      (finish_mission),
      ]),

    (0, 0, 0, [(key_clicked, key_f1)], # show some basic editing information
     [(call_script, "script_preset_message", "str_pw_editor_info", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 0, [(key_clicked, key_f2)], # list the meanings of scene prop values adjustable in the editor
     [(call_script, "script_preset_message", "str_pw_editor_values_info", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 0, [(key_clicked, key_f3)], # list castle names with the corresponding numbers in the editor
     [(str_clear, s0),
      (store_sub, reg1, castle_names_end, castle_names_begin),
      (try_for_range_backwards, ":castle_name_string_id", castle_names_begin, castle_names_end),
        (val_sub, reg1, 1),
        (str_store_string, s1, ":castle_name_string_id"),
        (str_store_string, s0, "str_castle_names_numbers_format"),
      (try_end),
      (str_store_string, s2, s0),
      (call_script, "script_preset_message", "str_pw_editor_castle_names", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 0, [(key_clicked, key_f12)], # measure distance between the player agent and the first pointer_arrow scene prop
     [(scene_prop_get_instance, ":instance_id", "spr_pointer_arrow", 0),
      (prop_instance_get_position, pos1, ":instance_id"),
      (get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_get_position, pos2, ":agent_id"),
      (get_distance_between_positions, reg1, pos1, pos2),
      (get_sq_distance_between_positions, reg2, pos1, pos2),
      (display_message, "str_distance_reg1_sq_distance_reg2"),
      ]),

    (0, 0, 0, [(key_clicked, key_f11)], # spawn an admin horse for fast movement
     [(get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_get_position, pos1, ":agent_id"),
      (position_move_x, 50),
      (set_spawn_position, pos1),
      (spawn_horse, "itm_admin_horse"),
      (agent_equip_item, ":agent_id", "itm_torch"),
      ]),

    (0, 0, 0, [(key_clicked, key_f10)], # iterate through the positions of all scene props added to the ship collison list
     [(troop_get_slot, ":collision_props_count", "trp_ship_array", slot_ship_array_collision_props_count),
      (try_begin),
        (ge, "$g_test_ship_collision_prop", ":collision_props_count"),
        (assign, "$g_test_ship_collision_prop", 0),
        (entry_point_get_position, pos1, 0),
      (else_try),
        (store_add, ":collision_prop_slot", slot_ship_array_collision_props_begin, "$g_test_ship_collision_prop"),
        (troop_get_slot, ":collision_instance_id", "trp_ship_array", ":collision_prop_slot"),
        (val_add, "$g_test_ship_collision_prop", 1),
        (prop_instance_get_position, pos1, ":collision_instance_id"),
      (try_end),
      (get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_set_position, ":agent_id", pos1),
      ]),

    (0, 0, 0, [(key_clicked, key_f9)], # respawn a new player agent using a random troop
     [(multiplayer_get_my_player, ":player_id"),
      (player_get_agent_id, ":agent_id", ":player_id"),
      (try_begin),
        (agent_is_active, ":agent_id"),
        (agent_is_alive, ":agent_id"),
        (agent_fade_out, ":agent_id"),
        (try_for_range, ":player_equip_slot", slot_player_equip_item_0, slot_player_equip_end),
          (player_set_slot, ":player_id", ":player_equip_slot", 0),
        (try_end),
      (try_end),
      (store_random_in_range, ":troop_id", playable_troops_begin, playable_troops_end),
      (player_set_troop_id, ":player_id", ":troop_id"),
      (call_script, "script_player_add_default_troop_items", ":player_id", ":troop_id"),
      (call_script, "script_get_random_equipment", "itm_linen_tunic", "itm_tribal_warrior_outfit"),
      (player_set_slot, ":player_id", slot_player_equip_body, reg0),
      (call_script, "script_get_random_equipment", "itm_sarranid_boots_a", "itm_khergit_leather_boots"),
      (player_set_slot, ":player_id", slot_player_equip_foot, reg0),
      (call_script, "script_player_add_spawn_items", ":player_id", 1),
      (player_spawn_new_agent, ":player_id", 0),
      (mission_cam_get_position, pos10),
      ]),

    (0, 0, 0, [(key_clicked, key_f8)], # iterate through positions of all scene props that are not correctly linked with the other required props
     [(troop_get_slot, ":unlinked_prop_count", "trp_removed_scene_props", slot_array_count),
      (try_begin),
        (gt, ":unlinked_prop_count", 0),
        (lt, "$g_test_unlinked_prop", ":unlinked_prop_count"),
        (val_add, "$g_test_unlinked_prop", 1),
        (troop_get_slot, ":unlinked_instance_id", "trp_removed_scene_props", "$g_test_unlinked_prop"),
        (prop_instance_is_valid, ":unlinked_instance_id"),
        (assign, reg10, ":unlinked_instance_id"),
        (prop_instance_get_scene_prop_kind, reg11, ":unlinked_instance_id"),
        (prop_instance_get_variation_id_2, reg12, ":unlinked_instance_id"),
        (display_message, "str_error_unlinked_scene_prop"),
      (else_try),
        (assign, ":unlinked_instance_id", -1),
        (ge, "$g_test_unlinked_prop", ":unlinked_prop_count"),
        (assign, "$g_test_unlinked_prop", 0),
        (display_message, "str_no_more_unlinked_scene_props"),
        (prop_instance_is_valid, 0),
        (prop_instance_get_scene_prop_kind, reg0, 0),
        (ge, reg0, "spr_pw_tree_a1"),
        (display_message, "str_error_scene_prop_0_pw"),
        (assign, ":unlinked_instance_id", 0),
      (try_end),
      (try_begin),
        (neq, ":unlinked_instance_id", -1),
        (prop_instance_get_position, pos1, ":unlinked_instance_id"),
        (init_position, pos2),
        (position_get_rotation_around_z, ":rotation", pos1),
        (position_copy_rotation, pos1, pos2),
        (position_rotate_z, pos1, ":rotation"),
        (copy_position, pos2, pos1),
        (position_move_z, pos2, 300, 1),
        (set_spawn_position, pos2),
        (spawn_item, "itm_pointer_arrow", 0, 4),
        (prop_instance_set_position, reg0, pos2),
        (prop_instance_animate_to_position, reg0, pos1, 200),
        (get_player_agent_no, ":agent_id"),
        (agent_is_active, ":agent_id"),
        (agent_is_alive, ":agent_id"),
        (agent_set_position, ":agent_id", pos1),
      (try_end),
      ]),

    ]),
]
