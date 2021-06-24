from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import header_debug as dbg
import header_lazy_evaluation as lazy

####################################################################################################################
#  Each scene prop record contains the following fields:
#  1) Scene prop id: used for referencing scene props in other files. The prefix spr_ is automatically added before each scene prop id.
#  2) Scene prop flags. See header_scene_props.py for a list of available flags
#  3) Mesh name: Name of the mesh.
#  4) Physics object name:
#  5) Triggers: Simple triggers that are associated with the scene prop
####################################################################################################################

# PN TRIGGERS START *************************************************************************
check_mm_on_destroy_window_trigger = (ti_on_scene_prop_destroy,
  [
    (try_begin),
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),

      (store_trigger_param_1, ":instance_id"),      
      (prop_instance_is_valid,":instance_id"),
      (prop_instance_get_scene_prop_kind,":prop_kind",":instance_id"),
      (prop_instance_get_position,pos49,":instance_id"),
      
      (copy_position,pos56,pos49),
      (position_move_z,pos56,140),
      (particle_system_burst, "psys_bottle_break", pos56, 10),
      (call_script, "script_multiplayer_server_play_sound_at_position", "snd_glass_break"),
      
      (assign,":prop_to_spawn",-1),
      (try_begin),
        (eq,":prop_kind","spr_mm_window1"),
        (assign,":prop_to_spawn","spr_mm_window1d"),
      (else_try),
        (eq,":prop_kind","spr_mm_window2"),
        (assign,":prop_to_spawn","spr_mm_window2d"),
      (else_try),
        (eq,":prop_kind","spr_mm_window1_poor"),
        (assign,":prop_to_spawn","spr_mm_window1d_poor"),
      (else_try),
        (eq,":prop_kind","spr_mm_window2_poor"),
        (assign,":prop_to_spawn","spr_mm_window2d_poor"),
      (else_try),
        (eq,":prop_kind","spr_mm_window3"),
        (assign,":prop_to_spawn","spr_mm_window3d"),
      (else_try),
        (eq,":prop_kind","spr_mm_window4"),
        (assign,":prop_to_spawn","spr_mm_window4d"),
      (else_try),
        (eq,":prop_kind","spr_mm_window3_poor"),
        (assign,":prop_to_spawn","spr_mm_window3d_poor"),
      (else_try),
        (eq,":prop_kind","spr_mm_window4_poor"),
        (assign,":prop_to_spawn","spr_mm_window4d_poor"),
      (try_end),
      
      (try_begin),
        (scene_prop_slot_eq, ":instance_id", scene_prop_slot_is_scaled, 1), # is scaled.
        (scene_prop_get_slot,":x_scale",":instance_id",scene_prop_slot_x_scale),
        (scene_prop_get_slot,":y_scale",":instance_id",scene_prop_slot_y_scale),
        (scene_prop_get_slot,":z_scale",":instance_id",scene_prop_slot_z_scale),
        (call_script, "script_find_or_create_scene_prop_instance", ":prop_to_spawn", 0, 0, 1, ":x_scale",":y_scale",":z_scale"),
      (else_try),
        (call_script, "script_find_or_create_scene_prop_instance", ":prop_to_spawn", 0, 0, 0),
      (try_end),
      (assign,":destroyed_prop",reg0),
      
      (scene_prop_set_slot, ":destroyed_prop", scene_prop_slot_replacing, ":instance_id"),
      
      (scene_prop_get_slot,":wall_instance",":instance_id", scene_prop_slot_parent_prop),
      (try_begin),
        (prop_instance_is_valid,":wall_instance"),
        (scene_prop_set_slot,":destroyed_prop",scene_prop_slot_parent_prop,":wall_instance"),
        
        (scene_prop_set_slot,":wall_instance",scene_prop_slot_child_prop1,":destroyed_prop"),
      (try_end),
      
      (call_script, "script_clean_up_prop_instance", ":instance_id"),
    (try_end),
])

check_common_destructible_props_destroy_trigger = (ti_on_scene_prop_destroy,
  [
    (play_sound, "snd_dummy_destroyed"),
    
    (try_begin),
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),

      (store_trigger_param_1, ":instance_no"),
      (prop_instance_get_scene_prop_kind, ":prop_kind", ":instance_no"),
      
      (prop_instance_get_position, pos49, ":instance_no"),
      
      (particle_system_burst, "psys_dummy_straw", pos49, 20),
      (particle_system_burst, "psys_dummy_smoke", pos49, 50),

      (call_script, "script_clean_up_prop_instance", ":instance_no"),
      
      (assign,":prop_to_spawn",-1),
      (try_begin),
        (eq,":prop_kind","spr_mm_stakes_destructible"),
        (assign,":prop_to_spawn","spr_mm_stakes_construct"),
      (else_try),
        (eq,":prop_kind","spr_mm_stakes2_destructible"),
        (assign,":prop_to_spawn","spr_mm_stakes2_construct"),
      (else_try),
        (eq,":prop_kind","spr_sandbags_destructible"),
        (assign,":prop_to_spawn","spr_sandbags_construct"),
      (else_try),
        (eq,":prop_kind","spr_chevaux_de_frise_tri_destructible"),
        (assign,":prop_to_spawn","spr_chevaux_de_frise_tri_construct"),
      (else_try),
        (eq,":prop_kind","spr_gabiondeploy_destructible"),
        (assign,":prop_to_spawn","spr_gabiondeploy_construct"),
      (else_try),
        (eq,":prop_kind","spr_mm_fence1"),
        (assign,":prop_to_spawn","spr_mm_fence1d"),  
      (try_end),
      
      (gt,":prop_to_spawn",-1),
      
      # Spawn destroyed prop
      (call_script, "script_find_or_create_scene_prop_instance", ":prop_to_spawn", 0, 0, 0),
    (try_end),
])

check_common_constructable_prop_on_hit_trigger = (ti_on_scene_prop_hit,
  [
    (store_trigger_param_1, ":instance_no"),
    (store_trigger_param_2, ":damage"),
    
    (try_begin),
      (prop_instance_is_valid,":instance_no"),
      (prop_instance_get_scene_prop_kind, ":prop_kind", ":instance_no"),
      
      (set_trigger_result,0), #Don't deal any normal damage to the prop
     
      (scene_prop_get_hit_points, ":health", ":instance_no"),
      (scene_prop_get_slot,":max_health",":instance_no",scene_prop_slot_max_health),
      
      (set_fixed_point_multiplier, 1),
      (position_get_x, ":agent_id", pos2),
      (set_fixed_point_multiplier, 100),
      (agent_is_active,":agent_id"),
      (agent_is_alive, ":agent_id"),
      
      (assign,":hit_sound","snd_dummy_hit"),
      (assign,":hit_smoke","psys_dummy_smoke"),
      (assign,":hit_particles","psys_dummy_straw"),
      (assign,":hit_smoke_size",3),
      (assign,":hit_particles_size",10),
      (assign,":apply_dmg",1),
      (assign,":update_dmg",1),
      
      (agent_get_wielded_item,":item_id",":agent_id",0),
      (try_begin),
        (this_or_next|eq,":item_id","itm_sapper_axe_rus"),
        (this_or_next|eq,":item_id","itm_sapper_axe"),
        (this_or_next|eq,":item_id","itm_russian_peasant_axe"),
        (eq,":item_id","itm_russian_peasant_2handed_axe"),

        (neq,":prop_kind","spr_earthwork1_destructible"), # not for earth prop.
        
        (val_mul,":damage",2),
      (else_try),
        (eq,":item_id","itm_construction_hammer"), #Only constructable with hammer
        
        (agent_get_troop_id,":troop_id",":agent_id"),
        (eq,":troop_id", "trp_sapper"),
        
        (neq,":prop_kind","spr_earthwork1_destructible"), # not for earth prop.
        
        (assign,":hit_sound","snd_hammer"),
        (assign,":apply_dmg",0),

        (assign,":old_health",":health"),
        (val_add,":health",25), # 25 hitpoints per hit with hammer.
        (val_min,":health",":max_health"),
        
        (try_begin),
          (eq,":old_health",":health"),
          (assign,":update_dmg",0),
        (try_end),

        (try_begin),
          (ge,":health",":max_health"),
          
          (is_between,":prop_kind","spr_mm_palisadedd","spr_crate_explosive"), # a construction object
          
          (assign,":update_dmg",0),
          
          (this_or_next|multiplayer_is_server), # only on servers.
          (neg|game_in_multiplayer_mode),
       
          (prop_instance_get_position, pos49, ":instance_no"),
          
          (call_script, "script_clean_up_prop_instance", ":instance_no"),
          
          (call_script, "script_get_prop_kind_for_constr_kind", ":prop_kind"),
          (assign,":prop_to_spawn",reg0),
          (assign,":x_offset",reg1),
          (assign,":y_offset",reg2),
          (assign,":z_offset",reg3),
          (assign,":dont_rotate_to_ground",reg4),
          
          (gt,":prop_to_spawn",-1),
          
          (try_begin),
            (eq,":dont_rotate_to_ground",1),
            (init_position,pos37),
            (position_copy_origin,pos37,pos49),
            (position_get_rotation_around_z,":z_rot",pos49),
            (position_rotate_z,pos37,":z_rot"),
            (copy_position,pos49,pos37),
          (try_end),
          
          (position_move_x,pos49,":x_offset"),
          (position_move_y,pos49,":y_offset"),
          (position_move_z,pos49,":z_offset"),
          
          (try_begin),
            (eq,":dont_rotate_to_ground",1),
            (call_script, "script_find_or_create_scene_prop_instance", ":prop_to_spawn", 0, 0, 0),
          (else_try),
            (call_script, "script_find_or_create_scene_prop_instance", ":prop_to_spawn", 0, 1, 0),
          (try_end),
          (assign,":new_instance_no",reg0),
          # init the new prop slots.
          (call_script,"script_multiplayer_server_initialise_destructable_prop_slots",":new_instance_no",":prop_to_spawn"),
        (try_end),
      (try_end),
     
      (try_begin), # with earth digs we have some specialll stuff.
        (eq,":prop_kind","spr_earthwork1_destructible"),
        
        (assign,":apply_dmg",0),
        
        (try_begin),
          (neq,":item_id","itm_shovel"),
          (neq,":item_id","itm_shovel_undig"),
          (assign,":hit_sound",-1),
          (assign,":hit_smoke",-1),
          (assign,":hit_particles",-1),
        (try_end),
        
        (this_or_next|eq,":item_id","itm_shovel"),
        (eq,":item_id","itm_shovel_undig"),
          
        (assign,":hit_sound","snd_shovel"),
        
        (call_script,"script_move_pioneer_ground",":instance_no",":item_id",":health",":max_health"),
        (assign,":health",reg0),
      (try_end),
      
      (try_begin), # not a pioneer
        (eq,":apply_dmg",1),
        (try_begin), # for construction objects hit by anyone else then pioneers dont do anything.
          (is_between,":prop_kind","spr_mm_palisadedd","spr_mm_stakes_construct"), # a construction object that is not placable by sapper.
          (assign,":hit_sound",-1),
          (assign,":hit_smoke",-1),
          (assign,":hit_particles",-1),
        (else_try), # else apply the damage. (that could mean destroying the placed stuff by sapper!)
          (scene_prop_set_slot,":instance_no",scene_prop_slot_last_hit_by,":agent_id"),
          (val_sub,":health",":damage"),
          (val_max,":health",0),
        (try_end),
      (try_end),
      
      (try_begin),
        (eq,":update_dmg",1),
        (this_or_next|multiplayer_is_server), # only on servers.
        (neg|game_in_multiplayer_mode),
        (scene_prop_set_cur_hit_points, ":instance_no", ":health"),
        (scene_prop_set_slot,":instance_no",scene_prop_slot_health,":health"),
      (try_end),
      
      (try_begin),
        (gt, ":health", 0),
        (try_begin),
          (gt,":hit_sound",-1),
          (play_sound, ":hit_sound"),
        (try_end),
      (else_try),
        (neg|multiplayer_is_server),
        (neq,":prop_kind","spr_earthwork1_destructible"),
        (play_sound, "snd_dummy_destroyed"),
      (try_end),

      (try_begin),
        (neg|multiplayer_is_dedicated_server),
        (try_begin),
          (gt,":hit_smoke",-1),
          (particle_system_burst_no_sync, ":hit_smoke", pos1, ":hit_smoke_size"),
        (try_end),
        
        (try_begin),
          (gt,":hit_particles",-1),
          (particle_system_burst_no_sync, ":hit_particles", pos1, ":hit_particles_size"),
        (try_end),
      (try_end),
    (try_end),
])

check_common_constructible_props_destroy_trigger = (ti_on_scene_prop_destroy,
  [
    (play_sound, "snd_dummy_destroyed"),
    
    (try_begin),
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),

      (store_trigger_param_1, ":instance_no"),
      
      (prop_instance_get_position, pos49, ":instance_no"),
      
      (particle_system_burst, "psys_dummy_straw", pos49, 20),
      (particle_system_burst, "psys_dummy_smoke", pos49, 50),

      (call_script, "script_clean_up_prop_instance", ":instance_no"),
    (try_end),
])

check_common_dummy_destroy_trigger = (ti_on_scene_prop_destroy,
  [
    (play_sound, "snd_dummy_destroyed"),
    
    (try_begin),
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),
   
      (store_trigger_param_1, ":instance_no"),
      (scene_prop_get_slot,":attacker_agent_id",":instance_no",scene_prop_slot_last_hit_by),
      
      (prop_instance_get_starting_position, pos1, ":instance_no"),
      
      (assign, ":rotate_side", 80),
      (try_begin),
        (agent_is_active,":attacker_agent_id"),
        (agent_get_position, pos2, ":attacker_agent_id"),
        (position_is_behind_position, pos2, pos1),
        (val_mul, ":rotate_side", -1),
      (try_end),
      (position_rotate_x, pos1, ":rotate_side"),
      (prop_instance_animate_to_position, ":instance_no", pos1, 70), #animate to position 1 in 0.7 second
        
      (try_begin),
        (neg|game_in_multiplayer_mode),
        (eq,"$g_is_tutorial",1),
        (val_add,"$g_tutorial_targets_destroyed",1),
      (try_end),
    (try_end),
])

check_common_dummy_on_hit_trigger = (ti_on_scene_prop_hit,
    [
      (play_sound, "snd_dummy_hit"),
      
      (try_begin),
        (this_or_next|multiplayer_is_server),
        (neg|game_in_multiplayer_mode),
        
        (store_trigger_param_1, ":instance_no"),
        (store_trigger_param_2, ":damage"),
        (set_fixed_point_multiplier, 1),
        (position_get_x, ":attacker_agent_id", pos2),
        (set_fixed_point_multiplier, 100),
        
        (scene_prop_set_slot,":instance_no",scene_prop_slot_last_hit_by,":attacker_agent_id"),
      
        (assign, reg60, ":damage"),
        (val_div, ":damage", 8),
        (prop_instance_get_position, pos2, ":instance_no"),

        (try_begin),
          (agent_is_active,":attacker_agent_id"),
          (agent_get_position, pos3, ":attacker_agent_id"),
          (position_is_behind_position, pos3, pos2),
          (val_mul, ":damage", -1),
        (try_end),
        (position_rotate_x, pos2, ":damage"),
        
        (try_begin),
          (game_in_multiplayer_mode),
          
          (agent_get_player_id,":player_id",":attacker_agent_id"),
          (player_is_active,":player_id"),
          
          (multiplayer_send_string_to_player, ":player_id", multiplayer_event_show_server_message, "str_delivered_damage"),
        (else_try),
          (neg|game_in_multiplayer_mode),
          (call_script, "script_client_get_my_agent"),
          (eq, ":attacker_agent_id", reg0), # Only for myself.
          (display_message, "str_delivered_damage"),
        (try_end),

        (prop_instance_animate_to_position, ":instance_no", pos2, 30), #animate to position 2 in 0.3 second
        
        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),
      (try_end),
])

check_common_explosive_crate_use_trigger = (ti_on_scene_prop_use,
  [
    (store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":instance_id"),
    
    (try_begin),
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),
      
      (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
      (le,":cur_time",0),
      (scene_prop_set_slot,":instance_id", scene_prop_slot_time, 5), #Seconds until exploding
      (scene_prop_set_slot,":instance_id", scene_prop_slot_user_agent, ":agent_id"), #User agent
      
      (scene_prop_enable_after_time, ":instance_id", 500),
      
      (prop_instance_get_position,pos56,":instance_id"),
      (call_script,"script_multiplayer_server_play_sound_at_position","snd_crate_fuse"),
    (try_end),
])

check_cannon_animation_finished_trigger = (ti_on_scene_prop_animation_finished,
  [
    (store_trigger_param_1, ":instance_id"),
    
    (try_begin),
      (prop_instance_is_valid, ":instance_id"),
      
      (scene_prop_slot_eq, ":instance_id", scene_prop_slot_just_pushed_back, 1), # Just has been pushed back by player.
      (scene_prop_set_slot,":instance_id",scene_prop_slot_just_pushed_back,0),
      
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),
      
      (call_script,"script_cannon_instance_get_barrel",":instance_id"),
      (call_script, "script_prop_instance_find_first_child_of_type", reg0, "spr_mm_aim_button"),
      (call_script,"script_set_prop_child_active",reg0),
    (try_end),
])

check_cannon_wheels_animation_finished_trigger = (ti_on_scene_prop_animation_finished,
  [
    (store_trigger_param_1, ":instance_id"),
    
    (try_begin),
      (prop_instance_is_valid, ":instance_id"),
      (scene_prop_slot_eq, ":instance_id", scene_prop_slot_just_pushed_back, 1), # Just has been pushed back by player.
      (scene_prop_set_slot,":instance_id",scene_prop_slot_just_pushed_back,0),
      
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),
      
      (scene_prop_get_slot,reg0,":instance_id", scene_prop_slot_parent_prop),
      (call_script,"script_cannon_instance_get_barrel",reg0), # then activate the aim button.
      (call_script, "script_prop_instance_find_first_child_of_type", reg0, "spr_mm_aim_button"),
      (call_script,"script_set_prop_child_active",reg0),
    (try_end),
])

check_mm_use_cannon_prop_start_trigger = (ti_on_scene_prop_start_use,
  [
    (store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":instance_id"),
    
    (call_script, "script_multiplayer_server_check_if_can_use_button", ":agent_id", ":instance_id"),
    (eq, reg0, 1),
    
    (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
     
    (assign, ":anim_id", -1),
    (try_begin),
      (is_between, ":scene_prop_id", mm_unlimber_button_types_begin, mm_unlimber_button_types_end), 
    (else_try),
      (eq, ":scene_prop_id", "spr_mm_limber_button"),
    (else_try),
      (eq, ":scene_prop_id", "spr_mm_aim_button"),
    (else_try),
      (eq, ":scene_prop_id", "spr_mm_load_rocket_button"),
      (assign, ":anim_id", "anim_rocket_load"),
    (else_try),
      (is_between,":scene_prop_id","spr_mm_load_cartridge_button","spr_mm_reload_button"), # Load something button
      (assign, ":anim_id", "anim_cannon_load"),
      (try_begin),
        (agent_get_slot, ":frizzle_times", ":agent_id", slot_agent_frizzle_times),
        (val_add,":frizzle_times",1),
        (agent_set_slot, ":agent_id", slot_agent_frizzle_times, ":frizzle_times"),
        (try_begin),
          (le,":frizzle_times",3), # only 2 times before calling it off
          (prop_instance_get_position,pos56,":instance_id"),
          (call_script,"script_multiplayer_server_play_sound_at_position","snd_cannon_ball"),
        (try_end),
      (try_end),
    (else_try),
      (eq, ":scene_prop_id", "spr_mm_reload_button"),
      (assign, ":anim_id", "anim_cannon_reload"),
      (try_begin),
        (agent_get_slot, ":frizzle_times", ":agent_id", slot_agent_frizzle_times),
        (val_add,":frizzle_times",1),
        (agent_set_slot, ":agent_id", slot_agent_frizzle_times, ":frizzle_times"),
        (try_begin),
          (le,":frizzle_times",3), # only 2 times before calling it off
          (prop_instance_get_position,pos56,":instance_id"),
          (call_script,"script_multiplayer_server_play_sound_at_position","snd_ramrod"),
        (try_end),
      (try_end),
    (else_try),
      (eq, ":scene_prop_id", "spr_mm_round_button"),
    (else_try),
      (eq, ":scene_prop_id", "spr_mm_shell_button"),
    (else_try),
      (eq, ":scene_prop_id", "spr_mm_canister_button"),
    (else_try),
      (eq, ":scene_prop_id", "spr_mm_bomb_button"),
    (try_end),
    
    (try_begin),
      (gt,":anim_id",-1),
      # stop current anim
      (agent_set_animation, ":agent_id", "anim_cannon_end", 1),
      (agent_set_animation_progress, ":agent_id", 100),
      # and play new
      (agent_set_animation, ":agent_id", ":anim_id", 1),
    (try_end),
])

check_mm_use_cannon_prop_end_trigger = (ti_on_scene_prop_use,
  [
    (store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":instance_id"),
    
    (call_script, "script_multiplayer_server_check_if_can_use_button", ":agent_id", ":instance_id"),
    (eq, reg0, 1),
    
    (agent_set_slot,":agent_id", slot_agent_frizzle_times,0), # Reset frizzles
    
    (call_script, "script_use_item", ":instance_id", ":agent_id"),
])

check_mm_use_cannon_prop_cancel_trigger = (ti_on_scene_prop_cancel_use,
  [
    (store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":instance_id"),

    (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
    
    (try_begin),
      (this_or_next|is_between,":scene_prop_id","spr_mm_load_cartridge_button","spr_mm_reload_button"),
      (eq, ":scene_prop_id", "spr_mm_reload_button"),
      (agent_set_animation, ":agent_id", "anim_cannon_end", 1),
    (try_end),
])

check_common_earth_on_hit_trigger = (ti_on_scene_prop_hit,
  [
    (set_trigger_result, 0), # do no damage
    
    (set_fixed_point_multiplier, 1),
    (position_get_x, ":agent_id", pos2),
    (ge, ":agent_id", 0),
    (agent_is_alive, ":agent_id"),
    (agent_get_wielded_item,":item_id",":agent_id",0),
    
    (this_or_next|eq,":item_id","itm_shovel"),
    (eq,":item_id","itm_shovel_undig"),
    
    (play_sound, "snd_shovel"),
  
    (try_begin),
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),
      
      (store_trigger_param_1, ":instance_no"),
      (prop_instance_get_scene_prop_kind, ":prop_kind", ":instance_no"),
      
      
      (prop_instance_get_position,pos4,":instance_no"),
      
      (assign,":continue",1),
      
      (try_begin),
        (eq,":prop_kind","spr_mm_tunnel_wall"),
        
        (assign,":keep_searching",1),
        (try_for_prop_instances, ":cur_instance_id", "spr_mm_tunnel_wall", somt_object),
          (neq,":cur_instance_id",":instance_no"),
          (eq,":keep_searching",1),
          (prop_instance_get_position,pos3,":cur_instance_id"),
          (get_distance_between_positions,":distance",pos4,pos3),
          (lt,":distance",100),
    
          (particle_system_burst, "psys_dummy_smoke_big", pos4, 100),
          
          (position_move_z,pos4,-2000,1),
          (prop_instance_animate_to_position, ":instance_no", pos4, 0),
          (prop_instance_animate_to_position, ":cur_instance_id", pos4, 0),
          
          (assign,":keep_searching",0),
          (assign,":continue",0),
        (try_end),
        
        (position_move_y,pos4,-12,0),
      (else_try),
        (position_move_z,pos4,-12,0),
      (try_end),
      
      (eq,":continue",1),
      
      (prop_instance_animate_to_position, ":instance_no", pos4, 6),
      
      (particle_system_burst, "psys_dummy_smoke", pos1, 10),
    (try_end),
])

# PN TRIGGERS END *************************************************************************

from header_item_modifiers import *

link_scene_prop = -100.0
link_scene_prop_self = 1
init_scene_prop = -101.0

def pad_list(li, value, length):
  li.extend([value] * (length - len(li)))
  return li

def flatten_list(li):
  return (e for s in li for e in s)

def spr_tag(name):
  if name != -1:
    name = "spr_"+name
  return name

def spr_check_value(value, low, high, name):
  if value < low or value > high:
    raise Exception("%s value must be between %d and %d" % (name, low, high))
  return value

def spr_check_hit_points(hp, low_hp=min_scene_prop_hit_points):
  return spr_check_value(hp, low_hp + 1, max_correctly_displayed_hp, "Hit points")

def spr_check_inventory_count(count):
  return spr_check_value(count, 1, inventory_count_maximum, "Inventory count")

# Helper to set common slots for props related to a particular item, like stockpiles.
def spr_item_init_trigger(item_id, use_string=None, tableau=None, stockpile=False, price_multiplier=None, resource_stock_count=False):
  init_trigger = (ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_item_id, item_id),
      ])
  if use_string is not None:
    init_trigger[1].append((scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string))
  if tableau is not None:
    init_trigger[1].append((cur_scene_prop_set_tableau_material, tableau, 0))
  if stockpile is True:
    init_trigger[1].extend([
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_stock_count_update_time, -1),
      (try_begin),
        (neq, "$g_game_type", "mt_quick_battle"),
        (prop_instance_get_variation_id_2, ":initial_stock_count", ":instance_id")])
    if resource_stock_count is True:
      init_trigger[1].extend([
        (val_mod, ":initial_stock_count", 10),
        (val_mul, ":initial_stock_count", 10),
        (scene_prop_set_slot, ":instance_id", slot_scene_prop_is_resource_stockpile, 1)])
    init_trigger[1].extend([
        (val_mul, ":initial_stock_count", "$g_initial_stockpile_multiplier"),
        (val_div, ":initial_stock_count", 100),
        (scene_prop_set_slot, ":instance_id", slot_scene_prop_stock_count, ":initial_stock_count"),
      (try_end)])
  if price_multiplier is not None:
    init_trigger[1].append((scene_prop_set_slot, ":instance_id", slot_scene_prop_gold_multiplier, price_multiplier))
  return init_trigger

# Helper to generate a trigger that just passes the parameters on to a script.
def spr_call_script_trigger(trigger_type, script_name, *args):
  use_trigger = (trigger_type,
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      ])
  call_script_list = [call_script, script_name, ":agent_id", ":instance_id"]
  call_script_list.extend(args)
  use_trigger[1].append(tuple(call_script_list))
  return use_trigger

# Helper to generate a trigger that calls a script after completely using.
def spr_call_script_use_trigger(script_name, *args):
  return spr_call_script_trigger(ti_on_scene_prop_use, script_name, *args)

# Helper to generate a trigger that calls a script after starting usage.
def spr_call_script_start_use_trigger(script_name, *args):
  return spr_call_script_trigger(ti_on_scene_prop_start_use, script_name, *args)

# Helper to generate a trigger that calls a script after canceling usage.
def spr_call_script_cancel_use_trigger(script_name, *args):
  return spr_call_script_trigger(ti_on_scene_prop_cancel_use, script_name, *args)

def spr_buy_item_flags(use_time=1):
  use_time = max(use_time, 1)
  return spr_use_time(use_time)

crafting_data = []

# Helper to set a custom position offset and rotation for item spawning props.
def spr_apply_pos_offset(trigger_block, pos_offset, rotate):
  if pos_offset[0] != 0:
    trigger_block.append((position_move_x, pos1, pos_offset[0]))
  if pos_offset[1] != 0:
    trigger_block.append((position_move_y, pos1, pos_offset[1]))
  if pos_offset[2] != 0:
    trigger_block.append((position_move_z, pos1, pos_offset[2]))
  if rotate[0] != 0:
    trigger_block.append((position_rotate_x, pos1, rotate[0]))
  if rotate[1] != 0:
    trigger_block.append((position_rotate_y, pos1, rotate[1]))
  if rotate[2] != 0:
    trigger_block.append((position_rotate_z, pos1, rotate[2]))

# Buying, selling, and crafting stockpile for 'item_id': if the 'resources' list is blank, the item will only be buyable.
# 'pos_offset' and 'rotate' are to adjust the position and rotation of the spawned item.
# 'resources' is a list of the items needed for crafting - only the first 4 will be used (total agent equip slots); multiple of the same item can in a tuple with the count second: ("itm_example", 2).
def spr_buy_item_triggers(item_id, pos_offset=(5,0,2), rotate=(0,0,0), use_string=None, tableau=None, resources=[], engineer=0, herding=0, tailoring=0, price_multiplier=None):
  buy_trigger = (ti_on_scene_prop_cancel_use,
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      (prop_instance_get_position, pos1, ":instance_id")])
  spr_apply_pos_offset(buy_trigger[1], pos_offset, rotate)
  if len(resources) > 0:
    buy_trigger[1].append((call_script, "script_cf_buy_sell_item_stockpile", ":agent_id", ":instance_id"))
  else:
    buy_trigger[1].append((call_script, "script_cf_buy_item", ":agent_id", ":instance_id"))
  craft_trigger = (ti_on_scene_prop_use, [])
  init_trigger = spr_item_init_trigger(item_id, use_string=use_string, tableau=tableau, stockpile=(len(resources) > 0), price_multiplier=price_multiplier)
  if len(resources) > 0:
    craft_trigger[1].extend([
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id")])
    resource_list = []
    for resource in resources:
      if isinstance(resource, tuple):
        for x in range(0, resource[1]):
          resource_list.append(resource[0])
      elif isinstance(resource, str):
        resource_list.append(resource)
      else:
        raise Exception("invalid resource entry", resource)
    pad_list(resource_list, value=-1, length=4)
    accepted_skills = [entry for entry in [
      ["skl_engineer", engineer],
      ["skl_tailoring", tailoring],
      ["skl_herding", herding]
      ] if entry[1] > 0]
    if len(accepted_skills) > 2:
      raise Exception("too many crafting skills specified")
    pad_list(accepted_skills, value=[-1, 0], length=2)
    operation_list = [call_script, "script_cf_craft_item_stockpile", ":agent_id", ":instance_id"]
    operation_list.extend(flatten_list(accepted_skills))
    operation_list.extend(resource_list[:4])
    craft_trigger[1].append(tuple(operation_list))
    average_craft_skill = accepted_skills[0][1]
    if accepted_skills[1][0] != -1 and accepted_skills[1][1] > 0:
      average_craft_skill = int(round((average_craft_skill + accepted_skills[1][1]) / 2.0))
    if average_craft_skill > 0:
      init_trigger[1].append((scene_prop_set_slot, ":instance_id", slot_scene_prop_average_craft_skill, min(max(average_craft_skill, 1), 10)))
    crafting_data.append([item_id, accepted_skills, resources, resource_list, average_craft_skill])
    init_trigger[1].extend([
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_resources_default_cost, lazy.add(
        lazy.price(resource_list[0]), lazy.price(resource_list[1]), lazy.price(resource_list[2]), lazy.price(resource_list[3]))),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_resource_refund_cost, -1),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_crafting_resource_1, resource_list[0]),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_crafting_resource_2, resource_list[1]),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_crafting_resource_3, resource_list[2]),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_crafting_resource_4, resource_list[3]),
      ])
  return [init_trigger, buy_trigger, craft_trigger]

# Export an item, removing it from the game world in exchange for money.
def spr_export_item_triggers(item_id, use_string="str_export", price_multiplier=None):
  return [spr_item_init_trigger(item_id, use_string=use_string, price_multiplier=price_multiplier),
    spr_call_script_use_trigger("script_cf_export_item")]

# Import an item from outside the game world, normally for an inflated price.
def spr_import_item_triggers(item_id, pos_offset=(5,0,2), rotate=(0,0,0), use_string="str_import", price_multiplier=500, check_script=None):
  buy_trigger = (ti_on_scene_prop_use,
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      (prop_instance_get_position, pos1, ":instance_id")])
  spr_apply_pos_offset(buy_trigger[1], pos_offset, rotate)
  buy_trigger[1].append((call_script, "script_cf_buy_item", ":agent_id", ":instance_id"))
  triggers = [spr_item_init_trigger(item_id, use_string=use_string, price_multiplier=price_multiplier), buy_trigger]
  if check_script is not None:
    triggers.append(spr_call_script_start_use_trigger(check_script))
  return triggers

# Stockpile a resource item: only allows buying and selling, with custom pricing rules.
def spr_stockpile_resource_triggers(item_id, use_string="str_stockpile"):
  return [spr_item_init_trigger(item_id, use_string=use_string, stockpile=True, resource_stock_count=True),
    spr_call_script_use_trigger("script_cf_use_resource_stockpile")]

# Gain gold directly after using.
def spr_gain_gold_triggers(gold_value, use_string="str_collect_reg1_gold"):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_gold_value, gold_value),
      ]),
    spr_call_script_use_trigger("script_cf_gain_gold")]

# Regain health in exchange for food points, after using. 'heal_pct' is the percentage healed, and 'min_health_pct' is the minimum health percentage required to rest.
def spr_rest_triggers(heal_pct, min_health_pct=30, horse=0, use_string="str_rest"):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      ]),
    (ti_on_scene_prop_start_use,
     [(store_trigger_param_1, ":agent_id"),
      (call_script, "script_cf_rest", ":agent_id", horse, 0, min_health_pct),
      ]),
    (ti_on_scene_prop_use,
     [(store_trigger_param_1, ":agent_id"),
      (call_script, "script_cf_rest", ":agent_id", horse, heal_pct, min_health_pct),
      ]),
    ]

# Clean blood from the user if they are not too badly wounded.
def spr_clean_blood_triggers():
  return [spr_call_script_use_trigger("script_cf_clean_blood")]

# Train as a different troop type, changing faction as well if owned by a different one.
# The 'mercenary' setting links the training station with the faction which started the mission owning the castle, to allow joining a faction that currently doesn't own any castles.
# The 'after_respawn' setting allows players to click the use button to change faction only, changing to the troop when after dying if it is judged to be worse.
def spr_change_troop_triggers(troop_id, cost=0, mercenary=False, after_respawn=False, use_string=None):
  init_trigger = (ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_troop_id, troop_id),
      ])
  if cost != 0:
    init_trigger[1].append((call_script, "script_scene_prop_get_gold_value", ":instance_id", -1, cost))
  if mercenary is True:
    init_trigger[1].append((scene_prop_set_slot, ":instance_id", slot_scene_prop_is_mercenary, 1))
  if use_string is not None:
    init_trigger[1].append((scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string))
  if after_respawn is True:
    cancel_trigger = spr_call_script_cancel_use_trigger("script_cf_change_faction_worse_respawn_troop")
  else:
    cancel_trigger = spr_call_script_cancel_use_trigger("script_cf_change_troop", 1)
  return [init_trigger, cancel_trigger, spr_call_script_use_trigger("script_cf_change_troop", 0)]

# Buy a banner with faction heraldry, for capturing castles.
# The 'mercenary' setting links with the faction which started the mission owning the castle, to allow capturing a castle with none currently owned.
def spr_buy_banner_triggers(banner_item_begin, mercenary=False, use_string="str_buy_banner_faction"):
  init_trigger = spr_item_init_trigger(banner_item_begin, use_string=use_string)
  if mercenary is True:
    init_trigger[1].append((scene_prop_set_slot, ":instance_id", slot_scene_prop_is_mercenary, 1))
  return [init_trigger, spr_call_script_use_trigger("script_cf_buy_banner")]

# Teleport to a linked door of the same scene prop type. 'pos_offset' specifies the relative position from each door that the character will be moved to.
def spr_teleport_door_triggers(pos_offset=(0,0,0), pickable=1):
  triggers = [spr_call_script_use_trigger("script_cf_use_teleport_door", pos_offset[0], pos_offset[1], pos_offset[2], pickable),
    [link_scene_prop, link_scene_prop_self]]
  if pickable == 1:
    triggers.append(spr_call_script_cancel_use_trigger("script_cf_lock_teleport_door"))
  return triggers

def spr_rotate_door_flags(use_time=1):
  return sokf_static_movement|sokf_destructible|spr_use_time(use_time)

# A rotating door, destructable and repairable with the resource class specified. The 'left' setting adjusts which way it will rotate, for matched left and right doors.
def spr_rotate_door_triggers(hit_points=1000, resource_class=item_class_wood, left=0):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (assign, ":hit_points", spr_check_hit_points(hit_points)),
      (prop_instance_get_variation_id_2, ":is_weak", ":instance_id"),
      (val_and, ":is_weak", 0x8),
      (try_begin),
        (eq, ":is_weak", 0x8),
        (val_div, ":hit_points", 2),
      (try_end),
      (scene_prop_set_hit_points, ":instance_id", ":hit_points"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, ":hit_points"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_next_resource_hp, ":hit_points"),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_door", ":instance_id", ":hit_damage", resource_class),
      ]),
    (ti_on_scene_prop_destroy, []),
    spr_call_script_use_trigger("script_cf_use_rotate_door", left),
    [init_scene_prop, "script_cf_init_rotate_door", left]]

def spr_rotate_door_no_hit_flags(use_time=1):
  return sokf_static_movement|spr_use_time(use_time)

# A rotating door that cannot be destroyed. The 'left' setting adjusts which way it will rotate, for matched left and right doors.
def spr_rotate_door_no_hit_triggers(left=0):
  return [spr_call_script_use_trigger("script_cf_use_rotate_door", left),
    [init_scene_prop, "script_cf_init_rotate_door", left]]

# A drawbridge winch, moving a linked scene prop of the 'target' kind.
# Each movement will rotate by 'step_size' in degrees for 'animation_time' in millseconds, for 'rotation_steps' iterations.
def spr_drawbridge_winch_triggers(target, rotation_steps=10, step_size=-8, animation_time=200):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_winch_lower"),
      ]),
    spr_call_script_use_trigger("script_cf_use_winch", rotation_steps+1, step_size, animation_time, winch_type_drawbridge),
    [link_scene_prop, target],
    [init_scene_prop, "script_cf_init_winch", rotation_steps, step_size, winch_type_drawbridge]]

# A drawbridge winch, moving a linked scene prop of the 'target' kind.
# Each movement will move up by 'step_size' for 'animation_time' in millseconds, for 'rotation_steps' iterations; moving down will happen in one step.
def spr_portcullis_winch_triggers(target, move_steps=5, step_size=100, animation_time=100):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_winch_drop"),
      ]),
    spr_call_script_use_trigger("script_cf_use_winch", move_steps+1, step_size, animation_time, winch_type_portcullis),
    [link_scene_prop, target],
    [init_scene_prop, "script_cf_init_winch", move_steps, step_size, winch_type_portcullis]]

# Winch for controlling a lift platform; two must be placed at each limit of the platform travel.
# Each movement will move up or down by 'step_size' for 'animation_time' in millseconds.
def spr_lift_platform_winch_triggers(step_size=100, animation_time=100):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_winch_lower"),
      ]),
    spr_call_script_use_trigger("script_cf_use_winch", -1, step_size, animation_time, winch_type_platform)]

# Lift platform, requiring two linked winch scene props.
def spr_lift_platform_triggers(winch):
  return [[link_scene_prop, winch, winch],
    [init_scene_prop, "script_cf_init_lift_platform"]]

# Winch for controlling a sliding door; controlling a linked scene prop of the 'target' kind.
def spr_sliding_door_winch_triggers(target, move_steps=1, step_size=100, animation_time=100):
  return [spr_call_script_use_trigger("script_cf_use_winch", move_steps+1, step_size, animation_time, winch_type_sliding_door),
    [link_scene_prop, target],
    [init_scene_prop, "script_cf_init_winch", move_steps, step_size, winch_type_sliding_door]]

# Carts attachable to characters or horses. Set 'horse' to 1 to allow attaching to any horse, or the horse item id for restricting to a specific type.
# The cart mesh should be oriented with the horse or agent position at the origin, and when detached it will be rotated by 'detach_rotation' and moved vertically by 'detach_offset'.
# The absolute value of 'access_distance' is used for the radius from the origin that will allow attaching, and moved forwards by that value (back if negative) is the center of the radius for accessing.
def spr_cart_triggers(horse=-1, detach_offset=0, detach_rotation=0, inventory_count=0, max_item_length=100, access_distance=100, use_string="str_attach"):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_required_horse, horse),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_position, detach_offset),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_rotation, detach_rotation),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_attached_to_agent, -1),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_inventory_count, spr_check_inventory_count(inventory_count)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_inventory_max_length, max_item_length),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_width, access_distance),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_collision_kind, -1),
      (call_script, "script_add_cart_to_list", ":instance_id"),
      ]),
    (ti_on_scene_prop_use,
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      (call_script, "script_cart_choose_action", ":agent_id", ":instance_id"),
      (call_script, "script_cf_use_cart", ":agent_id", ":instance_id", reg0),
      ]),
    ]

def spr_tree_flags():
  return sokf_static_movement|sokf_destructible

# Tree which will regrow after being cut down for wood. 'resource_imod' sets the mesh variation of branches and blocks.
# 'fell_hp' is the hit points when the tree will fall over and start producing blocks, and 'resource_hp' is the amount of hit damage needed per resource.
def spr_tree_triggers(full_hp=1000, fell_hp=500, resource_hp=100, hardness=1, resource_imod=0, regrow_interval=3600, use_string="str_cut_down"):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(full_hp, fell_hp)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_next_resource_hp, full_hp - resource_hp),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, full_hp),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_tree", ":instance_id", ":hit_damage", spr_check_hit_points(fell_hp), resource_hp, hardness, resource_imod, regrow_interval),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_animation_finished,
     [(store_trigger_param_1, ":instance_id"),
      (prop_instance_clear_attached_missiles, ":instance_id"),
      (call_script, "script_cf_resource_animation_finished", ":instance_id", resource_hp),
      ]),
    (ti_on_scene_prop_use, [])]

# A tree that produces fruit without any character involvement. Passes parameters on to the spr_tree_triggers function.
def spr_fruit_tree_triggers(fruit, count, height, width, fruiting_interval=3600, **args):
  triggers = spr_tree_triggers(**args)
  assert triggers[0][0] == ti_on_scene_prop_init
  triggers[0][1].extend([
    (scene_prop_set_slot, ":instance_id", slot_scene_prop_regrow_script, "script_regrow_fruit_tree"),
    (scene_prop_set_slot, ":instance_id", slot_scene_prop_resource_item_id, fruit),
    (scene_prop_set_slot, ":instance_id", slot_scene_prop_fruit_count, count),
    (scene_prop_set_slot, ":instance_id", slot_scene_prop_height, height),
    (scene_prop_set_slot, ":instance_id", slot_scene_prop_width, width),
    (scene_prop_set_slot, ":instance_id", slot_scene_prop_fruiting_interval, fruiting_interval),
    ])
  return triggers


# Plant that can be hit to harvest resources, with optional tool class, skill, and attack direction range for optimum damage.
# The lower digit of 'attack_range' is the beginning direction of agent_get_action_dir, and the upper digit is how many consecutive directions to include. For example, 21 is left and right.
# If 'effect_script' is set to a script id, it will be called for the effect when a resource is produced.
def spr_hit_plant_triggers(resource_item, full_hp=1000, resource_hp=200, hardness=1, tool_class=-1, skill=-1, attack_range=21, spawn_on_ground=1, regrow_interval=600, use_string="str_harvest", effect_script=-1):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(full_hp)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_next_resource_hp, full_hp - resource_hp),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, full_hp),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_regrowing_resource", ":instance_id", ":hit_damage", resource_hp, resource_item, hardness, tool_class, skill, attack_range, spawn_on_ground, regrow_interval, effect_script, 0),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_animation_finished,
     [(store_trigger_param_1, ":instance_id"),
      (call_script, "script_cf_resource_animation_finished", ":instance_id", resource_hp),
      ]),
    (ti_on_scene_prop_use, [])]

# Plant that can be used by holding that control to harvest, decreasing the hit points by 'resource_hp' each time, and playing 'sound' if set.
def spr_use_plant_triggers(resource_item, full_hp=1000, resource_hp=200, regrow_interval=600, use_string="str_harvest", sound=-1):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(full_hp)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, full_hp),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_damage_resource", ":instance_id", ":hit_damage", regrow_interval),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_animation_finished,
     [(store_trigger_param_1, ":instance_id"),
      (call_script, "script_cf_resource_animation_finished", ":instance_id", 0),
      ]),
    (ti_on_scene_prop_use,
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      (call_script, "script_cf_use_resource", ":agent_id", ":instance_id", resource_item, resource_hp, regrow_interval, sound),
      ]),
    ]

def spr_resource_flags():
  return sokf_static_movement|sokf_destructible|sokf_missiles_not_attached

def spr_field_flags():
  return sokf_destructible|sokf_missiles_not_attached

# A field that is planted with 'plant_item' to produce 'resource_item'. 'plant_spr' is the scene prop type for the growing plants; set 'height' to the height of that mesh.
def spr_hit_field_triggers(resource_item, plant_item, plant_spr, height=200, full_hp=1000, resource_hp=200, tool_class=-1, regrow_interval=600, use_string="str_harvest"):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_height, height),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(full_hp)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, full_hp),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_field", ":instance_id", ":hit_damage", resource_hp, resource_item, plant_item, tool_class, regrow_interval),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_use, []),
    [init_scene_prop, "script_cf_setup_field", plant_spr]]

# The growing plants scene prop associated with a field prop, allowing adjustment of the optimum number of seeds and water buckets for the best harvest.
def spr_field_plant_triggers(seeds=4, water=2):
  return [(ti_on_scene_prop_animation_finished,
     [(store_trigger_param_1, ":instance_id"),
      (call_script, "script_cf_field_animation_finished", ":instance_id", seeds, water),
      ])]

# A vine that needs to be pruned with a knife before producing between 'resources' and half that amount of 'resource_item', if not damaged without the correct tool or skill.
# 'length' should be set to the length of the vine mesh for spawning resources, and 'height' should be set to the height above the mesh origin to spawn them.
def spr_hit_vine_triggers(resource_item, resources=1, length=300, height=150, full_hp=1000, tool_class=-1, regrow_interval=60, use_string="str_prune"):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_resource_item_id, resource_item),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_seeds, resources),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_length, length),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_height, height),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(full_hp)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, full_hp),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_next_resource_hp, full_hp),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_regrow_script, "script_regrow_vine"),
     ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_vine", ":instance_id", ":hit_damage", tool_class, regrow_interval),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_use, [])]

# A mine that produces 'resource_item' when hit with a mining tool, every 'resource_hp' plus a random extra amount from 0 to 'random_hp'; the maximum hit points is adjustable in the scene editor.
# The 'hardness' value makes attacks do less damage, making mining resources slower.
def spr_hit_mine_triggers(resource_item, resource_hp=100, random_hp=0, hardness=1, regrow_interval=14400, use_string="str_mine"):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      (call_script, "script_initialize_resource_hit_points", ":instance_id", resource_hp),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_regrowing_resource", ":instance_id", ":hit_damage", resource_hp, resource_item, hardness, item_class_mining, "skl_labouring", 21, 0, regrow_interval, "script_hit_iron_mine_effect", random_hp),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_animation_finished,
     [(store_trigger_param_1, ":instance_id"),
      (call_script, "script_cf_resource_animation_finished", ":instance_id", resource_hp),
      ]),
    (ti_on_scene_prop_use, [])]

# Process resources into different items, by calling the script 'script_name'.
def spr_process_resource_triggers(script_name, use_string):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      ]),
    (ti_on_scene_prop_start_use,
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      (store_mission_timer_a, ":time"),
      (neg|scene_prop_slot_ge, ":instance_id", slot_scene_prop_stock_count_update_time, ":time"),
      (call_script, script_name, ":agent_id", ":instance_id", 0),
      (val_add, ":time", 5),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_stock_count_update_time, ":time"),
      ]),
    (ti_on_scene_prop_use,
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      (call_script, script_name, ":agent_id", ":instance_id", 1),
      ]),
    ]

# Moveable ship. 'length' is the distance forwards and backwards from the origin that terrain collisions will be tested at, and the distance back required to use the rudder.
# 'width' is the range along the sides necessary to be within to climb the ship sides. 'height' is the distance from the origin to the bottom of the hull for terrain collision detection.
# 'speed' is the maximum forward speed setting the ship sails can be set to with the necessary sailing skill.
# 'sail' is the sail scene prop when moving, 'sail_off' is the sail scene prop when stopped. 'ramp' and 'hold' are optional linked props.
# 'collision' is the prop with a very simple collision mesh used for detecting collisions between ships.
def spr_ship_triggers(hit_points=1000, length=1000, width=200, height=100, speed=5, sail=-1, sail_off=-1, ramp=-1, hold=-1, collision="pw_ship_a_cd"):
  if speed < 1 or speed > ship_forwards_maximum:
    raise Exception("Ship speed must be between 1 and %d" % ship_forwards_maximum)
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(hit_points)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_next_resource_hp, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_length, length),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_width, width),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_height, height),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_collision_kind, spr_tag(collision)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_speed_limit, speed + 1),
      (neg|multiplayer_is_server),
      (call_script, "script_setup_ship", ":instance_id"),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),

      (assign, ":is_little_boat", 0),
      (try_begin),
        (eq, length, 290),
        (assign, ":is_little_boat", 1),
      (try_end),

      (call_script, "script_cf_damage_ship", ":instance_id", ":hit_damage", hit_points, 0, ":is_little_boat"),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_animation_finished,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_slot_eq, ":instance_id", slot_scene_prop_state, scene_prop_state_regenerating),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_state, scene_prop_state_active),
      ]),
    [init_scene_prop, "script_setup_ship", spr_tag(sail), spr_tag(sail_off), spr_tag(ramp), spr_tag(hold)]]

def spr_ship_ramp_triggers():
  return [spr_call_script_use_trigger("script_use_ship_ramp")]

# Winchable ferry boat, requiring two 'platform' props at each end of the movement range, and a 'winch' scene prop for movement on the boat.
# 'length' is the dimension of the boat in the direction of travel, used to move close to the platforms.
# 'winch_height' is the height above the platform that the winch prop is centred at. 'move distance' is the distance moved each iteration.
def spr_ferry_triggers(platform, winch, length, winch_height, move_distance=500):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_length, length),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_height, winch_height),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_speed_limit, move_distance),
      ]),
    [init_scene_prop, "script_setup_ferry", spr_tag(winch)],
    [link_scene_prop, platform, platform]]

def spr_ferry_winch_triggers(is_platform=0):
  return [spr_call_script_use_trigger("script_cf_use_ferry_winch", is_platform)]

def spr_structure_flags():
  return sokf_static_movement|sokf_destructible

# Destructable and rebuildable bridge: requires linking with two 'footing' scene props for rebuilding on either side.
def spr_bridge_triggers(footing, hit_points=1000):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(hit_points)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_next_resource_hp, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_destructible"),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_bridge", ":instance_id", ":hit_damage", 0),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_use, []),
    [link_scene_prop, footing, footing]]

def spr_build_flags():
  return sokf_destructible

# Footings for rebuilding after the bridge is totally destroyed.
def spr_bridge_footing_triggers():
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", 1000),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_show_linked_hit_points, 1),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_build"),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_bridge_footing", ":instance_id", ":hit_damage"),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_use, [])]

def spr_ladder_flags():
  return sokf_type_ladder|sokf_static_movement|sokf_destructible

# Buildable walls, also used for ladders: requires a 'build' scene prop for construction when totally destroyed. 'height' should be set to the height of the mesh.
# 'no_move_physics' disables walking on the prop until the construction animation is completed.
def spr_wall_triggers(build, hit_points=1000, height=1000, no_move_physics=False):
  triggers = [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(hit_points)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_height, height),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_destructible"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_no_move_physics, int(no_move_physics))
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_wall", ":instance_id", ":hit_damage", 0),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_use, []),
    [link_scene_prop, build],
    [init_scene_prop, "script_cf_init_wall"]]
  if no_move_physics:
    triggers.append((ti_on_scene_prop_animation_finished,
       [(store_trigger_param_1, ":instance_id"),
        (prop_instance_enable_physics, ":instance_id", 1),
        ]))
  return triggers

# Building station for walls.
def spr_build_wall_triggers():
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", 1000),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_show_linked_hit_points, 1),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_build"),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_build_wall", ":instance_id", ":hit_damage"),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_use, [])]

# Construction box which disappears when built, allowing access to stations hidden inside.
def spr_construction_box_triggers(resource_class=item_class_wood):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_build"),
      (call_script, "script_initialize_resource_hit_points", ":instance_id", -1),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_state, scene_prop_state_destroyed),
      (scene_prop_set_hit_points, ":instance_id", 1),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_construction_box", ":instance_id", ":hit_damage", resource_class),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_use, [])]

# Point to capture castles using a faction banner.
def spr_capture_castle_triggers():
  return [spr_call_script_start_use_trigger("script_cf_use_capture_point", 0),
    (ti_on_scene_prop_cancel_use,
     [(store_trigger_param_2, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_disabled, 0),
      ]),
    spr_call_script_use_trigger("script_cf_use_capture_point", 1)]

def spr_chest_flags(use_time=1):
  return sokf_destructible|spr_use_time(max(use_time, 1))

# Money chest that can be linked with a castle to store tax automatically gathered, and allow the lord to control the access.
# A 'probability' of the default 100 will give 1% chance of successful lock picking per looting skill level, which can be increased up to 10000 for guaranteed success.
def spr_castle_money_chest_triggers(use_string="str_gold_reg2", hit_points=1000, probability=100):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(hit_points)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_next_resource_hp, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      (neq, "$g_game_type", "mt_no_money"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_stock_count_update_time, -1),
      (prop_instance_get_variation_id_2, ":initial_gold_value", ":instance_id"),
      (val_mul, ":initial_gold_value", 1000),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_stock_count, ":initial_gold_value"),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_chest", ":instance_id", ":hit_damage", hit_points),
      ]),
    (ti_on_scene_prop_destroy, []),
    spr_call_script_cancel_use_trigger("script_cf_pick_chest_lock", 0),
    spr_call_script_use_trigger("script_cf_pick_chest_lock", probability)]

# Item storage chest that can be linked with a castle to allow the lord to control the access.
# A 'probability' of the default 100 will give 1% chance of successful lock picking per looting skill level, which can be increased up to 10000 for guaranteed success.
def spr_item_chest_triggers(inventory_count=6, max_item_length=100, use_string="str_access", hit_points=1000, probability=100):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", spr_check_hit_points(hit_points)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_full_hit_points, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_next_resource_hp, hit_points),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_inventory_count, spr_check_inventory_count(inventory_count)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_inventory_max_length, max_item_length),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":hit_damage"),
      (call_script, "script_cf_hit_chest", ":instance_id", ":hit_damage", hit_points),
      ]),
    (ti_on_scene_prop_destroy, []),
    spr_call_script_cancel_use_trigger("script_cf_pick_chest_lock", 0),
    spr_call_script_use_trigger("script_cf_use_inventory", probability)]

# Item storage without any lock.
def spr_item_storage_triggers(inventory_count=6, max_item_length=100, use_string="str_access"):
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_inventory_count, spr_check_inventory_count(inventory_count)),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_inventory_max_length, max_item_length),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, use_string),
      ]),
    spr_call_script_use_trigger("script_cf_use_inventory", 0)]

# A fire place that can be stocked with wood and visibly lit on fire.
def spr_fire_place_triggers():
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_hit_points, ":instance_id", 1000),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_burn"),
      (call_script, "script_cf_init_fire_place", ":instance_id"),
      ]),
    (ti_on_scene_prop_hit,
     [(store_trigger_param_1, ":instance_id"),
      (call_script, "script_cf_hit_fire_place", ":instance_id"),
      ]),
    (ti_on_scene_prop_destroy, []),
    (ti_on_scene_prop_use, [])]

# A well for gathering water using buckets.
def spr_well_triggers():
  return [(ti_on_scene_prop_use,
     [(store_trigger_param_1, ":agent_id"),
      (agent_get_wielded_item, ":wielded_item_id", ":agent_id", 0),
      (eq, ":wielded_item_id", "itm_bucket"),
      (call_script, "script_cf_agent_consume_item", ":agent_id", "itm_bucket", 1),
      (agent_equip_item, ":agent_id", "itm_water_bucket"),
      (agent_set_wielded_item, ":agent_id", "itm_water_bucket"),
      ])]

# A heap to destroy unwanted items held or in a cart.
def spr_destroy_heap_triggers():
  return [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_use_string, "str_destroy_s1"),
      ]),
    spr_call_script_use_trigger("script_cf_use_destroy_heap")]

scene_props = [
  ("invalid_object",0,"question_mark","0", []),
  ("inventory",sokf_type_container|sokf_place_at_origin,"package","bobaggage", []),
  ("empty", 0, "0", "0", []),
  ("chest_a",sokf_type_container,"chest_gothic","bochest_gothic", []),
  ("container_small_chest",sokf_type_container,"package","bobaggage", []),
  ("container_chest_b",sokf_type_container,"chest_b","bo_chest_b", []),
  ("container_chest_c",sokf_type_container,"chest_c","bo_chest_c", []),
  ("player_chest",sokf_type_container,"player_chest","bo_player_chest", []),
  ("locked_player_chest",0,"player_chest","bo_player_chest", []),

  ("light_sun",sokf_invisible,"light_sphere","0",
   [(ti_on_scene_prop_init,
     [(neg|is_currently_night),
      (store_trigger_param_1, ":prop_instance_no"),
      (set_fixed_point_multiplier, 100),
      (prop_instance_get_scale, pos5, ":prop_instance_no"),
      (position_get_scale_x, ":scale", pos5),
      (store_time_of_day,reg(12)),
      (try_begin),
        (is_between,reg(12),5,20),
        (store_mul, ":red", 5 * 200, ":scale"),
        (store_mul, ":green", 5 * 193, ":scale"),
        (store_mul, ":blue", 5 * 180, ":scale"),
      (else_try),
        (store_mul, ":red", 5 * 90, ":scale"),
        (store_mul, ":green", 5 * 115, ":scale"),
        (store_mul, ":blue", 5 * 150, ":scale"),
      (try_end),
      (val_div, ":red", 100),
      (val_div, ":green", 100),
      (val_div, ":blue", 100),
      (set_current_color,":red", ":green", ":blue"),
      (set_position_delta,0,0,0),
      (add_point_light_to_entity, 0, 0),
      ]),
    ]),
  ("light",sokf_invisible,"light_sphere","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":prop_instance_no"),
      (set_fixed_point_multiplier, 100),
      (prop_instance_get_scale, pos5, ":prop_instance_no"),
      (position_get_scale_x, ":scale", pos5),
      (store_mul, ":red", 3 * 200, ":scale"),
      (store_mul, ":green", 3 * 145, ":scale"),
      (store_mul, ":blue", 3 * 45, ":scale"),
      (val_div, ":red", 100),
      (val_div, ":green", 100),
      (val_div, ":blue", 100),
      (set_current_color,":red", ":green", ":blue"),
      (set_position_delta,0,0,0),
      (add_point_light_to_entity, 10, 30),
      ]),
    ]),
  ("light_red",sokf_invisible,"light_sphere","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":prop_instance_no"),
      (set_fixed_point_multiplier, 100),
      (prop_instance_get_scale, pos5, ":prop_instance_no"),
      (position_get_scale_x, ":scale", pos5),
      (store_mul, ":red", 2 * 170, ":scale"),
      (store_mul, ":green", 2 * 100, ":scale"),
      (store_mul, ":blue", 2 * 30, ":scale"),
      (val_div, ":red", 100),
      (val_div, ":green", 100),
      (val_div, ":blue", 100),
      (set_current_color,":red", ":green", ":blue"),
      (set_position_delta,0,0,0),
      (add_point_light_to_entity, 20, 30),
      ]),
    ]),
  ("light_night",sokf_invisible,"light_sphere","0",
   [(ti_on_scene_prop_init,
     [(is_currently_night, 0),
      (store_trigger_param_1, ":prop_instance_no"),
      (set_fixed_point_multiplier, 100),
      (prop_instance_get_scale, pos5, ":prop_instance_no"),
      (position_get_scale_x, ":scale", pos5),
      (store_mul, ":red", 3 * 160, ":scale"),
      (store_mul, ":green", 3 * 145, ":scale"),
      (store_mul, ":blue", 3 * 100, ":scale"),
      (val_div, ":red", 100),
      (val_div, ":green", 100),
      (val_div, ":blue", 100),
      (set_current_color,":red", ":green", ":blue"),
      (set_position_delta,0,0,0),
      (add_point_light_to_entity, 10, 30),
      ]),
    ]),
  ("torch",0,"torch_a","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (prop_instance_play_sound, ":instance_id", "snd_fire_loop"),
      (set_position_delta,0,-35,48),
      (particle_system_add_new, "psys_torch_fire"),
      (particle_system_add_new, "psys_torch_smoke"),
      (particle_system_add_new, "psys_torch_fire_sparks"),
      (set_position_delta,0,-35,56),
      (particle_system_add_new, "psys_fire_glow_1"),
      (get_trigger_object_position, pos2),
      (set_position_delta,0,0,0),
      (position_move_y, pos2, -35),
      (position_move_z, pos2, 55),
      (particle_system_burst, "psys_fire_glow_fixed", pos2, 1),
      ]),
    ]),
  ("torch_night",0,"torch_a","0",
   [(ti_on_scene_prop_init,
     [(is_currently_night, 0),
      (store_trigger_param_1, ":instance_id"),
      (prop_instance_play_sound, ":instance_id", "snd_fire_loop"),
      (set_position_delta,0,-35,48),
      (particle_system_add_new, "psys_torch_fire"),
      (particle_system_add_new, "psys_torch_smoke"),
      (particle_system_add_new, "psys_torch_fire_sparks"),
      (set_position_delta,0,-35,56),
      (particle_system_add_new, "psys_fire_glow_1"),
      (particle_system_emit, "psys_fire_glow_1",9000000),
      ]),
    ]),

  ("barrier_20m",sokf_invisible|sokf_type_barrier,"barrier_20m","bo_barrier_20m", []),
  ("barrier_16m",sokf_invisible|sokf_type_barrier,"barrier_16m","bo_barrier_16m", []),
  ("barrier_8m" ,sokf_invisible|sokf_type_barrier,"barrier_8m" ,"bo_barrier_8m" , []),
  ("barrier_4m" ,sokf_invisible|sokf_type_barrier,"barrier_4m" ,"bo_barrier_4m" , []),
  ("barrier_2m" ,sokf_invisible|sokf_type_barrier,"barrier_2m" ,"bo_barrier_2m" , []),

  ("exit_4m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_4m" ,"bo_barrier_4m" , []),
  ("exit_8m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_8m" ,"bo_barrier_8m" , []),
  ("exit_16m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_16m" ,"bo_barrier_16m" , []),

  ("ai_limiter_2m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_2m" ,"bo_barrier_2m" , []),
  ("ai_limiter_4m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_4m" ,"bo_barrier_4m" , []),
  ("ai_limiter_8m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_8m" ,"bo_barrier_8m" , []),
  ("ai_limiter_16m",sokf_invisible|sokf_type_ai_limiter,"barrier_16m","bo_barrier_16m", []),
  ("shield",sokf_dynamic,"0","boshield", []),
  ("shelves",0,"shelves","boshelves", []),
  ("table_tavern",0,"table_tavern","botable_tavern", []),
  ("table_castle_a",0,"table_castle_a","bo_table_castle_a", []),
  ("chair_castle_a",0,"chair_castle_a","bo_chair_castle_a", []),

  ("pillow_a",0,"pillow_a","bo_pillow", []),
  ("pillow_b",0,"pillow_b","bo_pillow", []),
  ("pillow_c",0,"pillow_c","0", []),

  ("interior_castle_g_square_keep_b",0,"interior_castle_g_square_keep_b","bo_interior_castle_g_square_keep_b", []),

  ("carpet_with_pillows_a",0,"carpet_with_pillows_a","bo_carpet_with_pillows", []),
  ("carpet_with_pillows_b",0,"carpet_with_pillows_b","bo_carpet_with_pillows", []),
  ("table_round_a",0,"table_round_a","bo_table_round_a", []),
  ("table_round_b",0,"table_round_b","bo_table_round_b", []),
  ("fireplace_b",0,"fireplace_b","bo_fireplace_b", []),
  ("fireplace_c",0,"fireplace_c","bo_fireplace_c", []),

  ("sofa_a",0,"sofa_a","bo_sofa", []),
  ("sofa_b",0,"sofa_b","bo_sofa", []),
  ("ewer_a",0,"ewer_a","bo_ewer_a", []),
  ("end_table_a",0,"end_table_a","bo_end_table_a", []),

  ("fake_houses_steppe_a",0,"fake_houses_steppe_a","0", []),
  ("fake_houses_steppe_b",0,"fake_houses_steppe_b","0", []),
  ("fake_houses_steppe_c",0,"fake_houses_steppe_c","0", []),

  ("boat_destroy",0,"boat_destroy","bo_boat_destroy", []),
  ("destroy_house_a",0,"destroy_house_a","bo_destroy_house_a", []),
  ("destroy_house_b",0,"destroy_house_b","bo_destroy_house_b", []),
  ("destroy_house_c",0,"destroy_house_c","bo_destroy_house_c", []),
  ("destroy_heap",0,"destroy_heap","bo_destroy_heap", []),
  ("destroy_castle_a",0,"destroy_castle_a","bo_destroy_castle_a", []),
  ("destroy_castle_b",0,"destroy_castle_b","bo_destroy_castle_b", []),
  ("destroy_castle_c",0,"destroy_castle_c","bo_destroy_castle_c", []),
  ("destroy_castle_d",0,"destroy_castle_d","bo_destroy_castle_d", []),
  ("destroy_windmill",0,"destroy_windmill","bo_destroy_windmill", []),
  ("destroy_tree_a",0,"destroy_tree_a","bo_destroy_tree_a", []),
  ("destroy_tree_b",0,"destroy_tree_b","bo_destroy_tree_b", []),
  ("destroy_bridge_a",0,"destroy_bridge_a","bo_destroy_bridge_a", []),
  ("destroy_bridge_b",0,"destroy_bridge_b","bo_destroy_bridge_b", []),

  ("catapult",0,"Catapult","bo_Catapult", []),
  ("catapult_destructible",sokf_moveable|sokf_destructible,"Catapult","bo_Catapult", []),

  ("broom",0,"broom","0", []),
  ("garlic",0,"garlic","0", []),
  ("garlic_b",0,"garlic_b","0", []),

  ("destroy_a",0,"destroy_a","0", []),
  ("destroy_b",0,"destroy_b","0", []),

  ("bridge_wooden",0,"bridge_wooden","bo_bridge_wooden", []),
  ("bridge_wooden_snowy",0,"bridge_wooden_snowy","bo_bridge_wooden", []),

  ("grave_a",0,"grave_a","bo_grave_a", []),

  ("village_house_e",0,"village_house_e","bo_village_house_e", []),
  ("village_house_f",0,"village_house_f","bo_village_house_f", []),
  ("village_house_g",0,"village_house_g","bo_village_house_g", []),
  ("village_house_h",0,"village_house_h","bo_village_house_h", []),
  ("village_house_i",0,"village_house_i","bo_village_house_i", []),
  ("village_house_j",0,"village_house_j","bo_village_house_j", []),
  ("village_wall_a",0,"village_wall_a","bo_village_wall_a", []),
  ("village_wall_b",0,"village_wall_b","bo_village_wall_b", []),

  ("village_snowy_house_a",0,"village_snowy_house_a","bo_village_snowy_house_a", []),
  ("village_snowy_house_b",0,"village_snowy_house_b","bo_village_snowy_house_b", []),
  ("village_snowy_house_c",0,"village_snowy_house_c","bo_village_snowy_house_c", []),
  ("village_snowy_house_d",0,"village_snowy_house_d","bo_village_snowy_house_d", []),
  ("village_snowy_house_e",0,"village_snowy_house_e","bo_village_snowy_house_e", []),
  ("village_snowy_house_f",0,"village_snowy_house_f","bo_village_snowy_house_f", []),

  ("town_house_steppe_a",0,"town_house_steppe_a","bo_town_house_steppe_a", []),
  ("town_house_steppe_b",0,"town_house_steppe_b","bo_town_house_steppe_b", []),
  ("town_house_steppe_c",0,"town_house_steppe_c","bo_town_house_steppe_c", []),
  ("town_house_steppe_d",0,"town_house_steppe_d","bo_town_house_steppe_d", []),
  ("town_house_steppe_e",0,"town_house_steppe_e","bo_town_house_steppe_e", []),
  ("town_house_steppe_f",0,"town_house_steppe_f","bo_town_house_steppe_f", []),
  ("town_house_steppe_g",0,"town_house_steppe_g","bo_town_house_steppe_g", []),
  ("town_house_steppe_h",0,"town_house_steppe_h","bo_town_house_steppe_h", []),
  ("town_house_steppe_i",0,"town_house_steppe_i","bo_town_house_steppe_i", []),

  ("carpet_a",0,"carpet_a","0", []),
  ("carpet_b",0,"carpet_b","0", []),
  ("carpet_c",0,"carpet_c","0", []),
  ("carpet_d",0,"carpet_d","0", []),
  ("carpet_e",0,"carpet_e","0", []),
  ("carpet_f",0,"carpet_f","0", []),

  ("awning_a",0,"awning_a","bo_awning", []),
  ("awning_b",0,"awning_b","bo_awning", []),
  ("awning_c",0,"awning_c","bo_awning", []),
  ("awning_long",0,"awning_long","bo_awning_long", []),
  ("awning_long_b",0,"awning_long_b","bo_awning_long", []),
  ("awning_d",0,"awning_d","bo_awning_d", []),

  ("ship",0,"ship","bo_ship", []),

  ("ship_b",0,"ship_b","bo_ship_b", []),
  ("ship_c",0,"ship_c","bo_ship_c", []),

  ("ship_d",0,"ship_d","bo_ship_d", []),

  ("snowy_barrel_a",0,"snowy_barrel_a","bo_snowy_barrel_a", []),
  ("snowy_fence",0,"snowy_fence","bo_snowy_fence", []),
  ("snowy_wood_heap",0,"snowy_wood_heap","bo_snowy_wood_heap", []),

  ("village_snowy_stable_a",0,"village_snowy_stable_a","bo_village_snowy_stable_a", []),

  ("village_straw_house_a",0,"village_straw_house_a","bo_village_straw_house_a", []),
  ("village_stable_a",0,"village_stable_a","bo_village_stable_a", []),
  ("village_shed_a",0,"village_shed_a","bo_village_shed_a", []),
  ("village_shed_b",0,"village_shed_b","bo_village_shed_b", []),

  ("dungeon_door_cell_a",0,"dungeon_door_cell_a","bo_dungeon_door_cell_a", []),
  ("dungeon_door_cell_b",0,"dungeon_door_cell_b","bo_dungeon_door_cell_b", []),
  ("dungeon_door_entry_a",0,"dungeon_door_entry_a","bo_dungeon_door_entry_a", []),
  ("dungeon_door_entry_b",0,"dungeon_door_entry_b","bo_dungeon_door_entry_a", []),
  ("dungeon_door_entry_c",0,"dungeon_door_entry_c","bo_dungeon_door_entry_a", []),
  ("dungeon_door_direction_a",0,"dungeon_door_direction_a","bo_dungeon_door_direction_a", []),
  ("dungeon_door_direction_b",0,"dungeon_door_direction_b","bo_dungeon_door_direction_a", []),
  ("dungeon_door_stairs_a",0,"dungeon_door_stairs_a","bo_dungeon_door_stairs_a", []),
  ("dungeon_door_stairs_b",0,"dungeon_door_stairs_b","bo_dungeon_door_stairs_a", []),
  ("dungeon_bed_a",0,"dungeon_bed_a","0", []),
  ("dungeon_bed_b",0,"dungeon_bed_b","bo_dungeon_bed_b", []),
  ("torture_tool_a",0,"torture_tool_a","bo_torture_tool_a", []),
  ("torture_tool_b",0,"torture_tool_b","0", []),
  ("torture_tool_c",0,"torture_tool_c","bo_torture_tool_c", []),
  ("skeleton_head",0,"skeleton_head","0", []),
  ("skeleton_bone",0,"skeleton_bone","0", []),
  ("skeleton_a",0,"skeleton_a","bo_skeleton_a", []),
  ("dungeon_stairs_a",sokf_type_ladder,"dungeon_stairs_a","bo_dungeon_stairs_a", []),
  ("dungeon_stairs_b",sokf_type_ladder,"dungeon_stairs_b","bo_dungeon_stairs_a", []),
  ("dungeon_torture_room_a",0,"dungeon_torture_room_a","bo_dungeon_torture_room_a", []),
  ("dungeon_entry_a",0,"dungeon_entry_a","bo_dungeon_entry_a", []),
  ("dungeon_entry_b",0,"dungeon_entry_b","bo_dungeon_entry_b", []),
  ("dungeon_entry_c",0,"dungeon_entry_c","bo_dungeon_entry_c", []),
  ("dungeon_cell_a",0,"dungeon_cell_a","bo_dungeon_cell_a", []),
  ("dungeon_cell_b",0,"dungeon_cell_b","bo_dungeon_cell_b", []),
  ("dungeon_cell_c",0,"dungeon_cell_c_open","bo_dungeon_cell_c_open", []),
  ("dungeon_corridor_a",0,"dungeon_corridor_a","bo_dungeon_corridor_a", []),
  ("dungeon_corridor_b",0,"dungeon_corridor_b","bo_dungeon_corridor_b", []),
  ("dungeon_corridor_c",0,"dungeon_corridor_c","bo_dungeon_corridor_a", []),
  ("dungeon_corridor_d",0,"dungeon_corridor_d","bo_dungeon_corridor_b", []),
  ("dungeon_direction_a",0,"dungeon_direction_a","bo_dungeon_direction_a", []),
  ("dungeon_direction_b",0,"dungeon_direction_b","bo_dungeon_direction_a", []),
  ("dungeon_room_a",0,"dungeon_room_a","bo_dungeon_room_a", []),
  ("dungeon_tower_stairs_a",sokf_type_ladder,"dungeon_tower_stairs_a","bo_dungeon_tower_stairs_a", []),
  ("dungeon_tower_cell_a",0,"dungeon_tower_cell_a","bo_dungeon_tower_cell_a", []),
  ("tunnel_a",0,"tunnel_a","bo_tunnel_a", []),
  ("tunnel_salt",0,"tunnel_salt","bo_tunnel_salt", []),
  ("salt_a",0,"salt_a","bo_salt_a", []),

  ("door_destructible",sokf_moveable|sokf_destructible|spr_use_time(2),"tutorial_door_a","bo_tutorial_door_a", []),

  ("tutorial_door_a",sokf_moveable,"tutorial_door_a","bo_tutorial_door_a", []),
  ("tutorial_door_b",sokf_moveable,"tutorial_door_b","bo_tutorial_door_b", []),

  ("tutorial_flag_yellow",sokf_moveable|sokf_face_player,"tutorial_flag_yellow","0", []),
  ("tutorial_flag_red",sokf_moveable|sokf_face_player,"tutorial_flag_red","0", []),
  ("tutorial_flag_blue",sokf_moveable|sokf_face_player,"tutorial_flag_blue","0", []),

  ("interior_prison_a",0,"interior_prison_a","bo_interior_prison_a", []),
  ("interior_prison_b",0,"interior_prison_b","bo_interior_prison_b", []),
  ("interior_prison_cell_a",0,"interior_prison_cell_a","bo_interior_prison_cell_a", []),
  ("interior_prison_d",0,"interior_prison_d","bo_interior_prison_d", []),

  ("arena_archery_target_a",0,"arena_archery_target_a","bo_arena_archery_target_a", []),
  ("archery_butt_a",0,"archery_butt","bo_archery_butt", []),
  ("archery_target_with_hit_a",0,"arena_archery_target_a","bo_arena_archery_target_a", []),
  ("dummy_a",sokf_destructible|sokf_moveable,"arena_archery_target_b","bo_arena_archery_target_b", []),

  ("band_a",0,"band_a","0", []),
  ("arena_sign",0,"arena_arms","0", []),

  ("castle_h_battlement_a",0,"castle_h_battlement_a","bo_castle_h_battlement_a", []),
  ("castle_h_battlement_b",0,"castle_h_battlement_b","bo_castle_h_battlement_b", []),
  ("castle_h_battlement_c",0,"castle_h_battlement_c","bo_castle_h_battlement_c", []),
  ("castle_h_battlement_a2",0,"castle_h_battlement_a2","bo_castle_h_battlement_a2", []),
  ("castle_h_battlement_b2",0,"castle_h_battlement_b2","bo_castle_h_battlement_b2", []),
  ("castle_h_corner_a",0,"castle_h_corner_a","bo_castle_h_corner_a", []),
  ("castle_h_corner_c",0,"castle_h_corner_c","bo_castle_h_corner_c", []),
  ("castle_h_stairs_a",sokf_type_ladder,"castle_h_stairs_a","bo_castle_h_stairs_a", []),
  ("castle_h_stairs_b",0,"castle_h_stairs_b","bo_castle_h_stairs_b", []),
  ("castle_h_gatehouse_a",0,"castle_h_gatehouse_a","bo_castle_h_gatehouse_a", []),
  ("castle_h_keep_a",0,"castle_h_keep_a","bo_castle_h_keep_a", []),
  ("castle_h_keep_b",0,"castle_h_keep_b","bo_castle_h_keep_b", []),
  ("castle_h_house_a",0,"castle_h_house_a","bo_castle_h_house_a", []),
  ("castle_h_house_b",0,"castle_h_house_b","bo_castle_h_house_b", []),
  ("castle_h_house_c",0,"castle_h_house_c","bo_castle_h_house_b", []),
  ("castle_h_battlement_barrier",0,"castle_h_battlement_barrier","bo_castle_h_battlement_barrier", []),

  ("full_keep_b",0,"full_keep_b","bo_full_keep_b", []),

  ("castle_f_keep_a",0,"castle_f_keep_a","bo_castle_f_keep_a", []),
  ("castle_f_battlement_a",0,"castle_f_battlement_a","bo_castle_f_battlement_a", []),
  ("castle_f_battlement_a_destroyed",0,"castle_f_battlement_a_destroyed","bo_castle_f_battlement_a_destroyed", []),
  ("castle_f_battlement_b",0,"castle_f_battlement_b","bo_castle_f_battlement_b", []),
  ("castle_f_battlement_c",0,"castle_f_battlement_c","bo_castle_f_battlement_c", []),
  ("castle_f_battlement_d",0,"castle_f_battlement_d","bo_castle_f_battlement_d", []),
  ("castle_f_battlement_e",0,"castle_f_battlement_e","bo_castle_f_battlement_e", []),
  ("castle_f_sally_port_elevation",0,"castle_f_sally_port_elevation","bo_castle_f_sally_port_elevation", []),
  ("castle_f_battlement_corner_a",0,"castle_f_battlement_corner_a","bo_castle_f_battlement_corner_a", []),
  ("castle_f_battlement_corner_b",0,"castle_f_battlement_corner_b","bo_castle_f_battlement_corner_b", []),
  ("castle_f_battlement_corner_c",0,"castle_f_battlement_corner_c","bo_castle_f_battlement_corner_c", []),

  ("castle_f_door_a",sokf_moveable|sokf_destructible|spr_use_time(0),"castle_f_door_a","bo_castle_f_door_a", []),
  ("mm_restroom_door",sokf_moveable|sokf_destructible|spr_use_time(0),"mm_restroom_door","bo_mm_restroom_door", []),
  ("castle_f_doors_top_a",0,"castle_f_doors_top_a","bo_castle_f_doors_top_a", []),
  ("castle_f_sally_door_a",sokf_moveable|sokf_destructible|spr_use_time(0),"castle_f_sally_door_a","bo_castle_f_sally_door_a", []),
  ("castle_f_stairs_a",sokf_type_ladder,"castle_f_stairs_a","bo_castle_f_stairs_a", []),
  ("castle_f_tower_a",0,"castle_f_tower_a","bo_castle_f_tower_a", []),
  ("castle_f_wall_stairs_a",sokf_type_ladder,"castle_f_wall_stairs_a","bo_castle_f_wall_stairs_a", []),
  ("castle_f_wall_stairs_b",sokf_type_ladder,"castle_f_wall_stairs_b","bo_castle_f_wall_stairs_b", []),
  ("castle_f_wall_way_a",0,"castle_f_wall_way_a","bo_castle_f_wall_way_a", []),
  ("castle_f_wall_way_b",0,"castle_f_wall_way_b","bo_castle_f_wall_way_b", []),
  ("castle_f_gatehouse_a",0,"castle_f_gatehouse_a","bo_castle_f_gatehouse_a", []),

  ("castle_g_battlement_a",0,"castle_g_battlement_a","bo_castle_g_battlement_a", []),
  ("castle_g_battlement_a1",0,"castle_g_battlement_a1","bo_castle_g_battlement_a1", []),
  ("castle_g_battlement_c",0,"castle_g_battlement_c","bo_castle_g_battlement_c", []),
  ("castle_g_corner_a",0,"castle_g_corner_a","bo_castle_g_corner_a", []),
  ("castle_g_corner_c",0,"castle_g_corner_c","bo_castle_g_corner_c", []),
  ("castle_g_tower_a",0,"castle_g_tower_a","bo_castle_g_tower_a", []),
  ("castle_g_gate_house",0,"castle_g_gate_house","bo_castle_g_gate_house", []),
  ("castle_g_gate_house_door_a",0,"castle_g_gate_house_door_a","bo_castle_g_gate_house_door_a", []),
  ("castle_g_gate_house_door_b",0,"castle_g_gate_house_door_b","bo_castle_g_gate_house_door_b", []),
  ("castle_g_square_keep_a",0,"castle_g_square_keep_a","bo_castle_g_square_keep_a", []),

  ("castle_i_battlement_a",0,"castle_i_battlement_a","bo_castle_i_battlement_a", []),
  ("castle_i_battlement_a1",0,"castle_i_battlement_a1","bo_castle_i_battlement_a1", []),
  ("castle_i_battlement_c",0,"castle_i_battlement_c","bo_castle_i_battlement_c", []),
  ("castle_i_corner_a",0,"castle_i_corner_a","bo_castle_i_corner_a", []),
  ("castle_i_corner_c",0,"castle_i_corner_c","bo_castle_i_corner_c", []),
  ("castle_i_tower_a",0,"castle_i_tower_a","bo_castle_i_tower_a", []),
  ("castle_i_gate_house",0,"castle_i_gate_house","bo_castle_i_gate_house", []),
  ("castle_i_gate_house_door_a",0,"castle_i_gate_house_door_a","bo_castle_i_gate_house_door_a", []),
  ("castle_i_gate_house_door_b",0,"castle_i_gate_house_door_b","bo_castle_i_gate_house_door_b", []),
  ("castle_i_square_keep_a",0,"castle_i_square_keep_a","bo_castle_i_square_keep_a", []),

  ("mosque_a",0,"mosque_a","bo_mosque_a", []),
  ("stone_minaret_a",0,"stone_minaret_a","bo_stone_minaret_a", []),
  ("stone_house_a",0,"stone_house_a","bo_stone_house_a", []),
  ("stone_house_b",0,"stone_house_b","bo_stone_house_b", []),
  ("stone_house_c",0,"stone_house_c","bo_stone_house_c", []),
  ("stone_house_d",0,"stone_house_d","bo_stone_house_d", []),
  ("stone_house_e",0,"stone_house_e","bo_stone_house_e", []),
  ("stone_house_f",0,"stone_house_f","bo_stone_house_f", []),

  ("banner_pole", sokf_moveable, "banner_pole", "bo_banner_pole", []),

  ("custom_banner_01",0,"pw_banner_castle","0", []),
  ("custom_banner_02",0,"pw_banner_castle","0", []),

  ("banner_a",0,"banner_a01","0", []),
  ("banner_b",0,"banner_a02","0", []),
  ("banner_c",0,"banner_a03","0", []),
  ("banner_d",0,"banner_a04","0", []),
  ("banner_e",0,"banner_a05","0", []),
  ("banner_f",0,"banner_a06","0", []),
  ("banner_g",0,"banner_a07","0", []),
  ("banner_h",0,"banner_a08","0", []),
  ("banner_i",0,"banner_a09","0", []),
  ("banner_j",0,"banner_a10","0", []),
  ("banner_k",0,"banner_a11","0", []),
  ("banner_l",0,"banner_a12","0", []),
  ("banner_m",0,"banner_a13","0", []),
  ("banner_n",0,"banner_a14","0", []),
  ("banner_o",0,"banner_a15","0", []),
  ("banner_p",0,"banner_a16","0", []),
  ("banner_q",0,"banner_a17","0", []),
  ("banner_r",0,"banner_a18","0", []),
  ("banner_s",0,"banner_a19","0", []),
  ("banner_t",0,"banner_a20","0", []),
  ("banner_u",0,"banner_a21","0", []),
  ("banner_ba",0,"banner_b01","0", []),
  ("banner_bb",0,"banner_b02","0", []),
  ("banner_bc",0,"banner_b03","0", []),
  ("banner_bd",0,"banner_b04","0", []),
  ("banner_be",0,"banner_b05","0", []),
  ("banner_bf",0,"banner_b06","0", []),
  ("banner_bg",0,"banner_b07","0", []),
  ("banner_bh",0,"banner_b08","0", []),
  ("banner_bi",0,"banner_b09","0", []),
  ("banner_bj",0,"banner_b10","0", []),
  ("banner_bk",0,"banner_b11","0", []),
  ("banner_bl",0,"banner_b12","0", []),
  ("banner_bm",0,"banner_b13","0", []),
  ("banner_bn",0,"banner_b14","0", []),
  ("banner_bo",0,"banner_b15","0", []),
  ("banner_bp",0,"banner_b16","0", []),
  ("banner_bq",0,"banner_b17","0", []),
  ("banner_br",0,"banner_b18","0", []),
  ("banner_bs",0,"banner_b19","0", []),
  ("banner_bt",0,"banner_b20","0", []),
  ("banner_bu",0,"banner_b21","0", []),
  ("banner_ca",0,"banner_c01","0", []),
  ("banner_cb",0,"banner_c02","0", []),
  ("banner_cc",0,"banner_c03","0", []),
  ("banner_cd",0,"banner_c04","0", []),
  ("banner_ce",0,"banner_c05","0", []),
  ("banner_cf",0,"banner_c06","0", []),
  ("banner_cg",0,"banner_c07","0", []),
  ("banner_ch",0,"banner_c08","0", []),
  ("banner_ci",0,"banner_c09","0", []),
  ("banner_cj",0,"banner_c10","0", []),
  ("banner_ck",0,"banner_c11","0", []),
  ("banner_cl",0,"banner_c12","0", []),
  ("banner_cm",0,"banner_c13","0", []),
  ("banner_cn",0,"banner_c14","0", []),
  ("banner_co",0,"banner_c15","0", []),
  ("banner_cp",0,"banner_c16","0", []),
  ("banner_cq",0,"banner_c17","0", []),
  ("banner_cr",0,"banner_c18","0", []),
  ("banner_cs",0,"banner_c19","0", []),
  ("banner_ct",0,"banner_c20","0", []),
  ("banner_cu",0,"banner_c21","0", []),
  ("banner_da",0,"banner_d01","0", []),
  ("banner_db",0,"banner_d02","0", []),
  ("banner_dc",0,"banner_d03","0", []),
  ("banner_dd",0,"banner_d04","0", []),
  ("banner_de",0,"banner_d05","0", []),
  ("banner_df",0,"banner_d06","0", []),
  ("banner_dg",0,"banner_d07","0", []),
  ("banner_dh",0,"banner_d08","0", []),
  ("banner_di",0,"banner_d09","0", []),
  ("banner_dj",0,"banner_d10","0", []),
  ("banner_dk",0,"banner_d11","0", []),
  ("banner_dl",0,"banner_d12","0", []),
  ("banner_dm",0,"banner_d13","0", []),
  ("banner_dn",0,"banner_d14","0", []),
  ("banner_do",0,"banner_d15","0", []),
  ("banner_dp",0,"banner_d16","0", []),
  ("banner_dq",0,"banner_d17","0", []),
  ("banner_dr",0,"banner_d18","0", []),
  ("banner_ds",0,"banner_d19","0", []),
  ("banner_dt",0,"banner_d20","0", []),
  ("banner_du",0,"banner_d21","0", []),
  ("banner_ea",0,"banner_e01","0", []),
  ("banner_eb",0,"banner_e02","0", []),
  ("banner_ec",0,"banner_e03","0", []),
  ("banner_ed",0,"banner_e04","0", []),
  ("banner_ee",0,"banner_e05","0", []),
  ("banner_ef",0,"banner_e06","0", []),
  ("banner_eg",0,"banner_e07","0", []),
  ("banner_eh",0,"banner_e08","0", []),
  ("banner_ei",0,"banner_e09","0", []),
  ("banner_ej",0,"banner_e10","0", []),
  ("banner_ek",0,"banner_e11","0", []),
  ("banner_el",0,"banner_e12","0", []),
  ("banner_em",0,"banner_e13","0", []),
  ("banner_en",0,"banner_e14","0", []),
  ("banner_eo",0,"banner_e15","0", []),
  ("banner_ep",0,"banner_e16","0", []),
  ("banner_eq",0,"banner_e17","0", []),
  ("banner_er",0,"banner_e18","0", []),
  ("banner_es",0,"banner_e19","0", []),
  ("banner_et",0,"banner_e20","0", []),
  ("banner_eu",0,"banner_e21","0", []),

  ("banner_f01", 0, "banner_f01", "0", []),
  ("banner_f02", 0, "banner_f02", "0", []),
  ("banner_f03", 0, "banner_f03", "0", []),
  ("banner_f04", 0, "banner_f04", "0", []),
  ("banner_f05", 0, "banner_f05", "0", []),
  ("banner_f06", 0, "banner_f06", "0", []),
  ("banner_f07", 0, "banner_f07", "0", []),
  ("banner_f08", 0, "banner_f08", "0", []),
  ("banner_f09", 0, "banner_f09", "0", []),
  ("banner_f10", 0, "banner_f10", "0", []),
  ("banner_f11", 0, "banner_f11", "0", []),
  ("banner_f12", 0, "banner_f12", "0", []),
  ("banner_f13", 0, "banner_f13", "0", []),
  ("banner_f14", 0, "banner_f14", "0", []),
  ("banner_f15", 0, "banner_f15", "0", []),
  ("banner_f16", 0, "banner_f16", "0", []),
  ("banner_f17", 0, "banner_f17", "0", []),
  ("banner_f18", 0, "banner_f18", "0", []),
  ("banner_f19", 0, "banner_f19", "0", []),
  ("banner_f20", 0, "banner_f20", "0", []),
  ("banner_f21", 0, "banner_f21", "0", []),

  ("banner_g01", 0, "banner_f01", "0", []),
  ("banner_g02", 0, "banner_f02", "0", []),
  ("banner_g03", 0, "banner_f03", "0", []),
  ("banner_g04", 0, "banner_f04", "0", []),
  ("banner_g05", 0, "banner_f05", "0", []),
  ("banner_g06", 0, "banner_f06", "0", []),
  ("banner_g07", 0, "banner_f07", "0", []),
  ("banner_g08", 0, "banner_f08", "0", []),
  ("banner_g09", 0, "banner_f09", "0", []),
  ("banner_g10", 0, "banner_f10", "0", []),

  ("banner_kingdom_a", 0, "banner_kingdom_a", "0", []),
  ("banner_kingdom_b", 0, "banner_kingdom_b", "0", []),
  ("banner_kingdom_c", 0, "banner_kingdom_c", "0", []),
  ("banner_kingdom_d", 0, "banner_kingdom_d", "0", []),
  ("banner_kingdom_e", 0, "banner_kingdom_e", "0", []),
  ("banner_kingdom_f", 0, "banner_kingdom_f", "0", []),

  ("tavern_chair_a",0,"tavern_chair_a","bo_tavern_chair_a", []),
  ("tavern_chair_b",0,"tavern_chair_b","bo_tavern_chair_b", []),
  ("tavern_table_a",0,"tavern_table_a","bo_tavern_table_a", []),
  ("tavern_table_b",0,"tavern_table_b","bo_tavern_table_b", []),
  ("fireplace_a",0,"fireplace_a","bo_fireplace_a", []),
  ("barrel",0,"barrel","bobarrel", []),
  ("bench_tavern",0,"bench_tavern","bobench_tavern", []),
  ("bench_tavern_b",0,"bench_tavern_b","bo_bench_tavern_b", []),
  ("bowl_wood",0,"bowl_wood","0", []),
  ("chandelier_table",0,"chandelier_table","0", []),
  ("chandelier_tavern",0,"chandelier_tavern","0", []),
  ("chest_gothic",0,"chest_gothic","bochest_gothic", []),
  ("chest_b",0,"chest_b","bo_chest_b", []),
  ("chest_c",0,"chest_c","bo_chest_c", []),
  ("counter_tavern",0,"counter_tavern","bocounter_tavern", []),
  ("cup",0,"cup","0", []),
  ("dish_metal",0,"dish_metal","0", []),
  ("gothic_chair",0,"gothic_chair","bogothic_chair", []),
  ("gothic_stool",0,"gothic_stool","bogothic_stool", []),
  ("grate",0,"grate","bograte", []),
  ("jug",0,"jug","0", []),
  ("potlamp",0,"potlamp","0", []),
  ("weapon_rack",0,"weapon_rack","boweapon_rack", []),
  ("weapon_rack_big",0,"weapon_rack_big","boweapon_rack_big", []),
  ("tavern_barrel",0,"barrel","bobarrel", []),
  ("tavern_barrel_b",0,"tavern_barrel_b","bo_tavern_barrel_b", []),
  ("merchant_sign",0,"merchant_sign","bo_tavern_sign", []),
  ("tavern_sign",0,"tavern_sign","bo_tavern_sign", []),
  ("sack",0,"sack","0", []),
  ("skull_a",0,"skull_a","0", []),
  ("skull_b",0,"skull_b","0", []),
  ("skull_c",0,"skull_c","0", []),
  ("skull_d",0,"skull_d","0", []),
  ("skeleton_cow",0,"skeleton_cow","0", []),
  ("cupboard_a",0,"cupboard_a","bo_cupboard_a_fixed", []),
  ("box_a",0,"box_a","bo_box_a", []),
  ("bucket_a",0,"bucket_a","bo_bucket_a", []),
  ("straw_a",0,"straw_a","0", []),
  ("straw_b",0,"straw_b","0", []),
  ("straw_c",0,"straw_c","0", []),
  ("cloth_a",0,"cloth_a","0", []),
  ("cloth_b",0,"cloth_b","0", []),
  ("mat_a",0,"mat_a","0", []),
  ("mat_b",0,"mat_b","0", []),
  ("mat_c",0,"mat_c","0", []),
  ("mat_d",0,"mat_d","0", []),

  ("wood_a",0,"wood_a","bo_wood_a", []),
  ("wood_b",0,"wood_b","bo_wood_b", []),
  ("wood_heap",0,"wood_heap_a","bo_wood_heap_a", []),
  ("wood_heap_b",0,"wood_heap_b","bo_wood_heap_b", []),
  ("water_well_a",spr_use_time(5),"water_well_a","bo_water_well_a", spr_well_triggers()),
  ("net_a",0,"net_a","bo_net_a", []),
  ("net_b",0,"net_b","0", []),

  ("meat_hook",0,"meat_hook","0", []),
  ("cooking_pole",0,"cooking_pole","0", []),
  ("bowl_a",0,"bowl_a","0", []),
  ("bucket_b",0,"bucket_b","0", []),
  ("washtub_a",0,"washtub_a","bo_washtub_a", []),
  ("washtub_b",0,"washtub_b","bo_washtub_b", []),

  ("table_trunk_a",0,"table_trunk_a","bo_table_trunk_a", []),
  ("chair_trunk_a",0,"chair_trunk_a","bo_chair_trunk_a", []),
  ("chair_trunk_b",0,"chair_trunk_b","bo_chair_trunk_b", []),
  ("chair_trunk_c",0,"chair_trunk_c","bo_chair_trunk_c", []),

  ("table_trestle_long",0,"table_trestle_long","bo_table_trestle_long", []),
  ("table_trestle_small",0,"table_trestle_small","bo_table_trestle_small", []),
  ("chair_trestle",0,"chair_trestle","bo_chair_trestle", []),

  ("wheel",0,"wheel","bo_wheel", []),
  ("ladder",sokf_type_ladder,"ladder","boladder", []),
  ("cart",0,"cart","bo_cart", []),
  ("village_stand",0,"village_stand","bovillage_stand", []),
  ("wooden_stand",0,"wooden_stand","bowooden_stand", []),
  ("table_small",0,"table_small","bo_table_small", []),
  ("table_small_b",0,"table_small_b","bo_table_small_b", []),
  ("small_timber_frame_house_a",0,"small_timber_frame_house_a","bo_small_timber_frame_house_a", []),
  ("timber_frame_house_b",0,"tf_house_b","bo_tf_house_b", []),
  ("timber_frame_house_c",0,"tf_house_c","bo_tf_house_c", []),
  ("timber_frame_extension_a",0,"timber_frame_extension_a","bo_timber_frame_extension_a", []),
  ("timber_frame_extension_b",0,"timber_frame_extension_b","bo_timber_frame_extension_b", []),
  ("stone_stairs_a",sokf_type_ladder,"stone_stairs_a","bo_stone_stairs_a", []),
  ("stone_stairs_b",sokf_type_ladder,"stone_stairs_b","bo_stone_stairs_b", []),
  ("railing_a",0,"railing_a","bo_railing_a", []),
  ("side_building_a",0,"side_building_a","bo_side_building_a", []),
  ("battlement_a",0,"battlement_a","bo_battlement_a", []),

  ("battlement_a_destroyed",0,"battlement_a_destroyed","bo_battlement_a_destroyed", []),

  ("round_tower_a",0,"round_tower_a","bo_round_tower_a", []),
  ("small_round_tower_a",0,"small_round_tower_a","bo_small_round_tower_a", []),
  ("small_round_tower_roof_a",0,"small_round_tower_roof_a","bo_small_round_tower_roof_a", []),
  ("square_keep_a",0,"square_keep_a","bo_square_keep_a", []),
  ("square_tower_roof_a",0,"square_tower_roof_a","0", []),
  ("gate_house_a",0,"gate_house_a","bo_gate_house_a", []),
  ("gate_house_b",0,"gate_house_b","bo_gate_house_b", []),
  ("small_wall_a",0,"small_wall_a","bo_small_wall_a", []),
  ("small_wall_b",0,"small_wall_b","bo_small_wall_b", []),
  ("small_wall_c",0,"small_wall_c","bo_small_wall_c", []),
  ("small_wall_c_destroy",0,"small_wall_c_destroy","bo_small_wall_c_destroy", []),
  ("small_wall_d",0,"small_wall_d","bo_small_wall_d", []),
  ("small_wall_e",0,"small_wall_e","bo_small_wall_d", []),
  ("small_wall_f",0,"small_wall_f","bo_small_wall_f", []),
  ("small_wall_f2",0,"small_wall_f2","bo_small_wall_f2", []),

  ("town_house_a",0,"town_house_a","bo_town_house_a", []),
  ("town_house_b",0,"town_house_b","bo_town_house_b", []),
  ("town_house_c",0,"town_house_c","bo_town_house_c", []),
  ("town_house_d",0,"town_house_d","bo_town_house_d", []),
  ("town_house_e",0,"town_house_e","bo_town_house_e", []),
  ("town_house_f",0,"town_house_f","bo_town_house_f", []),
  ("town_house_g",0,"town_house_g","bo_town_house_g", []),
  ("town_house_h",0,"town_house_h","bo_town_house_h", []),
  ("town_house_i",0,"town_house_i","bo_town_house_i", []),
  ("town_house_j",0,"town_house_j","bo_town_house_j", []),
  ("town_house_l",0,"town_house_l","bo_town_house_l", []),

  ("town_house_m",0,"town_house_m","bo_town_house_m", []),
  ("town_house_n",0,"town_house_n","bo_town_house_n", []),
  ("town_house_o",0,"town_house_o","bo_town_house_o", []),
  ("town_house_p",0,"town_house_p","bo_town_house_p", []),
  ("town_house_q",0,"town_house_q","bo_town_house_q_fixed", []),

  ("passage_house_a",0,"passage_house_a","bo_passage_house_a", []),
  ("passage_house_b",0,"passage_house_b","bo_passage_house_b", []),
  ("passage_house_c",0,"passage_house_c","bo_passage_house_c", []),
  ("passage_house_d",0,"passage_house_d","bo_passage_house_d", []),
  ("passage_house_c_door",0,"passage_house_c_door","bo_passage_house_c_door", []),

  ("house_extension_a",0,"house_extension_a","bo_house_extension_a", []),
  ("house_extension_b",0,"house_extension_b","bo_house_extension_b", []),
  ("house_extension_c",0,"house_extension_c","bo_house_extension_a", []),
  ("house_extension_d",0,"house_extension_d","bo_house_extension_d", []),

  ("house_extension_e",0,"house_extension_e","bo_house_extension_e", []),
  ("house_extension_f",0,"house_extension_f","bo_house_extension_f", []),
  ("house_extension_f2",0,"house_extension_f2","bo_house_extension_f", []),
  ("house_extension_g",0,"house_extension_g","bo_house_extension_g", []),
  ("house_extension_g2",0,"house_extension_g2","bo_house_extension_g", []),
  ("house_extension_h",0,"house_extension_h","bo_house_extension_h", []),
  ("house_extension_i",0,"house_extension_i","bo_house_extension_i", []),

  ("house_roof_door",0,"house_roof_door","bo_house_roof_door", []),

  ("door_extension_a",0,"door_extension_a","bo_door_extension_a", []),
  ("stairs_arch_a",sokf_type_ladder,"stairs_arch_a","bo_stairs_arch_a", []),

  ("town_house_r",0,"town_house_r","bo_town_house_r", []),
  ("town_house_s",0,"town_house_s","bo_town_house_s", []),
  ("town_house_t",0,"town_house_t","bo_town_house_t", []),
  ("town_house_u",0,"town_house_u","bo_town_house_u", []),
  ("town_house_v",0,"town_house_v","bo_town_house_v", []),
  ("town_house_w",0,"town_house_w","bo_town_house_w", []),

  ("town_house_y",0,"town_house_y","bo_town_house_y", []),
  ("town_house_z",0,"town_house_z","bo_town_house_z", []),
  ("town_house_za",0,"town_house_za","bo_town_house_za", []),

  ("windmill",0,"windmill","bo_windmill", []),
  ("windmill_fan_turning",sokf_moveable,"windmill_fan_turning","bo_windmill_fan_turning", []),
  ("windmill_fan",0,"windmill_fan","bo_windmill_fan", []),
  ("fake_house_a",0,"fake_house_a","bo_fake_house_a", []),
  ("fake_house_b",0,"fake_house_b","bo_fake_house_b", []),
  ("fake_house_c",0,"fake_house_c","bo_fake_house_c", []),
  ("fake_house_d",0,"fake_house_d","bo_fake_house_d", []),
  ("fake_house_e",0,"fake_house_e","bo_fake_house_e", []),
  ("fake_house_f",0,"fake_house_f","bo_fake_house_f", []),

  ("fake_house_snowy_a",0,"fake_house_snowy_a","bo_fake_house_a", []),
  ("fake_house_snowy_b",0,"fake_house_snowy_b","bo_fake_house_b", []),
  ("fake_house_snowy_c",0,"fake_house_snowy_c","bo_fake_house_c", []),
  ("fake_house_snowy_d",0,"fake_house_snowy_d","bo_fake_house_d", []),

  ("fake_house_far_a",0,"fake_house_far_a","0", []),
  ("fake_house_far_b",0,"fake_house_far_b","0", []),
  ("fake_house_far_c",0,"fake_house_far_c","0", []),
  ("fake_house_far_d",0,"fake_house_far_d","0", []),
  ("fake_house_far_e",0,"fake_house_far_e","0", []),
  ("fake_house_far_f",0,"fake_house_far_f","0", []),

  ("fake_house_far_snowycrude_a",0,"fake_house_far_snowy_a","0", []),
  ("fake_house_far_snowy_b",0,"fake_house_far_snowy_b","0", []),
  ("fake_house_far_snowy_c",0,"fake_house_far_snowy_c","0", []),
  ("fake_house_far_snowy_d",0,"fake_house_far_snowy_d","0", []),

  ("earth_wall_a",0,"earth_wall_a","bo_earth_wall_a", []),
  ("earth_wall_a2",0,"earth_wall_a2","bo_earth_wall_a2", []),
  ("earth_wall_b",0,"earth_wall_b","bo_earth_wall_b", []),
  ("earth_wall_b2",0,"earth_wall_b2","bo_earth_wall_b2", []),
  ("earth_stairs_a",sokf_type_ladder,"earth_stairs_a","bo_earth_stairs_a", []),
  ("earth_stairs_b",sokf_type_ladder,"earth_stairs_b","bo_earth_stairs_b", []),
  ("earth_tower_small_a",0,"earth_tower_small_a","bo_earth_tower_small_a", []),
  ("earth_gate_house_a",0,"earth_gate_house_a","bo_earth_gate_house_a", []),
  ("earth_gate_a",0,"earth_gate_a","bo_earth_gate_a", []),
  ("earth_square_keep_a",0,"earth_square_keep_a","bo_earth_square_keep_a", []),
  ("earth_house_a",0,"earth_house_a","bo_earth_house_a", []),
  ("earth_house_b",0,"earth_house_b","bo_earth_house_b", []),
  ("earth_house_c",0,"earth_house_c","bo_earth_house_c", []),
  ("earth_house_d",0,"earth_house_d","bo_earth_house_d", []),

  ("village_steppe_a",0,"village_steppe_a","bo_village_steppe_a", []),
  ("village_steppe_b",0,"village_steppe_b","bo_village_steppe_b", []),
  ("village_steppe_c",0,"village_steppe_c","bo_village_steppe_c", []),
  ("village_steppe_d",0,"village_steppe_d","bo_village_steppe_d", []),
  ("village_steppe_e",0,"village_steppe_e","bo_village_steppe_e", []),
  ("village_steppe_f",0,"village_steppe_f","bo_village_steppe_f", []),
  ("town_house_aa",0,"town_house_aa","bo_town_house_aa", []),

  ("snowy_house_a",0,"snowy_house_a","bo_snowy_house_a", []),
  ("snowy_house_b",0,"snowy_house_b","bo_snowy_house_b", []),
  ("snowy_house_c",0,"snowy_house_c","bo_snowy_house_c", []),
  ("snowy_house_d",0,"snowy_house_d","bo_snowy_house_d", []),
  ("snowy_house_e",0,"snowy_house_e","bo_snowy_house_e", []),
  ("snowy_house_f",0,"snowy_house_f","bo_snowy_house_f", []),
  ("snowy_house_g",0,"snowy_house_g","bo_snowy_house_g", []),
  ("snowy_house_h",0,"snowy_house_h","bo_snowy_house_h", []),
  ("snowy_house_i",0,"snowy_house_i","bo_snowy_house_i", []),
  ("snowy_wall_a",0,"snowy_wall_a","bo_snowy_wall_a", []),

  ("snowy_stand",0,"snowy_stand","bo_snowy_stand", []),

  ("snowy_heap_a",0,"snowy_heap_a","bo_snowy_heap_a", []),
  ("snowy_trunks_a",0,"snowy_trunks_a","bo_snowy_trunks_a", []),

  ("snowy_castle_tower_a",0,"snowy_castle_tower_a","bo_snowy_castle_tower_a", []),
  ("snowy_castle_battlement_a",0,"snowy_castle_battlement_a","bo_snowy_castle_battlement_a", []),
  ("snowy_castle_battlement_a_destroyed",0,"snowy_castle_battlement_a_destroyed","bo_snowy_castle_battlement_a_destroyed", []),

  ("snowy_castle_battlement_b",0,"snowy_castle_battlement_b","bo_snowy_castle_battlement_b", []),
  ("snowy_castle_battlement_corner_a",0,"snowy_castle_battlement_corner_a","bo_snowy_castle_battlement_corner_a", []),
  ("snowy_castle_battlement_corner_b",0,"snowy_castle_battlement_corner_b","bo_snowy_castle_battlement_corner_b", []),
  ("snowy_castle_battlement_corner_c",0,"snowy_castle_battlement_corner_c","bo_snowy_castle_battlement_corner_c", []),
  ("snowy_castle_battlement_stairs_a",0,"snowy_castle_battlement_stairs_a","bo_snowy_castle_battlement_stairs_a", []),
  ("snowy_castle_battlement_stairs_b",0,"snowy_castle_battlement_stairs_b","bo_snowy_castle_battlement_stairs_b", []),
  ("snowy_castle_gate_house_a",0,"snowy_castle_gate_house_a","bo_snowy_castle_gate_house_a", []),
  ("snowy_castle_round_tower_a",0,"snowy_castle_round_tower_a","bo_snowy_castle_round_tower_a", []),
  ("snowy_castle_square_keep_a",0,"snowy_castle_square_keep_a","bo_snowy_castle_square_keep_a", []),
  ("snowy_castle_stairs_a",sokf_type_ladder,"snowy_castle_stairs_a","bo_snowy_castle_stairs_a", []),

  ("square_keep_b",0,"square_keep_b","bo_square_keep_b", []),
  ("square_keep_c",0,"square_keep_c","bo_square_keep_c", []),
  ("square_keep_d",0,"square_keep_d","bo_square_keep_d", []),
  ("square_keep_e",0,"square_keep_e","bo_square_keep_e", []),
  ("square_keep_f",0,"square_keep_f","bo_square_keep_f", []),

  ("square_extension_a",0,"square_extension_a","bo_square_extension_a", []),
  ("square_stairs_a",0,"square_stairs_a","bo_square_stairs_a", []),

  ("castle_courtyard_house_a",0,"castle_courtyard_house_a","bo_castle_courtyard_house_a", []),
  ("castle_courtyard_house_b",0,"castle_courtyard_house_b","bo_castle_courtyard_house_b", []),
  ("castle_courtyard_house_c",0,"castle_courtyard_house_c","bo_castle_courtyard_house_c", []),
  ("castle_courtyard_a",0,"castle_courtyard_a","bo_castle_courtyard_a", []),

  ("gatehouse_b",0,"gatehouse_b","bo_gatehouse_b", []),
  ("castle_gaillard",0,"castle_gaillard","bo_castle_gaillard", []),

  ("castle_e_battlement_a",0,"castle_e_battlement_a","bo_castle_e_battlement_a", []),
  ("castle_e_battlement_c",0,"castle_e_battlement_c","bo_castle_e_battlement_c", []),
  ("castle_e_battlement_a_destroyed",0,"castle_e_battlement_a_destroyed","bo_castle_e_battlement_a_destroyed", []),
  ("castle_e_sally_door_a",sokf_moveable|sokf_destructible|spr_use_time(0),"castle_e_sally_door_a","bo_castle_e_sally_door_a", []),
  ("castle_e_corner",0,"castle_e_corner","bo_castle_e_corner", []),
  ("castle_e_corner_b",0,"castle_e_corner_b","bo_castle_e_corner_b", []),
  ("castle_e_corner_c",0,"castle_e_corner_c","bo_castle_e_corner_c", []),
  ("castle_e_stairs_a",0,"castle_e_stairs_a","bo_castle_e_stairs_a", []),
  ("castle_e_tower",0,"castle_e_tower","bo_castle_e_tower", []),
  ("castle_e_gate_house_a",0,"castle_e_gate_house_a","bo_castle_e_gate_house_a", []),
  ("castle_e_keep_a",0,"castle_e_keep_a","bo_castle_e_keep_a", []),
  ("stand_thatched",0,"stand_thatched","bo_stand_thatched", []),
  ("stand_cloth",0,"stand_cloth","bo_stand_cloth", []),
  ("castle_e_house_a",0,"castle_e_house_a","bo_castle_e_house_a", []),
  ("castle_e_house_b",0,"castle_e_house_b","bo_castle_e_house_b", []),

  ("arena_block_a",0,"arena_block_a","bo_arena_block_ab", []),
  ("arena_block_b",0,"arena_block_b","bo_arena_block_ab", []),
  ("arena_block_c",0,"arena_block_c","bo_arena_block_c", []),
  ("arena_block_d",0,"arena_block_d","bo_arena_block_def", []),
  ("arena_block_e",0,"arena_block_e","bo_arena_block_def", []),
  ("arena_block_f",0,"arena_block_f","bo_arena_block_def", []),
  ("arena_block_g",0,"arena_block_g","bo_arena_block_ghi", []),
  ("arena_block_h",0,"arena_block_h","bo_arena_block_ghi", []),
  ("arena_block_i",0,"arena_block_i","bo_arena_block_ghi", []),

  ("arena_block_j",0,"arena_block_j","bo_arena_block_j", []),
  ("arena_block_j_awning",0,"arena_block_j_awning","bo_arena_block_j_awning", []),

  ("arena_palisade_a",0,"pw_wooden_palisade_a","bo_arena_palisade_a", []),
  ("arena_wall_a",0,"arena_wall_a","bo_arena_wall_ab", []),
  ("arena_wall_b",0,"arena_wall_b","bo_arena_wall_ab", []),
  ("arena_barrier_a",0,"arena_barrier_a","bo_arena_barrier_a", []),
  ("arena_barrier_b",0,"arena_barrier_b","bo_arena_barrier_bc", []),
  ("arena_barrier_c",0,"arena_barrier_c","bo_arena_barrier_bc", []),
  ("arena_tower_a",0,"arena_tower_a","bo_arena_tower_abc", []),
  ("arena_tower_b",0,"arena_tower_b","bo_arena_tower_abc", []),
  ("arena_tower_c",0,"arena_tower_c","bo_arena_tower_abc", []),
  ("arena_spectator_a",0,"arena_spectator_a","0", []),
  ("arena_spectator_b",0,"arena_spectator_b","0", []),
  ("arena_spectator_c",0,"arena_spectator_c","0", []),
  ("arena_spectator_sitting_a",0,"arena_spectator_sitting_a","0", []),
  ("arena_spectator_sitting_b",0,"arena_spectator_sitting_b","0", []),
  ("arena_spectator_sitting_c",0,"arena_spectator_sitting_c","0", []),

  ("courtyard_gate_a",0,"courtyard_entry_a","bo_courtyard_entry_a", []),
  ("courtyard_gate_b",0,"courtyard_entry_b","bo_courtyard_entry_b", []),
  ("courtyard_gate_c",0,"courtyard_entry_c","bo_courtyard_entry_c", []),
  ("courtyard_gate_snowy",0,"courtyard_entry_snowy","bo_courtyard_entry_a", []),

  ("castle_tower_a",0,"castle_tower_a","bo_castle_tower_a", []),
  ("castle_battlement_a",0,"castle_battlement_a","bo_castle_battlement_a", []),
  ("castle_battlement_b",0,"castle_battlement_b","bo_castle_battlement_b", []),
  ("castle_battlement_c",0,"castle_battlement_c","bo_castle_battlement_c", []),

  ("castle_battlement_a_destroyed",0,"castle_battlement_a_destroyed","bo_castle_battlement_a_destroyed", []),
  ("castle_battlement_b_destroyed",0,"castle_battlement_b_destroyed","bo_castle_battlement_b_destroyed", []),

  ("castle_battlement_corner_a",0,"castle_battlement_corner_a","bo_castle_battlement_corner_a", []),
  ("castle_battlement_corner_b",0,"castle_battlement_corner_b","bo_castle_battlement_corner_b", []),
  ("castle_battlement_corner_c",0,"castle_battlement_corner_c","bo_castle_battlement_corner_c", []),
  ("castle_battlement_stairs_a",0,"castle_battlement_stairs_a","bo_castle_battlement_stairs_a", []),
  ("castle_battlement_stairs_b",0,"castle_battlement_stairs_b","bo_castle_battlement_stairs_b", []),
  ("castle_gate_house_a",0,"castle_gate_house_a","bo_castle_gate_house_a", []),
  ("castle_round_tower_a",0,"castle_round_tower_a","bo_castle_round_tower_a", []),
  ("castle_square_keep_a",0,"castle_square_keep_a","bo_castle_square_keep_a", []),
  ("castle_stairs_a",sokf_type_ladder,"castle_stairs_a","bo_castle_stairs_a", []),

  ("castle_drawbridge_open",0,"castle_drawbridges_open","bo_castle_drawbridges_open", []),
  ("castle_drawbridge_closed",0,"castle_drawbridges_closed","bo_castle_drawbridges_closed", []),
  ("spike_group_a",0,"spike_group_a","bo_spike_group_a", []),
  ("spike_a",0,"spike_a","bo_spike_a", []),
  ("belfry_a",sokf_moveable,"belfry_a","bo_belfry_a", []),

  ("belfry_b",sokf_moveable,"belfry_b","bo_belfry_b", []),
  ("belfry_b_platform_a",sokf_moveable,"belfry_b_platform_a","bo_belfry_b_platform_a", []),

  ("belfry_old",0,"belfry_a","bo_belfry_a", []),
  ("belfry_platform_a",sokf_moveable,"belfry_platform_a","bo_belfry_platform_a", []),
  ("belfry_platform_b",sokf_moveable,"belfry_platform_b","bo_belfry_platform_b", []),
  ("belfry_platform_old",0,"belfry_platform_b","bo_belfry_platform_b", []),
  ("belfry_wheel",sokf_moveable,"belfry_wheel",0, []),
  ("belfry_wheel_old",0,"belfry_wheel",0, []),

  ("mangonel",0,"mangonel","bo_mangonel", []),
  ("trebuchet_old",0,"trebuchet_old","bo_trebuchet_old", []),
  ("trebuchet_new",0,"trebuchet_new","bo_trebuchet_old", []),

  ("trebuchet_destructible",sokf_moveable|sokf_destructible,"trebuchet_new","bo_trebuchet_old", []),

  ("stone_ball",0,"stone_ball","0", []),

  ("village_house_a",0,"village_house_a","bo_village_house_a", []),
  ("village_house_b",0,"village_house_b","bo_village_house_b", []),
  ("village_house_c",0,"village_house_c","bo_village_house_c", []),
  ("village_house_d",0,"village_house_d","bo_village_house_d", []),
  ("farm_house_a",0,"farm_house_a","bo_farm_house_a", []),
  ("farm_house_b",0,"farm_house_b","bo_farm_house_b", []),
  ("farm_house_c",0,"farm_house_c","bo_farm_house_c", []),
  ("mountain_house_a",0,"mountain_house_a","bo_mountain_house_a", []),
  ("mountain_house_b",0,"mountain_house_b","bo_mountain_house_b", []),
  ("village_hut_a",0,"village_hut_a","bo_village_hut_a", []),
  ("crude_fence",0,"fence","bo_fence", []),
  ("crude_fence_small",0,"crude_fence_small","bo_crude_fence_small", []),
  ("crude_fence_small_b",0,"crude_fence_small_b","bo_crude_fence_small_b", []),

  ("ramp_12m",0,"ramp_12m","bo_ramp_12m", []),
  ("ramp_14m",0,"ramp_14m","bo_ramp_14m", []),

  ("siege_ladder_6m",sokf_type_ladder,"siege_ladder_move_6m","bo_siege_ladder_move_6m", []),
  ("siege_ladder_8m",sokf_type_ladder,"siege_ladder_move_8m","bo_siege_ladder_move_8m", []),
  ("siege_ladder_10m",sokf_type_ladder,"siege_ladder_move_10m","bo_siege_ladder_move_10m", []),
  ("siege_ladder_12m",sokf_type_ladder,"siege_ladder_12m","bo_siege_ladder_12m", []),
  ("siege_ladder_14m",sokf_type_ladder,"siege_ladder_14m","bo_siege_ladder_14m", []),

  ("siege_ladder_move_6m",sokf_type_ladder|sokf_moveable|spr_use_time(2),"siege_ladder_move_6m","bo_siege_ladder_move_6m", []),
  ("siege_ladder_move_8m",sokf_type_ladder|sokf_moveable|spr_use_time(2),"siege_ladder_move_8m","bo_siege_ladder_move_8m", []),
  ("siege_ladder_move_10m",sokf_type_ladder|sokf_moveable|spr_use_time(3),"siege_ladder_move_10m","bo_siege_ladder_move_10m", []),
  ("siege_ladder_move_12m",sokf_type_ladder|sokf_moveable|spr_use_time(3),"siege_ladder_move_12m","bo_siege_ladder_move_12m", []),
  ("siege_ladder_move_14m",sokf_type_ladder|sokf_moveable|spr_use_time(4),"siege_ladder_move_14m","bo_siege_ladder_move_14m", []),

  ("portcullis",sokf_moveable,"portcullis_a","bo_portcullis_a", []),
  ("bed_a",0,"bed_a","bo_bed_a", []),
  ("bed_b",0,"bed_b","bo_bed_b", []),
  ("bed_c",0,"bed_c","bo_bed_c", []),
  ("bed_d",0,"bed_d","bo_bed_d", []),
  ("bed_e",0,"bed_e","bo_bed_e", []),

  ("bed_f",0,"bed_f","bo_bed_f", []),

  ("towngate_door_left",sokf_moveable,"door_g_left","bo_door_left", []),
  ("towngate_door_right",sokf_moveable,"door_g_right","bo_door_right", []),
  ("towngate_rectangle_door_left",sokf_moveable,"towngate_rectangle_door_left","bo_towngate_rectangle_door_left", []),
  ("towngate_rectangle_door_right",sokf_moveable,"towngate_rectangle_door_right","bo_towngate_rectangle_door_right", []),

  ("door_screen",sokf_moveable,"door_screen","0", []),
  ("door_a",sokf_moveable,"door_a","bo_door_a", []),
  ("door_b",sokf_moveable,"door_b","bo_door_a", []),
  ("door_c",sokf_moveable,"door_c","bo_door_a", []),
  ("door_d",sokf_moveable,"door_d","bo_door_a", []),
  ("tavern_door_a",sokf_moveable,"tavern_door_a","bo_tavern_door_a", []),
  ("tavern_door_b",sokf_moveable,"tavern_door_b","bo_tavern_door_a", []),
  ("door_e_left",sokf_moveable,"door_e_left","bo_door_left", []),
  ("door_e_right",sokf_moveable,"door_e_right","bo_door_right", []),
  ("door_f_left",sokf_moveable,"door_f_left","bo_door_left", []),
  ("door_f_right",sokf_moveable,"door_f_right","bo_door_right", []),
  ("door_h_left",sokf_moveable,"door_g_left","bo_door_left", []),
  ("door_h_right",sokf_moveable,"door_g_right","bo_door_right", []),
  ("draw_bridge_a",0,"draw_bridge_a","bo_draw_bridge_a", []),
  ("chain_1m",0,"chain_1m","0", []),
  ("chain_2m",0,"chain_2m","0", []),
  ("chain_5m",0,"chain_5m","0", []),
  ("chain_10m",0,"chain_10m","0", []),
  ("bridge_modular_a",0,"bridge_modular_a","bo_bridge_modular_a", []),
  ("bridge_modular_b",0,"bridge_modular_b","bo_bridge_modular_b", []),
  ("church_a",0,"church_a","bo_church_a", []),
  ("church_tower_a",0,"church_tower_a","bo_church_tower_a", []),
  ("stone_step_a",0,"floor_stone_a","bo_floor_stone_a", []),
  ("stone_step_b",0,"stone_step_b","0", []),
  ("stone_step_c",0,"stone_step_c","0", []),
  ("stone_heap",0,"stone_heap","bo_stone_heap", []),
  ("stone_heap_b",0,"stone_heap_b","bo_stone_heap", []),

  ("panel_door_a",0,"house_door_a","bo_house_door_a", []),
  ("panel_door_b",0,"house_door_b","bo_house_door_a", []),
  ("smoke_stain",0,"soot_a","0", []),
  ("brazier_with_fire",0,"brazier","bo_brazier",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (prop_instance_play_sound, ":instance_id", "snd_fire_loop"),
      (set_position_delta,0,0,85),
      (particle_system_add_new, "psys_brazier_fire_1"),
      (particle_system_add_new, "psys_fire_sparks_1"),
      (set_position_delta,0,0,100),
      (particle_system_add_new, "psys_fire_glow_1"),
      (particle_system_emit, "psys_fire_glow_1",9000000),
      ]),
    ]),

  ("cooking_fire",0,"fire_floor","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (prop_instance_play_sound, ":instance_id", "snd_fire_loop"),
      (set_position_delta,0,0,12),
      (particle_system_add_new, "psys_cooking_fire_1"),
      (particle_system_add_new, "psys_fire_sparks_1"),
      (particle_system_add_new, "psys_cooking_smoke"),
      (set_position_delta,0,0,50),
      (particle_system_add_new, "psys_fire_glow_1"),
      (particle_system_emit, "psys_fire_glow_1",9000000),
      ]),
    ]),
  ("cauldron_a",0,"cauldron_a","bo_cauldron_a", []),
  ("fry_pan_a",0,"fry_pan_a","0", []),
  ("tripod_cauldron_a",0,"tripod_cauldron_a","bo_tripod_cauldron_a", []),
  ("tripod_cauldron_b",0,"tripod_cauldron_b","bo_tripod_cauldron_b", []),
  ("open_stable_a",0,"open_stable_a","bo_open_stable_a", []),
  ("open_stable_b",0,"open_stable_b","bo_open_stable_b", []),
  ("plate_a",0,"plate_a","0", []),
  ("plate_b",0,"plate_b","0", []),
  ("plate_c",0,"plate_c","0", []),
  ("lettuce",0,"lettuce","0", []),
  ("hanger",0,"hanger","0", []),
  ("knife_eating",0,"knife_eating","0", []),
  ("colander",0,"colander","0", []),
  ("ladle",0,"ladle","0", []),
  ("spoon",0,"spoon","0", []),
  ("skewer",0,"skewer","0", []),
  ("grape_a",0,"grape_a","0", []),
  ("grape_b",0,"grape_b","0", []),
  ("apple_a",0,"apple_a","0", []),
  ("apple_b",0,"apple_b","0", []),
  ("maize_a",0,"maize_a","0", []),
  ("maize_b",0,"maize_b","0", []),
  ("cabbage",0,"cabbage","0", []),
  ("flax_bundle",0,"raw_flax","0",[]),
  ("olive_plane",0,"olive_plane","0",[]),
  ("grapes_plane",0,"grapes_plane","0",[]),
  ("date_fruit_plane",0,"date_fruit_plane","0",[]),
  ("bowl",0,"bowl_big","0",[]),
  ("bowl_small",0,"bowl_small","0",[]),
  ("dye_blue",0,"raw_dye_blue","0",[]),
  ("dye_red",0,"raw_dye_red","0",[]),
  ("dye_yellow",0,"raw_dye_yellow","0",[]),
  ("basket",0,"basket_small","0",[]),
  ("basket_big",0,"basket_large","0",[]),
  ("basket_big_green",0,"basket_big","0",[]),
  ("leatherwork_frame",0,"leatherwork_frame","0", []),

  ("cabbage_b",0,"cabbage_b","0", []),
  ("bean",0,"bean","0", []),
  ("basket_a",0,"basket_a","bo_basket_a", []),
  ("feeding_trough_a",0,"feeding_trough_a","bo_feeding_trough_a", []),

  ("marrow_a",0,"marrow_a","0", []),
  ("marrow_b",0,"marrow_b","0", []),
  ("squash_plant",0,"marrow_c","0", []),

  ("gatehouse_new_a",0,"gatehouse_new_a","bo_gatehouse_new_a", []),
  ("gatehouse_new_b",0,"gatehouse_new_b","bo_gatehouse_new_b_fixed", []),
  ("gatehouse_new_snowy_a",0,"gatehouse_new_snowy_a","bo_gatehouse_new_b_fixed", []),

  ("winch",sokf_moveable,"winch","bo_winch", []),
  ("winch_b",sokf_moveable|spr_use_time(5),"winch_b","bo_winch", []),

  ("drawbridge",0,"drawbridge","bo_drawbridge", []),
  ("gatehouse_door_left",sokf_moveable,"gatehouse_door_left","bo_gatehouse_door_left", []),
  ("gatehouse_door_right",sokf_moveable,"gatehouse_door_right","bo_gatehouse_door_right", []),

  ("cheese_a",0,"cheese_a","0", []),
  ("cheese_b",0,"cheese_b","0", []),
  ("cheese_slice_a",0,"cheese_slice_a","0", []),
  ("bread_a",0,"bread_a","0", []),
  ("bread_b",0,"bread_b","0", []),
  ("bread_slice_a",0,"bread_slice_a","0", []),
  ("fish_a",0,"fish_a","0", []),
  ("fish_roasted_a",0,"fish_roasted_a","0", []),
  ("chicken_roasted",0,"chicken","0", []),
  ("food_steam",0,"0","0",
   [(ti_on_scene_prop_init,
     [(set_position_delta,0,0,0),
      (particle_system_add_new, "psys_food_steam"),
      ]),
    ]),
  ("city_smoke",0,"0","0",
   [(ti_on_scene_prop_init,
     [(store_time_of_day,reg(12)),
      (neg|is_between,reg(12),5,20),
      (set_position_delta,0,0,0),
      (particle_system_add_new, "psys_night_smoke_1"),
      ]),
    ]),
  ("city_fire_fly_night",0,"0","0",
   [(ti_on_scene_prop_init,
     [(store_time_of_day,reg(12)),
      (neg|is_between,reg(12),5,20),
      (set_position_delta,0,0,0),
      (particle_system_add_new, "psys_fire_fly_1"),
      ]),
    ]),
  ("city_fly_day",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_bug_fly_1")])]),
  ("flue_smoke_tall",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_flue_smoke_tall")])]),
  ("flue_smoke_short",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_flue_smoke_short")])]),
  ("moon_beam",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_moon_beam_1"), (particle_system_add_new, "psys_moon_beam_particle_1")])]),
  ("fire_small",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_fireplace_fire_small")])]),
  ("fire_big",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_fireplace_fire_big")])]),
  ("battle_field_smoke",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_war_smoke_tall")])]),
  ("village_fire_big",0,"0","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (prop_instance_play_sound, ":instance_id", "snd_fire_loop"),
      (particle_system_add_new, "psys_village_fire_big"),
      (set_position_delta,0,0,100),
      (particle_system_add_new, "psys_village_fire_smoke_big"),
      ]),
    ]),
  ("candle_a",0,"candle_a","0", [(ti_on_scene_prop_init, [(set_position_delta,0,0,27), (particle_system_add_new, "psys_candle_light")])]),
  ("candle_b",0,"candle_b","0", [(ti_on_scene_prop_init, [(set_position_delta,0,0,25), (particle_system_add_new, "psys_candle_light")])]),
  ("candle_c",0,"candle_c","0", [(ti_on_scene_prop_init, [(set_position_delta,0,0,10), (particle_system_add_new, "psys_candle_light_small")])]),
  ("lamp_a",0,"lamp_a","0", [(ti_on_scene_prop_init, [(set_position_delta,66,0,2), (particle_system_add_new, "psys_candle_light")])]),
  ("lamp_b",0,"lamp_b","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (prop_instance_play_sound, ":instance_id", "snd_fire_loop"),
      (set_position_delta,65,0,-7),
      (particle_system_add_new, "psys_lamp_fire"),
      (set_position_delta,70,0,-5),
      (particle_system_add_new, "psys_fire_glow_1"),
      (particle_system_emit, "psys_fire_glow_1",9000000),
      ]),
    ]),
  ("hook_a",0,"hook_a","0", []),
  ("window_night",0,"window_night","0", []),
  ("fried_pig",0,"pork","0", []),
  ("village_oven",0,"village_oven","bo_village_oven", []),
  ("dungeon_water_drops",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_dungeon_water_drops")])]),
  ("shadow_circle_1",0,"shadow_circle_1","0", []),
  ("shadow_circle_2",0,"shadow_circle_2","0", []),
  ("shadow_square_1",0,"shadow_square_1","0", []),
  ("shadow_square_2",0,"shadow_square_2","0", []),
  ("wheelbarrow",0,"wheelbarrow","bo_wheelbarrow", []),
  ("gourd",sokf_moveable|sokf_destructible|spr_hit_points(1),"gourd","bo_gourd", []),
  ("gourd_spike",sokf_moveable,"gourd_spike","bo_gourd_spike",[]),

  ("obstacle_fence_1",0,"fence","bo_fence", []),
  ("obstacle_fallen_tree_a",0,"destroy_tree_a","bo_destroy_tree_a", []),
  ("obstacle_fallen_tree_b",0,"destroy_tree_b","bo_destroy_tree_b", []),
  ("siege_wall_a",0,"siege_wall_a","bo_siege_wall_a", []),
  ("siege_large_shield_a",0,"siege_large_shield_a","bo_siege_large_shield_a", []),
  ("granary_a",0,"granary_a","bo_granary_a", []),
  ("small_wall_connect_a",0,"small_wall_connect_a","bo_small_wall_connect_a", []),

  ("full_stable_a",0,"full_stable_a","bo_full_stable_a", []),
  ("full_stable_b",0,"full_stable_b","bo_full_stable_b", []),
  ("full_stable_c",0,"full_stable_c","bo_full_stable_c", []),
  ("full_stable_d",0,"full_stable_d","bo_full_stable_d", []),

  ("arabian_house_a",0,"arabian_house_a","bo_arabian_house_a", []),
  ("arabian_house_b",0,"arabian_house_b","bo_arabian_house_b", []),
  ("arabian_house_c",0,"arabian_house_c","bo_arabian_house_c", []),
  ("arabian_house_d",0,"arabian_house_d","bo_arabian_house_d", []),
  ("arabian_house_e",0,"arabian_house_e","bo_arabian_house_e", []),
  ("arabian_house_f",0,"arabian_house_f","bo_arabian_house_f", []),
  ("arabian_house_g",0,"arabian_house_g","bo_arabian_house_g", []),
  ("arabian_house_h",0,"arabian_house_h","bo_arabian_house_h", []),
  ("arabian_house_i",0,"arabian_house_i","bo_arabian_house_i", []),
  ("arabian_square_keep_a",0,"arabian_square_keep_a","bo_arabian_square_keep_a", []),
  ("arabian_passage_house_a",0,"arabian_passage_house_a","bo_arabian_passage_house_a", []),
  ("arabian_wall_a",0,"arabian_wall_a","bo_arabian_wall_a", []),
  ("arabian_wall_b",0,"arabian_wall_b","bo_arabian_wall_b", []),
  ("arabian_ground_a",0,"arabian_ground_a","bo_arabian_ground_a_fixed", []),
  ("arabian_parterre_a",0,"arabian_parterre_a","bo_arabian_parterre_a", []),
  ("well_shaft",spr_use_time(5),"well_shaft","bo_well_shaft", spr_well_triggers()),
  ("horse_mill",0,"horse_mill","bo_horse_mill", []),
  ("horse_mill_collar",0,"horse_mill_collar","bo_horse_mill_collar", []),
  ("arabian_stable",0,"arabian_stable","bo_arabian_stable", []),
  ("arabian_tent",0,"arabian_tent","bo_arabian_tent", []),
  ("arabian_tent_b",0,"arabian_tent_b","bo_arabian_tent_b", []),
  ("desert_plant_a",0,"desert_plant_a","0", []),

  ("arabian_castle_battlement_a",0,"arabian_castle_battlement_a","bo_arabian_castle_battlement_a", []),
  ("arabian_castle_battlement_b_destroyed",0,"arabian_castle_battlement_b_destroyed","bo_arabian_castle_battlement_b_destroyed", []),
  ("arabian_castle_battlement_c",0,"arabian_castle_battlement_c","bo_arabian_castle_battlement_c", []),
  ("arabian_castle_battlement_d",0,"arabian_castle_battlement_d","bo_arabian_castle_battlement_d", []),
  ("arabian_castle_corner_a",0,"arabian_castle_corner_a","bo_arabian_castle_corner_a", []),
  ("arabian_castle_stairs",sokf_type_ladder,"arabian_castle_stairs","bo_arabian_castle_stairs", []),
  ("arabian_castle_stairs_b",sokf_type_ladder,"arabian_castle_stairs_b","bo_arabian_castle_stairs_b", []),
  ("arabian_castle_stairs_c",sokf_type_ladder,"arabian_castle_stairs_c","bo_arabian_castle_stairs_c", []),
  ("arabian_castle_battlement_section_a",0,"arabian_castle_battlement_section_a","bo_arabian_castle_battlement_section_a", []),
  ("arabian_castle_gate_house_a",0,"arabian_castle_gate_house_a","bo_arabian_castle_gate_house_a", []),
  ("arabian_castle_house_a",0,"arabian_castle_house_a","bo_arabian_castle_house_a", []),
  ("arabian_castle_house_b",0,"arabian_castle_house_b","bo_arabian_castle_house_b", []),
  ("arabian_castle_keep_a",0,"arabian_castle_keep_a","bo_arabian_castle_keep_a", []),

  ("arabian_house_a2",0,"arabian_house_a2","bo_arabian_house_a2", []),
  ("arabian_village_house_a",0,"arabian_village_house_a","bo_arabian_village_house_a", []),
  ("arabian_village_house_b",0,"arabian_village_house_b","bo_arabian_village_house_b", []),
  ("arabian_village_house_c",0,"arabian_village_house_c","bo_arabian_village_house_c", []),
  ("arabian_village_house_d",0,"arabian_village_house_d","bo_arabian_village_house_d", []),

  ("arabian_village_stable",0,"arabian_village_stable","bo_arabian_village_stable", []),
  ("arabian_village_hut",0,"arabian_village_hut","bo_arabian_village_hut", []),
  ("arabian_village_stairs",sokf_type_ladder,"arabian_village_stairs","bo_arabian_village_stairs", []),

  ("tree_a01",0,"tree_a01","bo_tree_a01", []),

  ("stairs_a",sokf_type_ladder,"stairs_a","bo_stairs_a", []),

  ("headquarters_flag_red",sokf_moveable|sokf_face_player,"tutorial_flag_red","0", []),
  ("headquarters_flag_blue",sokf_moveable|sokf_face_player,"tutorial_flag_blue","0", []),
  ("headquarters_flag_gray",sokf_moveable|sokf_face_player,"tutorial_flag_yellow","0", []),

  ("headquarters_flag_red_code_only",sokf_moveable|sokf_face_player,"mp_flag_red","0", []),
  ("headquarters_flag_blue_code_only",sokf_moveable|sokf_face_player,"mp_flag_blue","0", []),
  ("headquarters_flag_gray_code_only",sokf_moveable|sokf_face_player,"mp_flag_white","0", []),
  ("headquarters_pole_code_only",sokf_moveable,"mp_flag_pole","0", []),

  ("headquarters_flag_swadian",sokf_moveable|sokf_face_player,"flag_swadian","0", []),
  ("headquarters_flag_vaegir",sokf_moveable|sokf_face_player,"flag_vaegir","0", []),
  ("headquarters_flag_khergit",sokf_moveable|sokf_face_player,"flag_khergit","0", []),
  ("headquarters_flag_nord",sokf_moveable|sokf_face_player,"flag_nord","0", []),
  ("headquarters_flag_rhodok",sokf_moveable|sokf_face_player,"flag_rhodok","0", []),
  ("headquarters_flag_sarranid",sokf_moveable|sokf_face_player,"flag_sarranid","0", []),

  ("glow_a", 0, "glow_a", "0", []),
  ("glow_b", 0, "glow_b", "0", []),

  ("arabian_castle_corner_b",0,"arabian_castle_corner_b","bo_arabian_castle_corner_b", []),

  ("dummy_a_undestructable",sokf_destructible,"arena_archery_target_b","bo_arena_archery_target_b", []),
  ("cave_entrance_1",0,"cave_entrance_1","bo_cave_entrance_1", []),

  ("pointer_arrow", 0, "pointer_arrow", "0", []),
  ("fireplace_d_interior",0,"fireplace_d","bo_fireplace_d", []),
  ("ship_sail_off",0,"ship_sail_off","bo_ship_sail_off", []),
  ("ship_sail_off_b",0,"ship_sail_off_b","bo_ship_sail_off", []),
  ("ship_c_sail_off",0,"ship_c_sail_off","bo_ship_c_sail_off", []),
  ("ramp_small_a",0,"ramp_small_a","bo_ramp_small_a", []),
  ("castle_g_battlement_b",0,"castle_g_battlement_b","bo_castle_g_battlement_b", []),
  ("box_a_dynamic",sokf_moveable|sokf_dynamic_physics,"box_a","bo_box_a", []),

  ("desert_field",0,"desert_field","bo_desert_field", []),

  ("water_river",0,"water_plane","0", []),
  ("viking_house_a",0,"viking_house_a","bo_viking_house_a", []),
  ("viking_house_b",0,"viking_house_b","bo_viking_house_b", []),
  ("viking_house_c",0,"viking_house_c","bo_viking_house_c", []),
  ("viking_house_d",0,"viking_house_d","bo_viking_house_d", []),
  ("viking_house_e",0,"viking_house_e","bo_viking_house_e", []),
  ("viking_stable_a",0,"viking_stable_a","bo_viking_stable_a", []),
  ("viking_keep",0,"viking_keep","bo_viking_keep", []),

  ("viking_house_c_destroy",0,"viking_house_c_destroy","bo_viking_house_c_destroy", []),
  ("viking_house_b_destroy",0,"viking_house_b_destroy","bo_viking_house_b_destroy", []),

  ("harbour_a",0,"harbour_a","bo_harbour_a", []),
  ("sea_foam_a",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_sea_foam_a")])]),

  ("viking_keep_destroy",0,"viking_keep_destroy","bo_viking_keep_destroy", []),
  ("viking_keep_destroy_door",0,"viking_keep_destroy_door","bo_viking_keep_destroy_door", []),
  ("earth_tower_small_b",0,"earth_tower_small_b","bo_earth_tower_small_b", []),
  ("earth_gate_house_b",0,"earth_gate_house_b","bo_earth_gate_house_b", []),
  ("earth_tower_a",0,"earth_tower_a","bo_earth_tower_a", []),
  ("earth_stairs_c",0,"earth_stairs_c","bo_earth_stairs_c", []),

  ("earth_sally_gate_left",sokf_moveable|sokf_destructible|spr_use_time(0),"earth_sally_gate_left","bo_earth_sally_gate_left", []),
  ("earth_sally_gate_right",sokf_moveable|sokf_destructible|spr_use_time(0),"earth_sally_gate_right","bo_earth_sally_gate_right", []),

  ("barrier_box",sokf_invisible|sokf_type_barrier3d,"barrier_box","bo_barrier_box", []),
  ("barrier_capsule",sokf_invisible|sokf_type_barrier3d,"barrier_capsule","bo_barrier_capsule", []),
  ("barrier_cone" ,sokf_invisible|sokf_type_barrier3d,"barrier_cone" ,"bo_barrier_cone" , []),
  ("barrier_sphere" ,sokf_invisible|sokf_type_barrier3d,"barrier_sphere" ,"bo_barrier_sphere" , []),

  ("viking_keep_destroy_sally_door_right",sokf_moveable|sokf_destructible|spr_use_time(0),"viking_keep_destroy_sally_door_right","bo_viking_keep_destroy_sally_door_right", []),
  ("viking_keep_destroy_sally_door_left",sokf_moveable|sokf_destructible|spr_use_time(0),"viking_keep_destroy_sally_door_left","bo_viking_keep_destroy_sally_door_left", []),

  ("castle_f_door_b",sokf_moveable|sokf_destructible|spr_use_time(0),"castle_e_sally_door_a","bo_castle_e_sally_door_a", []),

  ("ctf_flag_kingdom_1", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_1", "0", []),
  ("ctf_flag_kingdom_2", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_2", "0", []),
  ("ctf_flag_kingdom_3", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_3", "0", []),
  ("ctf_flag_kingdom_4", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_4", "0", []),
  ("ctf_flag_kingdom_5", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_5", "0", []),
  ("ctf_flag_kingdom_6", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_6", "0", []),
  ("ctf_flag_kingdom_7", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_7", "0", []),

  ("headquarters_flag_rebel",sokf_moveable|sokf_face_player,"flag_rebel","0", []),
  ("arabian_lighthouse_a",0,"arabian_lighthouse_a","bo_arabian_lighthouse_a", []),
  ("arabian_ramp_a",0,"arabian_ramp_a","bo_arabian_ramp_a", []),
  ("arabian_ramp_b",0,"arabian_ramp_b","bo_arabian_ramp_b", []),

  ("winery_interior",0,"winery_interior","bo_winery_interior", []),
  ("winery_barrel_shelf",0,"winery_barrel_shelf","bo_winery_barrel_shelf", []),
  ("winery_wall_shelf",0,"winery_wall_shelf","bo_winery_wall_shelf", []),
  ("winery_huge_barrel",0,"winery_huge_barrel","bo_winery_huge_barrel", []),
  ("winery_wine_press",0,"winery_wine_press","bo_winery_wine_press", []),
  ("winery_middle_barrel",0,"winery_middle_barrel","bo_winery_middle_barrel", []),
  ("winery_wine_cart_small_loaded",0,"winery_wine_cart_small_loaded","bo_winery_wine_cart_small_loaded", []),
  ("winery_wine_cart_small_empty",0,"winery_wine_cart_small_empty","bo_winery_wine_cart_small_empty", []),
  ("winery_wine_cart_empty",0,"winery_wine_cart_empty","bo_winery_wine_cart_empty", []),
  ("winery_wine_cart_loaded",0,"winery_wine_cart_loaded","bo_winery_wine_cart_loaded", []),

  ("weavery_interior",0,"weavery_interior","bo_weavery_interior", []),
  ("weavery_loom_a",0,"weavery_loom_a","bo_weavery_loom_a", []),
  ("weavery_spinning_wheel",0,"weavery_spinning_wheel","bo_weavery_spinning_wheel", []),

  ("mill_interior",0,"mill_interior","bo_mill_interior", []),
  ("mill_flour_sack", 0,"mill_flour_sack","bo_mill_flour_sack", []),
  ("mill_flour_sack_desk_a", 0,"mill_flour_sack_desk_a","bo_mill_flour_sack_desk_a", []),
  ("mill_flour_sack_desk_b", 0,"mill_flour_sack_desk_b","bo_mill_flour_sack_desk_b", []),

  ("smithy_interior", 0,"smithy_interior","bo_smithy_interior", []),
  ("smithy_grindstone_wheel", 0,"smithy_grindstone_wheel","bo_smithy_grindstone_wheel", []),
  ("smithy_forge_bellows", 0,"smithy_forge_bellows","bo_smithy_forge_bellows", []),
  ("smithy_forge", 0,"smithy_forge","bo_smithy_forge", []),
  ("smithy_anvil", 0,"smithy_anvil","bo_smithy_anvil", []),

  ("tannery_hide_a", 0,"pw_tannery_hide_a","0", []),
  ("tannery_hide_b", 0,"pw_tannery_hide_b","0", []),
  ("tannery_pools_a", 0,"tannery_pools_a","bo_tannery_pools_a", []),
  ("tannery_pools_b", 0,"tannery_pools_b","bo_tannery_pools_b", []),

  ("fountain", spr_use_time(10), "fountain", "bo_fountain", spr_well_triggers()),

  ("rhodok_houses_a",0,"rhodok_houses_a","bo_rhodok_houses_a", []),
  ("rhodok_houses_b",0,"rhodok_houses_b","bo_rhodok_houses_b", []),
  ("rhodok_houses_c",0,"rhodok_houses_c","bo_rhodok_houses_c", []),
  ("rhodok_houses_d",0,"rhodok_houses_d","bo_rhodok_houses_d", []),
  ("rhodok_houses_e",0,"rhodok_houses_e","bo_rhodok_houses_e", []),
  ("rhodok_house_passage_a",0,"rhodok_house_passage_a","bo_rhodok_house_passage_a", []),

  ("bridge_b",0,"bridge_b","bo_bridge_b", []),

  ("brewery_pool", 0,"brewery_pool","bo_brewery_pool", []),
  ("brewery_big_bucket", 0,"brewery_big_bucket","bo_brewery_big_bucket", []),
  ("brewery_interior", 0,"brewery_interior","bo_brewery_interior", []),
  ("brewery_bucket_platform_a", 0,"brewery_bucket_platform_a","bo_brewery_bucket_platform_a", []),
  ("brewery_bucket_platform_b", 0,"brewery_bucket_platform_b","bo_brewery_bucket_platform_b", []),

  ("weavery_dye_pool_r",0,"weavery_dye_pool_r","bo_weavery_dye_pool_r", []),
  ("weavery_dye_pool_y",0,"weavery_dye_pool_y","bo_weavery_dye_pool_y", []),
  ("weavery_dye_pool_b",0,"weavery_dye_pool_b","bo_weavery_dye_pool_b", []),
  ("weavery_dye_pool_p",0,"weavery_dye_pool_p","bo_weavery_dye_pool_p", []),
  ("weavery_dye_pool_g",0,"weavery_dye_pool_g","bo_weavery_dye_pool_g", []),

  ("oil_press_interior",0,"oil_press_interior","bo_oil_press_interior", []),

  ("city_swad_01" ,0,"city_swad_01" ,"bo_city_swad_01" , []),
  ("city_swad_02" ,0,"city_swad_02" ,"bo_city_swad_02" , []),
  ("city_swad_03" ,0,"city_swad_03" ,"bo_city_swad_03" , []),
  ("city_swad_04" ,0,"city_swad_04" ,"bo_city_swad_04" , []),
  ("city_swad_passage_01" ,0,"city_swad_passage_01" ,"bo_city_swad_passage_01" , []),
  ("city_swad_05" ,0,"city_swad_05" ,"bo_city_swad_05" , []),

  ("arena_block_j_a",0,"arena_block_j_a","bo_arena_block_j_a", []),
  ("arena_underway_a",0,"arena_underway_a","bo_arena_underway_a", []),
  ("arena_circle_a",0,"arena_circle_a","bo_arena_circle_a", []),

  ("rope_bridge_15m",0,"rope_bridge_15m","bo_rope_bridge_15m", []),
  ("tree_house_a",0,"tree_house_a","bo_tree_house_a", []),
  ("tree_house_guard_a",0,"tree_house_guard_a","bo_tree_house_guard_a", []),
  ("tree_house_guard_b",0,"tree_house_guard_b","bo_tree_house_guard_b", []),
  ("tree_shelter_a",0,"tree_shelter_a","bo_tree_shelter_a", []),
  ("yellow_fall_leafs_a",0,"0","0", [(ti_on_scene_prop_init, [(particle_system_add_new, "psys_fall_leafs_a")])]),

  ("rock_bridge_a",0,"rock_bridge_a","bo_rock_bridge_a", []),
  ("suspension_bridge_a",0,"suspension_bridge_a","bo_suspension_bridge_a", []),
  ("mine_a",0,"mine_a","bo_mine_a", []),

  ("snowy_destroy_house_a",0,"snowy_destroy_house_a","bo_snowy_destroy_house_a", []),
  ("snowy_destroy_house_b",0,"snowy_destroy_house_b","bo_snowy_destroy_house_b", []),
  ("snowy_destroy_house_c",0,"snowy_destroy_house_c","bo_snowy_destroy_house_c", []),
  ("snowy_destroy_heap",0,"snowy_destroy_heap","bo_snowy_destroy_heap", []),
  ("snowy_destroy_castle_a",0,"snowy_destroy_castle_a","bo_snowy_destroy_castle_a", []),
  ("snowy_destroy_castle_b",0,"snowy_destroy_castle_b","bo_snowy_destroy_castle_b", []),
  ("snowy_destroy_castle_c",0,"snowy_destroy_castle_c","bo_snowy_destroy_castle_c", []),
  ("snowy_destroy_castle_d",0,"snowy_destroy_castle_d","bo_snowy_destroy_castle_d", []),
  ("snowy_destroy_windmill",0,"snowy_destroy_windmill","bo_snowy_destroy_windmill", []),
  ("snowy_destroy_tree_a",0,"snowy_destroy_tree_a","bo_snowy_destroy_tree_a", []),
  ("snowy_destroy_tree_b",0,"snowy_destroy_tree_b","bo_snowy_destroy_tree_b", []),
  ("snowy_destroy_bridge_a",0,"snowy_destroy_bridge_a","bo_snowy_destroy_bridge_a", []),
  ("snowy_destroy_bridge_b",0,"snowy_destroy_bridge_b","bo_snowy_destroy_bridge_b", []),

  ("prison_cart",sokf_moveable,"prison_cart","bo_prison_cart", []),
  ("prison_cart_door_right",spr_rotate_door_flags(),"prison_cart_door_right","bo_prison_cart_door_right", spr_rotate_door_triggers(hit_points=3000, left=1)),
  ("prison_cart_door_left",spr_rotate_door_flags(),"prison_cart_door_left","bo_prison_cart_door_left", spr_rotate_door_triggers(hit_points=3000, left=0)),

  ("castle_h_battlement_b3",0,"castle_h_battlement_b3","bo_castle_h_battlement_b3", []),
  ("castle_h_gatehouse_a2",0,"castle_h_gatehouse_a2","bo_castle_h_gatehouse_a2", []),
  ("arena_palisade_b",0,"pw_wooden_palisade_b","bo_pw_wooden_palisade_b", []),

  ("interior_castle_a",0,"interior_castle_a","bo_interior_castle_a", []),
  ("interior_castle_b",0,"interior_castle_b","bo_interior_castle_b", []),
  ("interior_castle_c",0,"interior_castle_c","bo_interior_castle_c", []),
  ("interior_castle_d",0,"interior_castle_d","bo_interior_castle_d", []),
  ("interior_castle_e",0,"interior_castle_e","bo_interior_castle_e", []),
  ("interior_castle_f",0,"interior_castle_f","bo_interior_castle_f", []),
  ("interior_castle_g",0,"interior_castle_g","bo_interior_castle_g", []),
  ("interior_castle_h",0,"interior_castle_h","bo_interior_castle_h", []),
  ("interior_castle_i",0,"interior_castle_i","bo_interior_castle_i", []),
  ("interior_castle_j",0,"interior_castle_j","bo_interior_castle_j", []),
  ("interior_castle_k",0,"interior_castle_k","bo_interior_castle_k", []),
  ("interior_castle_l",0,"interior_castle_l","bo_interior_castle_l", []),
  ("interior_castle_m",0,"interior_castle_m","bo_interior_castle_m", []),
  ("interior_castle_n",0,"interior_castle_n","bo_interior_castle_n", []),
  ("interior_castle_o",0,"interior_castle_o","bo_interior_castle_o", []),
  ("interior_castle_p",0,"interior_castle_p","bo_interior_castle_p", []),
  ("interior_castle_q",0,"interior_castle_q","bo_interior_castle_q", []),
  ("interior_castle_r",0,"interior_castle_r","bo_interior_castle_r", []),
  ("interior_castle_t",0,"interior_castle_t","bo_interior_castle_t", []),
  ("interior_castle_u",0,"interior_castle_u","bo_interior_castle_u", []),
  ("interior_castle_v",0,"interior_castle_v","bo_interior_castle_v", []),
  ("interior_castle_w",0,"interior_castle_w","bo_interior_castle_w", []),
  ("interior_castle_x",0,"interior_castle_x","bo_interior_castle_x", []),
  ("interior_castle_y",0,"interior_castle_y","bo_interior_castle_y", []),
  ("interior_castle_z",0,"interior_castle_z","bo_interior_castle_z", []),
  ("interior_square_keep_a",0,"interior_square_keep_a","bo_interior_square_keep_a", []),
  ("interior_square_keep_b",0,"interior_square_keep_b","bo_interior_square_keep_b", []),
  ("interior_round_keep_a",0,"interior_round_keep_a","bo_interior_round_keep_a", []),
  ("interior_castle_g_square_keep",0,"interior_castle_g_square_keep","bo_interior_castle_g_square_keep", []),
  ("castle_h_interior_a",0,"castle_h_interior_a","bo_castle_h_interior_a", []),
  ("castle_h_interior_b",0,"castle_h_interior_b","bo_castle_h_interior_b", []),
  ("interior_house_a",0,"interior_house_a","bo_interior_house_a", []),
  ("interior_house_b",0,"interior_house_b","bo_interior_house_b", []),
  ("interior_tavern_a",0,"interior_tavern_a","bo_interior_tavern_a", []),
  ("interior_tavern_b",0,"interior_tavern_b","bo_interior_tavern_b", []),
  ("interior_tavern_c",0,"interior_tavern_c","bo_interior_tavern_c", []),
  ("interior_tavern_d",0,"interior_tavern_d","bo_interior_tavern_d", []),
  ("interior_tavern_e",0,"interior_tavern_e","bo_interior_tavern_e", []),
  ("interior_tavern_f",0,"interior_tavern_f","bo_interior_tavern_f", []),
  ("interior_tavern_g",0,"interior_tavern_g","bo_interior_tavern_g", []),
  ("interior_tavern_h",0,"interior_tavern_h","bo_interior_tavern_h", []),
  ("interior_town_house_aa",0,"interior_town_house_aa","bo_interior_town_house_aa", []),
  ("interior_town_house_a",0,"interior_town_house_a","bo_interior_town_house_a", []),
  ("interior_town_house_c",0,"interior_town_house_c","bo_interior_town_house_c", []),
  ("interior_town_house_d",0,"interior_town_house_d","bo_interior_town_house_d", []),
  ("interior_town_house_e",0,"interior_town_house_e","bo_interior_town_house_e", []),
  ("interior_town_house_f",0,"interior_town_house_f","bo_interior_town_house_f", []),
  ("interior_town_house_i",0,"interior_town_house_i","bo_interior_town_house_i", []),
  ("interior_town_house_j",0,"interior_town_house_j","bo_interior_town_house_j", []),
  ("interior_town_house_steppe_c",0,"interior_town_house_steppe_c","bo_interior_town_house_steppe_c", []),
  ("interior_town_house_steppe_d",0,"interior_town_house_steppe_d","bo_interior_town_house_steppe_d", []),
  ("interior_town_house_steppe_g",0,"interior_town_house_steppe_g","bo_interior_town_house_steppe_g", []),
  ("interior_house_extension_h",0,"interior_house_extension_h","bo_interior_house_extension_h", []),
  ("arabian_interior_keep_a",0,"arabian_interior_keep_a","bo_arabian_interior_keep_a", []),
  ("arabian_interior_keep_b",0,"arabian_interior_keep_b","bo_arabian_interior_keep_b", []),
  ("viking_interior_keep_a",0,"viking_interior_keep_a","bo_viking_interior_keep_a", []),
  ("viking_interior_merchant_a",0,"viking_interior_merchant_a","bo_viking_interior_merchant_a", []),
  ("viking_interior_tavern_a",0,"viking_interior_tavern_a","bo_viking_interior_tavern_a", []),
  ("interior_rhodok_houses_b",0,"interior_rhodok_houses_b","bo_interior_rhodok_houses_b", []),
  ("interior_rhodok_houses_d",0,"interior_rhodok_houses_d","bo_interior_rhodok_houses_d", []),
  ("interior_prison_e",0,"interior_prison_e","bo_interior_prison_e", []),
  ("interior_prison_f",0,"interior_prison_f","bo_interior_prison_f", []),
  ("interior_prison_g",0,"interior_prison_g","bo_interior_prison_g", []),
  ("interior_prison_h",0,"interior_prison_h","bo_interior_prison_h", []),
  ("interior_prison_i",0,"interior_prison_i","bo_interior_prison_i", []),
  ("interior_prison_j",0,"interior_prison_j","bo_interior_prison_j", []),
  ("interior_prison_k",0,"interior_prison_k","bo_interior_prison_k", []),
  ("interior_prison_l",0,"interior_prison_l","bo_interior_prison_l", []),
  ("interior_prison_m",0,"interior_prison_m","bo_interior_prison_m", []),
  ("interior_prison_n",0,"interior_prison_n","bo_interior_prison_n", []),
  ("interior_prison_o",0,"interior_prison_o","bo_interior_prison_o", []),
  ("interior_tutorial_1",0,"tutorial_1_scene","bo_tutorial_1_scene", []),
  ("interior_tutorial_2",0,"tutorial_2_scene","bo_tutorial_2_scene", []),
  ("interior_tutorial_3",0,"tutorial_3_scene","bo_tutorial_3_scene", []),
  ("interior_training_house",0,"training_house_a","bo_training_house_a", []),
  ("interior_dungeon_a",0,"dungeon_a","bo_dungeon_a", []),
  ("interior_window_cover",0,"pw_window_cover","bo_pw_window_cover", []),
  ("merchant_shelf_a",0,"merchant_shelf_a","bo_merchant_shelf_a", []),

  ("enterable_church_a",0,"pw_enterable_church_a","bo_pw_enterable_church_a",[]),
  ("enterable_church_b",0,"pw_enterable_church_b","bo_pw_enterable_church_b",[]),
  ("enterable_church_b2",0,"pw_enterable_church_b2","bo_pw_enterable_church_b",[]),
  ("enterable_church_b3",0,"pw_enterable_church_b3","bo_pw_enterable_church_b",[]),
  ("enterable_castle_house_b",0,"pw_enterable_castle_house_b","bo_pw_enterable_castle_house_b",[]),
  ("enterable_castle_house_b2",0,"pw_enterable_castle_house_b2","bo_pw_enterable_castle_house_b",[]),
  ("enterable_castle_house_b3",0,"pw_enterable_castle_house_b3","bo_pw_enterable_castle_house_b",[]),
  ("enterable_castle_house_c",0,"pw_enterable_castle_house_c","bo_pw_enterable_castle_house_c",[]),
  ("enterable_castle_h_keep_a",0,"pw_enterable_castle_h_keep_a","bo_pw_enterable_castle_h_keep_a",[]),
  ("enterable_town_house_o",0,"pw_enterable_town_house_o","bo_pw_enterable_town_house_o",[]),
  ("enterable_town_house_s",0,"pw_enterable_town_house_s","bo_pw_enterable_town_house_s",[]),
  ("enterable_town_house_s2",0,"pw_enterable_town_house_s2","bo_pw_enterable_town_house_s",[]),
  ("enterable_town_house_s3",0,"pw_enterable_town_house_s3","bo_pw_enterable_town_house_s",[]),
  ("enterable_city_swad_2",0,"pw_enterable_city_swad_2","bo_pw_enterable_city_swad_2",[]),
  ("enterable_city_swad_5",0,"pw_enterable_city_swad_5","bo_pw_enterable_city_swad_5",[]),
  ("enterable_village_house_e",0,"pw_enterable_village_house_e","bo_pw_enterable_village_house_e",[]),
  ("enterable_village_house_e_snowy",0,"pw_enterable_village_house_e_snowy","bo_pw_enterable_village_house_e",[]),
  ("enterable_village_house_f",0,"pw_enterable_village_house_f","bo_pw_enterable_village_house_f",[]),
  ("enterable_village_house_f_snowy",0,"pw_enterable_village_house_f_snowy","bo_pw_enterable_village_house_f",[]),
  ("enterable_village_house_f_ceiling_a",0,"pw_enterable_village_house_f_ceiling_a","bo_pw_enterable_village_house_f_ceiling_a",[]),
  ("enterable_village_house_f_ceiling_b",0,"pw_enterable_village_house_f_ceiling_b","bo_pw_enterable_village_house_f_ceiling_b",[]),
  ("enterable_village_house_f_wall_a",0,"pw_enterable_village_house_f_wall_a","bo_pw_enterable_village_house_f_wall_a",[]),
  ("enterable_village_house_g",0,"pw_enterable_village_house_g","bo_pw_enterable_village_house_g",[]),
  ("enterable_village_house_h",0,"pw_enterable_village_house_h","bo_pw_enterable_village_house_h",[]),
  ("enterable_steppe_village_house_a",0,"pw_enterable_steppe_village_house_a","bo_pw_enterable_steppe_village_house_a",[]),
  ("enterable_steppe_village_house_d",0,"pw_enterable_steppe_village_house_d","bo_pw_enterable_steppe_village_house_d",[]),
  ("enterable_steppe_village_hut",0,"pw_enterable_steppe_village_hut","bo_pw_enterable_steppe_village_hut",[]),
  ("enterable_steppe_town_house_g",0,"pw_enterable_steppe_town_house_g","bo_pw_enterable_steppe_town_house_g",[]),
  ("enterable_arabian_village_house_b",0,"pw_enterable_arabian_village_house_b","bo_pw_enterable_arabian_village_house_b",[]),
  ("enterable_arabian_village_house_d",0,"pw_enterable_arabian_village_house_d","bo_pw_enterable_arabian_village_house_d",[]),
  ("enterable_rhodok_house_e",0,"pw_enterable_rhodok_house_e","bo_pw_enterable_rhodok_house_e",[]),
  ("enterable_earth_house_d",0,"pw_enterable_earth_house_d","bo_pw_enterable_earth_house_d",[]),
  ("enterable_viking_house_c",0,"pw_enterable_viking_house_c","bo_pw_enterable_viking_house_c",[]),
  ("enterable_viking_house_e",0,"pw_enterable_viking_house_e","bo_pw_enterable_viking_house_e",[]),

  ("tunnel_chasm",0,"pw_tunnel_chasm","bo_pw_tunnel_chasm",[]),
  ("tunnel_crossing",0,"pw_tunnel_crossing","bo_pw_tunnel_crossing",[]),
  ("tunnel_crossing_supports",0,"pw_tunnel_crossing_supports","bo_pw_tunnel_crossing_supports",[]),
  ("tunnel_curved_left",0,"pw_tunnel_curved_left","bo_pw_tunnel_curved_left",[]),
  ("tunnel_curved_left_supports",0,"pw_tunnel_curved_left_supports","bo_pw_tunnel_curved_left_supports",[]),
  ("tunnel_curved_right",0,"pw_tunnel_curved_right","bo_pw_tunnel_curved_right",[]),
  ("tunnel_curved_right_supports",0,"pw_tunnel_curved_right_supports","bo_pw_tunnel_curved_right_supports",[]),
  ("tunnel_end",0,"pw_tunnel_end","bo_pw_tunnel_end",[]),
  ("tunnel_room",0,"pw_tunnel_room","bo_pw_tunnel_room",[]),
  ("tunnel_room_corner",0,"pw_tunnel_room_corner","bo_pw_tunnel_room_corner",[]),
  ("tunnel_room_corner_supports",0,"pw_tunnel_room_corner_supports","bo_pw_tunnel_room_corner_supports",[]),
  ("tunnel_short",0,"pw_tunnel_short","bo_pw_tunnel_short",[]),
  ("tunnel_short_supports",0,"pw_tunnel_short_supports","bo_pw_tunnel_short_supports",[]),
  ("tunnel_sloped",0,"pw_tunnel_sloped","bo_pw_tunnel_sloped",[]),
  ("tunnel_sloped_supports",0,"pw_tunnel_sloped_supports","bo_pw_tunnel_sloped_supports",[]),
  ("tunnel_split",0,"pw_tunnel_split","bo_pw_tunnel_split",[]),
  ("tunnel_split_supports",0,"pw_tunnel_split_supports","bo_pw_tunnel_split_supports",[]),
  ("tunnel_straight",0,"pw_tunnel_straight","bo_pw_tunnel_straight",[]),
  ("tunnel_straight_supports",0,"pw_tunnel_straight_supports","bo_pw_tunnel_straight_supports",[]),
  ("tunnel_support",0,"pw_tunnel_support","bo_pw_tunnel_support",[]),

  ("rock_1",0,"rock1","bo_rock1", []),
  ("rock_2",0,"rock2","bo_rock2", []),
  ("rock_3",0,"rock3","bo_rock3", []),
  ("rock_4",0,"rock4","bo_rock4", []),
  ("rock_5",0,"rock5","bo_rock5", []),
  ("rock_6",0,"rock6","bo_rock6", []),
  ("rock_7",0,"rock7","bo_rock7", []),
  ("rock_a",0,"rock_a","bo_rock_a_fixed", []),
  ("rock_b",0,"rock_b","bo_rock_b_fixed", []),
  ("rock_c",0,"rock_c","bo_rock_c", []),
  ("rock_d",0,"rock_d","bo_rock_d", []),
  ("rock_e",0,"rock_e","bo_rock_e", []),
  ("rock_f",0,"rock_f","bo_rock_f", []),
  ("rock_g",0,"rock_g","bo_rock_g", []),
  ("rock_h",0,"rock_h","bo_rock_h", []),
  ("rock_i",0,"rock_i","bo_rock_i", []),
  ("rock_k",0,"rock_k","bo_rock_k", []),
  ("rock_medium_1",0,"pw_rock_medium_1","bo_pw_rock_medium_1", []),
  ("rock_medium_2",0,"pw_rock_medium_2","bo_pw_rock_medium_2", []),
  ("rock_medium_3",0,"pw_rock_medium_3","bo_pw_rock_medium_3", []),
  ("rock_medium_4",0,"pw_rock_medium_4","bo_pw_rock_medium_4", []),
  ("rock_small_1",0,"pw_rock_small_1","bo_pw_rock_small_1", []),
  ("rock_small_2",0,"pw_rock_small_2","bo_pw_rock_small_2", []),
  ("rock_small_3",0,"pw_rock_small_3","bo_pw_rock_small_3", []),
  ("rock_small_4",0,"pw_rock_small_4","bo_pw_rock_small_4", []),
  ("rock_small_5",0,"pw_rock_small_5","bo_pw_rock_small_5", []),
  ("rock_small_6",0,"pw_rock_small_6","bo_pw_rock_small_6", []),
  ("rock_small_7",0,"pw_rock_small_7","bo_pw_rock_small_7", []),
  ("tree_stump_a",0,"tree_stump_a","bo_tree_stump_a", []),
  ("tree_stump_b",0,"tree_stump_b","bo_tree_stump_b", []),
  ("tree_stump_c",0,"tree_stump_c","bo_tree_stump_c", []),

  ("pw_tree_a1",spr_tree_flags(),"tree_a01","bo_tree_a01_fixed", spr_tree_triggers(full_hp=3500, fell_hp=1200)),
  ("pw_tree_a2",spr_tree_flags(),"tree_a02","bo_tree_a02_fixed", spr_tree_triggers(full_hp=4000, fell_hp=1700)),
  ("pw_tree_b1",spr_tree_flags(),"tree_b01","bo_tree_b01_fixed", spr_tree_triggers(full_hp=3000, fell_hp=1500)),
  ("pw_tree_b2",spr_tree_flags(),"tree_b02","bo_tree_b02_fixed", spr_tree_triggers(full_hp=3200, fell_hp=1500)),
  ("pw_tree_c1",spr_tree_flags(),"tree_c01","bo_tree_c01_fixed", spr_tree_triggers(full_hp=2500, fell_hp=1100)),
  ("pw_tree_c2",spr_tree_flags(),"tree_c02","bo_tree_c02_fixed", spr_tree_triggers(full_hp=3000, fell_hp=1300)),
  ("pw_tree_e1",spr_tree_flags(),"tree_e_1_fixed","bo_tree_e_1_fixed", spr_tree_triggers(full_hp=2500, fell_hp=1200, resource_imod=imod_battered)),
  ("pw_tree_e2",spr_tree_flags(),"tree_e_2_fixed","bo_tree_e_2_fixed", spr_tree_triggers(full_hp=2100, fell_hp=800, resource_imod=imod_battered)),
  ("pw_tree_e3",spr_tree_flags(),"tree_e_3_fixed","bo_tree_e_3_fixed", spr_tree_triggers(full_hp=2300, fell_hp=900, resource_imod=imod_battered)),
  ("pw_tree_f1",spr_tree_flags(),"tree_f_1","bo_tree_f_1_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000)),
  ("pw_tree_f2",spr_tree_flags(),"tree_f_2","bo_tree_f_1_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000)),
  ("pw_tree_f3",spr_tree_flags(),"tree_f_3","bo_tree_f_1_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000)),
  ("pw_tree_aspen_a",spr_tree_flags(),"aspen_a","bo_aspen_a", spr_tree_triggers(full_hp=2000, fell_hp=500)),
  ("pw_tree_aspen_b",spr_tree_flags(),"aspen_b","bo_aspen_b", spr_tree_triggers(full_hp=2000, fell_hp=500)),
  ("pw_tree_aspen_c",spr_tree_flags(),"aspen_c","bo_aspen_c", spr_tree_triggers(full_hp=3000, fell_hp=700)),
  ("pw_tree_pine_1a",spr_tree_flags(),"pine_1_a","bo_pine_1_a", spr_tree_triggers(full_hp=5000, fell_hp=2000, resource_hp=200, resource_imod=imod_heavy)),
  ("pw_tree_pine_1b",spr_tree_flags(),"pine_1_b","bo_pine_1_b", spr_tree_triggers(full_hp=5000, fell_hp=2000, resource_hp=200, resource_imod=imod_heavy)),
  ("pw_tree_pine_2a",spr_tree_flags(),"pine_2_a","bo_pine_2_a", spr_tree_triggers(full_hp=5000, fell_hp=2000, resource_hp=200, resource_imod=imod_heavy)),
  ("pw_tree_pine_3a",spr_tree_flags(),"pine_3_a","bo_pine_3_a", spr_tree_triggers(full_hp=5000, fell_hp=2000, resource_hp=200, resource_imod=imod_heavy)),
  ("pw_tree_pine_4a",spr_tree_flags(),"pine_4_a","bo_pine_4_a", spr_tree_triggers(full_hp=5000, fell_hp=2000, resource_hp=200, resource_imod=imod_heavy)),
  ("pw_tree_pine_6a",spr_tree_flags(),"pine_6_a","bo_pine_6_a", spr_tree_triggers(full_hp=5000, fell_hp=2000, resource_hp=200, resource_imod=imod_heavy)),
  ("pw_tree_plane_a",spr_tree_flags(),"tree_plane_a","bo_tree_plane_a_fixed", spr_tree_triggers(full_hp=3500, fell_hp=1400)),
  ("pw_tree_plane_b",spr_tree_flags(),"tree_plane_b","bo_tree_plane_b_fixed", spr_tree_triggers(full_hp=3000, fell_hp=1000)),
  ("pw_tree_plane_c",spr_tree_flags(),"tree_plane_c","bo_tree_plane_c_fixed", spr_tree_triggers(full_hp=2500, fell_hp=1000)),
  ("pw_tree_plane_d",spr_tree_flags(),"plane_d","bo_plane_d_fixed", spr_tree_triggers(full_hp=1700, fell_hp=600)),
  ("pw_tree_beech_d",spr_tree_flags(),"beech_d","bo_beech_d_fixed", spr_tree_triggers(full_hp=3500, fell_hp=1500, resource_imod=imod_battered)),
  ("pw_tree_beech_e",spr_tree_flags(),"beech_e","bo_beech_e_fixed", spr_tree_triggers(full_hp=3800, fell_hp=1700, resource_imod=imod_battered)),
  ("pw_tree_tall_a",spr_tree_flags(),"tall_tree_a","bo_tall_tree_a_fixed", spr_tree_triggers(full_hp=3000, fell_hp=1300, resource_hp=200)),
  ("pw_tree_snowy_a",spr_tree_flags(),"tree_snowy_a","bo_tree_snowy_a", spr_tree_triggers(full_hp=6000, fell_hp=1900, resource_imod=imod_heavy)),
  ("pw_tree_snowy_b",spr_tree_flags(),"snowy_pine_2","bo_snowy_pine_2_fixed", spr_tree_triggers(full_hp=6000, fell_hp=2000, resource_imod=imod_heavy)),
  ("pw_tree_1a",spr_tree_flags(),"tree_1_a","bo_tree_1_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000)),
  ("pw_tree_1b",spr_tree_flags(),"tree_1_b","bo_tree_1_b_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000)),
  ("pw_tree_2a",spr_tree_flags(),"tree_2_a_fixed","bo_tree_1_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000)),
  ("pw_tree_2b",spr_tree_flags(),"tree_2_b_fixed","bo_tree_1_b_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000)),
  ("pw_tree_3a",spr_tree_flags(),"tree_3_a","bo_tree_3_a_fixed", spr_tree_triggers(full_hp=2500, fell_hp=1300)),
  ("pw_tree_3b",spr_tree_flags(),"tree_3_b","bo_tree_3_a_fixed", spr_tree_triggers(full_hp=2700, fell_hp=1400)),
  ("pw_tree_4a",spr_tree_flags(),"tree_4_a","bo_tree_4_a_fixed", spr_tree_triggers(full_hp=2500, fell_hp=1500)),
  ("pw_tree_4b",spr_tree_flags(),"tree_4_b","bo_tree_4_b_fixed", spr_tree_triggers(full_hp=2100, fell_hp=1000)),
  ("pw_tree_5a",spr_tree_flags(),"tree_5_a","bo_tree_5_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=700)),
  ("pw_tree_5b",spr_tree_flags(),"tree_5_b","bo_tree_5_b_fixed", spr_tree_triggers(full_hp=1800, fell_hp=700)),
  ("pw_tree_5c",spr_tree_flags(),"tree_5_c","bo_tree_5_c_fixed", spr_tree_triggers(full_hp=1700, fell_hp=650)),
  ("pw_tree_5d",spr_tree_flags(),"tree_5_d","bo_tree_5_d_fixed", spr_tree_triggers(full_hp=1800, fell_hp=800)),
  ("pw_tree_6a",spr_tree_flags(),"tree_6_a","bo_tree_6_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=900)),
  ("pw_tree_6b",spr_tree_flags(),"tree_6_b","bo_tree_6_b_fixed", spr_tree_triggers(full_hp=2300, fell_hp=1100)),
  ("pw_tree_6c",spr_tree_flags(),"tree_6_c","bo_tree_6_c_fixed", spr_tree_triggers(full_hp=1800, fell_hp=1000)),
  ("pw_tree_6d",spr_tree_flags(),"tree_6_d","bo_tree_6_d_fixed", spr_tree_triggers(full_hp=2100, fell_hp=1100)),
  ("pw_tree_7a",spr_tree_flags(),"tree_7_a","bo_tree_7_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000)),
  ("pw_tree_7b",spr_tree_flags(),"tree_7_b","bo_tree_7_b_fixed", spr_tree_triggers(full_hp=2200, fell_hp=1000)),
  ("pw_tree_7c",spr_tree_flags(),"tree_7_c","bo_tree_7_c_fixed", spr_tree_triggers(full_hp=2300, fell_hp=1300)),
  ("pw_tree_8a",spr_tree_flags(),"tree_8_a_fixed","bo_tree_8_a_fixed", spr_tree_triggers(full_hp=2400, fell_hp=1800, resource_imod=imod_battered)),
  ("pw_tree_8b",spr_tree_flags(),"tree_8_b_fixed","bo_tree_8_b_fixed", spr_tree_triggers(full_hp=2700, fell_hp=1700, resource_imod=imod_battered)),
  ("pw_tree_8c",spr_tree_flags(),"tree_8_c_fixed","bo_tree_8_c_fixed", spr_tree_triggers(full_hp=2600, fell_hp=1300, resource_imod=imod_battered)),
  ("pw_tree_9a",spr_tree_flags(),"tree_9_a","bo_tree_9_a_fixed", spr_tree_triggers(full_hp=2100, fell_hp=1000, resource_imod=imod_battered)),
  ("pw_tree_9b",spr_tree_flags(),"tree_9_b","bo_tree_9_b_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000, resource_imod=imod_battered)),
  ("pw_tree_9c",spr_tree_flags(),"tree_9_c","bo_tree_9_a_fixed", spr_tree_triggers(full_hp=2400, fell_hp=1000, resource_imod=imod_battered)),
  ("pw_tree_10a",spr_tree_flags(),"tree_10_a","bo_tree_10_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000, resource_imod=imod_battered)),
  ("pw_tree_10b",spr_tree_flags(),"tree_10_b","bo_tree_10_b_fixed", spr_tree_triggers(full_hp=1900, fell_hp=900, resource_imod=imod_battered)),
  ("pw_tree_10c",spr_tree_flags(),"tree_10_c","bo_tree_10_c_fixed", spr_tree_triggers(full_hp=1700, fell_hp=700, resource_imod=imod_battered)),
  ("pw_tree_11a",spr_tree_flags(),"tree_11_a","bo_tree_11_a_fixed", spr_tree_triggers(full_hp=2200, fell_hp=1000, resource_imod=imod_battered)),
  ("pw_tree_11b",spr_tree_flags(),"tree_11_b","bo_tree_11_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000, resource_imod=imod_battered)),
  ("pw_tree_11c",spr_tree_flags(),"tree_11_c","bo_tree_11_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1100, resource_imod=imod_battered)),
  ("pw_tree_12a",spr_tree_flags(),"tree_12_a","bo_tree_12_a_fixed", spr_tree_triggers(full_hp=1800, fell_hp=700, resource_imod=imod_battered)),
  ("pw_tree_12b",spr_tree_flags(),"tree_12_b","bo_tree_12_b_fixed", spr_tree_triggers(full_hp=2000, fell_hp=1000, resource_imod=imod_battered)),
  ("pw_tree_12c",spr_tree_flags(),"tree_12_c","bo_tree_12_c_fixed", spr_tree_triggers(full_hp=1700, fell_hp=1000, resource_imod=imod_battered)),
  ("pw_tree_14a",spr_tree_flags(),"tree_14_a","bo_tree_14_a_fixed", spr_tree_triggers(full_hp=2200, fell_hp=1000)),
  ("pw_tree_14b",spr_tree_flags(),"tree_14_b","bo_tree_14_b_fixed", spr_tree_triggers(full_hp=2400, fell_hp=1200)),
  ("pw_tree_14c",spr_tree_flags(),"tree_14_c","bo_tree_14_c_fixed", spr_tree_triggers(full_hp=2500, fell_hp=1200)),
  ("pw_tree_15a",spr_tree_flags(),"tree_15_a","bo_tree_15_a_fixed", spr_tree_triggers(full_hp=2500, fell_hp=1100)),
  ("pw_tree_15b",spr_tree_flags(),"tree_15_b","bo_tree_15_b_fixed", spr_tree_triggers(full_hp=2300, fell_hp=1100)),
  ("pw_tree_15c",spr_tree_flags(),"tree_15_c","bo_tree_15_c_fixed", spr_tree_triggers(full_hp=2000, fell_hp=900)),
  ("pw_tree_16a",spr_tree_flags(),"tree_16_a","bo_tree_16_a_fixed", spr_tree_triggers(full_hp=3000, fell_hp=1600)),
  ("pw_tree_16b",spr_tree_flags(),"tree_16_b","bo_tree_16_b_fixed", spr_tree_triggers(full_hp=2200, fell_hp=1300)),
  ("pw_tree_17a",spr_tree_flags(),"tree_17_a","bo_tree_17_a_fixed", spr_tree_triggers(full_hp=1400, fell_hp=500)),
  ("pw_tree_17b",spr_tree_flags(),"tree_17_b","bo_tree_17_b_fixed", spr_tree_triggers(full_hp=1500, fell_hp=600)),
  ("pw_tree_17c",spr_tree_flags(),"tree_17_c","bo_tree_17_c_fixed", spr_tree_triggers(full_hp=1500, fell_hp=700)),
  ("pw_tree_17d",spr_tree_flags(),"tree_17_d","bo_tree_17_d_fixed", spr_tree_triggers(full_hp=1400, fell_hp=600)),
  ("pw_tree_18a",spr_tree_flags(),"tree_18_a","bo_tree_18_a_fixed", spr_tree_triggers(full_hp=2000, fell_hp=900, resource_imod=imod_battered)),
  ("pw_tree_18b",spr_tree_flags(),"tree_18_b","bo_tree_18_b_fixed", spr_tree_triggers(full_hp=2000, fell_hp=800, resource_imod=imod_battered)),
  ("pw_tree_19a",spr_tree_flags(),"tree_19_a","bo_tree_19_a_fixed", spr_tree_triggers(full_hp=2500, fell_hp=1500, resource_imod=imod_battered)),
  ("pw_tree_20a",spr_tree_flags(),"tree_20_a","bo_tree_20_a_fixed", spr_tree_triggers(full_hp=2200, fell_hp=1000)),
  ("pw_tree_20b",spr_tree_flags(),"tree_20_b","bo_tree_20_b_fixed", spr_tree_triggers(full_hp=2200, fell_hp=1000)),
  ("pw_tree_palm_a",spr_tree_flags(),"palm_a","bo_palm_a_fixed", spr_tree_triggers(full_hp=1500, fell_hp=700)),
  ("pw_tree_trunk_a",0,"pw_tree_trunk_a","bo_pw_tree_trunk_a", []),
  ("pw_tree_trunk_b",0,"pw_tree_trunk_b","bo_pw_tree_trunk_b", []),
  ("pw_stick_bush_2a",spr_resource_flags(),"bushes02_a","bo_bushes02_a_fixed", spr_hit_plant_triggers("itm_stick", full_hp=1000, resource_hp=50, regrow_interval=70, effect_script="script_hit_bush_effect")),
  ("pw_stick_bush_2b",spr_resource_flags(),"bushes02_b","bo_bushes02_b_fixed", spr_hit_plant_triggers("itm_stick", full_hp=700, resource_hp=50, regrow_interval=60, effect_script="script_hit_bush_effect")),
  ("pw_stick_bush_2c",spr_resource_flags(),"bushes02_c","bo_bushes02_a_fixed", spr_hit_plant_triggers("itm_stick", full_hp=1500, resource_hp=50, regrow_interval=120, effect_script="script_hit_bush_effect")),
  ("pw_herb_bush_a",spr_resource_flags(),"pw_herb_a_bush","bo_pw_herb_bush", spr_hit_plant_triggers("itm_healing_herb", full_hp=400, resource_hp=40, regrow_interval=600)),
  ("pw_herb_bush_poison",spr_resource_flags(),"pw_herb_b_bush","bo_pw_herb_bush", spr_hit_plant_triggers("itm_poison_herb", full_hp=600, resource_hp=30, regrow_interval=2000)),
  ("pw_wheat_field",spr_field_flags(),"pw_wheat_field","bo_pw_wheat_field", spr_hit_field_triggers(resource_item="itm_wheat_sheaf", plant_item="itm_wheat_sack", plant_spr="spr_code_wheat", height=180, full_hp=2000, resource_hp=50, tool_class=item_class_grain_harvesting, regrow_interval=600)),
  ("code_wheat",0,"pw_wheat","0", spr_field_plant_triggers(seeds=4, water=2)),
  ("pw_grape_vine",spr_resource_flags(),"pw_grape_vine","bo_pw_grape_vine", spr_hit_vine_triggers("itm_grapes", resources=16, full_hp=300, length=350, height=100, tool_class=item_class_knife, regrow_interval=300)),
  ("pw_grape_vine_stake",0,"pw_grape_vine_stake","bo_pw_grape_vine_stake", []),
  ("pw_flax_plants",spr_field_flags()|spr_use_time(1),"pw_flax_plants","bo_pw_flax_plants", spr_use_plant_triggers("itm_flax_bundle", full_hp=300, resource_hp=50, regrow_interval=300, sound="snd_pull_flax")),
  ("pw_apple_tree_a",spr_tree_flags(),"pw_apple_tree_a","bo_pw_apple_tree_a", spr_fruit_tree_triggers(fruit="itm_red_apple", count=10, height=350, width=150, fruiting_interval=1200, full_hp=600, fell_hp=100, regrow_interval=1800)),

  ("pw_iron_mine",spr_resource_flags(),"pw_iron_vein_a2","bo_pw_iron_vein_a2", spr_hit_mine_triggers("itm_iron_ore", resource_hp=60, hardness=4)),
  ("pw_iron_mine_a",spr_resource_flags(),"pw_iron_vein_a1","bo_pw_iron_vein_a1", spr_hit_mine_triggers("itm_iron_ore", resource_hp=70, hardness=4)),
  ("pw_iron_mine_b",spr_resource_flags(),"pw_iron_vein_b","bo_pw_iron_vein_b", spr_hit_mine_triggers("itm_iron_ore", resource_hp=50, hardness=5)),
  ("pw_iron_mine_small",spr_resource_flags(),"pw_iron_vein_a1","bo_pw_iron_vein_a1", spr_hit_mine_triggers("itm_iron_ore_small", resource_hp=40, hardness=4)),
  ("pw_gold_mine",spr_resource_flags(),"pw_gold_vein","bo_pw_gold_vein", spr_hit_mine_triggers("itm_gold_nugget", resource_hp=200, random_hp=200, hardness=6)),
  ("pw_silver_mine",spr_resource_flags(),"pw_silver_vein","bo_pw_gold_vein", spr_hit_mine_triggers("itm_silver_nugget", resource_hp=150, random_hp=100, hardness=5)),
  ("pw_salt_mine",spr_resource_flags(),"pw_salt_mine","bo_pw_salt_mine", spr_hit_mine_triggers("itm_salt_sack", resource_hp=30, random_hp=20, hardness=5)),

  ("pw_stockpile_wood_block",spr_use_time(1),"pw_wood_heap_a","bo_wood_heap_a", spr_stockpile_resource_triggers("itm_wood_block")),
  ("pw_stockpile_wood_branch",spr_use_time(1),"wood_heap_b","bo_wood_heap_b", spr_stockpile_resource_triggers("itm_branch")),
  ("pw_stockpile_wood_pole",spr_use_time(1),"pw_wood_pole","bo_pw_weapon_big", spr_stockpile_resource_triggers("itm_wood_pole")),
  ("pw_stockpile_wood_pole_short",spr_use_time(1),"pw_wood_pole_short","bo_pw_weapon", spr_stockpile_resource_triggers("itm_wood_pole_short")),
  ("pw_stockpile_stick",spr_use_time(1),"wooden_stick","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_stick")),
  ("pw_stockpile_board",spr_use_time(1),"pw_board","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_board")),
  ("pw_stockpile_iron_ore_small",spr_use_time(1),"pw_iron_ore_small","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_iron_ore_small")),
  ("pw_stockpile_iron_ore",spr_use_time(1),"pw_iron_ore","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_iron_ore")),
  ("pw_stockpile_iron_bar",spr_use_time(1),"pw_chest_c","bo_pw_chest_c", spr_stockpile_resource_triggers("itm_iron_bar")),
  ("pw_stockpile_flour_sack",spr_use_time(1),"mill_flour_sack_desk_a","bo_mill_flour_sack_desk_a_fixed", spr_stockpile_resource_triggers("itm_flour_sack")),
  ("pw_stockpile_salt_sack",spr_use_time(1),"pw_salt_sack","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_salt_sack")),
  ("pw_stockpile_salt",spr_use_time(1),"pw_salt","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_salt")),
  ("pw_stockpile_salted_fish",spr_use_time(1),"pw_fish","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_salted_fish")),
  ("pw_stockpile_salted_meat",spr_use_time(1),"pw_meat_salted","bo_pw_weapon", spr_stockpile_resource_triggers("itm_salted_meat")),
  ("pw_stockpile_wheat_sheaf",spr_use_time(1),"pw_wheat_sheaf","bo_pw_weapon", spr_stockpile_resource_triggers("itm_wheat_sheaf")),
  ("pw_stockpile_beer_cask",spr_use_time(1),"pw_beer_cask_carry","bo_pw_beer_wine_barrel", spr_stockpile_resource_triggers("itm_beer_cask")),
  ("pw_stockpile_wine_barrel",spr_use_time(1),"pw_wine_barrel_carry","bo_pw_beer_wine_barrel", spr_stockpile_resource_triggers("itm_wine_barrel")),
  ("pw_stockpile_linen_thread",spr_use_time(1),"pw_linen_thread","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_linen_thread")),
  ("pw_stockpile_linen_cloth",spr_use_time(1),"pw_linen_cloth","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_linen_cloth")),
  ("pw_stockpile_leather_roll",spr_use_time(1),"pw_leather_roll","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_leather_roll")),
  ("pw_stockpile_leather_piece",spr_use_time(1),"pw_leather_piece","bo_pw_weapon_small", spr_stockpile_resource_triggers("itm_leather_piece")),
  ("pw_import_wheat_sack",spr_use_time(30),"pw_wheat_sack","bo_pw_weapon_small", spr_import_item_triggers("itm_wheat_sack", pos_offset=(0,0,-20), price_multiplier=3000)),
  ("pw_import_fawn",spr_use_time(20),"sack","bo_sack_fixed", spr_import_item_triggers("itm_fawn", pos_offset=(0,50,50), price_multiplier=300, check_script="script_cf_can_spawn_herd_animal")),
  ("pw_import_boarlet",spr_use_time(10),"sack","bo_sack_fixed", spr_import_item_triggers("itm_boarlet", pos_offset=(0,50,50), price_multiplier=300, check_script="script_cf_can_spawn_herd_animal")),
  ("pw_import_calf",spr_use_time(25),"sack","bo_sack_fixed", spr_import_item_triggers("itm_calf", pos_offset=(0,50,50), price_multiplier=300, check_script="script_cf_can_spawn_herd_animal")),
  ("pw_export_wood_stick",spr_use_time(2),"pw_wood_box","bo_pw_wood_box", spr_export_item_triggers("itm_stick")),
  ("pw_export_wood_branch",spr_use_time(5),"wood_heap_b","bo_wood_heap_b", spr_export_item_triggers("itm_branch")),
  ("pw_export_wood_pole",spr_use_time(6),"pw_wood_pole","bo_pw_weapon_big", spr_export_item_triggers("itm_wood_pole")),
  ("pw_export_wood_block",spr_use_time(5),"pw_wood_heap_a","bo_wood_heap_a", spr_export_item_triggers("itm_wood_block")),
  ("pw_export_board",spr_use_time(6),"pw_board","bo_pw_weapon_small", spr_export_item_triggers("itm_board")),
  ("pw_export_iron_ore_small",spr_use_time(10),"pw_iron_ore_small","bo_pw_weapon_small", spr_export_item_triggers("itm_iron_ore_small")),
  ("pw_export_iron_ore",spr_use_time(14),"pw_iron_ore","bo_pw_weapon_small", spr_export_item_triggers("itm_iron_ore")),
  ("pw_export_iron_bar_short",spr_use_time(10),"pw_iron_bar_short","bo_pw_weapon_small", spr_export_item_triggers("itm_iron_bar_short")),
  ("pw_export_iron_bar",spr_use_time(13),"pw_iron_bar","bo_pw_weapon_small", spr_export_item_triggers("itm_iron_bar")),
  ("pw_export_iron_bar_long",spr_use_time(16),"pw_iron_bar_long","bo_pw_weapon_small", spr_export_item_triggers("itm_iron_bar_long")),
  ("pw_export_gold_nugget",spr_use_time(7),"pw_gold_nugget","bo_pw_weapon_small", spr_export_item_triggers("itm_gold_nugget")),
  ("pw_export_gold_bar",spr_use_time(15),"pw_gold_bar","bo_pw_weapon_small", spr_export_item_triggers("itm_gold_bar")),
  ("pw_export_silver_nugget",spr_use_time(7),"pw_silver_nugget","bo_pw_weapon_small", spr_export_item_triggers("itm_silver_nugget")),
  ("pw_export_silver_bar",spr_use_time(15),"pw_silver_bar","bo_pw_weapon_small", spr_export_item_triggers("itm_silver_bar")),
  ("pw_export_salt_sack",spr_use_time(8),"pw_salt_sack","bo_pw_weapon_small", spr_export_item_triggers("itm_salt_sack")),
  ("pw_export_salted_fish",spr_use_time(5),"pw_fish","bo_pw_weapon_small", spr_export_item_triggers("itm_salted_fish")),
  ("pw_export_salted_meat",spr_use_time(7),"pw_meat_salted","bo_pw_weapon_small", spr_export_item_triggers("itm_salted_meat")),
  ("pw_export_beer_cask",spr_use_time(8),"pw_beer_cask_carry","bo_pw_beer_wine_barrel", spr_export_item_triggers("itm_beer_cask")),
  ("pw_export_wine_barrel",spr_use_time(9),"pw_wine_barrel_carry","bo_pw_beer_wine_barrel", spr_export_item_triggers("itm_wine_barrel")),
  ("pw_export_linen_cloth",spr_use_time(8),"pw_linen_cloth","bo_pw_weapon_small", spr_export_item_triggers("itm_linen_cloth")),
  ("pw_export_leather_roll",spr_use_time(8),"pw_leather_roll","bo_pw_weapon_small", spr_export_item_triggers("itm_leather_roll")),
  ("pw_process_wood",spr_use_time(4),"bench_tavern_b","bo_bench_tavern_b", spr_process_resource_triggers("script_cf_process_wood", use_string="str_process_wood")),
  ("pw_process_iron",spr_use_time(10),"pw_smithy_forge","bo_pw_smithy_forge", spr_process_resource_triggers("script_cf_process_iron", use_string="str_process_metal")),
  ("pw_process_iron_divide_only",spr_use_time(5),"smithy_anvil","bo_smithy_anvil", spr_process_resource_triggers("script_cf_process_iron_divide_only", use_string="str_process_hammer_metal")),
  ("pw_process_grind_fast",spr_use_time(3)|sokf_invisible,"pw_invisible_station","bo_pw_invisible_station", spr_process_resource_triggers("script_cf_process_grind", use_string="str_process_grind")),
  ("pw_process_grind_slow",spr_use_time(10),"horse_mill","bo_horse_mill", spr_process_resource_triggers("script_cf_process_grind", use_string="str_process_grind")),
  ("pw_process_cook_fast",spr_use_time(4),"village_oven","bo_village_oven_fixed", spr_process_resource_triggers("script_cf_process_cook", use_string="str_process_cook")),
  ("pw_process_cook_slow",spr_use_time(5)|sokf_invisible,"pw_invisible_station","bo_pw_invisible_station", spr_process_resource_triggers("script_cf_process_cook", use_string="str_process_cook")),
  ("pw_process_press",spr_use_time(5),"winery_wine_press","bo_winery_wine_press", spr_process_resource_triggers("script_cf_process_press", use_string="str_process_press")),
  ("pw_process_brew",spr_use_time(30),"brewery_pool","bo_brewery_pool", spr_process_resource_triggers("script_cf_process_brew", use_string="str_process_brew")),
  ("pw_process_tavern",spr_use_time(2),"tavern_table_a","bo_tavern_table_a", spr_process_resource_triggers("script_cf_process_tavern", use_string="str_process_tavern")),
  ("pw_process_preserve",spr_use_time(5),"table_small","bo_table_small", spr_process_resource_triggers("script_cf_process_preserve", use_string="str_process_preserve")),
  ("pw_process_spin",spr_use_time(1),"pw_spinning_wheel","bo_pw_spinning_wheel", spr_process_resource_triggers("script_cf_process_spin", use_string="str_process_spin")),
  ("pw_process_weave",spr_use_time(3),"pw_weaving_loom","bo_pw_weaving_loom", spr_process_resource_triggers("script_cf_process_weave", use_string="str_process_weave")),
  ("pw_process_cut",spr_use_time(1),"pw_shears","bo_pw_weapon_small", spr_process_resource_triggers("script_cf_process_cut", use_string="str_process_cut")),
  ("pw_process_leather",spr_use_time(6),"tannery_pools_b","bo_tannery_pools_b", spr_process_resource_triggers("script_cf_process_leather", use_string="str_process_leather")),
  ("pw_process_leather_alt",spr_use_time(7),"leatherwork_frame","bo_leatherwork_frame", spr_process_resource_triggers("script_cf_process_leather", use_string="str_process_leather")),

  ("pw_buy_straw_hat",spr_buy_item_flags(1),"straw_hat_new","bo_pw_armor_head", spr_buy_item_triggers("itm_straw_hat", resources=["itm_wheat_sheaf"], tailoring=1)),
  ("pw_buy_head_wrappings",spr_buy_item_flags(1),"head_wrapping","bo_pw_armor_head", spr_buy_item_triggers("itm_head_wrappings", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_headcloth",spr_buy_item_flags(2),"headcloth_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_headcloth", resources=["itm_linen_cloth_small"], tailoring=1, tableau="tableau_colored_helmets_new_d")),
  ("pw_buy_woolen_cap",spr_buy_item_flags(2),"woolen_cap_new","bo_pw_armor_head", spr_buy_item_triggers("itm_woolen_cap", resources=["itm_linen_cloth_small"], tailoring=1, tableau="tableau_colored_helmets_new_e")),
  ("pw_buy_sarranid_felt_hat",spr_buy_item_flags(2),"sar_helmet3","bo_pw_armor_head", spr_buy_item_triggers("itm_sarranid_felt_hat", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_sarranid_felt_head_cloth",spr_buy_item_flags(1),"common_tulbent","bo_pw_armor_head_armature", spr_buy_item_triggers("itm_sarranid_felt_head_cloth", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_sarranid_felt_head_cloth_b",spr_buy_item_flags(1),"common_tulbent_b","bo_pw_armor_head_armature", spr_buy_item_triggers("itm_sarranid_felt_head_cloth_b", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_bride_crown",spr_buy_item_flags(5),"bride_crown","bo_pw_armor_head_armature", spr_buy_item_triggers("itm_bride_crown", resources=["itm_linen_cloth_small"], tailoring=2)),
  ("pw_buy_khergit_lady_hat",spr_buy_item_flags(3),"khergit_lady_hat","bo_pw_armor_head", spr_buy_item_triggers("itm_khergit_lady_hat", resources=["itm_linen_cloth_small"], tailoring=2)),
  ("pw_buy_khergit_lady_hat_b",spr_buy_item_flags(3),"khergit_lady_hat_b","bo_pw_armor_head", spr_buy_item_triggers("itm_khergit_lady_hat_b", resources=["itm_leather_piece"], tailoring=2)),
  ("pw_buy_sarranid_head_cloth",spr_buy_item_flags(2),"tulbent","bo_pw_armor_head_armature", spr_buy_item_triggers("itm_sarranid_head_cloth", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_sarranid_head_cloth_b",spr_buy_item_flags(2),"tulbent_b","bo_pw_armor_head_armature", spr_buy_item_triggers("itm_sarranid_head_cloth_b", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_wimple_a",spr_buy_item_flags(3),"wimple_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_wimple_a", resources=["itm_linen_cloth_small"], tailoring=2)),
  ("pw_buy_wimple_b",spr_buy_item_flags(3),"wimple_b_new","bo_pw_armor_head", spr_buy_item_triggers("itm_wimple_b", resources=["itm_linen_cloth_small"], tailoring=2)),
  ("pw_buy_barbette",spr_buy_item_flags(3),"barbette_new","bo_pw_armor_head", spr_buy_item_triggers("itm_barbette", resources=["itm_linen_cloth_small"], tailoring=2)),
  ("pw_buy_arming_cap",spr_buy_item_flags(2),"arming_cap_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_arming_cap", resources=["itm_linen_cloth_small"], tailoring=1, tableau="tableau_colored_helmets_new_d")),
  ("pw_buy_ladys_hood",spr_buy_item_flags(2),"ladys_hood_new","bo_pw_armor_head", spr_buy_item_triggers("itm_ladys_hood", resources=["itm_linen_cloth_small"], tailoring=2)),
  ("pw_buy_fur_hat",spr_buy_item_flags(3),"fur_hat_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_fur_hat", resources=["itm_leather_piece"], tailoring=1)),
  ("pw_buy_felt_hat",spr_buy_item_flags(2),"felt_hat_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_felt_hat", resources=["itm_linen_cloth_small"], tailoring=1, tableau="tableau_colored_helmets_new_b")),
  ("pw_buy_felt_hat_b",spr_buy_item_flags(2),"felt_hat_b_new","bo_pw_armor_head", spr_buy_item_triggers("itm_felt_hat_b", resources=["itm_linen_cloth_small"], tailoring=2, tableau="tableau_colored_helmets_new_b")),
  ("pw_buy_leather_cap",spr_buy_item_flags(3),"leather_cap_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_leather_cap", resources=["itm_leather_piece"], tailoring=2)),
  ("pw_buy_common_hood",spr_buy_item_flags(2),"hood_new","bo_pw_armor_head", spr_buy_item_triggers("itm_common_hood", resources=["itm_linen_cloth_small"], tailoring=1, tableau="tableau_colored_helmets_new_e")),
  ("pw_buy_hood_b",spr_buy_item_flags(2),"hood_b","bo_pw_armor_head", spr_buy_item_triggers("itm_hood_b", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_hood_c",spr_buy_item_flags(2),"hood_c","bo_pw_armor_head", spr_buy_item_triggers("itm_hood_c", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_hood_d",spr_buy_item_flags(2),"hood_d","bo_pw_armor_head", spr_buy_item_triggers("itm_hood_d", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_nomad_cap",spr_buy_item_flags(5),"nomad_cap_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_nomad_cap", resources=["itm_iron_piece","itm_leather_piece"], tailoring=3, engineer=2)),
  ("pw_buy_nomad_cap_b",spr_buy_item_flags(4),"nomad_cap_b_new","bo_pw_armor_head", spr_buy_item_triggers("itm_nomad_cap_b", resources=["itm_leather_piece"], tailoring=2)),
  ("pw_buy_black_hood",spr_buy_item_flags(3),"hood_black","bo_pw_armor_head", spr_buy_item_triggers("itm_black_hood", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_surgeon_coif",spr_buy_item_flags(2),"pw_surgeon_coif","bo_pw_armor_head", spr_buy_item_triggers("itm_surgeon_coif", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_pilgrim_hood",spr_buy_item_flags(2),"pilgrim_hood","bo_pw_armor_head", spr_buy_item_triggers("itm_pilgrim_hood", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_priest_coif",spr_buy_item_flags(4),"pw_priest_coif","bo_pw_armor_head", spr_buy_item_triggers("itm_priest_coif", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_padded_coif",spr_buy_item_flags(5),"padded_coif_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_padded_coif", resources=[("itm_linen_cloth_small",2)], tailoring=2, tableau="tableau_colored_helmets_new_b")),
  ("pw_buy_turban",spr_buy_item_flags(1),"tuareg_open","bo_pw_armor_head", spr_buy_item_triggers("itm_turban", resources=[("itm_linen_cloth_small",2)], tailoring=1)),
  ("pw_buy_leather_steppe_cap_a",spr_buy_item_flags(4),"leather_steppe_cap_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_leather_steppe_cap_a", resources=[("itm_leather_piece",2)], tailoring=2)),
  ("pw_buy_leather_steppe_cap_b",spr_buy_item_flags(5),"tattered_steppe_cap_b_new","bo_pw_armor_head", spr_buy_item_triggers("itm_leather_steppe_cap_b", resources=["itm_leather_piece","itm_iron_piece"], tailoring=2, engineer=2)),
  ("pw_buy_nordic_archer_helmet",spr_buy_item_flags(5),"Helmet_A_vs2","bo_pw_armor_head", spr_buy_item_triggers("itm_nordic_archer_helmet", resources=["itm_leather_piece","itm_iron_piece"], engineer=2)),
  ("pw_buy_vaegir_fur_cap",spr_buy_item_flags(5),"vaeg_helmet3","bo_pw_armor_head", spr_buy_item_triggers("itm_vaegir_fur_cap", resources=["itm_leather_piece","itm_iron_piece"], engineer=2)),
  ("pw_buy_steppe_cap",spr_buy_item_flags(5),"steppe_cap_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_steppe_cap", resources=["itm_leather_piece","itm_iron_piece"], engineer=2)),
  ("pw_buy_leather_warrior_cap",spr_buy_item_flags(5),"skull_cap_new_b","bo_pw_armor_head", spr_buy_item_triggers("itm_leather_warrior_cap", resources=[("itm_leather_piece",2)], engineer=2, tailoring=3)),
  ("pw_buy_sarranid_warrior_cap",spr_buy_item_flags(5),"tuareg_helmet","bo_pw_armor_head", spr_buy_item_triggers("itm_sarranid_warrior_cap", resources=["itm_iron_piece","itm_linen_cloth_small"], engineer=2)),
  ("pw_buy_nordic_veteran_archer_helmet",spr_buy_item_flags(6),"Helmet_A","bo_pw_armor_head", spr_buy_item_triggers("itm_nordic_veteran_archer_helmet", resources=["itm_iron_piece","itm_leather_piece"], engineer=2)),
  ("pw_buy_skullcap",spr_buy_item_flags(6),"skull_cap_new_a","bo_pw_armor_head", spr_buy_item_triggers("itm_skullcap", resources=["itm_iron_piece","itm_leather_piece"], engineer=2)),
  ("pw_buy_vaegir_fur_helmet",spr_buy_item_flags(6),"vaeg_helmet2","bo_pw_armor_head", spr_buy_item_triggers("itm_vaegir_fur_helmet", resources=["itm_iron_bar_short","itm_leather_piece"], engineer=2)),
  ("pw_buy_bishop_mitre",spr_buy_item_flags(10),"pw_bishop_mitre","bo_pw_armor_head", spr_buy_item_triggers("itm_bishop_mitre", resources=["itm_linen_cloth_small"], engineer=3, tailoring=3)),
  ("pw_buy_mail_coif",spr_buy_item_flags(7),"mail_coif_new","bo_pw_armor_head", spr_buy_item_triggers("itm_mail_coif", resources=[("itm_iron_piece",2)], engineer=3)),
  ("pw_buy_footman_helmet",spr_buy_item_flags(7),"skull_cap_new","bo_pw_armor_head", spr_buy_item_triggers("itm_footman_helmet", resources=["itm_iron_bar_short","itm_linen_cloth_small"], engineer=2)),
  ("pw_buy_sarranid_horseman_helmet",spr_buy_item_flags(7),"sar_helmet2","bo_pw_armor_head", spr_buy_item_triggers("itm_sarranid_horseman_helmet", resources=["itm_iron_bar_short","itm_linen_cloth"], engineer=3)),
  ("pw_buy_nasal_helmet",spr_buy_item_flags(7),"nasal_helmet_b","bo_pw_armor_head", spr_buy_item_triggers("itm_nasal_helmet", resources=["itm_iron_bar_short","itm_leather_piece"], engineer=2)),
  ("pw_buy_norman_helmet",spr_buy_item_flags(7),"norman_helmet_a","bo_pw_armor_head", spr_buy_item_triggers("itm_norman_helmet", resources=["itm_iron_bar_short","itm_linen_cloth_small"], engineer=2)),
  ("pw_buy_nordic_footman_helmet",spr_buy_item_flags(8),"Helmet_B_vs2","bo_pw_armor_head", spr_buy_item_triggers("itm_nordic_footman_helmet", resources=["itm_iron_bar_short","itm_leather_piece"], engineer=3)),
  ("pw_buy_khergit_war_helmet",spr_buy_item_flags(8),"tattered_steppe_cap_a_new","bo_pw_armor_head", spr_buy_item_triggers("itm_khergit_war_helmet", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=3)),
  ("pw_buy_segmented_helmet",spr_buy_item_flags(8),"segmented_helm_new","bo_pw_armor_head", spr_buy_item_triggers("itm_segmented_helmet", resources=["itm_iron_bar_short","itm_linen_cloth"], engineer=3)),
  ("pw_buy_vaegir_spiked_helmet",spr_buy_item_flags(8),"vaeg_helmet1","bo_pw_armor_head", spr_buy_item_triggers("itm_vaegir_spiked_helmet", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=4)),
  ("pw_buy_helmet_with_neckguard",spr_buy_item_flags(9),"neckguard_helm_new","bo_pw_armor_head", spr_buy_item_triggers("itm_helmet_with_neckguard", resources=["itm_iron_bar_short","itm_leather_piece"], engineer=3)),
  ("pw_buy_flat_topped_helmet",spr_buy_item_flags(9),"flattop_helmet_new","bo_pw_armor_head", spr_buy_item_triggers("itm_flat_topped_helmet", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=4)),
  ("pw_buy_nordic_fighter_helmet",spr_buy_item_flags(10),"Helmet_B","bo_pw_armor_head", spr_buy_item_triggers("itm_nordic_fighter_helmet", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=4)),
  ("pw_buy_kettle_hat",spr_buy_item_flags(10),"kettle_hat_new","bo_pw_armor_head", spr_buy_item_triggers("itm_kettle_hat", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=4)),
  ("pw_buy_sarranid_helmet1",spr_buy_item_flags(10),"sar_helmet1","bo_pw_armor_head", spr_buy_item_triggers("itm_sarranid_helmet1", resources=["itm_iron_bar_short","itm_linen_cloth_small"], engineer=4)),
  ("pw_buy_vaegir_lamellar_helmet",spr_buy_item_flags(10),"vaeg_helmet4","bo_pw_armor_head", spr_buy_item_triggers("itm_vaegir_lamellar_helmet", resources=["itm_iron_bar_short","itm_leather_piece"], engineer=4)),
  ("pw_buy_spiked_helmet",spr_buy_item_flags(11),"spiked_helmet_new","bo_pw_armor_head", spr_buy_item_triggers("itm_spiked_helmet", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=4)),
  ("pw_buy_sarranid_mail_coif",spr_buy_item_flags(11),"tuareg_helmet2","bo_pw_armor_head", spr_buy_item_triggers("itm_sarranid_mail_coif", resources=["itm_iron_bar_short","itm_iron_piece","itm_linen_cloth_small"], engineer=4)),
  ("pw_buy_nordic_huscarl_helmet",spr_buy_item_flags(12),"Helmet_C_vs2","bo_pw_armor_head", spr_buy_item_triggers("itm_nordic_huscarl_helmet", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=5)),
  ("pw_buy_bascinet",spr_buy_item_flags(13),"bascinet_avt_new","bo_pw_armor_head", spr_buy_item_triggers("itm_bascinet", resources=["itm_iron_bar_short","itm_leather_piece"], engineer=5)),
  ("pw_buy_bascinet_2",spr_buy_item_flags(13),"bascinet_new_a","bo_pw_armor_head", spr_buy_item_triggers("itm_bascinet_2", resources=[("itm_iron_bar_short",2)], engineer=5)),
  ("pw_buy_bascinet_3",spr_buy_item_flags(13),"bascinet_new_b","bo_pw_armor_head", spr_buy_item_triggers("itm_bascinet_3", resources=[("itm_iron_bar_short",2)], engineer=5)),
  ("pw_buy_vaegir_noble_helmet",spr_buy_item_flags(14),"vaeg_helmet7","bo_pw_armor_head", spr_buy_item_triggers("itm_vaegir_noble_helmet", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=5)),
  ("pw_buy_guard_helmet",spr_buy_item_flags(14),"reinf_helmet_new","bo_pw_armor_head", spr_buy_item_triggers("itm_guard_helmet", resources=["itm_iron_bar_short","itm_iron_piece"], engineer=5)),
  ("pw_buy_sarranid_veiled_helmet",spr_buy_item_flags(14),"sar_helmet4","bo_pw_armor_head", spr_buy_item_triggers("itm_sarranid_veiled_helmet", resources=[("itm_iron_bar_short",2)], engineer=5)),
  ("pw_buy_vaegir_war_helmet",spr_buy_item_flags(14),"vaeg_helmet6","bo_pw_armor_head", spr_buy_item_triggers("itm_vaegir_war_helmet", resources=[("itm_iron_bar_short",2)], engineer=5)),
  ("pw_buy_nordic_warlord_helmet",spr_buy_item_flags(15),"Helmet_C","bo_pw_armor_head", spr_buy_item_triggers("itm_nordic_warlord_helmet", resources=[("itm_iron_bar_short",2)], engineer=5)),
  ("pw_buy_bishop_helm",spr_buy_item_flags(18),"pw_bishop_helm","bo_pw_armor_head", spr_buy_item_triggers("itm_bishop_helm", resources=[("itm_iron_bar_short",2),"itm_linen_cloth_small"], engineer=6)),
  ("pw_buy_full_helm",spr_buy_item_flags(17),"great_helmet_new_b","bo_pw_armor_head", spr_buy_item_triggers("itm_full_helm", resources=[("itm_iron_bar_short",2),"itm_leather_piece"], engineer=6)),
  ("pw_buy_vaegir_mask",spr_buy_item_flags(17),"vaeg_helmet8","bo_pw_armor_head", spr_buy_item_triggers("itm_vaegir_mask", resources=[("itm_iron_bar_short",2),"itm_iron_piece"], engineer=6)),
  ("pw_buy_vaegir_mask_b",spr_buy_item_flags(18),"vaeg_helmet9","bo_pw_armor_head", spr_buy_item_triggers("itm_vaegir_mask_b", resources=[("itm_iron_bar_short",2),"itm_iron_piece"], engineer=6)),
  ("pw_buy_great_helmet",spr_buy_item_flags(20),"great_helmet_new","bo_pw_armor_head", spr_buy_item_triggers("itm_great_helmet", resources=["itm_iron_bar","itm_linen_cloth_small"], engineer=6)),
  ("pw_buy_winged_great_helmet",spr_buy_item_flags(21),"maciejowski_helmet_new","bo_pw_armor_head", spr_buy_item_triggers("itm_winged_great_helmet", resources=["itm_iron_bar","itm_iron_bar_short","itm_linen_cloth_small"], engineer=6)),
  ("pw_buy_black_helmet",spr_buy_item_flags(21),"black_helm","bo_pw_armor_head", spr_buy_item_triggers("itm_black_helmet", resources=["itm_iron_bar","itm_linen_cloth_small"], engineer=6)),

  ("pw_buy_shirt",spr_buy_item_flags(1),"shirt","bo_pw_armor_body", spr_buy_item_triggers("itm_shirt", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_linen_tunic",spr_buy_item_flags(2),"shirt_a","bo_pw_armor_body", spr_buy_item_triggers("itm_linen_tunic", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_black_robe",spr_buy_item_flags(3),"robe","bo_pw_armor_body", spr_buy_item_triggers("itm_black_robe", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_dress",spr_buy_item_flags(3),"dress","bo_pw_armor_body", spr_buy_item_triggers("itm_dress", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_blue_dress",spr_buy_item_flags(3),"blue_dress_new","bo_pw_armor_body", spr_buy_item_triggers("itm_blue_dress", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_peasant_dress",spr_buy_item_flags(3),"peasant_dress_b_new","bo_pw_armor_body", spr_buy_item_triggers("itm_peasant_dress", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_woolen_dress",spr_buy_item_flags(3),"woolen_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_woolen_dress", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_sarranid_common_dress",spr_buy_item_flags(3),"sarranid_common_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_common_dress", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_sarranid_common_dress_b",spr_buy_item_flags(3),"sarranid_common_dress_b","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_common_dress_b", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_lady_dress_ruby",spr_buy_item_flags(5),"lady_dress_r","bo_pw_armor_body", spr_buy_item_triggers("itm_lady_dress_ruby", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_lady_dress_green",spr_buy_item_flags(5),"lady_dress_g","bo_pw_armor_body", spr_buy_item_triggers("itm_lady_dress_green", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_lady_dress_blue",spr_buy_item_flags(5),"lady_dress_b","bo_pw_armor_body", spr_buy_item_triggers("itm_lady_dress_blue", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_court_dress",spr_buy_item_flags(5),"court_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_court_dress", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_red_dress",spr_buy_item_flags(5),"red_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_red_dress", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_brown_dress",spr_buy_item_flags(5),"brown_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_brown_dress", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_green_dress",spr_buy_item_flags(5),"green_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_green_dress", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_sarranid_lady_dress",spr_buy_item_flags(5),"sarranid_lady_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_lady_dress", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_sarranid_lady_dress_b",spr_buy_item_flags(5),"sarranid_lady_dress_b","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_lady_dress_b", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_khergit_lady_dress",spr_buy_item_flags(5),"khergit_lady_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_khergit_lady_dress", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_khergit_lady_dress_b",spr_buy_item_flags(6),"khergit_lady_dress_b","bo_pw_armor_body", spr_buy_item_triggers("itm_khergit_lady_dress_b", resources=["itm_leather_roll"], tailoring=2)),
  ("pw_buy_bride_dress",spr_buy_item_flags(7),"bride_dress","bo_pw_armor_body", spr_buy_item_triggers("itm_bride_dress", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_tunic_with_green_cape",spr_buy_item_flags(3),"peasant_man_a","bo_pw_armor_body", spr_buy_item_triggers("itm_tunic_with_green_cape", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_rough_tunic",spr_buy_item_flags(2),"pw_rough_tunic","bo_pw_armor_body", spr_buy_item_triggers("itm_rough_tunic", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_red_shirt",spr_buy_item_flags(2),"rich_tunic_a","bo_pw_armor_body", spr_buy_item_triggers("itm_red_shirt", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_pelt_coat",spr_buy_item_flags(2),"thick_coat_a","bo_pw_armor_body", spr_buy_item_triggers("itm_pelt_coat", resources=["itm_leather_roll","itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_sarranid_cloth_robe",spr_buy_item_flags(3),"sar_robe","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_cloth_robe", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_sarranid_cloth_robe_b",spr_buy_item_flags(3),"sar_robe_b","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_cloth_robe_b", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_rawhide_coat",spr_buy_item_flags(3),"coat_of_plates_b","bo_pw_armor_body", spr_buy_item_triggers("itm_rawhide_coat", resources=["itm_leather_roll","itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_coarse_tunic",spr_buy_item_flags(1),"coarse_tunic_a","bo_pw_armor_body", spr_buy_item_triggers("itm_coarse_tunic", resources=["itm_linen_cloth"], tailoring=1)),
  ("pw_buy_leather_apron",spr_buy_item_flags(2),"leather_apron","bo_pw_armor_body", spr_buy_item_triggers("itm_leather_apron", resources=[("itm_leather_piece",2),"itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_fur_coat",spr_buy_item_flags(4),"fur_coat","bo_pw_armor_body", spr_buy_item_triggers("itm_fur_coat", resources=["itm_leather_roll"], tailoring=2)),
  ("pw_buy_friar_robe",spr_buy_item_flags(2),"pw_friar_robe","bo_pw_armor_body", spr_buy_item_triggers("itm_friar_robe", resources=["itm_linen_cloth","itm_stick"], tailoring=2)),
  ("pw_buy_skirmisher_armor",spr_buy_item_flags(5),"skirmisher_armor","bo_pw_armor_body", spr_buy_item_triggers("itm_skirmisher_armor", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_rich_outfit",spr_buy_item_flags(5),"merchant_outf","bo_pw_armor_body", spr_buy_item_triggers("itm_rich_outfit", resources=["itm_linen_cloth"], tailoring=2)),
  ("pw_buy_tabard",spr_buy_item_flags(4),"tabard_b","bo_pw_armor_body", spr_buy_item_triggers("itm_tabard", resources=["itm_linen_cloth"], tailoring=2, tableau="tableau_heraldic_tabard_b")),
  ("pw_buy_khergit_armor",spr_buy_item_flags(3),"khergit_armor_new","bo_pw_armor_body", spr_buy_item_triggers("itm_khergit_armor", resources=["itm_linen_cloth","itm_leather_piece"], tailoring=1)),
  ("pw_buy_leather_vest_plain",spr_buy_item_flags(5),"leather_vest_a","bo_pw_armor_body", spr_buy_item_triggers("itm_leather_vest_plain", resources=["itm_leather_roll"], tailoring=2)),
  ("pw_buy_leather_vest",spr_buy_item_flags(5),"leather_vest_a","bo_pw_armor_body", spr_buy_item_triggers("itm_leather_vest", resources=["itm_leather_roll"], tailoring=2, tableau="tableau_heraldic_leather_vest_a")),
  ("pw_buy_leather_jacket",spr_buy_item_flags(6),"leather_jacket_new","bo_pw_armor_body", spr_buy_item_triggers("itm_leather_jacket", resources=["itm_leather_roll"], tailoring=2)),
  ("pw_buy_priest_robe",spr_buy_item_flags(8),"pw_priest_robe","bo_pw_armor_body", spr_buy_item_triggers("itm_priest_robe", resources=[("itm_linen_cloth",2),"itm_iron_piece"], tailoring=3)),
  ("pw_buy_arena_tunic",spr_buy_item_flags(6),"arena_tunicW_new","bo_pw_armor_body", spr_buy_item_triggers("itm_arena_tunic", resources=["itm_linen_cloth"], tailoring=2, tableau="tableau_colored_arena_tunic")),
  ("pw_buy_steppe_armor",spr_buy_item_flags(6),"lamellar_leather","bo_pw_armor_body", spr_buy_item_triggers("itm_steppe_armor", resources=["itm_linen_cloth","itm_leather_piece"], tailoring=2, engineer=2, tableau="tableau_colored_lamellar_leather")),
  ("pw_buy_leather_armor",spr_buy_item_flags(6),"tattered_leather_armor_a","bo_pw_armor_body", spr_buy_item_triggers("itm_leather_armor", resources=["itm_leather_roll","itm_iron_piece"], engineer=2)),
  ("pw_buy_pilgrim_disguise",spr_buy_item_flags(5),"pilgrim_outfit","bo_pw_armor_body", spr_buy_item_triggers("itm_pilgrim_disguise", resources=["itm_linen_cloth","itm_leather_piece"], tailoring=1)),
  ("pw_buy_red_gambeson",spr_buy_item_flags(7),"red_gambeson_a","bo_pw_armor_body", spr_buy_item_triggers("itm_red_gambeson", resources=["itm_linen_cloth","itm_leather_piece"], tailoring=3, engineer=2)),
  ("pw_buy_padded_cloth",spr_buy_item_flags(7),"padded_cloth_a","bo_pw_armor_body", spr_buy_item_triggers("itm_padded_cloth", resources=["itm_linen_cloth"], tailoring=3, engineer=2, tableau="tableau_heraldic_padded_cloth_a")),
  ("pw_buy_aketon_green",spr_buy_item_flags(7),"padded_cloth_b","bo_pw_armor_body", spr_buy_item_triggers("itm_aketon_green", resources=["itm_linen_cloth"], tailoring=3, engineer=2, tableau="tableau_heraldic_padded_cloth_b")),
  ("pw_buy_archers_vest",spr_buy_item_flags(7),"archers_vest","bo_pw_armor_body", spr_buy_item_triggers("itm_archers_vest", resources=["itm_linen_cloth"], tailoring=2, engineer=2)),
  ("pw_buy_nomad_vest",spr_buy_item_flags(7),"nomad_vest_new","bo_pw_armor_body", spr_buy_item_triggers("itm_nomad_vest", resources=["itm_leather_roll"], tailoring=3, engineer=2)),
  ("pw_buy_ragged_outfit",spr_buy_item_flags(6),"ragged_outfit_a_new","bo_pw_armor_body", spr_buy_item_triggers("itm_ragged_outfit", resources=["itm_linen_cloth"], tailoring=2, engineer=2)),
  ("pw_buy_surgeon_coat",spr_buy_item_flags(7),"pw_surgeon_coat","bo_pw_armor_body", spr_buy_item_triggers("itm_surgeon_coat", resources=["itm_linen_cloth","itm_board","itm_iron_piece"], engineer=2)),
  ("pw_buy_nomad_armor",spr_buy_item_flags(7),"nomad_armor_new","bo_pw_armor_body", spr_buy_item_triggers("itm_nomad_armor", resources=["itm_leather_roll"], tailoring=2, engineer=2)),
  ("pw_buy_nomad_robe",spr_buy_item_flags(8),"nomad_robe_a","bo_pw_armor_body", spr_buy_item_triggers("itm_nomad_robe", resources=["itm_linen_cloth","itm_leather_piece"], tailoring=3, engineer=2)),
  ("pw_buy_light_leather",spr_buy_item_flags(8),"light_leather","bo_pw_armor_body", spr_buy_item_triggers("itm_light_leather", resources=["itm_leather_roll"], tailoring=3, engineer=2)),
  ("pw_buy_leather_jerkin",spr_buy_item_flags(8),"ragged_leather_jerkin","bo_pw_armor_body", spr_buy_item_triggers("itm_leather_jerkin", resources=["itm_leather_roll","itm_linen_cloth_small"], tailoring=3, engineer=2)),
  ("pw_buy_padded_leather",spr_buy_item_flags(8),"leather_armor_b","bo_pw_armor_body", spr_buy_item_triggers("itm_padded_leather", resources=["itm_leather_roll","itm_linen_cloth_small"], tailoring=3, engineer=2)),
  ("pw_buy_arena_armor",spr_buy_item_flags(9),"arena_armorW_new","bo_pw_armor_body", spr_buy_item_triggers("itm_arena_armor", resources=["itm_linen_cloth","itm_iron_bar_short"], engineer=2, tableau="tableau_colored_arena_armor")),
  ("pw_buy_tribal_warrior_outfit",spr_buy_item_flags(9),"tribal_warrior_outfit_a_new","bo_pw_armor_body", spr_buy_item_triggers("itm_tribal_warrior_outfit", resources=["itm_leather_roll"], tailoring=3, engineer=3)),
  ("pw_buy_sarranid_leather_armor",spr_buy_item_flags(9),"sarranid_leather_armor","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_leather_armor", resources=["itm_leather_roll"], engineer=3)),
  ("pw_buy_courtly_outfit",spr_buy_item_flags(10),"nobleman_outf","bo_pw_armor_body", spr_buy_item_triggers("itm_courtly_outfit", resources=["itm_linen_cloth","itm_leather_piece"], tailoring=3)),
  ("pw_buy_nobleman_outfit",spr_buy_item_flags(10),"nobleman_outfit_b_new","bo_pw_armor_body", spr_buy_item_triggers("itm_nobleman_outfit", resources=["itm_linen_cloth","itm_leather_piece"], tailoring=3)),
  ("pw_buy_sarranid_cavalry_robe",spr_buy_item_flags(10),"arabian_armor_a","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_cavalry_robe", resources=["itm_linen_cloth","itm_iron_bar_short"], engineer=3)),
  ("pw_buy_studded_leather_coat",spr_buy_item_flags(10),"leather_armor_a","bo_pw_armor_body", spr_buy_item_triggers("itm_studded_leather_coat", resources=["itm_leather_roll","itm_linen_cloth_small","itm_iron_bar_short"], engineer=3)),
  ("pw_buy_byrnie",spr_buy_item_flags(11),"byrnie_a_new","bo_pw_armor_body", spr_buy_item_triggers("itm_byrnie", resources=["itm_iron_bar_short","itm_linen_cloth"], engineer=3)),
  ("pw_buy_haubergeon",spr_buy_item_flags(11),"haubergeon_c","bo_pw_armor_body", spr_buy_item_triggers("itm_haubergeon", resources=[("itm_iron_bar_short",2),"itm_linen_cloth_small"], engineer=3)),
  ("pw_buy_arabian_armor_b",spr_buy_item_flags(11),"arabian_armor_b","bo_pw_armor_body", spr_buy_item_triggers("itm_arabian_armor_b", resources=[("itm_iron_bar_short",2),"itm_linen_cloth_small"], engineer=4)),
  ("pw_buy_lamellar_vest",spr_buy_item_flags(11),"lamellar_vest_a","bo_pw_armor_body", spr_buy_item_triggers("itm_lamellar_vest", resources=["itm_iron_bar_short","itm_linen_cloth"], engineer=4)),
  ("pw_buy_lamellar_vest_khergit",spr_buy_item_flags(11),"lamellar_vest_b","bo_pw_armor_body", spr_buy_item_triggers("itm_lamellar_vest_khergit", resources=["itm_iron_bar_short","itm_linen_cloth"], engineer=4, tableau="tableau_colored_lamellar_vest_b")),
  ("pw_buy_mail_shirt",spr_buy_item_flags(11),"mail_shirt_a","bo_pw_armor_body", spr_buy_item_triggers("itm_mail_shirt", resources=["itm_iron_bar_short","itm_linen_cloth"], engineer=4)),
  ("pw_buy_mail_hauberk",spr_buy_item_flags(11),"hauberk_a_new","bo_pw_armor_body", spr_buy_item_triggers("itm_mail_hauberk", resources=[("itm_iron_bar_short",2),"itm_linen_cloth"], engineer=4)),
  ("pw_buy_sarranid_mail_shirt",spr_buy_item_flags(12),"sarranian_mail_shirt","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_mail_shirt", resources=[("itm_iron_bar_short",2),"itm_linen_cloth"], engineer=5)),
  ("pw_buy_bishop_armor",spr_buy_item_flags(16),"pw_bishop_armor","bo_pw_armor_body", spr_buy_item_triggers("itm_bishop_armor", resources=[("itm_iron_bar_short",2),"itm_linen_cloth","itm_gold_bar"], engineer=6)),
  ("pw_buy_mail_with_surcoat",spr_buy_item_flags(12),"mail_long_surcoat_new","bo_pw_armor_body", spr_buy_item_triggers("itm_mail_with_surcoat", resources=[("itm_iron_bar_short",2),"itm_linen_cloth"], engineer=5, tableau="tableau_heraldic_mail_long_surcoat")),
  ("pw_buy_surcoat_over_mail",spr_buy_item_flags(12),"surcoat_over_mail_new","bo_pw_armor_body", spr_buy_item_triggers("itm_surcoat_over_mail", resources=[("itm_iron_bar_short",2),"itm_linen_cloth"], engineer=5, tableau="tableau_heraldic_surcoat_over_mail")),
  ("pw_buy_brigandine_red",spr_buy_item_flags(13),"brigandine_b","bo_pw_armor_body", spr_buy_item_triggers("itm_brigandine_red", resources=[("itm_iron_bar_short",2),"itm_leather_roll"], engineer=6, tableau="tableau_heraldic_brigandine_b")),
  ("pw_buy_mamluke_mail",spr_buy_item_flags(14),"sarranid_elite_cavalary","bo_pw_armor_body", spr_buy_item_triggers("itm_mamluke_mail", resources=[("itm_iron_bar_short",2),"itm_linen_cloth","itm_linen_cloth_small"], engineer=6)),
  ("pw_buy_lamellar_armor",spr_buy_item_flags(15),"lamellar_armor_b","bo_pw_armor_body", spr_buy_item_triggers("itm_lamellar_armor", resources=[("itm_iron_bar_short",2),"itm_linen_cloth"], engineer=6)),
  ("pw_buy_scale_armor",spr_buy_item_flags(14),"lamellar_armor_e","bo_pw_armor_body", spr_buy_item_triggers("itm_scale_armor", resources=[("itm_iron_bar_short",2),"itm_linen_cloth"], engineer=6)),
  ("pw_buy_banded_armor",spr_buy_item_flags(15),"banded_armor_a","bo_pw_armor_body", spr_buy_item_triggers("itm_banded_armor", resources=[("itm_iron_bar_short",2),"itm_leather_roll"], engineer=6)),
  ("pw_buy_cuir_bouilli",spr_buy_item_flags(15),"cuir_bouilli_a","bo_pw_armor_body", spr_buy_item_triggers("itm_cuir_bouilli", resources=[("itm_iron_bar_short",2),"itm_leather_roll"], engineer=6)),
  ("pw_buy_coat_of_plates",spr_buy_item_flags(16),"coat_of_plates_a","bo_pw_armor_body", spr_buy_item_triggers("itm_coat_of_plates", resources=[("itm_iron_bar_short",2),"itm_leather_roll"], engineer=6)),
  ("pw_buy_coat_of_plates_red",spr_buy_item_flags(16),"coat_of_plates_red","bo_pw_armor_body", spr_buy_item_triggers("itm_coat_of_plates_red", resources=[("itm_iron_bar_short",2),"itm_leather_roll"], engineer=6, tableau="tableau_heraldic_coat_of_plates")),
  ("pw_buy_khergit_elite_armor",spr_buy_item_flags(17),"lamellar_armor_d","bo_pw_armor_body", spr_buy_item_triggers("itm_khergit_elite_armor", resources=[("itm_iron_bar",2),"itm_leather_piece","itm_linen_cloth"], engineer=6, tableau="tableau_heraldic_lamellar_armor_d")),
  ("pw_buy_vaegir_elite_armor",spr_buy_item_flags(17),"lamellar_armor_c","bo_pw_armor_body", spr_buy_item_triggers("itm_vaegir_elite_armor", resources=[("itm_iron_bar",2),"itm_leather_piece","itm_linen_cloth"], engineer=6)),
  ("pw_buy_sarranid_elite_armor",spr_buy_item_flags(17),"tunic_armor_a","bo_pw_armor_body", spr_buy_item_triggers("itm_sarranid_elite_armor", resources=[("itm_iron_bar",2),"itm_leather_piece","itm_linen_cloth"], engineer=6)),
  ("pw_buy_plate_armor",spr_buy_item_flags(23),"full_plate_armor","bo_pw_armor_body", spr_buy_item_triggers("itm_plate_armor", resources=[("itm_iron_bar_long",2),"itm_leather_piece","itm_linen_cloth"], engineer=7)),
  ("pw_buy_black_armor",spr_buy_item_flags(24),"black_armor","bo_pw_armor_body", spr_buy_item_triggers("itm_black_armor", resources=[("itm_iron_bar_long",2),"itm_leather_piece","itm_linen_cloth"], engineer=7)),
  ("pw_buy_light_heraldic_mail",spr_buy_item_flags(10),"heraldic_armor_new_c","bo_pw_armor_body", spr_buy_item_triggers("itm_light_heraldic_mail", resources=["itm_iron_bar_short","itm_linen_cloth","itm_leather_piece"], engineer=4, tableau="tableau_heraldic_armor_c")),
  ("pw_buy_heraldic_mail_with_tunic",spr_buy_item_flags(12),"heraldic_armor_new_b","bo_pw_armor_body", spr_buy_item_triggers("itm_heraldic_mail_with_tunic", resources=[("itm_iron_bar_short",2),"itm_linen_cloth"], engineer=4, tableau="tableau_heraldic_armor_b")),
  ("pw_buy_heraldic_mail_with_tabard",spr_buy_item_flags(14),"heraldic_armor_new_d","bo_pw_armor_body", spr_buy_item_triggers("itm_heraldic_mail_with_tabard", resources=[("itm_iron_bar_short",3),"itm_linen_cloth"], engineer=5, tableau="tableau_heraldic_armor_d")),
  ("pw_buy_heraldic_mail_with_surcoat",spr_buy_item_flags(16),"heraldic_armor_new_a","bo_pw_armor_body", spr_buy_item_triggers("itm_heraldic_mail_with_surcoat", resources=[("itm_iron_bar_short",3),"itm_leather_piece","itm_linen_cloth"], engineer=6, tableau="tableau_heraldic_armor_a")),

  ("pw_buy_wrapping_boots",spr_buy_item_flags(1),"wrapping_boots_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_wrapping_boots", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_woolen_hose",spr_buy_item_flags(1),"woolen_hose_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_woolen_hose", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_friar_sandals",spr_buy_item_flags(1),"pw_friar_sandals","bo_pw_armor_foot", spr_buy_item_triggers("itm_friar_sandals", resources=["itm_leather_piece"], tailoring=1)),
  ("pw_buy_blue_hose",spr_buy_item_flags(1),"blue_hose_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_blue_hose", resources=["itm_linen_cloth_small"], tailoring=1)),
  ("pw_buy_bride_shoes",spr_buy_item_flags(5),"bride_shoes","bo_pw_armor_foot", spr_buy_item_triggers("itm_bride_shoes", resources=["itm_linen_cloth_small"], tailoring=2)),
  ("pw_buy_priest_leggings",spr_buy_item_flags(2),"pw_priest_leggings","bo_pw_armor_foot", spr_buy_item_triggers("itm_priest_leggings", resources=[("itm_linen_cloth_small",2)], tailoring=2)),
  ("pw_buy_sarranid_boots_a",spr_buy_item_flags(2),"sarranid_shoes","bo_pw_armor_foot", spr_buy_item_triggers("itm_sarranid_boots_a", resources=[("itm_linen_cloth_small",2)], tailoring=1)),
  ("pw_buy_hunter_boots",spr_buy_item_flags(1),"hunter_boots_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_hunter_boots", resources=[("itm_leather_piece",2)], tailoring=2)),
  ("pw_buy_hide_boots",spr_buy_item_flags(2),"hide_boots_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_hide_boots", resources=[("itm_leather_piece",2)], tailoring=2)),
  ("pw_buy_ankle_boots",spr_buy_item_flags(3),"ankle_boots_a_new","bo_pw_armor_foot", spr_buy_item_triggers("itm_ankle_boots", resources=[("itm_linen_cloth_small",2)], tailoring=2)),
  ("pw_buy_nomad_boots",spr_buy_item_flags(3),"nomad_boots_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_nomad_boots", resources=["itm_linen_cloth_small","itm_leather_piece"], tailoring=2)),
  ("pw_buy_light_leather_boots",spr_buy_item_flags(3),"light_leather_boots","bo_pw_armor_foot", spr_buy_item_triggers("itm_light_leather_boots", resources=[("itm_leather_piece",2)], tailoring=2)),
  ("pw_buy_leather_boots",spr_buy_item_flags(4),"leather_boots_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_leather_boots", resources=[("itm_leather_piece",2)], tailoring=2, engineer=3)),
  ("pw_buy_sarranid_boots_b",spr_buy_item_flags(4),"sarranid_boots","bo_pw_armor_foot", spr_buy_item_triggers("itm_sarranid_boots_b", resources=[("itm_leather_piece",2)], tailoring=3, engineer=3)),
  ("pw_buy_khergit_leather_boots",spr_buy_item_flags(4),"khergit_leather_boots","bo_pw_armor_foot", spr_buy_item_triggers("itm_khergit_leather_boots", resources=[("itm_leather_piece",2)], tailoring=3, engineer=3)),
  ("pw_buy_sarranid_boots_c",spr_buy_item_flags(5),"sarranid_camel_boots","bo_pw_armor_foot", spr_buy_item_triggers("itm_sarranid_boots_c", resources=[("itm_leather_piece",2),"itm_iron_piece"], tailoring=3, engineer=3)),
  ("pw_buy_splinted_leather_greaves",spr_buy_item_flags(5),"leather_greaves_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_splinted_leather_greaves", resources=[("itm_leather_piece",2),"itm_iron_piece"], engineer=3)),
  ("pw_buy_bishop_chausses",spr_buy_item_flags(6),"pw_bishop_chausses","bo_pw_armor_foot", spr_buy_item_triggers("itm_bishop_chausses", resources=["itm_leather_piece",("itm_iron_piece",2)], engineer=3)),
  ("pw_buy_mail_chausses",spr_buy_item_flags(6),"mail_chausses_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_mail_chausses", resources=["itm_leather_piece",("itm_iron_piece",2)], engineer=4)),
  ("pw_buy_splinted_greaves",spr_buy_item_flags(6),"splinted_greaves_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_splinted_greaves", resources=["itm_linen_cloth_small",("itm_iron_piece",2)], engineer=4)),
  ("pw_buy_sarranid_boots_d",spr_buy_item_flags(6),"sarranid_mail_chausses","bo_pw_armor_foot", spr_buy_item_triggers("itm_sarranid_boots_d", resources=["itm_leather_piece",("itm_iron_piece",2)], engineer=5)),
  ("pw_buy_mail_boots",spr_buy_item_flags(7),"mail_boots_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_mail_boots", resources=["itm_leather_piece",("itm_iron_bar_short",2)], engineer=5)),
  ("pw_buy_iron_greaves",spr_buy_item_flags(8),"iron_greaves_a","bo_pw_armor_foot", spr_buy_item_triggers("itm_iron_greaves", resources=["itm_leather_piece",("itm_iron_bar_short",3)], engineer=6)),
  ("pw_buy_plate_boots",spr_buy_item_flags(10),"plate_boots","bo_pw_armor_foot", spr_buy_item_triggers("itm_plate_boots", resources=[("itm_leather_piece",2),("itm_iron_bar",2)], engineer=6)),
  ("pw_buy_black_greaves",spr_buy_item_flags(11),"black_greaves","bo_pw_armor_foot", spr_buy_item_triggers("itm_black_greaves", resources=[("itm_leather_piece",2),("itm_iron_bar",2)], engineer=6)),

  ("pw_buy_leather_gloves",spr_buy_item_flags(2),"leather_gloves_L","bo_pw_armor_hand", spr_buy_item_triggers("itm_leather_gloves", resources=["itm_leather_piece"], tailoring=2, engineer=4)),
  ("pw_buy_bishop_gloves",spr_buy_item_flags(4),"pw_bishop_glove_L","bo_pw_armor_hand", spr_buy_item_triggers("itm_bishop_gloves", resources=[("itm_linen_cloth_small",2)], tailoring=3)),
  ("pw_buy_mail_mittens",spr_buy_item_flags(4),"mail_mittens_L","bo_pw_armor_hand", spr_buy_item_triggers("itm_mail_mittens", resources=["itm_iron_piece"], engineer=3)),
  ("pw_buy_lamellar_gauntlets",spr_buy_item_flags(5),"scale_gauntlets_a_L","bo_pw_armor_hand", spr_buy_item_triggers("itm_lamellar_gauntlets", resources=["itm_leather_piece","itm_iron_piece"], engineer=4)),
  ("pw_buy_scale_gauntlets",spr_buy_item_flags(5),"scale_gauntlets_b_L","bo_pw_armor_hand", spr_buy_item_triggers("itm_scale_gauntlets", resources=["itm_leather_piece","itm_iron_piece"], engineer=5)),
  ("pw_buy_gauntlets",spr_buy_item_flags(6),"gauntlets_L","bo_pw_armor_hand", spr_buy_item_triggers("itm_gauntlets", resources=["itm_leather_piece",("itm_iron_bar_short",2)], engineer=6)),

  ("pw_buy_practice_sword",spr_buy_item_flags(1),"pw_practice_sword","bo_pw_weapon", spr_buy_item_triggers("itm_practice_sword", resources=["itm_wood_pole_short"], engineer=2)),
  ("pw_buy_heavy_practice_sword",spr_buy_item_flags(2),"pw_heavy_practice_sword","bo_pw_weapon", spr_buy_item_triggers("itm_heavy_practice_sword", resources=["itm_wood_pole_short"], engineer=2)),
  ("pw_buy_winged_mace",spr_buy_item_flags(3),"flanged_mace","bo_pw_weapon_small", spr_buy_item_triggers("itm_winged_mace", resources=["itm_iron_bar"], engineer=2)),
  ("pw_buy_spiked_mace",spr_buy_item_flags(2),"spiked_mace_new","bo_pw_weapon_small", spr_buy_item_triggers("itm_spiked_mace", resources=["itm_iron_bar"], engineer=2)),
  ("pw_buy_mace_2",spr_buy_item_flags(2),"mace_a","bo_pw_weapon_small", spr_buy_item_triggers("itm_mace_2", resources=["itm_iron_piece", "itm_stick"], engineer=1)),
  ("pw_buy_mace_4",spr_buy_item_flags(2),"mace_b","bo_pw_weapon_small", spr_buy_item_triggers("itm_mace_4", resources=["itm_iron_piece", "itm_stick"], engineer=1)),
  ("pw_buy_club_with_spike_head",spr_buy_item_flags(3),"mace_e","bo_pw_weapon", spr_buy_item_triggers("itm_club_with_spike_head", resources=["itm_iron_bar_short", "itm_wood_pole_short"], engineer=2)),
  ("pw_buy_long_spiked_club",spr_buy_item_flags(3),"mace_long_c","bo_pw_weapon_big", spr_buy_item_triggers("itm_long_spiked_club", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_long_hafted_spiked_mace",spr_buy_item_flags(4),"mace_long_b","bo_pw_weapon_big", spr_buy_item_triggers("itm_long_hafted_spiked_mace", resources=["itm_iron_bar_short", "itm_wood_pole"], engineer=3)),
  ("pw_buy_fighting_pick",spr_buy_item_flags(4),"fighting_pick_new","bo_pw_weapon_small", spr_buy_item_triggers("itm_fighting_pick", resources=["itm_iron_bar_short", "itm_stick"], engineer=2)),
  ("pw_buy_military_pick",spr_buy_item_flags(5),"steel_pick_new","bo_pw_weapon_small", spr_buy_item_triggers("itm_military_pick", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_military_sickle",spr_buy_item_flags(5),"military_sickle_a","bo_pw_weapon_small", spr_buy_item_triggers("itm_military_sickle", resources=["itm_iron_bar_short", "itm_stick"], engineer=2)),
  ("pw_buy_military_hammer",spr_buy_item_flags(4),"military_hammer","bo_pw_weapon_small", spr_buy_item_triggers("itm_military_hammer", resources=["itm_iron_bar_short", "itm_stick"], engineer=3)),
  ("pw_buy_morningstar",spr_buy_item_flags(14),"mace_morningstar_new","bo_pw_weapon", spr_buy_item_triggers("itm_morningstar", resources=["itm_iron_bar_long", "itm_iron_bar_short"], engineer=4)),
  ("pw_buy_falchion",spr_buy_item_flags(4),"falchion_new","bo_pw_weapon_small", spr_buy_item_triggers("itm_falchion", resources=["itm_iron_bar"], engineer=2)),
  ("pw_buy_curved_sword",spr_buy_item_flags(6),"khergit_sword","bo_pw_weapon", spr_buy_item_triggers("itm_curved_sword", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_sword_medieval_a",spr_buy_item_flags(7),"sword_medieval_a","bo_pw_weapon", spr_buy_item_triggers("itm_sword_medieval_a", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_sword_medieval_b_small",spr_buy_item_flags(6),"sword_medieval_b_small","bo_pw_weapon", spr_buy_item_triggers("itm_sword_medieval_b_small", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_sword_medieval_c_long",spr_buy_item_flags(8),"sword_medieval_c_long","bo_pw_weapon", spr_buy_item_triggers("itm_sword_medieval_c_long", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_sword_medieval_d_long",spr_buy_item_flags(10),"sword_medieval_d_long","bo_pw_weapon", spr_buy_item_triggers("itm_sword_medieval_d_long", resources=["itm_iron_bar"], engineer=4)),
  ("pw_buy_sword_viking_c",spr_buy_item_flags(7),"sword_viking_c","bo_pw_weapon", spr_buy_item_triggers("itm_sword_viking_c", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_sword_viking_b_small",spr_buy_item_flags(6),"sword_viking_b_small","bo_pw_weapon", spr_buy_item_triggers("itm_sword_viking_b_small", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_sword_viking_a_long",spr_buy_item_flags(8),"sword_viking_a_long","bo_pw_weapon", spr_buy_item_triggers("itm_sword_viking_a_long", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_arabian_sword_a",spr_buy_item_flags(6),"arabian_sword_a","bo_pw_weapon", spr_buy_item_triggers("itm_arabian_sword_a", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_arabian_sword_b",spr_buy_item_flags(7),"arabian_sword_b","bo_pw_weapon", spr_buy_item_triggers("itm_arabian_sword_b", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_arabian_sword_c",spr_buy_item_flags(9),"arabian_sword_c","bo_pw_weapon", spr_buy_item_triggers("itm_arabian_sword_c", resources=["itm_iron_bar"], engineer=4)),
  ("pw_buy_arabian_sword_d",spr_buy_item_flags(8),"arabian_sword_d","bo_pw_weapon", spr_buy_item_triggers("itm_arabian_sword_d", resources=["itm_iron_bar"], engineer=4)),
  ("pw_buy_scimitar",spr_buy_item_flags(9),"scimitar_a","bo_pw_weapon", spr_buy_item_triggers("itm_scimitar", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_scimitar_b",spr_buy_item_flags(10),"scimitar_b","bo_pw_weapon", spr_buy_item_triggers("itm_scimitar_b", resources=["itm_iron_bar"], engineer=4)),
  ("pw_buy_khergit_sword_c",spr_buy_item_flags(8),"khergit_sword_c","bo_pw_weapon", spr_buy_item_triggers("itm_khergit_sword_c", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_khergit_sword_d",spr_buy_item_flags(11),"khergit_sword_d","bo_pw_weapon", spr_buy_item_triggers("itm_khergit_sword_d", resources=["itm_iron_bar"], engineer=4)),
  ("pw_buy_khergit_sword_two_handed_a",spr_buy_item_flags(14),"khergit_sword_two_handed_a","bo_pw_weapon", spr_buy_item_triggers("itm_khergit_sword_two_handed_a", resources=["itm_iron_bar_long"], engineer=6)),
  ("pw_buy_two_handed_cleaver",spr_buy_item_flags(9),"military_cleaver_a","bo_pw_weapon", spr_buy_item_triggers("itm_two_handed_cleaver", resources=["itm_iron_bar_long"], engineer=4)),
  ("pw_buy_military_cleaver_b",spr_buy_item_flags(4),"military_cleaver_b","bo_pw_weapon", spr_buy_item_triggers("itm_military_cleaver_b", resources=["itm_iron_bar"], engineer=2)),
  ("pw_buy_military_cleaver_c",spr_buy_item_flags(5),"military_cleaver_c","bo_pw_weapon", spr_buy_item_triggers("itm_military_cleaver_c", resources=["itm_iron_bar"], engineer=2)),
  ("pw_buy_bastard_sword_a",spr_buy_item_flags(11),"bastard_sword_a","bo_pw_weapon", spr_buy_item_triggers("itm_bastard_sword_a", resources=["itm_iron_bar_long"], engineer=5)),
  ("pw_buy_bastard_sword_b",spr_buy_item_flags(12),"bastard_sword_b","bo_pw_weapon", spr_buy_item_triggers("itm_bastard_sword_b", resources=["itm_iron_bar_long"], engineer=5)),
  ("pw_buy_sword_two_handed_b",spr_buy_item_flags(13),"sword_two_handed_b","bo_pw_weapon", spr_buy_item_triggers("itm_sword_two_handed_b", resources=["itm_iron_bar_long"], engineer=6)),
  ("pw_buy_sword_two_handed_a",spr_buy_item_flags(15),"sword_two_handed_a","bo_pw_weapon", spr_buy_item_triggers("itm_sword_two_handed_a", resources=["itm_iron_bar_long"], engineer=7)),
  ("pw_buy_one_handed_war_axe_b",spr_buy_item_flags(3),"one_handed_war_axe_b","bo_pw_weapon_small", spr_buy_item_triggers("itm_one_handed_war_axe_b", resources=["itm_iron_bar_short", "itm_stick"], engineer=2)),
  ("pw_buy_one_handed_battle_axe_a",spr_buy_item_flags(3),"one_handed_battle_axe_a","bo_pw_weapon_small", spr_buy_item_triggers("itm_one_handed_battle_axe_a", resources=["itm_iron_bar_short", "itm_stick"], engineer=2)),
  ("pw_buy_one_handed_battle_axe_b",spr_buy_item_flags(4),"one_handed_battle_axe_b","bo_pw_weapon_small", spr_buy_item_triggers("itm_one_handed_battle_axe_b", resources=["itm_iron_bar_short", "itm_stick"], engineer=3)),
  ("pw_buy_one_handed_battle_axe_c",spr_buy_item_flags(4),"one_handed_battle_axe_c","bo_pw_weapon_small", spr_buy_item_triggers("itm_one_handed_battle_axe_c", resources=["itm_iron_bar_short", "itm_stick"], engineer=3)),
  ("pw_buy_sarranid_axe_a",spr_buy_item_flags(6),"one_handed_battle_axe_g","bo_pw_weapon_small", spr_buy_item_triggers("itm_sarranid_axe_a", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_sarranid_axe_b",spr_buy_item_flags(6),"one_handed_battle_axe_h","bo_pw_weapon_small", spr_buy_item_triggers("itm_sarranid_axe_b", resources=["itm_iron_bar"], engineer=3)),
  ("pw_buy_two_handed_axe",spr_buy_item_flags(7),"two_handed_battle_axe_a","bo_pw_weapon", spr_buy_item_triggers("itm_two_handed_axe", resources=["itm_wood_pole_short", "itm_iron_bar"], engineer=3)),
  ("pw_buy_two_handed_battle_axe",spr_buy_item_flags(9),"two_handed_battle_axe_b","bo_pw_weapon", spr_buy_item_triggers("itm_two_handed_battle_axe", resources=["itm_wood_pole_short", "itm_iron_bar"], engineer=4)),
  ("pw_buy_shortened_voulge",spr_buy_item_flags(10),"two_handed_battle_axe_c","bo_pw_weapon", spr_buy_item_triggers("itm_shortened_voulge", resources=["itm_wood_pole_short", "itm_iron_bar"], engineer=5)),
  ("pw_buy_bardiche",spr_buy_item_flags(11),"two_handed_battle_axe_d","bo_pw_weapon", spr_buy_item_triggers("itm_bardiche", resources=["itm_wood_pole_short", "itm_iron_bar"], engineer=5)),
  ("pw_buy_shortened_military_scythe",spr_buy_item_flags(9),"two_handed_battle_scythe_a","bo_pw_weapon", spr_buy_item_triggers("itm_shortened_military_scythe", resources=["itm_iron_bar_long", "itm_stick"], engineer=3)),
  ("pw_buy_sarranid_two_handed_axe_a",spr_buy_item_flags(9),"two_handed_battle_axe_g","bo_pw_weapon", spr_buy_item_triggers("itm_sarranid_two_handed_axe_a", resources=["itm_iron_bar_long"], engineer=5)),
  ("pw_buy_sarranid_two_handed_axe_b",spr_buy_item_flags(11),"two_handed_battle_axe_h","bo_pw_weapon", spr_buy_item_triggers("itm_sarranid_two_handed_axe_b", resources=["itm_iron_bar_long"], engineer=6)),
  ("pw_buy_long_axe_a",spr_buy_item_flags(13),"long_axe_a","bo_pw_weapon", spr_buy_item_triggers("itm_long_axe_a", resources=["itm_wood_pole", "itm_iron_bar"], engineer=5)),
  ("pw_buy_glaive",spr_buy_item_flags(9),"glaive_b","bo_pw_weapon_big", spr_buy_item_triggers("itm_glaive", resources=["itm_wood_pole", "itm_iron_bar"], engineer=3)),
  ("pw_buy_staff",spr_buy_item_flags(1),"wooden_staff","bo_pw_weapon_big", spr_buy_item_triggers("itm_staff", resources=["itm_wood_pole"], engineer=0)),
  ("pw_buy_quarter_staff",spr_buy_item_flags(1),"quarter_staff","bo_pw_weapon_big", spr_buy_item_triggers("itm_quarter_staff", resources=["itm_wood_pole"], engineer=1)),
  ("pw_buy_iron_staff",spr_buy_item_flags(3),"iron_staff","bo_pw_weapon_big", spr_buy_item_triggers("itm_iron_staff", resources=["itm_iron_bar_long"], engineer=2)),
  ("pw_buy_shortened_spear",spr_buy_item_flags(2),"spear_g_1-9m","bo_pw_weapon", spr_buy_item_triggers("itm_shortened_spear", resources=["itm_wood_pole", "itm_iron_piece"], engineer=1)),
  ("pw_buy_spear",spr_buy_item_flags(2),"spear_h_2-15m","bo_pw_weapon_big", spr_buy_item_triggers("itm_spear", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_bamboo_spear",spr_buy_item_flags(3),"arabian_spear_a_3m","bo_pw_weapon_big", spr_buy_item_triggers("itm_bamboo_spear", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_war_spear",spr_buy_item_flags(2),"spear_i_2-3m","bo_pw_weapon_big", spr_buy_item_triggers("itm_war_spear", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_light_lance",spr_buy_item_flags(2),"spear_b_2-75m","bo_pw_weapon_big", spr_buy_item_triggers("itm_light_lance", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_lance",spr_buy_item_flags(3),"spear_d_2-8m","bo_pw_weapon_big", spr_buy_item_triggers("itm_lance", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_heavy_lance",spr_buy_item_flags(3),"spear_f_2-9m","bo_pw_weapon_big", spr_buy_item_triggers("itm_heavy_lance", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_great_lance",spr_buy_item_flags(4),"pw_great_lance","bo_pw_weapon_big", spr_buy_item_triggers("itm_great_lance", resources=["itm_wood_pole", ("itm_iron_piece", 2)], engineer=3)),
  ("pw_buy_jousting_lance",spr_buy_item_flags(4),"pw_jousting_lance","bo_pw_weapon_big", spr_buy_item_triggers("itm_jousting_lance", resources=["itm_wood_pole", ("itm_iron_piece", 2)], engineer=3)),
  ("pw_buy_awlpike",spr_buy_item_flags(3),"awl_pike_b","bo_pw_weapon_big", spr_buy_item_triggers("itm_awlpike", resources=["itm_wood_pole", "itm_iron_bar_short"], engineer=2)),
  ("pw_buy_awlpike_long",spr_buy_item_flags(4),"awl_pike_a","bo_pw_weapon_big", spr_buy_item_triggers("itm_awlpike_long", resources=["itm_wood_pole", "itm_iron_bar_short"], engineer=2)),
  ("pw_buy_pike",spr_buy_item_flags(5),"spear_a_3m","bo_pw_weapon_big", spr_buy_item_triggers("itm_pike", resources=["itm_wood_pole", "itm_iron_piece"], engineer=3)),
  ("pw_buy_bec_de_corbin_a",spr_buy_item_flags(9),"bec_de_corbin_a","bo_pw_weapon", spr_buy_item_triggers("itm_bec_de_corbin_a", resources=["itm_wood_pole", "itm_iron_bar_short"], engineer=4)),
  ("pw_buy_bishop_crosier",spr_buy_item_flags(12),"pw_bishop_crosier","bo_pw_weapon_big", spr_buy_item_triggers("itm_bishop_crosier", resources=["itm_wood_pole","itm_gold_bar"], engineer=6)),
  ("pw_buy_hunting_bow",spr_buy_item_flags(2),"hunting_bow","bo_pw_weapon", spr_buy_item_triggers("itm_hunting_bow", resources=["itm_wood_pole_short"], engineer=2)),
  ("pw_buy_short_bow",spr_buy_item_flags(3),"short_bow","bo_pw_weapon", spr_buy_item_triggers("itm_short_bow", resources=["itm_wood_pole_short"], engineer=2)),
  ("pw_buy_nomad_bow",spr_buy_item_flags(3),"nomad_bow","bo_pw_weapon", spr_buy_item_triggers("itm_nomad_bow", resources=["itm_wood_pole_short"], engineer=3)),
  ("pw_buy_long_bow",spr_buy_item_flags(4),"long_bow","bo_pw_weapon", spr_buy_item_triggers("itm_long_bow", resources=["itm_wood_pole"], engineer=3)),
  ("pw_buy_khergit_bow",spr_buy_item_flags(6),"khergit_bow","bo_pw_weapon", spr_buy_item_triggers("itm_khergit_bow", resources=["itm_wood_pole_short"], engineer=3)),
  ("pw_buy_strong_bow",spr_buy_item_flags(7),"strong_bow","bo_pw_weapon", spr_buy_item_triggers("itm_strong_bow", resources=["itm_wood_pole_short"], engineer=4)),
  ("pw_buy_war_bow",spr_buy_item_flags(9),"war_bow","bo_pw_weapon", spr_buy_item_triggers("itm_war_bow", resources=["itm_wood_pole"], engineer=5)),
  ("pw_buy_arrows",spr_buy_item_flags(1),"arrow_b","bo_pw_weapon", spr_buy_item_triggers("itm_arrows", resources=[], engineer=1)),
  ("pw_buy_barbed_arrows",spr_buy_item_flags(1),"barbed_arrow","bo_pw_weapon", spr_buy_item_triggers("itm_barbed_arrows", resources=[], engineer=1)),
  ("pw_buy_khergit_arrows",spr_buy_item_flags(1),"arrow","bo_pw_weapon", spr_buy_item_triggers("itm_khergit_arrows", resources=[], engineer=1)),
  ("pw_buy_bodkin_arrows",spr_buy_item_flags(1),"piercing_arrow","bo_pw_weapon", spr_buy_item_triggers("itm_bodkin_arrows", resources=[], engineer=1)),
  ("pw_buy_hunting_crossbow",spr_buy_item_flags(5),"crossbow_a","bo_pw_weapon_small", spr_buy_item_triggers("itm_hunting_crossbow", pos_offset=(-5,0,0), resources=["itm_iron_piece", "itm_stick"], engineer=2)),
  ("pw_buy_light_crossbow",spr_buy_item_flags(6),"crossbow_b","bo_pw_weapon_small", spr_buy_item_triggers("itm_light_crossbow", pos_offset=(-5,0,0), resources=["itm_iron_piece", "itm_stick"], engineer=3)),
  ("pw_buy_crossbow",spr_buy_item_flags(8),"crossbow_a","bo_pw_weapon_small", spr_buy_item_triggers("itm_crossbow", pos_offset=(-5,0,0), resources=["itm_iron_piece", "itm_stick"], engineer=4)),
  ("pw_buy_heavy_crossbow",spr_buy_item_flags(10),"crossbow_c","bo_pw_weapon_small", spr_buy_item_triggers("itm_heavy_crossbow", pos_offset=(-5,0,0), resources=["itm_iron_piece", "itm_stick"], engineer=5)),
  ("pw_buy_sniper_crossbow",spr_buy_item_flags(15),"crossbow_c","bo_pw_weapon_small", spr_buy_item_triggers("itm_sniper_crossbow", pos_offset=(-5,0,0), resources=["itm_iron_piece", "itm_stick"], engineer=6)),
  ("pw_buy_bolts",spr_buy_item_flags(1),"bolt","bo_pw_weapon_small", spr_buy_item_triggers("itm_bolts", resources=[], engineer=1)),
  ("pw_buy_steel_bolts",spr_buy_item_flags(1),"bolt","bo_pw_weapon_small", spr_buy_item_triggers("itm_steel_bolts", resources=[], engineer=1)),
  ("pw_buy_practice_shield",spr_buy_item_flags(1),"tableau_shield_round_5","bo_pw_shield_round", spr_buy_item_triggers("itm_practice_shield", resources=["itm_board"], engineer=1, tableau="tableau_round_shield_5")),
  ("pw_buy_tab_shield_round_b",spr_buy_item_flags(3),"tableau_shield_round_3","bo_pw_shield_round", spr_buy_item_triggers("itm_tab_shield_round_b", resources=["itm_board"], engineer=1, tableau="tableau_round_shield_3")),
  ("pw_buy_tab_shield_round_c",spr_buy_item_flags(4),"tableau_shield_round_2","bo_pw_shield_round", spr_buy_item_triggers("itm_tab_shield_round_c", resources=["itm_board", "itm_iron_piece"], engineer=2, tableau="tableau_round_shield_2")),
  ("pw_buy_tab_shield_round_d",spr_buy_item_flags(6),"tableau_shield_round_1","bo_pw_shield_round", spr_buy_item_triggers("itm_tab_shield_round_d", resources=["itm_board", ("itm_iron_piece", 2)], engineer=3, tableau="tableau_round_shield_1")),
  ("pw_buy_tab_shield_round_e",spr_buy_item_flags(7),"tableau_shield_round_4","bo_pw_shield_round", spr_buy_item_triggers("itm_tab_shield_round_e", resources=["itm_board", ("itm_iron_piece", 3)], engineer=3, tableau="tableau_round_shield_4")),
  ("pw_buy_tab_shield_kite_b",spr_buy_item_flags(3),"tableau_shield_kite_3","bo_pw_shield_kite", spr_buy_item_triggers("itm_tab_shield_kite_b", resources=[("itm_board", 2)], engineer=1, tableau="tableau_kite_shield_3")),
  ("pw_buy_tab_shield_kite_c",spr_buy_item_flags(4),"tableau_shield_kite_2","bo_pw_shield_kite", spr_buy_item_triggers("itm_tab_shield_kite_c", resources=[("itm_board", 2), "itm_iron_piece"], engineer=2, tableau="tableau_kite_shield_2")),
  ("pw_buy_tab_shield_kite_d",spr_buy_item_flags(6),"tableau_shield_kite_2","bo_pw_shield_kite", spr_buy_item_triggers("itm_tab_shield_kite_d", resources=[("itm_board", 2), "itm_iron_piece"], engineer=3, tableau="tableau_kite_shield_2")),
  ("pw_buy_tab_shield_kite_cav_a",spr_buy_item_flags(4),"tableau_shield_kite_4","bo_pw_shield_kite_small", spr_buy_item_triggers("itm_tab_shield_kite_cav_a", resources=["itm_board", "itm_iron_piece"], engineer=2, tableau="tableau_kite_shield_4")),
  ("pw_buy_tab_shield_kite_cav_b",spr_buy_item_flags(6),"tableau_shield_kite_4","bo_pw_shield_kite_small", spr_buy_item_triggers("itm_tab_shield_kite_cav_b", resources=["itm_board", "itm_iron_piece"], engineer=3, tableau="tableau_kite_shield_4")),
  ("pw_buy_tab_shield_heater_b",spr_buy_item_flags(4),"tableau_shield_heater_1","bo_pw_shield_heater", spr_buy_item_triggers("itm_tab_shield_heater_b", resources=[("itm_board", 2), "itm_iron_piece"], engineer=2, tableau="tableau_heater_shield_1")),
  ("pw_buy_tab_shield_heater_c",spr_buy_item_flags(5),"tableau_shield_heater_1","bo_pw_shield_heater", spr_buy_item_triggers("itm_tab_shield_heater_c", resources=[("itm_board", 2), "itm_iron_piece"], engineer=2, tableau="tableau_heater_shield_1")),
  ("pw_buy_tab_shield_heater_d",spr_buy_item_flags(6),"tableau_shield_heater_1","bo_pw_shield_heater", spr_buy_item_triggers("itm_tab_shield_heater_d", resources=[("itm_board", 2), "itm_iron_piece"], engineer=3, tableau="tableau_heater_shield_1")),
  ("pw_buy_tab_shield_heater_cav_a",spr_buy_item_flags(4),"tableau_shield_heater_2","bo_pw_shield_heater_small", spr_buy_item_triggers("itm_tab_shield_heater_cav_a", resources=["itm_board", "itm_iron_piece"], engineer=3, tableau="tableau_heater_shield_2")),
  ("pw_buy_tab_shield_heater_cav_b",spr_buy_item_flags(5),"tableau_shield_heater_2","bo_pw_shield_heater_small", spr_buy_item_triggers("itm_tab_shield_heater_cav_b", resources=["itm_board", "itm_iron_piece"], engineer=3, tableau="tableau_heater_shield_2")),
  ("pw_buy_tab_shield_pavise_b",spr_buy_item_flags(5),"tableau_shield_pavise_2","bo_pw_shield_pavise", spr_buy_item_triggers("itm_tab_shield_pavise_b", resources=[("itm_board", 3)], engineer=1, tableau="tableau_pavise_shield_2")),
  ("pw_buy_tab_shield_pavise_c",spr_buy_item_flags(7),"tableau_shield_pavise_1","bo_pw_shield_pavise", spr_buy_item_triggers("itm_tab_shield_pavise_c", resources=[("itm_board", 3), "itm_iron_piece"], engineer=2, tableau="tableau_pavise_shield_1")),
  ("pw_buy_tab_shield_pavise_d",spr_buy_item_flags(9),"tableau_shield_pavise_1","bo_pw_shield_pavise", spr_buy_item_triggers("itm_tab_shield_pavise_d", resources=[("itm_board", 3), "itm_iron_piece"], engineer=3, tableau="tableau_pavise_shield_1")),
  ("pw_buy_tab_shield_small_round_a",spr_buy_item_flags(2),"tableau_shield_small_round_3","bo_pw_shield_round_small", spr_buy_item_triggers("itm_tab_shield_small_round_a", resources=["itm_board"], engineer=2, tableau="tableau_small_round_shield_3")),
  ("pw_buy_tab_shield_small_round_b",spr_buy_item_flags(3),"tableau_shield_small_round_1","bo_pw_shield_round_small", spr_buy_item_triggers("itm_tab_shield_small_round_b", resources=["itm_board", "itm_iron_piece"], engineer=2, tableau="tableau_small_round_shield_1")),
  ("pw_buy_tab_shield_small_round_c",spr_buy_item_flags(7),"tableau_shield_small_round_2","bo_pw_shield_round_small", spr_buy_item_triggers("itm_tab_shield_small_round_c", resources=["itm_board", "itm_iron_piece"], engineer=3, tableau="tableau_small_round_shield_2")),
  ("pw_buy_hide_covered_round_shield",spr_buy_item_flags(2),"shield_round_f","bo_pw_shield_round", spr_buy_item_triggers("itm_hide_covered_round_shield", resources=["itm_board", "itm_raw_hide"], engineer=2)),
  ("pw_buy_hide_covered_kite_shield",spr_buy_item_flags(3),"shield_kite_m","bo_pw_shield_round", spr_buy_item_triggers("itm_hide_covered_kite_shield", resources=[("itm_board", 2), "itm_raw_hide"], engineer=2)),
  ("pw_buy_steel_shield",spr_buy_item_flags(13),"shield_dragon","bo_pw_shield_round", spr_buy_item_triggers("itm_steel_shield", resources=["itm_iron_bar"], engineer=6)),

  ("pw_buy_sumpter_horse",spr_buy_item_flags(2),"sumpter_horse","bo_pw_horse", spr_buy_item_triggers("itm_sumpter_horse", resources=["itm_board", "itm_wheat_sheaf"], herding=1)),
  ("pw_buy_cart_horse",spr_buy_item_flags(3),"sumpter_horse","bo_pw_horse", spr_buy_item_triggers("itm_cart_horse", resources=["itm_board", ("itm_wheat_sheaf", 2)], herding=1)),
  ("pw_buy_saddle_horse",spr_buy_item_flags(5),"saddle_horse","bo_pw_horse", spr_buy_item_triggers("itm_saddle_horse", resources=["itm_saddle", "itm_wheat_sheaf"], herding=1)),
  ("pw_buy_steppe_horse",spr_buy_item_flags(6),"steppe_horse","bo_pw_horse", spr_buy_item_triggers("itm_steppe_horse", resources=["itm_saddle", "itm_wheat_sheaf"], herding=1)),
  ("pw_buy_arabian_horse_a",spr_buy_item_flags(7),"arabian_horse_a","bo_pw_horse", spr_buy_item_triggers("itm_arabian_horse_a", resources=["itm_saddle", "itm_wheat_sheaf"], herding=2)),
  ("pw_buy_arabian_horse_b",spr_buy_item_flags(8),"arabian_horse_b","bo_pw_horse", spr_buy_item_triggers("itm_arabian_horse_b", resources=["itm_saddle", "itm_wheat_sheaf"], herding=2)),
  ("pw_buy_courser",spr_buy_item_flags(10),"courser","bo_pw_horse", spr_buy_item_triggers("itm_courser", resources=["itm_saddle", "itm_wheat_sheaf"], herding=3)),
  ("pw_buy_hunter",spr_buy_item_flags(12),"hunting_horse","bo_pw_horse", spr_buy_item_triggers("itm_hunter", resources=["itm_saddle", "itm_wheat_sheaf"], herding=2)),
  ("pw_buy_warhorse",spr_buy_item_flags(15),"warhorse_chain","bo_pw_horse", spr_buy_item_triggers("itm_warhorse", resources=["itm_saddle", "itm_horse_armor", "itm_wheat_sheaf"], herding=3)),
  ("pw_buy_warhorse_steppe",spr_buy_item_flags(15),"warhorse_steppe","bo_pw_horse", spr_buy_item_triggers("itm_warhorse_steppe", resources=["itm_saddle", "itm_horse_armor", "itm_wheat_sheaf"], herding=3)),
  ("pw_buy_warhorse_sarranid",spr_buy_item_flags(15),"warhorse_sarranid","bo_pw_horse", spr_buy_item_triggers("itm_warhorse_sarranid", resources=["itm_saddle", "itm_horse_armor", ("itm_wheat_sheaf", 2)], herding=3)),
  ("pw_buy_charger",spr_buy_item_flags(17),"charger_new","bo_pw_horse", spr_buy_item_triggers("itm_charger", resources=["itm_saddle", "itm_horse_armor", ("itm_wheat_sheaf", 2)], herding=3)),
  ("pw_buy_plated_charger",spr_buy_item_flags(20),"plated_charger","bo_pw_horse", spr_buy_item_triggers("itm_plated_charger", resources=["itm_saddle", "itm_horse_armor", ("itm_wheat_sheaf", 2)], herding=3)),
  ("pw_buy_saddle",spr_buy_item_flags(4),"pw_saddle","bo_pw_saddle", spr_buy_item_triggers("itm_saddle", pos_offset=(0,0,20), resources=["itm_leather_roll", "itm_board"], engineer=2)),
  ("pw_buy_horse_armor",spr_buy_item_flags(16),"pw_horse_armor","bo_pw_horse_armor", spr_buy_item_triggers("itm_horse_armor", pos_offset=(0,80,0), resources=[("itm_iron_bar", 4)], engineer=6)),

  ("pw_buy_woodcutter_axe",spr_buy_item_flags(2),"pw_wood_axe","bo_pw_weapon", spr_buy_item_triggers("itm_woodcutter_axe", resources=["itm_iron_bar_short", "itm_wood_pole_short"], engineer=2)),
  ("pw_buy_small_mining_pick",spr_buy_item_flags(2),"pw_small_mining_pick","bo_pw_weapon", spr_buy_item_triggers("itm_small_mining_pick", resources=["itm_iron_bar_short", "itm_wood_pole_short"], engineer=2)),
  ("pw_buy_mining_pick",spr_buy_item_flags(5),"pw_mining_pick","bo_pw_weapon", spr_buy_item_triggers("itm_mining_pick", resources=["itm_iron_bar", "itm_wood_pole_short"], engineer=3)),
  ("pw_buy_repair_hammer",spr_buy_item_flags(3),"pw_repair_hammer","bo_pw_weapon_small", spr_buy_item_triggers("itm_repair_hammer", resources=["itm_iron_piece", "itm_stick"], engineer=2)),
  ("pw_buy_lock_pick",spr_buy_item_flags(8),"pw_lock_pick","bo_pw_weapon_small", spr_buy_item_triggers("itm_lock_pick", resources=["itm_iron_piece"], engineer=3)),
  ("pw_buy_bucket",spr_buy_item_flags(1),"pw_bucket_ground","bo_pw_bucket", spr_buy_item_triggers("itm_bucket", pos_offset=(0,0,20), resources=[("itm_board", 2), "itm_iron_piece"], engineer=2)),
  ("pw_buy_fishing_spear",spr_buy_item_flags(2),"pw_fishing_spear","bo_pw_weapon_big", spr_buy_item_triggers("itm_fishing_spear", resources=["itm_wood_pole", "itm_iron_bar_short"], engineer=2)),
  ("pw_buy_fishing_net",spr_buy_item_flags(4),"pw_fishing_net_b","bo_pw_fishing_net_b", spr_buy_item_triggers("itm_fishing_net", pos_offset=(150,-100,0), rotate=(0,-90,0), resources=[("itm_wood_pole_short", 2), ("itm_linen_thread", 2)], engineer=2)),
  ("pw_buy_sickle",spr_buy_item_flags(1),"pw_sickle","bo_pw_weapon_small", spr_buy_item_triggers("itm_sickle", resources=["itm_iron_bar_short", "itm_stick"], engineer=2)),
  ("pw_buy_scythe",spr_buy_item_flags(3),"pw_scythe","bo_pw_weapon_big", spr_buy_item_triggers("itm_scythe", resources=["itm_iron_bar", "itm_wood_pole"], engineer=2)),
  ("pw_buy_wheat_sack",spr_buy_item_flags(1),"pw_wheat_sack","bo_pw_weapon_small", spr_buy_item_triggers("itm_wheat_sack", pos_offset=(0,0,-20), resources=["itm_wheat_sheaf"])),
  ("pw_buy_kitchen_knife",spr_buy_item_flags(1),"pw_kitchen_knife","bo_pw_weapon_small", spr_buy_item_triggers("itm_kitchen_knife", resources=["itm_iron_piece"], engineer=2)),
  ("pw_buy_cleaver",spr_buy_item_flags(2),"cleaver_new","bo_pw_weapon_small", spr_buy_item_triggers("itm_cleaver", resources=["itm_iron_bar_short"], engineer=2)),
  ("pw_buy_knife",spr_buy_item_flags(1),"peasant_knife_new","bo_pw_weapon_small", spr_buy_item_triggers("itm_knife", resources=["itm_iron_bar_short"], engineer=2)),
  ("pw_buy_butchering_knife",spr_buy_item_flags(2),"khyber_knife_new","bo_pw_weapon_small", spr_buy_item_triggers("itm_butchering_knife", resources=["itm_iron_bar_short"], engineer=3)),
  ("pw_buy_broom",spr_buy_item_flags(1),"pw_broom","bo_pw_weapon", spr_buy_item_triggers("itm_broom", resources=["itm_wood_pole_short", "itm_flax_bundle"], engineer=0)),
  ("pw_buy_herding_crook",spr_buy_item_flags(2),"pw_herding_crook","bo_pw_weapon_big", spr_buy_item_triggers("itm_herding_crook", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_surgeon_scalpel",spr_buy_item_flags(8),"dagger_b_scabbard","bo_pw_weapon_small", spr_buy_item_triggers("itm_surgeon_scalpel", resources=["itm_iron_piece"], engineer=4)),
  ("pw_buy_dagger",spr_buy_item_flags(3),"scab_dagger","bo_pw_weapon_small", spr_buy_item_triggers("itm_dagger", resources=["itm_iron_bar_short"], engineer=3)),
  ("pw_buy_poisoned_dagger",spr_buy_item_flags(20),"scab_dagger","bo_pw_weapon_small", spr_buy_item_triggers("itm_poisoned_dagger", resources=["itm_dagger", "itm_poison_herb"], engineer=4)),
  ("pw_buy_thin_lance",spr_buy_item_flags(3),"spear_d_2-8m","bo_pw_weapon_big", spr_buy_item_triggers("itm_thin_lance", resources=["itm_wood_pole", "itm_iron_piece"], engineer=2)),
  ("pw_buy_torch",spr_use_time(1),"pw_torch","bo_pw_weapon_small", spr_buy_item_triggers("itm_torch", resources=["itm_stick"], engineer=1)),
  ("pw_buy_banner",spr_use_time(4),"pw_banner_pole_only","bo_pw_banner_pole", spr_buy_banner_triggers("itm_pw_banner_pole_a01")),
  ("pw_buy_banner_mercenary",spr_use_time(5),"pw_banner_pole_only","bo_pw_banner_pole", spr_buy_banner_triggers("itm_pw_banner_pole_a01", mercenary=True)),
  ("pw_buy_book_a",spr_buy_item_flags(20),"pw_book_a","bo_pw_weapon_small", spr_buy_item_triggers("itm_book_a", resources=["itm_linen_cloth_small","itm_leather_piece"], engineer=2)),
  ("pw_buy_book_b",spr_buy_item_flags(25),"pw_book_b","bo_pw_weapon_small", spr_buy_item_triggers("itm_book_b", resources=["itm_linen_cloth_small","itm_leather_piece"], engineer=2)),
  ("pw_buy_book_c",spr_buy_item_flags(27),"pw_book_c","bo_pw_weapon_small", spr_buy_item_triggers("itm_book_c", resources=["itm_linen_cloth_small","itm_leather_piece"], engineer=2)),
  ("pw_buy_book_d",spr_buy_item_flags(10),"pw_book_d","bo_pw_weapon_small", spr_buy_item_triggers("itm_book_d", resources=["itm_linen_cloth_small","itm_leather_piece"], engineer=2)),
  ("pw_buy_book_e",spr_buy_item_flags(5),"pw_book_e","bo_pw_weapon_small", spr_buy_item_triggers("itm_book_e", resources=["itm_linen_cloth_small","itm_leather_piece"], engineer=2)),
  ("pw_buy_book_f",spr_buy_item_flags(60),"pw_book_f","bo_pw_weapon_small", spr_buy_item_triggers("itm_book_f", resources=["itm_linen_cloth_small","itm_leather_piece"], engineer=2)),

  ("pw_buy_lyre",spr_buy_item_flags(7),"pw_lyre_carry","bo_pw_weapon_small", spr_buy_item_triggers("itm_lyre", pos_offset=(0,0,7), resources=["itm_board"], engineer=2)),
  ("pw_buy_lute",spr_buy_item_flags(8),"pw_lute_carry","bo_pw_weapon_small", spr_buy_item_triggers("itm_lute", pos_offset=(0,0,15), resources=[("itm_board", 2), "itm_stick"], engineer=3)),
  ("pw_buy_dart",spr_buy_item_flags(1),"pw_dart","bo_pw_weapon_small", spr_buy_item_triggers("itm_dart")),
  ("pw_buy_die",spr_buy_item_flags(1),"pw_die","bo_pw_weapon_small", spr_buy_item_triggers("itm_die", pos_offset=(7,7,0), resources=["itm_stick"], engineer=2)),

  ("pw_destroy_heap",spr_use_time(2),"destroy_heap","bo_destroy_heap", spr_destroy_heap_triggers()),

  ("pw_rest_bed_a",spr_use_time(30),"bed_a","bo_bed_a", spr_rest_triggers(40, min_health_pct=35)),
  ("pw_rest_bed_b",spr_use_time(18),"bed_b","bo_bed_b", spr_rest_triggers(20, min_health_pct=50)),
  ("pw_rest_bed_c",spr_use_time(22),"bed_c","bo_bed_c", spr_rest_triggers(30, min_health_pct=40)),
  ("pw_rest_bed_e",spr_use_time(30),"bed_e","bo_bed_e", spr_rest_triggers(50, min_health_pct=30)),
  ("pw_rest_bed_f",spr_use_time(15),"bed_f","bo_bed_f", spr_rest_triggers(15, min_health_pct=55)),
  ("pw_rest_dungeon_bed_a",spr_use_time(15),"dungeon_bed_a","bo_bed_b", spr_rest_triggers(10, min_health_pct=60)),
  ("pw_rest_dungeon_bed_b",spr_use_time(15),"dungeon_bed_b","bo_dungeon_bed_b", spr_rest_triggers(8, min_health_pct=70)),
  ("pw_rest_pillow_a",spr_use_time(18),"pillow_a","bo_pillow", spr_rest_triggers(20, min_health_pct=45)),
  ("pw_rest_pillow_b",spr_use_time(24),"pillow_b","bo_pillow", spr_rest_triggers(30, min_health_pct=40)),
  ("pw_rest_invisible",sokf_invisible|spr_use_time(15),"pw_invisible_door","bo_pw_invisible_door", spr_rest_triggers(10, min_health_pct=60)),
  ("pw_rest_horse_trough",spr_use_time(15),"feeding_trough_a","bo_feeding_trough_a", spr_rest_triggers(30, min_health_pct=30, horse=1, use_string="str_rest_horse")),
  ("pw_rest_horse_hay",spr_use_time(30),"pw_horse_hay","bo_pw_horse_hay", spr_rest_triggers(70, min_health_pct=30, horse=1, use_string="str_rest_horse")),
  ("pw_rest_horse_manger",spr_use_time(22),"wall_manger_a","bo_wall_manger_a", spr_rest_triggers(60, min_health_pct=25, horse=1, use_string="str_rest_horse")),
  ("pw_clean_blood",spr_use_time(3),"cloth_a","bo_cloth_a", spr_clean_blood_triggers()),

  ("code_spawn_marker",0,"0","0", []),
  ("pw_change_troop_peasant",spr_use_time(15),"wooden_staff","bo_pw_weapon_big", spr_change_troop_triggers("trp_peasant", cost=50, after_respawn=True, use_string="str_troop_become")),
  ("pw_change_troop_serf",spr_use_time(30),"trident","bo_pw_weapon_big", spr_change_troop_triggers("trp_serf", cost=150)),
  ("pw_change_troop_militia",spr_use_time(30),"practice_sword","bo_pw_weapon", spr_change_troop_triggers("trp_militia", cost=500)),
  ("pw_change_troop_huntsman",spr_use_time(30),"short_bow","bo_pw_weapon", spr_change_troop_triggers("trp_huntsman", cost=500)),
  ("pw_change_troop_craftsman",spr_use_time(50),"pw_repair_hammer","bo_pw_weapon_small", spr_change_troop_triggers("trp_craftsman", cost=800)),
  ("pw_change_troop_healer",spr_use_time(60),"package","bobaggage", spr_change_troop_triggers("trp_healer", cost=1000)),
  ("pw_change_troop_footman",spr_use_time(60),"heavy_practicesword","bo_pw_weapon", spr_change_troop_triggers("trp_footman", cost=1000)),
  ("pw_change_troop_archer",spr_use_time(60),"hunting_bow","bo_pw_weapon", spr_change_troop_triggers("trp_archer", cost=1100)),
  ("pw_change_troop_crossbowman",spr_use_time(60),"crossbow_a","bo_pw_weapon", spr_change_troop_triggers("trp_crossbowman", cost=1200)),
  ("pw_change_troop_lancer",spr_use_time(70),"arena_lance","bo_pw_weapon_big", spr_change_troop_triggers("trp_lancer", cost=1500)),
  ("pw_change_troop_man_at_arms",spr_use_time(90),"shield_heater_c","bo_pw_shield_kite_small", spr_change_troop_triggers("trp_man_at_arms", cost=5000)),
  ("pw_change_troop_sergeant",spr_use_time(90),"shield_heater_c","bo_pw_shield_kite_small", spr_change_troop_triggers("trp_sergeant", cost=5000)),
  ("pw_change_troop_engineer",spr_use_time(80),"pw_repair_hammer","bo_pw_weapon_small", spr_change_troop_triggers("trp_engineer", cost=2500)),
  ("pw_change_troop_master_smith",spr_use_time(120),"pw_repair_hammer","bo_pw_weapon_small", spr_change_troop_triggers("trp_master_smith", cost=7500)),
  ("pw_change_troop_doctor",spr_use_time(100),"package","bobaggage", spr_change_troop_triggers("trp_doctor", cost=3500)),
  ("pw_change_troop_sailor",spr_use_time(70),"scimeter","bo_pw_weapon", spr_change_troop_triggers("trp_sailor", cost=2000)),
  ("pw_change_troop_traveler",spr_use_time(70),"quarter_staff","bo_pw_weapon_big", spr_change_troop_triggers("trp_traveler", cost=1300, use_string="str_troop_become")),
  ("pw_change_troop_herdsman",spr_use_time(40),"quarter_staff","bo_pw_weapon_big", spr_change_troop_triggers("trp_herdsman", cost=900)),
  ("pw_change_troop_lord",spr_use_time(70),"gothic_chair","bogothic_chair", spr_change_troop_triggers("trp_lord", cost=500, use_string="str_troop_assume_role")),
  ("pw_change_troop_ruffian",spr_use_time(40),"sledgehammer","bo_pw_weapon", spr_change_troop_triggers("trp_ruffian", cost=800, after_respawn=True, use_string="str_troop_become")),
  ("pw_change_troop_brigand",spr_use_time(50),"spiked_club","bo_pw_weapon", spr_change_troop_triggers("trp_brigand", cost=900, after_respawn=True, use_string="str_troop_become")),
  
  # PN TROOPS BEGIN
  ("pw_change_troop_line_infantry",spr_use_time(60),"training_musket","bo_pw_weapon_big", spr_change_troop_triggers("trp_line_infantry", cost=1200)),
  ("pw_change_troop_military_musician",spr_use_time(60),"training_musket","bo_pw_weapon_big", spr_change_troop_triggers("trp_military_musician", cost=1200)),
  ("pw_change_troop_artillerist",spr_use_time(60),"training_musket","bo_pw_weapon_big", spr_change_troop_triggers("trp_artillerist", cost=1200)),
  # PN TROOPS END
  ("pw_change_troop_mercenary",spr_use_time(50),"spiked_mace","bo_pw_weapon", spr_change_troop_triggers("trp_mercenary", cost=700, mercenary=True, after_respawn=True, use_string="str_troop_become_for")),

  ("pw_door_teleport_small_arch_a",spr_use_time(1),"tutorial_door_a","bo_tutorial_door_a", spr_teleport_door_triggers(pos_offset=(-55,50,-98))),
  ("pw_door_teleport_square_a",spr_use_time(1),"tutorial_door_b","bo_tutorial_door_b", spr_teleport_door_triggers(pos_offset=(70,50,0))),
  ("pw_door_teleport_arch_a",spr_use_time(1),"dungeon_door_direction_a","bo_dungeon_door_direction_a", spr_teleport_door_triggers(pos_offset=(100,0,-230))),
  ("pw_door_teleport_roof",spr_use_time(1),"house_roof_door","bo_house_roof_door", spr_teleport_door_triggers(pos_offset=(0,0,100))),
  ("pw_door_teleport_inset_a",spr_use_time(1),"pw_teleport_door_a","bo_pw_teleport_door_a", spr_teleport_door_triggers(pos_offset=(0,50,0))),
  ("pw_door_teleport_inset_b",spr_use_time(1),"pw_teleport_door_b","bo_pw_teleport_door_a", spr_teleport_door_triggers(pos_offset=(0,50,0))),
  ("pw_door_teleport_inset_c",spr_use_time(1),"pw_teleport_door_c","bo_pw_teleport_door_a", spr_teleport_door_triggers(pos_offset=(0,50,0))),
  ("pw_door_teleport_invisible",sokf_invisible|spr_use_time(1),"pw_invisible_door","bo_pw_invisible_door", spr_teleport_door_triggers(pos_offset=(0,50,0))),
  ("pw_door_teleport_invisible_not_pickable",sokf_invisible|spr_use_time(1),"pw_invisible_door","bo_pw_invisible_door", spr_teleport_door_triggers(pos_offset=(0,50,0), pickable=0)),
  ("pw_door_rotate_a",spr_rotate_door_flags(1),"castle_f_sally_door_a","bo_castle_f_sally_door_a", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_b",spr_rotate_door_flags(1),"castle_e_sally_door_a","bo_castle_e_sally_door_a_fixed", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_c",spr_rotate_door_flags(1),"castle_f_door_a","bo_castle_f_door_a_fixed", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_d",spr_rotate_door_flags(1),"pw_door_d","bo_pw_door_d", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_viking_left",spr_rotate_door_flags(1),"viking_keep_destroy_sally_door_left","bo_viking_keep_destroy_sally_door_left_fixed", spr_rotate_door_triggers(hit_points=5000, left=1)),
  ("pw_door_rotate_viking_right",spr_rotate_door_flags(1),"viking_keep_destroy_sally_door_right","bo_viking_keep_destroy_sally_door_right_fixed", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_gatehouse_left",spr_rotate_door_flags(1),"pw_gatehouse_door_left","bo_pw_gatehouse_door_left", spr_rotate_door_triggers(hit_points=7000, left=1)),
  ("pw_door_rotate_gatehouse_right",spr_rotate_door_flags(1),"pw_gatehouse_door_right","bo_pw_gatehouse_door_right", spr_rotate_door_triggers(hit_points=7000)),
  ("pw_door_rotate_dungeon_cell_a",spr_rotate_door_no_hit_flags(2),"dungeon_door_cell_a","bo_dungeon_door_cell_a_fixed", spr_rotate_door_no_hit_triggers()),
  ("pw_door_rotate_dungeon_cell_b",spr_rotate_door_no_hit_flags(2),"dungeon_door_cell_b_fixed","bo_dungeon_door_cell_b_fixed", spr_rotate_door_no_hit_triggers()),
  ("pw_door_rotate_dungeon_cell_c",spr_rotate_door_no_hit_flags(2),"dungeon_door_cell_c","bo_dungeon_door_cell_c", spr_rotate_door_no_hit_triggers()),
  ("pw_door_rotate_dungeon_a",spr_rotate_door_flags(1),"pw_dungeon_door_a","bo_pw_dungeon_door_a", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_dungeon_b",spr_rotate_door_flags(1),"pw_dungeon_door_b","bo_pw_dungeon_door_a", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_dungeon_c",spr_rotate_door_flags(1),"pw_dungeon_door_c","bo_pw_dungeon_door_a", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_e_left",spr_rotate_door_flags(1),"pw_door_e_left","bo_pw_door_left", spr_rotate_door_triggers(hit_points=5000, left=1)),
  ("pw_door_rotate_e_right",spr_rotate_door_flags(1),"pw_door_e_right","bo_pw_door_right", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_f_left",spr_rotate_door_flags(1),"pw_door_f_left","bo_pw_door_left", spr_rotate_door_triggers(hit_points=5000, left=1)),
  ("pw_door_rotate_f_right",spr_rotate_door_flags(1),"pw_door_f_right","bo_pw_door_right", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_h_left",spr_rotate_door_flags(1),"pw_door_g_left","bo_pw_door_left", spr_rotate_door_triggers(hit_points=5000, left=1)),
  ("pw_door_rotate_h_right",spr_rotate_door_flags(1),"pw_door_g_right","bo_pw_door_right", spr_rotate_door_triggers(hit_points=5000)),
  ("pw_door_rotate_towngate_left",spr_rotate_door_flags(2),"towngate_rectangle_door_left","bo_towngate_rectangle_door_left_fixed", spr_rotate_door_triggers(hit_points=10000, left=1)),
  ("pw_door_rotate_towngate_right",spr_rotate_door_flags(2),"towngate_rectangle_door_right","bo_towngate_rectangle_door_right_fixed", spr_rotate_door_triggers(hit_points=10000)),
  ("pw_door_rotate_earth_left",spr_rotate_door_flags(2),"earth_sally_gate_left","bo_earth_sally_gate_left", spr_rotate_door_triggers(hit_points=10000, left=1)),
  ("pw_door_rotate_earth_right",spr_rotate_door_flags(2),"earth_sally_gate_right","bo_earth_sally_gate_right", spr_rotate_door_triggers(hit_points=10000)),
  ("pw_door_rotate_stable",spr_rotate_door_flags(1),"pw_full_stable_door_a","bo_pw_full_stable_door_a", spr_rotate_door_triggers(hit_points=1000, left=1)),
  ("pw_door_rotate_village_a",spr_rotate_door_flags(1),"pw_village_door_a","bo_pw_village_door_a", spr_rotate_door_triggers(hit_points=2000)),
  ("pw_door_rotate_village_b",spr_rotate_door_flags(1),"pw_village_door_b","bo_pw_village_door_a", spr_rotate_door_triggers(hit_points=2000)),

  ("pw_wooden_bridge_a",spr_structure_flags(),"bridge_wooden","bo_bridge_wooden_fixed", spr_bridge_triggers("pw_wooden_bridge_a_footing", hit_points=15000)),
  ("pw_wooden_bridge_a_footing",spr_build_flags(),"pw_build_bridge","bo_pw_build", spr_bridge_footing_triggers()),
  ("pw_snowy_bridge_a",spr_structure_flags(),"bridge_wooden_snowy","bo_bridge_wooden_fixed", spr_bridge_triggers("pw_snowy_bridge_a_footing", hit_points=15000)),
  ("pw_snowy_bridge_a_footing",spr_build_flags(),"pw_build_bridge","bo_pw_build", spr_bridge_footing_triggers()),
  ("pw_rope_bridge",spr_structure_flags(),"rope_bridge_15m","bo_rope_bridge_15m", spr_bridge_triggers("pw_rope_bridge_footing", hit_points=2000)),
  ("pw_rope_bridge_footing",spr_build_flags(),"castle_f_wall_way_a","bo_castle_f_wall_way_a", spr_bridge_footing_triggers()),

  ("pw_wooden_palisade",spr_structure_flags(),"pw_wooden_palisade_a","bo_arena_palisade_a", spr_wall_triggers("pw_wooden_palisade_build", hit_points=15000, height=1600)),
  ("pw_wooden_palisade_b",spr_structure_flags(),"pw_wooden_palisade_b","bo_pw_wooden_palisade_b", spr_wall_triggers("pw_wooden_palisade_build", hit_points=15000, height=1600)),
  ("pw_wooden_palisade_tower",spr_structure_flags(),"arena_tower_c","bo_arena_tower_c_fixed", spr_wall_triggers("pw_wooden_palisade_build", hit_points=15000, height=2500)),
  ("pw_wooden_palisade_build",spr_build_flags(),"pw_build_wall","bo_pw_build", spr_build_wall_triggers()),
  ("pw_siege_stairs_a",spr_structure_flags(),"pw_siege_stairs_a","bo_pw_siege_stairs_a", spr_wall_triggers("pw_siege_stairs_build", hit_points=3000, height=340)),
  ("pw_siege_stairs_build",spr_build_flags(),"pw_build_wall","bo_pw_build", spr_build_wall_triggers()),
  ("pw_siege_wall_a",spr_structure_flags(),"siege_wall_a","bo_siege_wall_a_fixed", spr_wall_triggers("pw_siege_wall_a_build", hit_points=5000, height=320)),
  ("pw_siege_wall_a_build",spr_build_flags(),"pw_build_wall","bo_pw_build", spr_build_wall_triggers()),
  ("pw_siege_wall_b",spr_structure_flags(),"pw_siege_wall_b","bo_pw_siege_wall_b", spr_wall_triggers("pw_siege_wall_b_build", hit_points=6000, height=560)),
  ("pw_siege_wall_b2",spr_structure_flags(),"pw_siege_wall_b2","bo_pw_siege_wall_b2", spr_wall_triggers("pw_siege_wall_b_build", hit_points=6000, height=560)),
  ("pw_siege_wall_b_build",spr_build_flags(),"pw_build_wall","bo_pw_build", spr_build_wall_triggers()),
  ("pw_siege_shield_a",spr_structure_flags(),"siege_large_shield_a","bo_siege_large_shield_a_fixed", spr_wall_triggers("pw_siege_shield_a_build", hit_points=2000, height=280)),
  ("pw_siege_shield_a_build",spr_build_flags(),"pw_build_wall","bo_pw_build", spr_build_wall_triggers()),
  ("pw_siege_ramp_14m",spr_structure_flags(),"pw_siege_ramp_14m","bo_pw_siege_ramp_14m", spr_wall_triggers("pw_siege_ramp_build", hit_points=1500, height=1400, no_move_physics=True)),
  ("pw_siege_ramp_build",spr_build_flags(),"pw_build_bridge","bo_pw_build", spr_build_wall_triggers()),
  ("pw_ladder_6m",spr_ladder_flags(),"siege_ladder_move_6m","bo_siege_ladder_move_6m_fixed", spr_wall_triggers("pw_ladder_build", hit_points=600, height=600, no_move_physics=True)),
  ("pw_ladder_8m",spr_ladder_flags(),"siege_ladder_move_8m","bo_siege_ladder_move_8m_fixed", spr_wall_triggers("pw_ladder_build", hit_points=660, height=800, no_move_physics=True)),
  ("pw_ladder_10m",spr_ladder_flags(),"siege_ladder_move_10m","bo_siege_ladder_move_10m_fixed", spr_wall_triggers("pw_ladder_build", hit_points=720, height=1000, no_move_physics=True)),
  ("pw_ladder_12m",spr_ladder_flags(),"siege_ladder_move_12m","bo_siege_ladder_move_12m_fixed", spr_wall_triggers("pw_ladder_build", hit_points=840, height=1200, no_move_physics=True)),
  ("pw_ladder_14m",spr_ladder_flags(),"siege_ladder_move_14m","bo_siege_ladder_move_14m_fixed", spr_wall_triggers("pw_ladder_build", hit_points=900, height=1400, no_move_physics=True)),
  ("pw_ladder_build",spr_build_flags(),"pw_build_ladder","bo_pw_build_ladder", spr_build_wall_triggers()),
  ("pw_construction_box",sokf_static_movement|sokf_destructible,"pw_construction_box","bo_pw_construction_box", spr_construction_box_triggers()),

  ("pw_winch_frame",0,"winch_stabilizer_a","bo_winch_stabilizer_a", []),
  ("pw_portcullis_winch",spr_use_time(1),"winch","bo_winch_fixed", spr_portcullis_winch_triggers("pw_portcullis")),
  ("pw_portcullis",sokf_static_movement,"portculis_new","bo_portculis_new", []),
  ("pw_portcullis_winch_a",spr_use_time(1),"winch","bo_winch_fixed", spr_portcullis_winch_triggers("pw_portcullis_a")),
  ("pw_portcullis_a",sokf_static_movement,"portcullis_a","bo_portcullis_a", []),
  ("pw_drawbridge_winch_a",spr_use_time(2),"winch_b","bo_winch_fixed", spr_drawbridge_winch_triggers("pw_drawbridge_a")),
  ("pw_drawbridge_a",sokf_moveable,"drawbridge","bo_drawbridge", []),
  ("pw_drawbridge_winch_b",spr_use_time(2),"winch_b","bo_winch_fixed", spr_drawbridge_winch_triggers("pw_drawbridge_b")),
  ("pw_drawbridge_b",sokf_moveable,"castle_drawbridges_open","bo_castle_drawbridges_open", []),
  ("pw_trapdoor_winch_a",spr_use_time(1),"winch","bo_winch_fixed", spr_drawbridge_winch_triggers("pw_trapdoor_a", rotation_steps=2, step_size=45, animation_time=50)),
  ("pw_trapdoor_a",sokf_static_movement,"belfry_b_platform_a","bo_belfry_b_platform_a", []),
  ("pw_sliding_door_winch_a",spr_use_time(1),"winch","bo_winch_fixed", spr_sliding_door_winch_triggers("pw_sliding_door_a", move_steps=1, step_size=150)),
  ("pw_sliding_door_a",sokf_moveable,"castle_e_sally_door_a","bo_castle_e_sally_door_a", []),
  ("pw_lift_platform_winch",spr_use_time(1),"winch_b","bo_winch_fixed", spr_lift_platform_winch_triggers()),
  ("pw_lift_platform",sokf_moveable,"pw_lift_platform","bo_pw_lift_platform", spr_lift_platform_triggers("pw_lift_platform_winch")),

  ("pw_cart_a",sokf_static_movement|spr_use_time(1),"pw_cart_a","bo_pw_cart_a", spr_cart_triggers(horse="itm_cart_horse", detach_offset=60, detach_rotation=-20, inventory_count=48, max_item_length=250, access_distance=-180)),
  ("pw_cart_b",sokf_static_movement|spr_use_time(1),"pw_cart_b","bo_pw_cart_b", spr_cart_triggers(horse="itm_cart_horse", detach_offset=110, detach_rotation=-6, inventory_count=42, max_item_length=250, access_distance=-170)),
  ("pw_wheelbarrow",sokf_static_movement|spr_use_time(1),"pw_hand_cart_a","bo_pw_hand_cart_a", spr_cart_triggers(detach_offset=47, detach_rotation=15, inventory_count=12, max_item_length=120, access_distance=110)),
  ("pw_hand_cart",sokf_static_movement|spr_use_time(1),"pw_hand_cart_b","bo_pw_hand_cart_b", spr_cart_triggers(detach_offset=90, inventory_count=24, max_item_length=150, access_distance=-170)),
  ("pw_back_basket",sokf_static_movement|spr_use_time(2),"pw_back_basket","bo_pw_back_basket", spr_cart_triggers(detach_offset=-12, inventory_count=5, max_item_length=95, access_distance=-60)),
  ("pw_back_box",sokf_static_movement|spr_use_time(3),"pw_back_box","bo_pw_back_box", spr_cart_triggers(detach_offset=-13, inventory_count=10, max_item_length=80, access_distance=-80)),
  ("pw_horse_pack",sokf_static_movement|spr_use_time(2),"pw_horse_pack","bo_pw_horse_pack", spr_cart_triggers(horse=1, detach_offset=49, inventory_count=20, max_item_length=100, access_distance=90)),

  ("pw_ship_a",sokf_moveable|sokf_destructible|sokf_show_hit_point_bar,"pw_ship_a","bo_pw_ship_a", spr_ship_triggers(hit_points=5000, length=800, width=150, height=-20, speed=6, sail="pw_ship_a_sail", sail_off="pw_ship_a_sail_off", collision="pw_ship_a_cd")),
  ("pw_ship_a_sail",sokf_moveable,"pw_ship_a_sail","bo_pw_ship_a_sail", []),
  ("pw_ship_a_sail_off",sokf_moveable,"pw_ship_a_sail_off","bo_pw_ship_a_sail_off", []),
  ("pw_ship_a_cd",sokf_invisible|sokf_dont_move_agent_over,"0","bo_pw_ship_a_cd", []),
  ("pw_ship_b",sokf_moveable|sokf_destructible|sokf_show_hit_point_bar,"pw_ship_b","bo_pw_ship_b", spr_ship_triggers(hit_points=8000, length=1400, width=230, height=100, speed=4, sail="pw_ship_b_sail", collision="pw_ship_b_cd")),
  ("pw_ship_b_sail",sokf_moveable,"pw_ship_b_sail","bo_pw_ship_b_sail", []),
  ("pw_ship_b_cd",sokf_invisible|sokf_dont_move_agent_over,"0","bo_pw_ship_b_cd", []),
  ("pw_ship_c",sokf_moveable|sokf_destructible|sokf_show_hit_point_bar,"pw_ship_c","bo_pw_ship_c", spr_ship_triggers(hit_points=10000, length=1400, width=300, height=300, speed=4, sail="pw_ship_c_sail", sail_off="pw_ship_c_sail_off", ramp="pw_ship_c_ramp", hold="pw_ship_c_hold", collision="pw_ship_c_cd")),
  ("pw_ship_c_sail",sokf_moveable,"pw_ship_c_sail","bo_pw_ship_c_sail", []),
  ("pw_ship_c_sail_off",sokf_moveable,"pw_ship_c_sail_off","bo_pw_ship_c_sail_off", []),
  ("pw_ship_c_ramp",sokf_moveable|spr_use_time(1),"pw_ship_c_ramp","bo_pw_ship_c_ramp", spr_ship_ramp_triggers()),
  ("pw_ship_c_hold",sokf_moveable|sokf_invisible|spr_use_time(2),"0","bo_pw_ship_c_hold", spr_item_storage_triggers(inventory_count=90, max_item_length=500)),
  ("pw_ship_c_cd",sokf_invisible|sokf_dont_move_agent_over,"0","bo_pw_ship_c_cd", []),
  ("pw_ship_d",sokf_moveable|sokf_destructible|sokf_show_hit_point_bar,"pw_ship_d","bo_pw_ship_d", spr_ship_triggers(hit_points=7000, length=900, width=250, height=120, speed=5, sail="pw_ship_d_sail", hold="pw_ship_d_hold", collision="pw_ship_d_cd")),
  ("pw_ship_d_sail",sokf_moveable,"pw_ship_d_sail","bo_pw_ship_d_sail", []),
  ("pw_ship_d_hold",sokf_moveable|sokf_invisible|spr_use_time(2),"0","bo_pw_ship_d_hold", spr_item_storage_triggers(inventory_count=64, max_item_length=500)),
  ("pw_ship_d_cd",sokf_invisible|sokf_dont_move_agent_over,"0","bo_pw_ship_d_cd", []),
  ("pw_ferry_boat",sokf_moveable,"pw_ferry_boat","bo_pw_ferry_boat", spr_ferry_triggers(platform="pw_ferry_platform", winch="code_ferry_winch", length=470, winch_height=70)),
  ("code_ferry_winch",sokf_moveable|spr_use_time(2),"pw_ferry_winch","bo_pw_ferry_winch", spr_ferry_winch_triggers()),
  ("pw_ferry_platform",spr_use_time(2),"pw_ferry_platform","bo_pw_ferry_platform", spr_ferry_winch_triggers(is_platform=1)),
  ("pw_ferry_chain_10m",0,"pw_ferry_chain_10m","0", []),
  ("pw_ferry_chain_20m",0,"pw_ferry_chain_20m","0", []),
  ("pw_ferry_chain_30m",0,"pw_ferry_chain_30m","0", []),

  ("pw_castle_sign",0,"tree_house_guard_a","bo_tree_house_guard_a", [(ti_on_scene_prop_use, [])]),
  ("pw_castle_capture_point",spr_use_time(20),"pw_castle_flag_post","bo_pw_castle_flag_post", spr_capture_castle_triggers()),
  ("pw_castle_wall_banner",0,"pw_banner_wall_rail","bo_pw_banner_wall_rail", []),
  ("pw_castle_money_chest",spr_chest_flags(2),"pw_chest_b","bo_pw_chest_b", spr_castle_money_chest_triggers(hit_points=6000)),
  ("pw_item_chest_a",spr_chest_flags(1),"pw_chest_c","bo_pw_chest_c", spr_item_chest_triggers(hit_points=7000, inventory_count=48, max_item_length=180)),
  ("pw_item_chest_b",spr_chest_flags(1),"pw_chest_b","bo_pw_chest_b", spr_item_chest_triggers(hit_points=5000, inventory_count=32, max_item_length=100)),
  ("pw_item_chest_invisible",sokf_invisible|spr_chest_flags(1),"pw_invisible_chest","bo_pw_invisible_chest", spr_item_chest_triggers(hit_points=2000, inventory_count=12, max_item_length=120)),

  ("pw_signpost_castle",0,"pw_signpost_castle","bo_pw_signpost", []),
  ("pw_signpost_docks",0,"pw_signpost_docks","bo_pw_signpost", []),
  ("pw_signpost_market",0,"pw_signpost_market","bo_pw_signpost", []),
  ("pw_signpost_tavern",0,"pw_signpost_tavern","bo_pw_signpost", []),
  ("pw_signpost_town",0,"pw_signpost_town","bo_pw_signpost", []),

  ("pw_dart_board",0,"pw_dart_board","bo_pw_dart_board", []),

  ("pw_scene_day_time",sokf_invisible,"barrier_box","0", []),
  ("pw_scene_cloud_haze",sokf_invisible,"barrier_box","0", []),
  ("pw_scene_ambient_sound",sokf_invisible,"barrier_cone","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (prop_instance_get_variation_id_2, ":probability", ":instance_id"),
      (eq, ":probability", 127),
      (prop_instance_get_variation_id, ":sound_id", ":instance_id"),
      (val_add, ":sound_id", ambient_sounds_begin),
      (is_between, ":sound_id", ambient_sounds_begin, ambient_sounds_end),
      (prop_instance_play_sound, ":instance_id", ":sound_id", sf_looping),
      ]),
    ]),
  ("pw_scene_light",sokf_invisible,"light_sphere","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (set_fixed_point_multiplier, 100),
      (prop_instance_get_scale, pos1, ":instance_id"),
      (position_get_scale_x, ":red", pos1),
      (position_get_scale_y, ":green", pos1),
      (position_get_scale_z, ":blue", pos1),
      (set_current_color,":red", ":green", ":blue"),
      (set_position_delta, 0, 0, 0),
      (prop_instance_get_variation_id, ":flicker_magnitude", ":instance_id"),
      (prop_instance_get_variation_id_2, ":flicker_interval", ":instance_id"),
      (add_point_light_to_entity, ":flicker_magnitude", ":flicker_interval"),
      ]),
    ]),
  ("pw_scene_precipitation",sokf_invisible,"pw_precipitation_area","0", []),
  ("pw_scene_fog",sokf_invisible,"barrier_box","0", []),
  ("pw_scene_snow_level",sokf_invisible,"barrier_box","0", []),
  ("pw_scene_wind_direction",sokf_invisible,"pw_wind_arrow","0", []),

  ("pw_fire_wood_heap",sokf_destructible|sokf_missiles_not_attached,"pw_wood_heap_c","bo_pw_wood_heap_c", spr_fire_place_triggers()),
  ("wood_heap_fire",0,"0","0",
   [(ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (particle_system_add_new, "psys_wood_heap_fire"),
      (particle_system_add_new, "psys_wood_heap_fire_sparks"),
      (set_position_delta,0,0,100),
      (particle_system_add_new, "psys_wood_heap_fire_smoke"),
      (prop_instance_play_sound, ":instance_id", "snd_fire_loop"),
      ]),
    ]),

  ("pw_fish_school",sokf_invisible,"barrier_capsule","0", [
    (ti_on_scene_prop_init,
     [(store_trigger_param_1, ":instance_id"),
      (scene_prop_set_slot, ":instance_id", slot_scene_prop_collision_kind, -1),
      ]),
    ]),
  ("pw_herd_animal_spawn",sokf_invisible,"pw_ground_arrow","0", []),

  ("pw_local_wood_price_area",sokf_invisible,"pw_local_wood_price_area","0", []),
  ("pw_local_iron_price_area",sokf_invisible,"pw_local_iron_price_area","0", []),
  ("pw_local_cloth_price_area",sokf_invisible,"pw_local_cloth_price_area","0", []),
  ("pw_local_leather_price_area",sokf_invisible,"pw_local_leather_price_area","0", []),
  ("pw_local_precious_price_area",sokf_invisible,"pw_local_precious_price_area","0", []),

  # PN START ************************************************************************************************************************

  ######################################################
  #### BUYABLE STUFF ************************************
  ######################################################

  #("pw_buy_french_charleville_musket", spr_buy_item_flags(4), "french_charleville", "bo_pw_weapon", spr_buy_item_triggers("itm_french_charleville", pos_offset=(-5,0,0), resources=["itm_iron_piece", "itm_stick"], engineer=5)),
  
  ######################################################
  #### STATIC STUFF ************************************
  ######################################################

  # SHIPS
  ("pn_ship_longboat",sokf_moveable|sokf_destructible|sokf_show_hit_point_bar,"pn_ship_longboat", "bo_pn_ship_longboat",spr_ship_triggers(hit_points=1200, length=290, width=90, height=-20, speed=1, sail="pn_ship_longboat_sail", collision="pn_ship_longboat_cd")),
  ("pn_ship_longboat_sail",sokf_moveable,"pn_ship_longboat_sail","bo_birdmodel", []),
  ("pn_ship_longboat_cd",sokf_invisible|sokf_dont_move_agent_over,"0","bo_pn_longboat", []),

  ("pn_ship_schooner",sokf_moveable|sokf_destructible|sokf_show_hit_point_bar,"pn_ship_schooner", "bo_pn_ship_schooner",spr_ship_triggers(hit_points=10000, length=1400, width=265, height=130, speed=5, sail="pn_ship_schooner_sail", collision="pn_ship_schooner_cd")),
  ("pn_ship_schooner_sail",sokf_moveable,"pn_ship_schooner_sail","bo_birdmodel", []),
  ("pn_ship_schooner_cd",sokf_invisible|sokf_dont_move_agent_over,"0","bo_pn_ship_schooner", []),

  ("pn_ship_frigate",sokf_moveable|sokf_destructible|sokf_show_hit_point_bar,"pn_ship_frigate", "bo_pn_ship_frigate",spr_ship_triggers(hit_points=14000, length=2100, width=520, height=200, speed=3, sail="pn_ship_frigate_sail", collision="pn_ship_frigate_cd")),
  ("pn_ship_frigate_sail",sokf_moveable,"pn_ship_frigate_sail","bo_birdmodel", []),
  ("pn_ship_frigate_sail_off",sokf_moveable,"pn_ship_frigate_sail_off","bo_birdmodel", []),
  ("pn_ship_frigate_cd",sokf_invisible|sokf_dont_move_agent_over,"0","bo_pn_frigate", []),

  ("mm_weather_time", 0, "0", "0", []), # var1 = time of day 0-23; Default = 15
  ("mm_weather_rain", 0, "0", "0", []), # var1 = rain type 1 = rain 2 = snow, var2 = rain ammount 0-25  
  ("mm_weather_clouds", 0, "0", "0", []), # var1 = cloud ammount 0-100; Default = 30
  ("mm_weather_fog", 0, "0", "0", []), # var1 = fog distance; meters x 10 where fog visibility ends 
  ("mm_weather_thunder", 0, "0", "0", []), # var1 = thunder type: 0 = none 1 = thunder only 2 = thunder & lighting, # var2 = thunder frequancy 0-100 ; the higher value the more thunder
  ("mm_weather_wind", 0, "0", "0", []), # var1 = flora_wind_strength in % 0-100; Default = 14 # var2 = water_wind_strength in % 0-100; Default = 14

  ("mm_spawn_with_cannon", 0, "0", "0", []), #  If this prop is in the map, the arty sarges spawn with a cannon attached.

  ("mm_tree_aspen1" ,sokf_handle_as_flora,"mm_aspen1" ,"bo_mm_aspen1" , []),
  ("mm_tree_aspen2" ,sokf_handle_as_flora,"mm_aspen2" ,"bo_mm_aspen2" , []),
  ("mm_tree_aspen3" ,sokf_handle_as_flora,"mm_aspen3" ,"bo_mm_aspen3" , []),
  ("mm_tree_aspen4" ,sokf_handle_as_flora,"mm_aspen4" ,"bo_mm_aspen4" , []),
  ("mm_tree_aspen5" ,sokf_handle_as_flora,"mm_aspen5" ,"bo_mm_aspen5" , []),
  ("mm_tree_aspen6" ,sokf_handle_as_flora,"mm_aspen6" ,"bo_mm_aspen6" , []),
  ("mm_tree_aspen7" ,sokf_handle_as_flora,"mm_aspen7" ,"bo_mm_aspen7" , []),
  ("mm_tree_aspen8" ,sokf_handle_as_flora,"mm_aspen8" ,"bo_mm_aspen8" , []),
  ("mm_tree_aspen9" ,sokf_handle_as_flora,"mm_aspen9" ,"bo_mm_aspen9" , []),
  ("mm_tree_aspen10" ,sokf_handle_as_flora,"mm_aspen10" ,"bo_mm_aspen10" , []),
  ("mm_tree_aspen11" ,sokf_handle_as_flora,"mm_aspen11" ,"bo_mm_aspen11" , []),
  ("mm_tree_aspen12" ,sokf_handle_as_flora,"mm_aspen12" ,"bo_mm_aspen12" , []),
  ("mm_tree_aspen13" ,sokf_handle_as_flora,"mm_aspen13" ,"bo_mm_aspen13" , []),
  ("mm_tree_aspen14" ,sokf_handle_as_flora,"mm_aspen14" ,"bo_mm_aspen14" , []),
  ("mm_tree_aspen15" ,sokf_handle_as_flora,"mm_aspen15" ,"bo_mm_aspen15" , []),
  
  ("mm_tree_pine1" ,sokf_handle_as_flora,"mm_pine1" ,"bo_mm_pine1" , []),
  ("mm_tree_pine2" ,sokf_handle_as_flora,"mm_pine2" ,"bo_mm_pine2" , []),
  ("mm_tree_pine3" ,sokf_handle_as_flora,"mm_pine3" ,"bo_mm_pine3" , []),
  ("mm_tree_pine4" ,sokf_handle_as_flora,"mm_pine4" ,"bo_mm_pine4" , []),
  ("mm_tree_pine5" ,sokf_handle_as_flora,"mm_pine5" ,"bo_mm_pine5" , []),
  ("mm_tree_pine6" ,sokf_handle_as_flora,"mm_pine6" ,"bo_mm_pine6" , []),
  ("mm_tree_pine7" ,sokf_handle_as_flora,"mm_pine7" ,"bo_mm_pine7" , []),
  
  ("mm_tree_pine_snowy1" ,sokf_handle_as_flora,"mm_pine1s" ,"bo_mm_pine1s" , []),
  ("mm_tree_pine_snowy2" ,sokf_handle_as_flora,"mm_pine2s" ,"bo_mm_pine2s" , []),
  ("mm_tree_pine_snowy3" ,sokf_handle_as_flora,"mm_pine3s" ,"bo_mm_pine3s" , []),
  ("mm_tree_pine_snowy4" ,sokf_handle_as_flora,"mm_pine4s" ,"bo_mm_pine4s" , []),
  ("mm_tree_pine_snowy5" ,sokf_handle_as_flora,"mm_pine5s" ,"bo_mm_pine5s" , []),
  ("mm_tree_pine_snowy6" ,sokf_handle_as_flora,"mm_pine6s" ,"bo_mm_pine6s" , []),
  ("mm_tree_pine_snowy7" ,sokf_handle_as_flora,"mm_pine7s" ,"bo_mm_pine7s" , []),
  
  ("mm_tree_northern1" ,sokf_handle_as_flora,"mm_northern_tree1" ,"bo_mm_northern_tree1" , []),
  ("mm_tree_northern2" ,sokf_handle_as_flora,"mm_northern_tree2" ,"bo_mm_northern_tree2" , []),
  ("mm_tree_northern3" ,sokf_handle_as_flora,"mm_northern_tree3" ,"bo_mm_northern_tree3" , []),
  ("mm_tree_northern4" ,sokf_handle_as_flora,"mm_northern_tree4" ,"bo_mm_northern_tree4" , []),
  ("mm_tree_northern5" ,sokf_handle_as_flora,"mm_pine_3" ,"bo_mm_pine_3" , []),
  ("mm_tree_northern6" ,sokf_handle_as_flora,"mm_pine_4" ,"bo_mm_pine_4" , []),
  ("mm_tree_northern7" ,sokf_handle_as_flora,"mm_pine_5" ,"bo_mm_pine_5" , []),
  
  ("mm_tree_autumn1" ,sokf_handle_as_flora,"mm_autumn_tree" ,"bo_mm_autumn_tree" , []),
  ("mm_tree_autumn2" ,sokf_handle_as_flora,"mm_autumn_tree1" ,"bo_mm_autumn_tree1" , []),
  ("mm_tree_autumn3" ,sokf_handle_as_flora,"mm_autumn_tree2" ,"bo_mm_autumn_tree2" , []),
  ("mm_tree_autumn4" ,sokf_handle_as_flora,"mm_autumn_tree3" ,"bo_mm_autumn_tree3" , []),
  ("mm_tree_autumn5" ,sokf_handle_as_flora,"mm_autumn_tree4" ,"bo_mm_autumn_tree4" , []),
  
  ("mm_tree_winter1" ,sokf_handle_as_flora,"mm_winter_tree" ,"bo_mm_winter_tree" , []),
  ("mm_tree_winter2" ,sokf_handle_as_flora,"mm_winter_tree1" ,"bo_mm_winter_tree1" , []),
  ("mm_tree_winter3" ,sokf_handle_as_flora,"mm_winter_tree2" ,"bo_mm_winter_tree2" , []),
  ("mm_tree_winter4" ,sokf_handle_as_flora,"mm_winter_tree3" ,"bo_mm_winter_tree3" , []),
  ("mm_tree_winter5" ,sokf_handle_as_flora,"mm_winter_tree4" ,"bo_mm_winter_tree4" , []),
  ("mm_tree_winter6" ,sokf_handle_as_flora,"mm_winter_tree5" ,"bo_mm_winter_tree5" , []),
  ("mm_tree_winter7" ,sokf_handle_as_flora,"mm_winter_tree6" ,"bo_mm_winter_tree6" , []),
  ("mm_tree_winter8" ,sokf_handle_as_flora,"mm_winter_tree7" ,"bo_mm_winter_tree7" , []),
  ("mm_tree_winter9" ,sokf_handle_as_flora,"mm_winter_tree8" ,"bo_mm_winter_tree8" , []),
  ("mm_tree_winter10" ,sokf_handle_as_flora,"mm_winter_tree9" ,"bo_mm_winter_tree9" , []),
  ("mm_tree_winter11" ,sokf_handle_as_flora,"mm_winter_tree10" ,"bo_mm_winter_tree10" , []),
  ("mm_tree_winter12" ,sokf_handle_as_flora,"mm_winter_tree11" ,"bo_mm_winter_tree11" , []),
  ("mm_tree_winter13" ,sokf_handle_as_flora,"mm_winter_tree12" ,"bo_mm_winter_tree12" , []),
  ("mm_tree_winter14" ,sokf_handle_as_flora,"mm_winter_tree13" ,"bo_mm_winter_tree13" , []),
  ("mm_tree_winter15" ,sokf_handle_as_flora,"mm_winter_tree14" ,"bo_mm_winter_tree14" , []),
  ("mm_tree_winter16" ,sokf_handle_as_flora,"mm_winter_tree15" ,"bo_mm_winter_tree15" , []),
  
  ("mm_tree_big1" ,sokf_handle_as_flora,"big_tree_mm" ,"bo_big_tree_mm" , []),
  ("mm_tree_big2" ,sokf_handle_as_flora,"big_tree_mm1" ,"bo_big_tree_mm1" , []),
  ("mm_tree_big3" ,sokf_handle_as_flora,"big_tree_mm2" ,"bo_big_tree_mm2" , []),
  ("mm_tree_big4" ,sokf_handle_as_flora,"big_tree_mm3" ,"bo_big_tree_mm3" , []),
  
  ("mm_tree_vegetation1" ,sokf_handle_as_flora,"mm_vegetation_tree1" ,"bo_mm_vegetation_tree1" , []),
  ("mm_tree_vegetation2" ,sokf_handle_as_flora,"mm_vegetation_tree2" ,"bo_mm_vegetation_tree2" , []),
  ("mm_tree_vegetation3" ,sokf_handle_as_flora,"mm_vegetation_tree3" ,"bo_mm_vegetation_tree3" , []),
  ("mm_tree_vegetation4" ,sokf_handle_as_flora,"mm_vegetation_tree4" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation5" ,sokf_handle_as_flora,"mm_vegetation_tree5" ,"bo_mm_vegetation_tree5" , []),
  ("mm_tree_vegetation6" ,sokf_handle_as_flora,"mm_vegetation_tree6" ,"bo_mm_vegetation_tree6" , []),
  ("mm_tree_vegetation7" ,sokf_handle_as_flora,"mm_vegetation_tree7" ,"bo_mm_vegetation_tree7" , []),
  ("mm_tree_vegetation8" ,sokf_handle_as_flora,"mm_vegetation_tree8" ,"bo_mm_vegetation_tree8" , []),
  ("mm_tree_vegetation9" ,sokf_handle_as_flora,"mm_vegetation_tree9" ,"bo_mm_vegetation_tree9" , []),
  ("mm_tree_vegetation10" ,sokf_handle_as_flora,"mm_vegetation_tree10" ,"bo_mm_vegetation_tree10" , []),
  ("mm_tree_vegetation11" ,sokf_handle_as_flora,"mm_vegetation_tree11" ,"bo_mm_vegetation_tree11" , []),
  ("mm_tree_vegetation12" ,sokf_handle_as_flora,"mm_vegetation_tree12" ,"bo_mm_vegetation_tree12" , []),
  ("mm_tree_vegetation14" ,sokf_handle_as_flora,"mm_vegetation_tree14" ,"bo_mm_vegetation_tree14" , []),
  ("mm_tree_vegetation15" ,sokf_handle_as_flora,"mm_vegetation_tree15" ,"bo_mm_vegetation_tree15" , []),
  
  ("mm_tree_vegetation2_1" ,sokf_handle_as_flora,"mm_vegetation_tree21" ,"bo_mm_vegetation_tree1" , []),
  ("mm_tree_vegetation2_2" ,sokf_handle_as_flora,"mm_vegetation_tree22" ,"bo_mm_vegetation_tree2" , []),
  ("mm_tree_vegetation2_3" ,sokf_handle_as_flora,"mm_vegetation_tree23" ,"bo_mm_vegetation_tree3" , []),
  ("mm_tree_vegetation2_4" ,sokf_handle_as_flora,"mm_vegetation_tree24" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation2_5" ,sokf_handle_as_flora,"mm_vegetation_tree25" ,"bo_mm_vegetation_tree5" , []),
  ("mm_tree_vegetation2_6" ,sokf_handle_as_flora,"mm_vegetation_tree26" ,"bo_mm_vegetation_tree6" , []),
  ("mm_tree_vegetation2_7" ,sokf_handle_as_flora,"mm_vegetation_tree27" ,"bo_mm_vegetation_tree7" , []),
  ("mm_tree_vegetation2_8" ,sokf_handle_as_flora,"mm_vegetation_tree28" ,"bo_mm_vegetation_tree8" , []),
  ("mm_tree_vegetation2_9" ,sokf_handle_as_flora,"mm_vegetation_tree29" ,"bo_mm_vegetation_tree9" , []),
  ("mm_tree_vegetation2_10" ,sokf_handle_as_flora,"mm_vegetation_tree210" ,"bo_mm_vegetation_tree10" , []),
  ("mm_tree_vegetation2_11" ,sokf_handle_as_flora,"mm_vegetation_tree211" ,"bo_mm_vegetation_tree11" , []),
  ("mm_tree_vegetation2_12" ,sokf_handle_as_flora,"mm_vegetation_tree212" ,"bo_mm_vegetation_tree12" , []),
  ("mm_tree_vegetation2_14" ,sokf_handle_as_flora,"mm_vegetation_tree214" ,"bo_mm_vegetation_tree14" , []),
  ("mm_tree_vegetation2_15" ,sokf_handle_as_flora,"mm_vegetation_tree215" ,"bo_mm_vegetation_tree15" , []),
  
  ("mm_tree_vegetation3_1" ,sokf_handle_as_flora,"mm_vegetation_tree31" ,"bo_mm_vegetation_tree1" , []),
  ("mm_tree_vegetation3_2" ,sokf_handle_as_flora,"mm_vegetation_tree32" ,"bo_mm_vegetation_tree2" , []),
  ("mm_tree_vegetation3_3" ,sokf_handle_as_flora,"mm_vegetation_tree33" ,"bo_mm_vegetation_tree3" , []),
  ("mm_tree_vegetation3_4" ,sokf_handle_as_flora,"mm_vegetation_tree34" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation3_5" ,sokf_handle_as_flora,"mm_vegetation_tree35" ,"bo_mm_vegetation_tree5" , []),
  ("mm_tree_vegetation3_6" ,sokf_handle_as_flora,"mm_vegetation_tree36" ,"bo_mm_vegetation_tree6" , []),
  ("mm_tree_vegetation3_7" ,sokf_handle_as_flora,"mm_vegetation_tree37" ,"bo_mm_vegetation_tree7" , []),
  ("mm_tree_vegetation3_8" ,sokf_handle_as_flora,"mm_vegetation_tree38" ,"bo_mm_vegetation_tree8" , []),
  ("mm_tree_vegetation3_9" ,sokf_handle_as_flora,"mm_vegetation_tree39" ,"bo_mm_vegetation_tree9" , []),
  ("mm_tree_vegetation3_10" ,sokf_handle_as_flora,"mm_vegetation_tree310" ,"bo_mm_vegetation_tree10" , []),
  ("mm_tree_vegetation3_11" ,sokf_handle_as_flora,"mm_vegetation_tree311" ,"bo_mm_vegetation_tree11" , []),
  ("mm_tree_vegetation3_12" ,sokf_handle_as_flora,"mm_vegetation_tree312" ,"bo_mm_vegetation_tree12" , []),
  ("mm_tree_vegetation3_14" ,sokf_handle_as_flora,"mm_vegetation_tree314" ,"bo_mm_vegetation_tree14" , []),
  ("mm_tree_vegetation3_15" ,sokf_handle_as_flora,"mm_vegetation_tree315" ,"bo_mm_vegetation_tree15" , []),
  
  ("mm_tree_vegetation7_1" ,sokf_handle_as_flora,"mm_vegetation_tree71" ,"bo_mm_vegetation_tree1" , []),
  ("mm_tree_vegetation7_2" ,sokf_handle_as_flora,"mm_vegetation_tree72" ,"bo_mm_vegetation_tree2" , []),
  ("mm_tree_vegetation7_3" ,sokf_handle_as_flora,"mm_vegetation_tree73" ,"bo_mm_vegetation_tree3" , []),
  ("mm_tree_vegetation7_4" ,sokf_handle_as_flora,"mm_vegetation_tree74" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation7_5" ,sokf_handle_as_flora,"mm_vegetation_tree75" ,"bo_mm_vegetation_tree5" , []),
  ("mm_tree_vegetation7_6" ,sokf_handle_as_flora,"mm_vegetation_tree76" ,"bo_mm_vegetation_tree6" , []),
  ("mm_tree_vegetation7_7" ,sokf_handle_as_flora,"mm_vegetation_tree77" ,"bo_mm_vegetation_tree7" , []),
  ("mm_tree_vegetation7_8" ,sokf_handle_as_flora,"mm_vegetation_tree78" ,"bo_mm_vegetation_tree8" , []),
  ("mm_tree_vegetation7_9" ,sokf_handle_as_flora,"mm_vegetation_tree79" ,"bo_mm_vegetation_tree9" , []),
  ("mm_tree_vegetation7_10" ,sokf_handle_as_flora,"mm_vegetation_tree710" ,"bo_mm_vegetation_tree10" , []),
  ("mm_tree_vegetation7_11" ,sokf_handle_as_flora,"mm_vegetation_tree711" ,"bo_mm_vegetation_tree11" , []),
  ("mm_tree_vegetation7_12" ,sokf_handle_as_flora,"mm_vegetation_tree712" ,"bo_mm_vegetation_tree12" , []),
  ("mm_tree_vegetation7_14" ,sokf_handle_as_flora,"mm_vegetation_tree714" ,"bo_mm_vegetation_tree14" , []),
  ("mm_tree_vegetation7_15" ,sokf_handle_as_flora,"mm_vegetation_tree715" ,"bo_mm_vegetation_tree15" , []),
  
  ("mm_tree_vegetation8_1" ,sokf_handle_as_flora,"mm_vegetation_tree81" ,"bo_mm_vegetation_tree1" , []),
  ("mm_tree_vegetation8_2" ,sokf_handle_as_flora,"mm_vegetation_tree82" ,"bo_mm_vegetation_tree2" , []),
  ("mm_tree_vegetation8_3" ,sokf_handle_as_flora,"mm_vegetation_tree83" ,"bo_mm_vegetation_tree3" , []),
  ("mm_tree_vegetation8_4" ,sokf_handle_as_flora,"mm_vegetation_tree84" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation8_5" ,sokf_handle_as_flora,"mm_vegetation_tree85" ,"bo_mm_vegetation_tree5" , []),
  ("mm_tree_vegetation8_6" ,sokf_handle_as_flora,"mm_vegetation_tree86" ,"bo_mm_vegetation_tree6" , []),
  ("mm_tree_vegetation8_7" ,sokf_handle_as_flora,"mm_vegetation_tree87" ,"bo_mm_vegetation_tree7" , []),
  ("mm_tree_vegetation8_8" ,sokf_handle_as_flora,"mm_vegetation_tree88" ,"bo_mm_vegetation_tree8" , []),
  ("mm_tree_vegetation8_9" ,sokf_handle_as_flora,"mm_vegetation_tree89" ,"bo_mm_vegetation_tree9" , []),
  ("mm_tree_vegetation8_10" ,sokf_handle_as_flora,"mm_vegetation_tree810" ,"bo_mm_vegetation_tree10" , []),
  ("mm_tree_vegetation8_11" ,sokf_handle_as_flora,"mm_vegetation_tree811" ,"bo_mm_vegetation_tree11" , []),
  ("mm_tree_vegetation8_12" ,sokf_handle_as_flora,"mm_vegetation_tree812" ,"bo_mm_vegetation_tree12" , []),
  ("mm_tree_vegetation8_14" ,sokf_handle_as_flora,"mm_vegetation_tree814" ,"bo_mm_vegetation_tree14" , []),
  ("mm_tree_vegetation8_15" ,sokf_handle_as_flora,"mm_vegetation_tree815" ,"bo_mm_vegetation_tree15" , []),
  
  ("mm_tree_vegetation9_1" ,sokf_handle_as_flora,"mm_vegetation_tree91" ,"bo_mm_vegetation_tree1" , []),
  ("mm_tree_vegetation9_2" ,sokf_handle_as_flora,"mm_vegetation_tree92" ,"bo_mm_vegetation_tree2" , []),
  ("mm_tree_vegetation9_3" ,sokf_handle_as_flora,"mm_vegetation_tree93" ,"bo_mm_vegetation_tree3" , []),
  ("mm_tree_vegetation9_4" ,sokf_handle_as_flora,"mm_vegetation_tree94" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation9_5" ,sokf_handle_as_flora,"mm_vegetation_tree95" ,"bo_mm_vegetation_tree5" , []),
  ("mm_tree_vegetation9_6" ,sokf_handle_as_flora,"mm_vegetation_tree96" ,"bo_mm_vegetation_tree6" , []),
  ("mm_tree_vegetation9_7" ,sokf_handle_as_flora,"mm_vegetation_tree97" ,"bo_mm_vegetation_tree7" , []),
  ("mm_tree_vegetation9_8" ,sokf_handle_as_flora,"mm_vegetation_tree98" ,"bo_mm_vegetation_tree8" , []),
  ("mm_tree_vegetation9_9" ,sokf_handle_as_flora,"mm_vegetation_tree99" ,"bo_mm_vegetation_tree9" , []),
  ("mm_tree_vegetation9_10" ,sokf_handle_as_flora,"mm_vegetation_tree910" ,"bo_mm_vegetation_tree10" , []),
  ("mm_tree_vegetation9_11" ,sokf_handle_as_flora,"mm_vegetation_tree911" ,"bo_mm_vegetation_tree11" , []),
  ("mm_tree_vegetation9_12" ,sokf_handle_as_flora,"mm_vegetation_tree912" ,"bo_mm_vegetation_tree12" , []),
  ("mm_tree_vegetation9_14" ,sokf_handle_as_flora,"mm_vegetation_tree914" ,"bo_mm_vegetation_tree14" , []),
  ("mm_tree_vegetation9_15" ,sokf_handle_as_flora,"mm_vegetation_tree915" ,"bo_mm_vegetation_tree15" , []),
  
  ("mm_tree_vegetation10_1" ,sokf_handle_as_flora,"mm_vegetation_tree101" ,"bo_mm_vegetation_tree1" , []),
  ("mm_tree_vegetation10_2" ,sokf_handle_as_flora,"mm_vegetation_tree102" ,"bo_mm_vegetation_tree2" , []),
  ("mm_tree_vegetation10_3" ,sokf_handle_as_flora,"mm_vegetation_tree103" ,"bo_mm_vegetation_tree3" , []),
  ("mm_tree_vegetation10_4" ,sokf_handle_as_flora,"mm_vegetation_tree104" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation10_5" ,sokf_handle_as_flora,"mm_vegetation_tree104" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation10_6" ,sokf_handle_as_flora,"mm_vegetation_tree106" ,"bo_mm_vegetation_tree6" , []),
  ("mm_tree_vegetation10_7" ,sokf_handle_as_flora,"mm_vegetation_tree107" ,"bo_mm_vegetation_tree7" , []),
  ("mm_tree_vegetation10_8" ,sokf_handle_as_flora,"mm_vegetation_tree108" ,"bo_mm_vegetation_tree8" , []),
  ("mm_tree_vegetation10_9" ,sokf_handle_as_flora,"mm_vegetation_tree109" ,"bo_mm_vegetation_tree9" , []),
  ("mm_tree_vegetation10_10" ,sokf_handle_as_flora,"mm_vegetation_tree1010" ,"bo_mm_vegetation_tree10" , []),
  ("mm_tree_vegetation10_11" ,sokf_handle_as_flora,"mm_vegetation_tree1011" ,"bo_mm_vegetation_tree11" , []),
  ("mm_tree_vegetation10_12" ,sokf_handle_as_flora,"mm_vegetation_tree1012" ,"bo_mm_vegetation_tree12" , []),
  ("mm_tree_vegetation10_14" ,sokf_handle_as_flora,"mm_vegetation_tree1014" ,"bo_mm_vegetation_tree14" , []),
  ("mm_tree_vegetation10_15" ,sokf_handle_as_flora,"mm_vegetation_tree1015" ,"bo_mm_vegetation_tree15" , []),
  
  ("mm_tree_vegetation11_1" ,sokf_handle_as_flora,"mm_vegetation_tree111" ,"bo_mm_vegetation_tree1" , []),
  ("mm_tree_vegetation11_2" ,sokf_handle_as_flora,"mm_vegetation_tree112" ,"bo_mm_vegetation_tree2" , []),
  ("mm_tree_vegetation11_3" ,sokf_handle_as_flora,"mm_vegetation_tree113" ,"bo_mm_vegetation_tree3" , []),
  ("mm_tree_vegetation11_4" ,sokf_handle_as_flora,"mm_vegetation_tree114" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation11_5" ,sokf_handle_as_flora,"mm_vegetation_tree114" ,"bo_mm_vegetation_tree4" , []),
  ("mm_tree_vegetation11_6" ,sokf_handle_as_flora,"mm_vegetation_tree116" ,"bo_mm_vegetation_tree6" , []),
  ("mm_tree_vegetation11_7" ,sokf_handle_as_flora,"mm_vegetation_tree117" ,"bo_mm_vegetation_tree7" , []),
  ("mm_tree_vegetation11_8" ,sokf_handle_as_flora,"mm_vegetation_tree118" ,"bo_mm_vegetation_tree8" , []),
  ("mm_tree_vegetation11_9" ,sokf_handle_as_flora,"mm_vegetation_tree119" ,"bo_mm_vegetation_tree9" , []),
  ("mm_tree_vegetation11_10" ,sokf_handle_as_flora,"mm_vegetation_tree1110" ,"bo_mm_vegetation_tree10" , []),
  ("mm_tree_vegetation11_11" ,sokf_handle_as_flora,"mm_vegetation_tree1111" ,"bo_mm_vegetation_tree11" , []),
  ("mm_tree_vegetation11_12" ,sokf_handle_as_flora,"mm_vegetation_tree1112" ,"bo_mm_vegetation_tree12" , []),
  ("mm_tree_vegetation11_14" ,sokf_handle_as_flora,"mm_vegetation_tree1114" ,"bo_mm_vegetation_tree14" , []),
  ("mm_tree_vegetation11_15" ,sokf_handle_as_flora,"mm_vegetation_tree1115" ,"bo_mm_vegetation_tree15" , []),
  
  ("mm_tree_palm1" ,sokf_handle_as_flora,"palmb_7" ,"bo_palmb_7" , []),
  ("mm_tree_palm2" ,sokf_handle_as_flora,"palmb_8" ,"bo_palmb_8" , []),
  ("mm_tree_palm3" ,sokf_handle_as_flora,"palmb_9" ,"bo_palmb_9" , []),
  ("mm_tree_palm4" ,sokf_handle_as_flora,"palmb_10" ,"bo_palmb_10" , []),
  ("mm_tree_palm5" ,sokf_handle_as_flora,"palmb_11" ,"bo_palmb_11" , []),
  ("mm_tree_palm6" ,sokf_handle_as_flora,"palmb_12" ,"bo_palmb_12" , []),

  ("mm_hugo1" ,0,"hugo1" ,"bo_hugo1" , []),
  ("mm_hugo11" ,0,"hugo11" ,"bo_hugo11" , []),
  ("mm_hugo2" ,0,"hugo2" ,"bo_hugo2" , []),
  ("mm_hugo3" ,0,"hugo3" ,"bo_hugo3" , []),
  ("mm_hugo4" ,0,"hugo4" ,"bo_hugo4" , []),
  ("mm_hugo5" ,0,"hugo5" ,"bo_hugo5" , []),
  ("mm_hugo6" ,0,"hugo6" ,"bo_hugo6" , []),
  ("mm_hugo7" ,0,"hugo7" ,"bo_hugo7" , []),
  ("mm_hugo8" ,0,"hugo8" ,"bo_hugo8" , []),
  ("mm_hugo9" ,0,"hugo9" ,"bo_hugo9" , []),
  ("mm_hugo10" ,0,"hugo10" ,"bo_hugo10" , []),
  ("mm_hugo12" ,0,"hugo12" ,"bo_hugo12" , []),
  ("mm_hugo13" ,0,"hugo13" ,"bo_hugo13" , []),
  ("mm_hugo14" ,0,"hugo14" ,"bo_hugo14" , []),

  ("mm_cupboardd1" ,0,"mm_cupboard1" ,"bo_mm_cupboard2" , []),
  ("mm_cupboardd2" ,0,"mm_cupboard2" ,"bo_mm_cupboard2" , []),
  ("mm_cupboardd3" ,0,"mm_cupboard3" ,"bo_mm_cupboard3" , []),
  ("mm_cupboardd4" ,0,"mm_cupboard4" ,"bo_mm_cupboard5" , []),
  ("mm_cupboardd5" ,0,"mm_cupboard5" ,"bo_mm_cupboard5" , []),
  ("mm_box_a" ,0,"mm_box_a" ,"bo_mm_box_a" , []),
  ("mm_marrows" ,0,"mm_marrows" ,"0" , []),
  ("mm_kitchentools1" ,0,"mm_kitchentools1" ,"0" , []),
  ("mm_sofa2" ,0,"mm_sofa2" ,"bo_mm_sofa2" , []),
  ("mm_sofa" ,0,"mm_sofa" ,"bo_mm_sofa2" , []),
  ("mm_tree_bench" ,0,"mm_tree_bench" ,"bo_mm_tree_bench" , []),
  ("mm_bedside_table" ,0,"mm_bedside_table" ,"bo_mm_bedside_table" , []),
  ("mm_tablebig4" ,0,"mm_tablebig4" ,"bo_mm_tablebig3" , []),
  ("mm_tablebig3" ,0,"mm_tablebig3" ,"bo_mm_tablebig3" , []),
  ("mm_tablebig2" ,0,"mm_tablebig2" ,"bo_mm_tablebig2" , []),
  ("mm_tablebig1" ,0,"mm_tablebig1" ,"bo_mm_tablebig2" , []),
  ("mm_mauers8" ,0,"mauers8" ,"bo_mauers8" , []),

  ("mm_redoubt_modular_corner" ,0,"mm_redoubt_modular_corner" ,"bo_mm_redoubt_modular_corner" , []),
  ("mm_redoubt_modular_endpart" ,0,"mm_redoubt_modular_endpart" ,"bo_mm_redoubt_modular_endpart" , []),
  ("mm_redoubt_modular_straight" ,0,"mm_redoubt_modular_straight" ,"bo_mm_redoubt_modular_straight" , []),
  ("mm_redoubt_modular_straight_d" ,0,"mm_redoubt_modular_straight_d" ,"bo_mm_redoubt_modular_straight_d" , []),
  ("mm_redoubt_modular_straight_d1" ,0,"mm_redoubt_modular_straight_d1" ,"bo_mm_redoubt_modular_straight_d1" , []),

  ("mm_flora_bush_new_3" ,sokf_handle_as_flora,"bush_new_b" ,"0" , []),

  ("mm_flora_flowers1a" ,sokf_handle_as_flora,"grass_bush_amm" ,"0" , []),
  ("mm_flora_flowers1b" ,sokf_handle_as_flora,"grass_bush_bmm" ,"0" , []),
 
  ("mm_flora_flowersa" ,sokf_handle_as_flora,"grass_bush_cmm" ,"0" , []),
  ("mm_flora_flowersb" ,sokf_handle_as_flora,"grass_bush_c2mm" ,"0" , []),
  ("mm_flora_flowersc" ,sokf_handle_as_flora,"grass_bush_c3mm" ,"0" , []),
  ("mm_flora_flowersd" ,sokf_handle_as_flora,"grass_bush_dmm" ,"0" , []),

  ("mm_flora_flowers2a" ,sokf_handle_as_flora,"grass_bush_emm" ,"0" , []),
  ("mm_flora_flowers2b" ,sokf_handle_as_flora,"grass_bush_fmm" ,"0" , []),
  ("mm_flora_flowers2c" ,sokf_handle_as_flora,"grass_bush_gmm" ,"0" , []),
  ("mm_flora_flowers2d" ,sokf_handle_as_flora,"grass_bush_hmm" ,"0" , []),
  ("mm_flora_flowers2e" ,sokf_handle_as_flora,"grass_bush_imm" ,"0" , []),
  ("mm_flora_flowers2f" ,sokf_handle_as_flora,"grass_bush_jmm" ,"0" , []),
  ("mm_flora_flowers2g" ,sokf_handle_as_flora,"grass_bush_kmm" ,"0" , []),
  ("mm_flora_flowers2h" ,sokf_handle_as_flora,"grass_bush_lmm" ,"0" , []),
  ("mm_flora_flowers2i" ,sokf_handle_as_flora,"grass_bush_mmm" ,"0" , []),

  ("mm_flora_mushrooms" ,sokf_handle_as_flora,"mm_mushrooms2" ,"0" , []),

  ("mm_flora_bush_greena" ,sokf_handle_as_flora,"mm_bush" ,"0" , []),
  ("mm_flora_bush_greenb" ,sokf_handle_as_flora,"mm_bush2" ,"0" , []),
  ("mm_flora_bush_greenc" ,sokf_handle_as_flora,"mm_bush3" ,"0" , []),
  ("mm_flora_bush_greend" ,sokf_handle_as_flora,"mm_bush4" ,"0" , []),
  ("mm_flora_bush_greene" ,sokf_handle_as_flora,"mm_bush5" ,"0" , []),
  ("mm_flora_bush_greenf" ,sokf_handle_as_flora,"mm_bush6" ,"0" , []),
  ("mm_flora_bush_greeng" ,sokf_handle_as_flora,"mm_bush7" ,"0" , []),

  ("mm_flora_bush_orangea" ,sokf_handle_as_flora,"mm_bush_new" ,"0" , []),
  ("mm_flora_bush_orangeb" ,sokf_handle_as_flora,"mm_bush_new2" ,"0" , []),
  ("mm_flora_bush_orangec" ,sokf_handle_as_flora,"mm_bush_new3" ,"0" , []),
  ("mm_flora_bush_oranged" ,sokf_handle_as_flora,"mm_bush_new4" ,"0" , []),
  ("mm_flora_bush_orangee" ,sokf_handle_as_flora,"mm_bush_new5" ,"0" , []),
  ("mm_flora_bush_orangef" ,sokf_handle_as_flora,"mm_bush_new6" ,"0" , []),
  ("mm_flora_bush_orangeg" ,sokf_handle_as_flora,"mm_bush_new7" ,"0" , []),

  ("mm_flora_giant_busha" ,sokf_handle_as_flora,"mm_giant_bush" ,"0" , []),
  ("mm_flora_giant_bushb" ,sokf_handle_as_flora,"mm_giant_bush2" ,"0" , []),
  ("mm_flora_giant_bushc" ,sokf_handle_as_flora,"mm_giant_bush3" ,"0" , []),
  ("mm_flora_giant_bushd" ,sokf_handle_as_flora,"mm_giant_bush4" ,"0" , []),
  ("mm_flora_giant_bushe" ,sokf_handle_as_flora,"mm_giant_bush5" ,"0" , []),
  ("mm_flora_giant_bushf" ,sokf_handle_as_flora,"mm_giant_bush6" ,"0" , []),
  ("mm_flora_giant_bushg" ,sokf_handle_as_flora,"mm_giant_bush7" ,"0" , []),

  ("mm_flora_old_busha" ,sokf_handle_as_flora,"mm_giant_bush_new" ,"0" , []),
  ("mm_flora_old_bushb" ,sokf_handle_as_flora,"mm_giant_bush_new2" ,"0" , []),
  ("mm_flora_old_bushc" ,sokf_handle_as_flora,"mm_giant_bush_new3" ,"0" , []),
  ("mm_flora_old_bushd" ,sokf_handle_as_flora,"mm_giant_bush_new4" ,"0" , []),
  ("mm_flora_old_bushe" ,sokf_handle_as_flora,"mm_giant_bush_new5" ,"0" , []),
  ("mm_flora_old_bushf" ,sokf_handle_as_flora,"mm_giant_bush_new6" ,"0" , []),
  ("mm_flora_old_bushg" ,sokf_handle_as_flora,"mm_giant_bush_new7" ,"0" , []),
 
  ("mm_flora_old_bush1a" ,sokf_handle_as_flora,"mm_old_bush" ,"0" , []),
  ("mm_flora_old_bush1b" ,sokf_handle_as_flora,"mm_old_bush2" ,"0" , []),
  ("mm_flora_old_bush1c" ,sokf_handle_as_flora,"mm_old_bush3" ,"0" , []),
  ("mm_flora_old_bush1d" ,sokf_handle_as_flora,"mm_old_bush4" ,"0" , []),
  ("mm_flora_old_bush1e" ,sokf_handle_as_flora,"mm_old_bush5" ,"0" , []),
  ("mm_flora_old_bush1f" ,sokf_handle_as_flora,"mm_old_bush6" ,"0" , []),
  ("mm_flora_old_bush1g" ,sokf_handle_as_flora,"mm_old_bush7" ,"0" , []),

  ("mm_flora_flower_busha" ,sokf_handle_as_flora,"bush_flower" ,"0" , []),
  ("mm_flora_flower_bushb" ,sokf_handle_as_flora,"bush_flower2" ,"0" , []),
  ("mm_flora_flower_bushc" ,sokf_handle_as_flora,"bush_flower3" ,"0" , []),
  ("mm_flora_flower_bushd" ,sokf_handle_as_flora,"bush_flower4" ,"0" , []),
  ("mm_flora_flower_bushe" ,sokf_handle_as_flora,"bush_flower5" ,"0" , []),
  ("mm_flora_flower_bushf" ,sokf_handle_as_flora,"bush_flower6" ,"0" , []),
  ("mm_flora_flower_bushg" ,sokf_handle_as_flora,"bush_flower7" ,"0" , []),  
  ("mm_flora_flower_bushh" ,sokf_handle_as_flora,"bush_flower8" ,"0" , []),
  ("mm_flora_flower_bushi" ,sokf_handle_as_flora,"bush_flower9" ,"0" , []),
  ("mm_flora_flower_bushk" ,sokf_handle_as_flora,"bush_flower11" ,"0" , []),
  ("mm_flora_flower_bushl" ,sokf_handle_as_flora,"bush_flower12" ,"0" , []),
  ("mm_flora_flower_bushm" ,sokf_handle_as_flora,"bush_flower13" ,"0" , []),
  ("mm_flora_flower_bushn" ,sokf_handle_as_flora,"bush_flower14" ,"0" , []),
  ("mm_flora_flower_busho" ,sokf_handle_as_flora,"bush_flower15" ,"0" , []),
  ("mm_flora_flower_bushp" ,sokf_handle_as_flora,"bush_flower16" ,"0" , []),
  ("mm_flora_flower_bushq" ,sokf_handle_as_flora,"bush_flower17" ,"0" , []),
  ("mm_flora_flower_bushr" ,sokf_handle_as_flora,"bush_flower18" ,"0" , []),
  ("mm_flora_flower_bushs" ,sokf_handle_as_flora,"bush_flower19" ,"0" , []),
  ("mm_flora_flower_busht" ,sokf_handle_as_flora,"bush_flower20" ,"0" , []),  

  ("mm_flora_bush_green_newa" ,sokf_handle_as_flora,"bush_new_green1" ,"0" , []),
  ("mm_flora_bush_green_newb" ,sokf_handle_as_flora,"bush_new_green2" ,"0" , []),
  ("mm_flora_bush_green_newc" ,sokf_handle_as_flora,"bush_new_green3" ,"0" , []),
  ("mm_flora_bush_green_newd" ,sokf_handle_as_flora,"bush_new_green4" ,"0" , []),
  ("mm_flora_bush_green_newe" ,sokf_handle_as_flora,"bush_new_green5" ,"0" , []),
  ("mm_flora_bush_green_newf" ,sokf_handle_as_flora,"bush_new_green6" ,"0" , []),
  ("mm_flora_bush_green_newg" ,sokf_handle_as_flora,"bush_new_green7" ,"0" , []),

  ("mm_flora_bush_wintera" ,sokf_handle_as_flora,"mm_bush_winter" ,"0" , []),
  ("mm_flora_bush_winterb" ,sokf_handle_as_flora,"mm_bush_winter2" ,"0" , []),
  ("mm_flora_bush_winterc" ,sokf_handle_as_flora,"mm_bush_winter3" ,"0" , []),
  ("mm_flora_bush_winterd" ,sokf_handle_as_flora,"mm_bush_winter4" ,"0" , []),
  ("mm_flora_bush_wintere" ,sokf_handle_as_flora,"mm_bush_winter5" ,"0" , []),
  ("mm_flora_bush_winterf" ,sokf_handle_as_flora,"mm_bush_winter6" ,"0" , []),
  ("mm_flora_bush_winterg" ,sokf_handle_as_flora,"mm_bush_winter7" ,"0" , []),  
  ("mm_flora_bush_winterh" ,sokf_handle_as_flora,"mm_bush_winter8" ,"0" , []),
  ("mm_flora_bush_winteri" ,sokf_handle_as_flora,"mm_bush_winter9" ,"0" , []),
  ("mm_flora_bush_winterj" ,sokf_handle_as_flora,"mm_bush_winter10" ,"0" , []),  
  
  ("mm_flora_bush_winter2a" ,sokf_handle_as_flora,"mm_bush_winter14" ,"0" , []),
  ("mm_flora_bush_winter2b" ,sokf_handle_as_flora,"mm_bush_winter15" ,"0" , []),
  ("mm_flora_bush_winter2c" ,sokf_handle_as_flora,"mm_bush_winter16" ,"0" , []),
  ("mm_flora_bush_winter2d" ,sokf_handle_as_flora,"mm_bush_winter17" ,"0" , []),

  ("mm_flora_roses" ,sokf_handle_as_flora,"roses" ,"0" , []),  

  ("mm_flora_buddy_planta" ,sokf_handle_as_flora,"buddy_plant" ,"0" , []),  
  ("mm_flora_buddy_plantb" ,sokf_handle_as_flora,"buddy_plant_b" ,"0" , []),  
 
  ("mm_flora_cattail1" ,sokf_handle_as_flora,"cattail1" ,"0" , []),  
  ("mm_flora_cattail2" ,sokf_handle_as_flora,"cattail2" ,"0" , []),  
  ("mm_flora_cattail3" ,sokf_handle_as_flora,"cattail3" ,"0" , []),  
  ("mm_flora_cattail4" ,sokf_handle_as_flora,"cattail4" ,"0" , []),  
  ("mm_flora_cattail5" ,sokf_handle_as_flora,"cattail5" ,"0" , []),  
  ("mm_flora_cattail6" ,sokf_handle_as_flora,"cattail6" ,"0" , []),  
  ("mm_flora_cattail7" ,sokf_handle_as_flora,"cattail7" ,"0" , []),  
  ("mm_flora_lilly1" ,sokf_handle_as_flora,"lilly1" ,"0" , []),

  ("mm_spanish" ,0,"spanish" ,"bo_spanish" , []),
  ("mm_spanish1" ,0,"spanish1" ,"bo_spanish1" , []),
  ("mm_spanish2" ,0,"spanish2" ,"bo_spanish2" , []),
  ("mm_spanish3" ,0,"spanish3" ,"bo_spanish3" , []),
  ("mm_spanish4" ,0,"spanish4" ,"bo_spanish4" , []),
  ("mm_spanish5" ,0,"spanish5" ,"bo_spanish5" , []),
  ("mm_spanish6" ,0,"spanish6" ,"bo_spanish6" , []),
  ("mm_spanish7" ,0,"spanish7" ,"bo_spanish7" , []),
  ("mm_spanish8" ,0,"spanish8" ,"bo_spanish8" , []),
  ("mm_spanish9" ,0,"spanish9" ,"bo_spanish9" , []),
  ("mm_spanish10" ,0,"spanish10" ,"bo_spanish10" , []),
  ("mm_spanish11" ,0,"spanish11" ,"bo_spanish11" , []),
  ("mm_spanish12" ,0,"spanish12" ,"bo_spanish12" , []),
  ("mm_spanish13" ,0,"spanish13" ,"bo_spanish13" , []),
  ("mm_spanish14" ,0,"spanish14" ,"bo_spanish14" , []),
  ("mm_spanish15" ,0,"spanish15" ,"bo_spanish15" , []),
  ("mm_spanish16" ,0,"spanish16" ,"bo_spanish16" , []),
  ("mm_spanishwallcorner" ,0,"spanishwallcorner" ,"bo_spanishwallcorner" , []),
  ("mm_spanishwallgate" ,0,"spanishwallgate" ,"bo_spanishwallgate" , []),

  ("mm_watersplash",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
      (store_trigger_param_1,":instance_id"),
      (store_random_in_range,":cur_time",1,3), #0-2 sec until first burst
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    ]),
   ]),


  ("mm_ambient_insects2",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
      (store_trigger_param_1,":instance_id"),
      (store_random_in_range,":cur_time",1,3),
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    ]),
   ]),


  ("mm_ambient_insects1",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
      (store_trigger_param_1,":instance_id"),
      (store_random_in_range,":cur_time",1,3),
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    ]),
   ]),


  ("mm_ambient_insects",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
      (store_trigger_param_1,":instance_id"),
      (store_random_in_range,":cur_time",1,3), #0-2 sec until first burst
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time"),
    ]),
  ]),

  ("mm_la_haye1" ,0,"la_haye_saint" ,"bo_la_haye_saint" , []),
  ("mm_la_haye2" ,0,"la_haye_saint" ,"bo_la_haye_saint" , []),
  ("mm_la_haye3" ,0,"la_haye_saint2" ,"bo_la_haye_saint2" , []),
  ("mm_la_haye4" ,0,"la_haye_saint3" ,"bo_la_haye_saint3" , []),
  ("mm_la_haye5" ,0,"la_haye_saint4" ,"bo_la_haye_saint4" , []),
  ("mm_la_haye6" ,0,"la_haye_saint5" ,"bo_la_haye_saint5" , []),
  ("mm_la_haye7" ,0,"la_haye_saint6" ,"bo_la_haye_saint6" , []),	

  ("mm_ammunition_depot" ,0,"ammunition_depot" ,"ammunition_depot_collision" , []),
  ("mm_gabion" ,0,"gabion" ,"gabion_collision" , []),
  ("mm_gunnest" ,0,"gunnest" ,"gunnest_collision" , []),
  ("mm_gabiondeploy" ,0,"gabiondeploy" ,"bo_gabiondeploy" , []),

  ("mm_mill2" ,0,"mmmill2" ,"bo_sp_poor_village_houses9" , []),

  ("mm_house_ornament1" ,0,"1owall" ,"0" , []),
  ("mm_house_ornament2" ,0,"2owall" ,"0" , []),
  ("mm_house_stair1" ,0,"stair" ,"bo_stair" , []),
  ("mm_house_stair2" ,0,"stair2" ,"bo_stair2" , []),
  ("mm_house_stair3" ,0,"stair3" ,"bo_stair3" , []),
  ("mm_house_basic1" ,0,"formen" ,"bo_formen" , []),
  ("mm_house_basic3" ,0,"formen3" ,"bo_formen3" , []),
  ("mm_house_basic4" ,0,"formen4" ,"bo_formen4" , []),
  ("mm_house_basic5" ,0,"formen5" ,"bo_formen5" , []),
  ("mm_house_basic6" ,0,"formen6" ,"bo_formen6" , []),
  ("mm_house_basic7" ,0,"formen7" ,"bo_formen7" , []),
  ("mm_house_basic8" ,0,"formen8" ,"bo_formen8" , []),
  ("mm_house_basic9" ,0,"formen9" ,"bo_formen9" , []),
  ("mm_house_basic10" ,0,"formen10" ,"bo_formen10" , []),
  ("mm_house_basic11" ,0,"formen11" ,"bo_formen11" , []),
  ("mm_house_basic12" ,0,"formen12" ,"bo_formen12" , []),
  ("mm_house_basic13" ,0,"formen13" ,"bo_formen13" , []),
  ("mm_house_basic14" ,0,"formen14" ,"bo_formen14" , []),

  ("mm_1housebuild" ,0,"1housebuild" ,"bo_1housebuild" , []),
  ("mm_2housebuild" ,0,"2housebuild" ,"bo_2housebuild" , []),
  ("mm_3housebuild" ,0,"3housebuild" ,"bo_3housebuild" , []),
  ("mm_4housebuild" ,0,"4housebuild" ,"bo_4housebuild" , []),
  ("mm_5housebuild" ,0,"5housebuild" ,"bo_5housebuild" , []),
  ("mm_6housebuild" ,0,"6housebuild" ,"bo_6housebuild" , []),
  ("mm_7housebuild" ,0,"7housebuild" ,"bo_7housebuild" , []),
  ("mm_8housebuild" ,0,"8housebuild" ,"bo_8housebuild" , []),
  ("mm_9housebuild" ,0,"9housebuild" ,"bo_9housebuild" , []),
  ("mm_10housebuild" ,0,"10housebuild" ,"bo_10housebuild" , []),
  ("mm_11housebuild" ,0,"11housebuild" ,"bo_11housebuild" , []),
  ("mm_11_brick_housebuild" ,0,"11_brick_housebuild" ,"bo_11housebuild" , []),
  ("mm_12housebuild" ,0,"12housebuild" ,"bo_12housebuild" , []),
  ("mm_13housebuild" ,0,"13housebuild" ,"bo_13housebuild" , []),
  ("mm_14housebuild" ,0,"14housebuild" ,"bo_14housebuild" , []),
  ("mm_15housebuild" ,0,"15housebuild" ,"bo_15housebuild" , []),
  ("mm_16housebuild" ,0,"16housebuild" ,"bo_16housebuild" , []),
  ("mm_17housebuild" ,0,"17housebuild" ,"bo_17housebuild" , []),
  ("mm_18housebuild" ,0,"18housebuild" ,"bo_18housebuild" , []),
  ("mm_19housebuild" ,0,"19housebuild" ,"bo_19housebuild" , []),
  ("mm_20housebuild" ,0,"20housebuild" ,"bo_20housebuild" , []),

  ("mm_new_1housebuild" ,0,"new_1housebuild" ,"bo_1housebuild" , []),
  ("mm_new_2housebuild" ,0,"new_2housebuild" ,"bo_2housebuild" , []),
  ("mm_new_3housebuild" ,0,"new_3housebuild" ,"bo_3housebuild" , []),
  ("mm_new_4housebuild" ,0,"new_4housebuild" ,"bo_4housebuild" , []),
  ("mm_new_5housebuild" ,0,"new_5housebuild" ,"bo_5housebuild" , []),
  ("mm_new_6housebuild" ,0,"new_6housebuild" ,"bo_6housebuild" , []),
  ("mm_new_7housebuild" ,0,"new_7housebuild" ,"bo_7housebuild" , []),
  ("mm_new_8housebuild" ,0,"new_8housebuild" ,"bo_8housebuild" , []),
  ("mm_new_9housebuild" ,0,"new_9housebuild" ,"bo_9housebuild" , []),
  ("mm_new_10housebuild" ,0,"new_10housebuild" ,"bo_10housebuild" , []),
  ("mm_new_11housebuild" ,0,"new_11housebuild" ,"bo_11housebuild" , []),
  ("mm_new_12housebuild" ,0,"new_12housebuild" ,"bo_12housebuild" , []),
  ("mm_new_13housebuild" ,0,"new_13housebuild" ,"bo_13housebuild" , []),
  ("mm_new_14housebuild" ,0,"new_14housebuild" ,"bo_14housebuild" , []),
  ("mm_new_15housebuild" ,0,"new_15housebuild" ,"bo_15housebuild" , []),
  ("mm_new_16housebuild" ,0,"new_16housebuild" ,"bo_16housebuild" , []),
  ("mm_new_17housebuild" ,0,"new_17housebuild" ,"bo_17housebuild" , []),
  ("mm_new_18housebuild" ,0,"new_18housebuild" ,"bo_18housebuild" , []),
  ("mm_new_19housebuild" ,0,"new_19housebuild" ,"bo_19housebuild" , []),
  ("mm_new_20housebuild" ,0,"new_20housebuild" ,"bo_20housebuild" , []),

  ("mm_build_church_tower" ,0,"church_tower" ,"bo_church_tower" , []),
  ("mm_build_church1" ,0,"church_building" ,"bo_church_building" , []),
  ("mm_build_church2" ,0,"church_building1" ,"bo_church_building" , []),

  ("mm_build_church_bell",0,"church_bell" ,"bo_church_bell" , []),
  ("mm_build_church_bellmov",sokf_static_movement,"church_bellmov" ,"0" , []),
  ("mm_build_church_rope",spr_use_time(1),"church_rope" ,"bo_church_rope" , [
   (ti_on_scene_prop_use,
    [
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),
      (store_trigger_param_2, ":rope_instance"),
      (prop_instance_get_position,pos3,":rope_instance"),
      (scene_prop_get_num_instances,":num_bells","spr_mm_build_church_bellmov"),
      (gt,":num_bells",0),
      (assign,":max_dist",999999),
      (try_for_prop_instances, ":bell_instance", "spr_mm_build_church_bellmov", somt_object),
        (prop_instance_get_position,pos1,":bell_instance"),
        (get_distance_between_positions,":dist",pos1,pos3),
        (lt,":dist",":max_dist"),
        (assign,":max_dist",":dist"),
        (assign,":use_bell_instance",":bell_instance"),
      (try_end),
      (scene_prop_get_slot,":bell_state",":use_bell_instance",scene_prop_slot_time),
      (neg|is_between,":bell_state",1,7),
      (scene_prop_set_slot,":use_bell_instance",scene_prop_slot_time,6),
    ]),
  ]),

  ("mm_woodenhouse" ,0,"woodenhouse" ,"bo_woodenhouse" , []),
  ("mm_woodensnowhouse" ,0,"woodensnowhouse" ,"bo_woodenhouse" , []),
  ("mm_woodenhouse2story" ,0,"woodenhouse2story" ,"bo_woodenhouse2story" , []),
  ("mm_woodenhouse2story2" ,0,"woodenhouse2story2" ,"bo_woodenhouse2story" , []),
  ("mm_woodenhouse2story3" ,0,"woodenhouse2story3" ,"bo_woodenhouse2story" , []),
  ("mm_woodenhouse2story4" ,0,"woodenhouse2story4" ,"bo_woodenhouse2story" , []),
  ("mm_woodenhouse2storysnowy" ,0,"woodenhouse2storysnowy" ,"bo_woodenhouse2story" , []),
  ("mm_woodenhouse2storysnowy2" ,0,"woodenhouse2storysnowy2" ,"bo_woodenhouse2story" , []),

  ("mm_tunnel_entrance" ,0,"mmtunnel1" ,"bo_mmtunnel1" , []),
  ("mm_tunnel" ,0,"mmtunnel2" ,"bo_mmtunnel2" , []),

  ("mm_ice1" ,0,"ice1" ,"bo_ice1" , []),
  ("mm_ice2" ,0,"ice2" ,"bo_ice2" , []),
  ("mm_ice3" ,0,"ice3" ,"bo_ice3" , []),
  ("mm_ice4" ,0,"ice4" ,"bo_ice4" , []),

  ("mm_window1_poor",sokf_static_movement|sokf_destructible,"window1_poor","bo_window1", [check_mm_on_destroy_window_trigger,]),
  ("mm_window2_poor",sokf_static_movement|sokf_destructible,"window2_poor","bo_window2", [check_mm_on_destroy_window_trigger,]),
  ("mm_window1",sokf_static_movement|sokf_destructible,"window1","bo_window1", [check_mm_on_destroy_window_trigger,]),
  ("mm_window2",sokf_static_movement|sokf_destructible,"window2","bo_window2", [check_mm_on_destroy_window_trigger,]),

  ("mm_window1d_poor",sokf_static_movement,"window1d_poor","0", []),
  ("mm_window2d_poor",sokf_static_movement,"window2d_poor","0", []),   
  ("mm_window1d",sokf_static_movement,"window1d","0", []),
  ("mm_window2d",sokf_static_movement,"window2d","0", []),

  ("mm_window3_poor",sokf_static_movement|sokf_destructible,"window_old_walls1_poor","bo_window_old_walls", [check_mm_on_destroy_window_trigger,]),
  ("mm_window4_poor",sokf_static_movement|sokf_destructible,"window_repos1_poor","bo_window_repos", [check_mm_on_destroy_window_trigger,]),
  ("mm_window3",sokf_static_movement|sokf_destructible,"window_old_walls1","bo_window_old_walls", [check_mm_on_destroy_window_trigger,]),
  ("mm_window4",sokf_static_movement|sokf_destructible,"window_repos1","bo_window_repos", [check_mm_on_destroy_window_trigger,]),

  ("mm_window3d_poor",sokf_static_movement,"window_old_walls1d_poor","0", []),
  ("mm_window4d_poor",sokf_static_movement,"window_repos1d_poor","0", []),   
  ("mm_window3d",sokf_static_movement,"window_old_walls1d","0", []),
  ("mm_window4d",sokf_static_movement,"window_repos1d","0", []),

  ("mm_windows_end",0,"0","0", []),

  ("mm_house_wall_1" ,sokf_static_movement,"1wall" ,"bo_1wall" , []),
  ("mm_house_wall_1d" ,sokf_static_movement,"1dwall" ,"bo_1dwall" , []),
  ("mm_house_wall_2" ,sokf_static_movement,"2wall" ,"bo_2wall" , []),
  ("mm_house_wall_2d" ,sokf_static_movement,"2dwall" ,"bo_2dwall" , []),
  ("mm_house_wall_3" ,sokf_static_movement,"3wall" ,"bo_3wall" , []),
  ("mm_house_wall_3d" ,sokf_static_movement,"3dwall" ,"bo_3dwall" , []),
  ("mm_house_wall_4" ,sokf_static_movement,"4wall" ,"bo_4wall" , []),
  ("mm_house_wall_4d" ,sokf_static_movement,"4dwall" ,"bo_4dwall" , []),
  ("mm_house_wall_5" ,sokf_static_movement,"5wall" ,"bo_5wall" , []),
  ("mm_house_wall_5d" ,sokf_static_movement,"5dwall" ,"bo_5dwall" , []),
  ("mm_house_wall_6" ,sokf_static_movement,"6wall" ,"bo_6wall" , []),
  ("mm_house_wall_6d" ,sokf_static_movement,"6dwall" ,"bo_6dwall" , []),
  ("mm_house_wall_7" ,sokf_static_movement,"7wall" ,"bo_7wall" , []),
  ("mm_house_wall_7d" ,sokf_static_movement,"7dwall" ,"bo_7dwall" , []),
  ("mm_house_wall_11" ,sokf_static_movement,"11wall" ,"bo_11wall" , []),
  ("mm_house_wall_11d" ,sokf_static_movement,"11dwall" ,"bo_11dwall" , []),
  ("mm_house_wall_21" ,sokf_static_movement,"21wall" ,"bo_21wall" , []),
  ("mm_house_wall_21d" ,sokf_static_movement,"21dwall" ,"bo_21dwall" , []),
  ("mm_house_wall_31" ,sokf_static_movement,"31wall" ,"bo_31wall" , []),
  ("mm_house_wall_31d" ,sokf_static_movement,"31dwall" ,"bo_31dwall" , []),
  ("mm_house_wall_41" ,sokf_static_movement,"41wall" ,"bo_41wall" , []),
  ("mm_house_wall_41d" ,sokf_static_movement,"41dwall" ,"bo_41dwall" , []),
  ("mm_house_wall_51" ,sokf_static_movement,"51wall" ,"bo_51wall" , []),
  ("mm_house_wall_51d" ,sokf_static_movement,"51dwall" ,"bo_51dwall" , []),
  ("mm_house_wall_61" ,sokf_static_movement,"61wall" ,"bo_61wall" , []),
  ("mm_house_wall_61d" ,sokf_static_movement,"61dwall" ,"bo_61dwall" , []),
  ("mm_house_wall_71" ,sokf_static_movement,"71wall" ,"bo_71wall" , []),
  ("mm_house_wall_71d" ,sokf_static_movement,"71dwall" ,"bo_71dwall" , []),
    
  ("mm_wall1", sokf_static_movement|sokf_dont_move_agent_over, "wall1", "bo_desertWall1" , []),
  ("mm_wall1d", sokf_static_movement|sokf_dont_move_agent_over, "wall1d", "bo_desertWall1d" , []),
  ("mm_wall1dd", sokf_static_movement|sokf_dont_move_agent_over, "wall1dd", "bo_desertWall1dd" , []),

  ("mm_walldesert1", sokf_static_movement|sokf_dont_move_agent_over, "desertWall1", "bo_desertWall1" , []),
  ("mm_walldesert1d", sokf_static_movement|sokf_dont_move_agent_over, "desertWall1d", "bo_desertWall1d" , []),
  ("mm_walldesert1dd", sokf_static_movement|sokf_dont_move_agent_over, "desertWall1dd", "bo_desertWall1dd" , []),
    
  ("mm_wallwood1", sokf_static_movement|sokf_dont_move_agent_over, "woodWall1", "bo_woodWall1" , []),
  ("mm_wallwood1d", sokf_static_movement|sokf_dont_move_agent_over, "woodWall1d", "bo_woodWall1d" , []),
  ("mm_wallwood1dd", sokf_static_movement|sokf_dont_move_agent_over, "woodWall1dd", "bo_woodWall1dd" , []),

  ("mm_wall3", sokf_static_movement|sokf_dont_move_agent_over, "wall3", "wall3_collision" , []),
  ("mm_wall4", sokf_static_movement|sokf_dont_move_agent_over, "wall4", "wall4_collision" , []),
  ("mm_wall5", sokf_static_movement|sokf_dont_move_agent_over, "wall5", "wall5_collision" , []),
  
  ("mm_stockade" ,sokf_static_movement,"stockade" ,"stockade_collision" , []),
  ("mm_stockade_cannon" ,sokf_static_movement,"stockade_cannon" ,"stockade_cannon_collision" , []),
    
  ("mm_palisade", sokf_static_movement, "mmpalisade", "bo_mmpalisade" , []),
  ("mm_palisaded", sokf_static_movement, "mmpalisaded", "bo_mmpalisaded" , []),
  ("mm_sp_poor_bridge1", sokf_static_movement|sokf_dont_move_agent_over, "sp_poor_village_bridge1", "bo_sp_poor_village_bridge1" , []),
  ("mm_pontoon_bridge1", sokf_static_movement|sokf_dont_move_agent_over, "pontoon", "bo_pontoon" , []),
  ("mm_pontoon_bridge2", sokf_static_movement|sokf_dont_move_agent_over, "pontoon2", "bo_pontoon" , []),
  ("mm_earthwork1", sokf_static_movement, "earthwork1", "bo_earthwork1" , []),
    
  ("fortnew", sokf_static_movement|sokf_dont_move_agent_over, "fortnew", "bo_fortnew" , []),
  ("fortnew1", sokf_static_movement|sokf_dont_move_agent_over, "fortnew1", "bo_fortnew" , []),
  ("fortnew2", sokf_static_movement|sokf_dont_move_agent_over, "fortnew2", "bo_fortnew" , []),
  ("fortnew3", sokf_static_movement|sokf_dont_move_agent_over, "fortnew3", "bo_fortnew" , []),
  ("fortnew4", sokf_static_movement|sokf_dont_move_agent_over, "fortnew4", "bo_fortnew" , []),
  ("fortnew5", sokf_static_movement|sokf_dont_move_agent_over, "fortnew5", "bo_fortnew5" , []),
  ("fortnew6", sokf_static_movement|sokf_dont_move_agent_over, "fortnew6", "bo_fortnew6" , []),
  ("fortnew7", sokf_static_movement|sokf_dont_move_agent_over, "fortnew7", "bo_fortnew6" , []),
  ("fortnew8", sokf_static_movement|sokf_dont_move_agent_over, "fortnew8", "bo_fortnew8" , []),

  ("fortnew_1", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_1", "bo_fortnew_1" , []),
  ("fortnew_12", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_12", "bo_fortnew_1" , []),
  ("fortnew_13", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_13", "bo_fortnew_1" , []),
  ("fortnew_14", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_14", "bo_fortnew_1" , []),
  ("fortnew_15", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_15", "bo_fortnew_1" , []),
  ("fortnew_16", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_16", "bo_fortnew_1" , []),
  ("fortnew_17", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_17", "bo_fortnew_17" , []),
  ("fortnew_18", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_18", "bo_fortnew_17" , []),
  ("fortnew_19", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_19", "bo_fortnew_19" , []),
  ("fortnew_110", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_110", "bo_fortnew_110" , []),

  ("fortnew_2", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_2", "bo_fortnew_2" , []),
  ("fortnew_21", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_21", "bo_fortnew_2" , []),
  ("fortnew_22", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_22", "bo_fortnew_2" , []),
  ("fortnew_23", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_23", "bo_fortnew_2" , []),
  ("fortnew_24", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_24", "bo_fortnew_2" , []),
  ("fortnew_25", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_25", "bo_fortnew_2" , []),
  ("fortnew_26", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_26", "bo_fortnew_2" , []),
  ("fortnew_27", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_27", "bo_fortnew_2" , []),
  ("fortnew_28", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_28", "bo_fortnew_2" , []),

  ("fortnew_3", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_3", "bo_fortnew_3" , []),
  ("fortnew_31", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_31", "bo_fortnew_3" , []),
  ("fortnew_32", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_32", "bo_fortnew_3" , []),
  ("fortnew_33", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_33", "bo_fortnew_3" , []),
  ("fortnew_34", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_34", "bo_fortnew_3" , []),
  ("fortnew_35", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_35", "bo_fortnew_3" , []),
  ("fortnew_36", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_36", "bo_fortnew_36" , []),
  ("fortnew_37", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_37", "bo_fortnew_36" , []),
  ("fortnew_38", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_38", "bo_fortnew_38" , []),
  ("fortnew_4", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_4", "bo_fortnew_4" , []),
    
  ("mm_new_wall_1_1" ,sokf_static_movement,"newall1" ,"bo_newall1" , []),
  ("mm_new_wall_1_1d" ,sokf_static_movement,"newall1d" ,"bo_newall1" , []),
  ("mm_new_wall_1_2" ,sokf_static_movement,"newall2" ,"bo_newall1" , []),
  ("mm_new_wall_1_2d" ,sokf_static_movement,"newall2d" ,"bo_newall1" , []),
  ("mm_new_wall_1_3" ,sokf_static_movement,"newall3" ,"bo_newall1" , []),
  ("mm_new_wall_1_3d" ,sokf_static_movement,"newall3d" ,"bo_newall1" , []),
  ("mm_new_wall_1_4" ,sokf_static_movement,"newall4" ,"bo_newall1" , []),
  ("mm_new_wall_1_4d" ,sokf_static_movement,"newall4d" ,"bo_newall1" , []),
  ("mm_new_wall_1_5" ,sokf_static_movement,"newall5" ,"bo_newall5" , []),
  ("mm_new_wall_1_5d" ,sokf_static_movement,"newall5d" ,"bo_newall5" , []),
  ("mm_new_wall_1_6" ,sokf_static_movement,"newall6" ,"bo_newall6" , []),
  ("mm_new_wall_1_6d" ,sokf_static_movement,"newall6d" ,"bo_newall6" , []),
  ("mm_new_wall_1_7" ,sokf_static_movement,"newall7" ,"bo_newall7" , []),
  ("mm_new_wall_1_7d" ,sokf_static_movement,"newall7d" ,"bo_newall7" , []),
  ("mm_new_wall_1_8" ,sokf_static_movement,"newall8" ,"bo_newall8" , []),
  ("mm_new_wall_1_8d" ,sokf_static_movement,"newall8d" ,"bo_newall8" , []),
  ("mm_new_wall_1_9" ,sokf_static_movement,"newall9" ,"bo_newall7" , []),
  ("mm_new_wall_1_9d" ,sokf_static_movement,"newall9d" ,"bo_newall7" , []),
  ("mm_new_wall_1_10" ,sokf_static_movement,"newall10" ,"bo_newall10" , []),
  ("mm_new_wall_1_10d" ,sokf_static_movement,"newall10d" ,"bo_newall10" , []),
  ("mm_new_wall_1_11" ,sokf_static_movement,"newall11" ,"bo_newall7" , []),
  ("mm_new_wall_1_11d" ,sokf_static_movement,"newall11d" ,"bo_newall7" , []),
    
  ("mm_new_wall_2_1" ,sokf_static_movement,"ne1wall1" ,"bo_newall1" , []),
  ("mm_new_wall_2_1d" ,sokf_static_movement,"ne1wall1d" ,"bo_newall1" , []),
  ("mm_new_wall_2_2" ,sokf_static_movement,"ne1wall2" ,"bo_newall1" , []),
  ("mm_new_wall_2_2d" ,sokf_static_movement,"ne1wall2d" ,"bo_newall1" , []),
  ("mm_new_wall_2_3" ,sokf_static_movement,"ne1wall3" ,"bo_newall1" , []),
  ("mm_new_wall_2_3d" ,sokf_static_movement,"ne1wall3d" ,"bo_newall1" , []),
  ("mm_new_wall_2_4" ,sokf_static_movement,"ne1wall4" ,"bo_newall1" , []),
  ("mm_new_wall_2_4d" ,sokf_static_movement,"ne1wall4d" ,"bo_newall1" , []),
  ("mm_new_wall_2_5" ,sokf_static_movement,"ne1wall5" ,"bo_newall5" , []),
  ("mm_new_wall_2_5d" ,sokf_static_movement,"ne1wall5d" ,"bo_newall5" , []),
  ("mm_new_wall_2_6" ,sokf_static_movement,"ne1wall6" ,"bo_newall6" , []),
  ("mm_new_wall_2_6d" ,sokf_static_movement,"ne1wall6d" ,"bo_newall6" , []),
  ("mm_new_wall_2_7" ,sokf_static_movement,"ne1wall7" ,"bo_newall7" , []),
  ("mm_new_wall_2_7d" ,sokf_static_movement,"ne1wall7d" ,"bo_newall7" , []),
  ("mm_new_wall_2_8" ,sokf_static_movement,"ne1wall8" ,"bo_newall8" , []),
  ("mm_new_wall_2_8d" ,sokf_static_movement,"ne1wall8d" ,"bo_newall8" , []),
  ("mm_new_wall_2_9" ,sokf_static_movement,"ne1wall9" ,"bo_newall7" , []),
  ("mm_new_wall_2_9d" ,sokf_static_movement,"ne1wall9d" ,"bo_newall7" , []),
  ("mm_new_wall_2_10" ,sokf_static_movement,"ne1wall10" ,"bo_newall10" , []),
  ("mm_new_wall_2_10d" ,sokf_static_movement,"ne1wall10d" ,"bo_newall10" , []),
  ("mm_new_wall_2_11" ,sokf_static_movement,"ne1wall11" ,"bo_newall7" , []),
  ("mm_new_wall_2_11d" ,sokf_static_movement,"ne1wall11d" ,"bo_newall7" , []),
    
  ("mm_new_wall_3_1" ,sokf_static_movement,"ne2wall1" ,"bo_newall1" , []),
  ("mm_new_wall_3_1d" ,sokf_static_movement,"ne2wall1d" ,"bo_newall1" , []),
  ("mm_new_wall_3_2" ,sokf_static_movement,"ne2wall2" ,"bo_newall1" , []),
  ("mm_new_wall_3_2d" ,sokf_static_movement,"ne2wall2d" ,"bo_newall1" , []),
  ("mm_new_wall_3_3" ,sokf_static_movement,"ne2wall3" ,"bo_newall1" , []),
  ("mm_new_wall_3_3d" ,sokf_static_movement,"ne2wall3d" ,"bo_newall1" , []),
  ("mm_new_wall_3_4" ,sokf_static_movement,"ne2wall4" ,"bo_newall1" , []),
  ("mm_new_wall_3_4d" ,sokf_static_movement,"ne2wall4d" ,"bo_newall1" , []),
  ("mm_new_wall_3_5" ,sokf_static_movement,"ne2wall5" ,"bo_newall5" , []),
  ("mm_new_wall_3_5d" ,sokf_static_movement,"ne2wall5d" ,"bo_newall5" , []),
  ("mm_new_wall_3_6" ,sokf_static_movement,"ne2wall6" ,"bo_newall6" , []),
  ("mm_new_wall_3_6d" ,sokf_static_movement,"ne2wall6d" ,"bo_newall6" , []),
  ("mm_new_wall_3_7" ,sokf_static_movement,"ne2wall7" ,"bo_newall7" , []),
  ("mm_new_wall_3_7d" ,sokf_static_movement,"ne2wall7d" ,"bo_newall7" , []),
  ("mm_new_wall_3_8" ,sokf_static_movement,"ne2wall8" ,"bo_newall8" , []),
  ("mm_new_wall_3_8d" ,sokf_static_movement,"ne2wall8d" ,"bo_newall8" , []),
  ("mm_new_wall_3_9" ,sokf_static_movement,"ne2wall9" ,"bo_newall7" , []),
  ("mm_new_wall_3_9d" ,sokf_static_movement,"ne2wall9d" ,"bo_newall7" , []),
  ("mm_new_wall_3_10" ,sokf_static_movement,"ne2wall10" ,"bo_newall10" , []),
  ("mm_new_wall_3_10d" ,sokf_static_movement,"ne2wall10d" ,"bo_newall10" , []),
  ("mm_new_wall_3_11" ,sokf_static_movement,"ne2wall11" ,"bo_newall7" , []),
  ("mm_new_wall_3_11d" ,sokf_static_movement,"ne2wall11d" ,"bo_newall7" , []),
    
  ("mm_woodenwall1" ,sokf_static_movement,"woodenwall1" ,"bo_woodenwall1" , []),
  ("mm_woodenwall1d" ,sokf_static_movement,"woodenwall1d" ,"bo_woodenwall1d" , []),
  ("mm_woodenwall2" ,sokf_static_movement,"woodenwall2" ,"bo_woodenwall2" , []),
  ("mm_woodenwall2d" ,sokf_static_movement,"woodenwall2d" ,"bo_woodenwall2d" , []),
  ("mm_woodenwall3" ,sokf_static_movement,"woodenwall3" ,"bo_woodenwall3" , []),
  ("mm_woodenwall3d" ,sokf_static_movement,"woodenwall3d" ,"bo_woodenwall3d" , []),
    
  ("mm_woodenwallsnowy1" ,sokf_static_movement,"woodenwallsnowy1" ,"bo_woodenwallsnowy1" , []),
  ("mm_woodenwallsnowy1d" ,sokf_static_movement,"woodenwallsnowy1d" ,"bo_woodenwall1d" , []),
  ("mm_woodenwallsnowy2" ,sokf_static_movement,"woodenwallsnowy2" ,"bo_woodenwallsnowy2" , []),
  ("mm_woodenwallsnowy2d" ,sokf_static_movement,"woodenwallsnowy2d" ,"bo_woodenwallsnowy2d" , []),
  ("mm_woodenwallsnowy3" ,sokf_static_movement,"woodenwallsnowy3" ,"bo_woodenwallsnowy3" , []),
  ("mm_woodenwallsnowy3d" ,sokf_static_movement,"woodenwallsnowy3d" ,"bo_woodenwallsnowy3d" , []),
    
  ("mm_sp_rich_bridge4" ,sokf_static_movement|sokf_dont_move_agent_over,"sp_rich_village_bridge13" ,"bo_sp_rich_village_bridge13" , []),
  ("mm_sp_rich_bridge1", sokf_static_movement|sokf_dont_move_agent_over, "sp_rich_village_bridge1", "bo_sp_rich_village_bridge1" , []),
  ("mm_sp_rich_bridge2", sokf_static_movement|sokf_dont_move_agent_over, "sp_rich_village_bridge11", "bo_sp_rich_village_bridge11" , []),
  ("mm_sp_rich_bridge3", sokf_static_movement|sokf_dont_move_agent_over, "sp_rich_village_bridge12", "bo_sp_rich_village_bridge12" , []),

  ("mm_stakes" ,sokf_static_movement|sokf_dont_move_agent_over,"stackes" ,"stackes_collision" , []),
    ("mm_stakes_destructible", sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible, "stackes" , "stackes_collision" , 
     [
       check_common_constructable_prop_on_hit_trigger,
       check_common_destructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),
    ("mm_stakes2_destructible", sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible, "mmstackes" , "bo_mmstackes" , 
     [
       check_common_constructable_prop_on_hit_trigger,
       check_common_destructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),
    ("sandbags_destructible", sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible, "sandbags" , "bo_sandbags" , 
     [
       check_common_constructable_prop_on_hit_trigger,
       check_common_destructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),
    ("chevaux_de_frise_tri_destructible", sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible, "chevaux_de_frise_tri" , "bo_chevaux_de_frise_tri" , 
     [
       check_common_constructable_prop_on_hit_trigger,
       check_common_destructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),
    
    ("gabiondeploy_destructible", sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible, "gabiondeploy" , "bo_gabiondeploy" , 
     [
       check_common_constructable_prop_on_hit_trigger,
       check_common_destructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),
    
    ("mm_fence1", sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible, "mmfence1", "bo_mmfence1" ,
    [    
       check_common_constructable_prop_on_hit_trigger,
       check_common_destructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),
    
    ("plank_destructible2" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"mm_plank1" ,"bo_mm_plank1" ,
    [
       check_common_constructable_prop_on_hit_trigger,
       check_common_constructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),
    
    ("earthwork1_destructible", sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible, "earthwork1" ,"bo_earthwork1" , 
     [
       check_common_constructable_prop_on_hit_trigger,
       check_common_destructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),

    ("mm_destructible_pioneer_builds_end", 0,"0" ,"0" , []),
    
    ("plank_destructible" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"mm_plank1" ,"bo_mm_plank1" ,
    [
       check_common_constructable_prop_on_hit_trigger,
       check_common_constructible_props_destroy_trigger,
       (ti_on_scene_prop_use,[]),
    ]),

  ("mm_pontoon_bridge_short" ,sokf_static_movement|sokf_dont_move_agent_over,"pontoon_deploy_short" ,"bo_pontoon_deploy_short" , []),
  ("mm_pontoon_bridge_med" ,sokf_static_movement|sokf_dont_move_agent_over,"pontoon_deploy_med" ,"bo_pontoon_deploy_med" , []),
  ("mm_pontoon_bridge_long" ,sokf_static_movement|sokf_dont_move_agent_over,"pontoon_deploy_long" ,"bo_pontoon_deploy_long" , []),

  ("mm_watchtower" ,sokf_static_movement|sokf_dont_move_agent_over,"deploy_watchtower" ,"bo_deploy_watchtower" , []),

  ("mm_dummy",sokf_static_movement|sokf_show_hit_point_bar|sokf_destructible,"mm_dummy","bo_arena_archery_target_b",   [
    check_common_dummy_destroy_trigger,
    check_common_dummy_on_hit_trigger,
  ]),

  ("crate_explosive_fra" ,sokf_static_movement|sokf_dont_move_agent_over|spr_use_time(2),"barreltriangulated_fra" ,"barreltriangulated_collision" , [check_common_explosive_crate_use_trigger,]),
  ("crate_explosive_ger" ,sokf_static_movement|sokf_dont_move_agent_over|spr_use_time(2),"barreltriangulated_prus" ,"barreltriangulated_collision" , [check_common_explosive_crate_use_trigger,]),
  ("crate_explosive_rus" ,sokf_static_movement|sokf_dont_move_agent_over|spr_use_time(2),"barreltriangulated_rus" ,"barreltriangulated_collision" , [check_common_explosive_crate_use_trigger,]),
  ("crate_explosive_brit" ,sokf_static_movement|sokf_dont_move_agent_over|spr_use_time(2),"barreltriangulated_brit" ,"barreltriangulated_collision" , [check_common_explosive_crate_use_trigger,]),

  ("mm_bird",sokf_static_movement|sokf_destructible,"birdmodel" ,"bo_birdmodel",
     [
       (ti_on_scene_prop_destroy,
        [
          (try_begin),
            (this_or_next|multiplayer_is_server),
            (neg|game_in_multiplayer_mode),
            (store_trigger_param_1, ":instance_no"),
            (prop_instance_get_position, pos1, ":instance_no"),
            (particle_system_burst, "psys_dummy_straw", pos1, 70),
            (particle_system_burst, "psys_bird_blood", pos1, 70),
            (call_script,"script_clean_up_prop_instance",":instance_no"),
          (try_end),
        ]),
  ]),

  ("mm_house_wall_2dd" ,sokf_static_movement,"2ddwall" ,"bo_2ddwall" , []),
    ("mm_house_wall_2ddd" ,sokf_static_movement,"2dddwall" ,"bo_2dddwall" , []),
    ("mm_house_wall_3dd" ,sokf_static_movement,"3ddwall" ,"bo_3ddwall" , []),
    ("mm_house_wall_3ddd" ,sokf_static_movement,"3dddwall" ,"bo_3dddwall" , []),
    ("mm_house_wall_4dd" ,sokf_static_movement,"4ddwall" ,"bo_4ddwall" , []),
    ("mm_house_wall_4ddd" ,sokf_static_movement,"4dddwall" ,"bo_4dddwall" , []),
    ("mm_house_wall_5dd" ,sokf_static_movement,"5ddwall" ,"bo_5ddwall" , []),
    ("mm_house_wall_5ddd" ,sokf_static_movement,"5dddwall" ,"bo_5dddwall" , []),
    ("mm_house_wall_6dd" ,sokf_static_movement,"6ddwall" ,"bo_6ddwall" , []),
    ("mm_house_wall_6ddd" ,sokf_static_movement,"6dddwall" ,"bo_6dddwall" , []),
    ("mm_house_wall_7dd" ,sokf_static_movement,"7ddwall" ,"bo_7ddwall" , []),
    ("mm_house_wall_7ddd" ,sokf_static_movement,"7dddwall" ,"bo_7dddwall" , []),
    ("mm_house_wall_11dd" ,sokf_static_movement,"11ddwall" ,"bo_11ddwall" , []),
    ("mm_house_wall_11ddd" ,sokf_static_movement,"11dddwall" ,"bo_11dddwall" , []),
    ("mm_house_wall_21dd" ,sokf_static_movement,"21ddwall" ,"bo_21ddwall" , []),
    ("mm_house_wall_21ddd" ,sokf_static_movement,"21dddwall" ,"bo_21dddwall" , []),
    ("mm_house_wall_31dd" ,sokf_static_movement,"31ddwall" ,"bo_31ddwall" , []),
    ("mm_house_wall_31ddd" ,sokf_static_movement,"31dddwall" ,"bo_31dddwall" , []),
    ("mm_house_wall_41dd" ,sokf_static_movement,"41ddwall" ,"bo_41ddwall" , []),
    ("mm_house_wall_41ddd" ,sokf_static_movement,"41dddwall" ,"bo_41dddwall" , []),
    ("mm_house_wall_51dd" ,sokf_static_movement,"51ddwall" ,"bo_51ddwall" , []),
    ("mm_house_wall_51ddd" ,sokf_static_movement,"51dddwall" ,"bo_51dddwall" , []),
    ("mm_house_wall_61dd" ,sokf_static_movement,"61ddwall" ,"bo_61ddwall" , []),
    ("mm_house_wall_61ddd" ,sokf_static_movement,"61dddwall" ,"bo_61dddwall" , []),
    ("mm_house_wall_71dd" ,sokf_static_movement,"71ddwall" ,"bo_71ddwall" , []),
    ("mm_house_wall_71ddd" ,sokf_static_movement,"71dddwall" ,"bo_71dddwall" , []),
    
    ("mm_wall2" ,sokf_static_movement,"wall2" ,"wall2_collision" , []),
    ("mm_walldesert2" ,sokf_static_movement,"desertWall1ddd" ,"bo_desertWall1ddd" , []),
    ("mm_wallwood2" ,sokf_static_movement,"woodWall1ddd" ,"bo_woodWall1ddd" , []),
    ("mm_wall_destoyed" ,sokf_static_movement,"wall_destoyed" ,"wall_destoyed_collision" , []),
    
    ("fortnew9", sokf_static_movement|sokf_dont_move_agent_over, "fortnew9", "bo_fortnew9" , []),
    ("fortnew_111", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_111", "bo_fortnew_111" , []),
    ("fortnew_29", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_29", "bo_fortnew_29" , []),
    ("fortnew_39", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_39", "bo_fortnew_39" , []),
    ("fortnew_41", sokf_static_movement|sokf_dont_move_agent_over, "fortnew_41", "bo_fortnew_41" , []),
    
    ("mm_new_wall_1_1dd" ,sokf_static_movement,"newall1dd" ,"bo_newall1dd" , []),
    ("mm_new_wall_1_1ddd" ,sokf_static_movement,"newall1ddd" ,"bo_newall1ddd" , []),
    ("mm_new_wall_1_2dd" ,sokf_static_movement,"newall2dd" ,"bo_newall2dd" , []),
    ("mm_new_wall_1_2ddd" ,sokf_static_movement,"newall2ddd" ,"bo_newall2ddd" , []),
    ("mm_new_wall_1_3dd" ,sokf_static_movement,"newall3dd" ,"bo_newall3dd" , []),
    ("mm_new_wall_1_3ddd" ,sokf_static_movement,"newall3ddd" ,"bo_newall3ddd" , []),
    ("mm_new_wall_1_4dd" ,sokf_static_movement,"newall4dd" ,"bo_newall4dd" , []),
    ("mm_new_wall_1_4ddd" ,sokf_static_movement,"newall4ddd" ,"bo_newall4ddd" , []),
    ("mm_new_wall_1_5dd" ,sokf_static_movement,"newall5dd" ,"bo_newall5dd" , []),
    ("mm_new_wall_1_5ddd" ,sokf_static_movement,"newall5ddd" ,"bo_newall5ddd" , []),
    ("mm_new_wall_1_6dd" ,sokf_static_movement,"newall6dd" ,"bo_newall6dd" , []),
    ("mm_new_wall_1_6ddd" ,sokf_static_movement,"newall6ddd" ,"bo_newall6ddd" , []),
    ("mm_new_wall_1_7dd" ,sokf_static_movement,"newall7dd" ,"bo_newall7dd" , []),
    ("mm_new_wall_1_7ddd" ,sokf_static_movement,"newall7ddd" ,"bo_newall7ddd" , []),
    ("mm_new_wall_1_8dd" ,sokf_static_movement,"newall8dd" ,"bo_newall8dd" , []),
    ("mm_new_wall_1_8ddd" ,sokf_static_movement,"newall8ddd" ,"bo_newall8ddd" , []),
    ("mm_new_wall_1_9dd" ,sokf_static_movement,"newall9dd" ,"bo_newall9dd" , []),
    ("mm_new_wall_1_9ddd" ,sokf_static_movement,"newall9ddd" ,"bo_newall9ddd" , []),
    ("mm_new_wall_1_10dd" ,sokf_static_movement,"newall10dd" ,"bo_newall10dd" , []),
    ("mm_new_wall_1_10ddd" ,sokf_static_movement,"newall10ddd" ,"bo_newall10ddd" , []),
    ("mm_new_wall_1_11dd" ,sokf_static_movement,"newall11dd" ,"bo_newall11dd" , []),
    ("mm_new_wall_1_11ddd" ,sokf_static_movement,"newall11ddd" ,"bo_newall11ddd" , []),
    
    ("mm_new_wall_2_1dd" ,sokf_static_movement,"ne1wall1dd" ,"bo_newall1dd" , []),
    ("mm_new_wall_2_1ddd" ,sokf_static_movement,"ne1wall1ddd" ,"bo_newall1ddd" , []),
    ("mm_new_wall_2_2dd" ,sokf_static_movement,"ne1wall2dd" ,"bo_newall2dd" , []),
    ("mm_new_wall_2_2ddd" ,sokf_static_movement,"ne1wall2ddd" ,"bo_newall2ddd" , []),
    ("mm_new_wall_2_3dd" ,sokf_static_movement,"ne1wall3dd" ,"bo_newall3dd" , []),
    ("mm_new_wall_2_3ddd" ,sokf_static_movement,"ne1wall3ddd" ,"bo_newall3ddd" , []),
    ("mm_new_wall_2_4dd" ,sokf_static_movement,"ne1wall4dd" ,"bo_newall4dd" , []),
    ("mm_new_wall_2_4ddd" ,sokf_static_movement,"ne1wall4ddd" ,"bo_newall4ddd" , []),
    ("mm_new_wall_2_5dd" ,sokf_static_movement,"ne1wall5dd" ,"bo_newall5dd" , []),
    ("mm_new_wall_2_5ddd" ,sokf_static_movement,"ne1wall5ddd" ,"bo_newall5ddd" , []),
    ("mm_new_wall_2_6dd" ,sokf_static_movement,"ne1wall6dd" ,"bo_newall6dd" , []),
    ("mm_new_wall_2_6ddd" ,sokf_static_movement,"ne1wall6ddd" ,"bo_newall6ddd" , []),
    ("mm_new_wall_2_7dd" ,sokf_static_movement,"ne1wall7dd" ,"bo_newall7dd" , []),
    ("mm_new_wall_2_7ddd" ,sokf_static_movement,"ne1wall7ddd" ,"bo_newall7ddd" , []),
    ("mm_new_wall_2_8dd" ,sokf_static_movement,"ne1wall8dd" ,"bo_newall8dd" , []),
    ("mm_new_wall_2_8ddd" ,sokf_static_movement,"ne1wall8ddd" ,"bo_newall8ddd" , []),
    ("mm_new_wall_2_9dd" ,sokf_static_movement,"ne1wall9dd" ,"bo_newall9dd" , []),
    ("mm_new_wall_2_9ddd" ,sokf_static_movement,"ne1wall9ddd" ,"bo_newall9ddd" , []),
    ("mm_new_wall_2_10dd" ,sokf_static_movement,"ne1wall10dd" ,"bo_newall10dd" , []),
    ("mm_new_wall_2_10ddd" ,sokf_static_movement,"ne1wall10ddd" ,"bo_newall10ddd" , []),
    ("mm_new_wall_2_11dd" ,sokf_static_movement,"ne1wall11dd" ,"bo_newall11dd" , []),
    ("mm_new_wall_2_11ddd" ,sokf_static_movement,"ne1wall11ddd" ,"bo_newall11ddd" , []),
    
    ("mm_new_wall_3_1dd" ,sokf_static_movement,"ne2wall1dd" ,"bo_newall1dd" , []),
    ("mm_new_wall_3_1ddd" ,sokf_static_movement,"ne2wall1ddd" ,"bo_newall1ddd" , []),
    ("mm_new_wall_3_2dd" ,sokf_static_movement,"ne2wall2dd" ,"bo_newall2dd" , []),
    ("mm_new_wall_3_2ddd" ,sokf_static_movement,"ne2wall2ddd" ,"bo_newall2ddd" , []),
    ("mm_new_wall_3_3dd" ,sokf_static_movement,"ne2wall3dd" ,"bo_newall3dd" , []),
    ("mm_new_wall_3_3ddd" ,sokf_static_movement,"ne2wall3ddd" ,"bo_newall3ddd" , []),
    ("mm_new_wall_3_4dd" ,sokf_static_movement,"ne2wall4dd" ,"bo_newall4dd" , []),
    ("mm_new_wall_3_4ddd" ,sokf_static_movement,"ne2wall4ddd" ,"bo_newall4ddd" , []),
    ("mm_new_wall_3_5dd" ,sokf_static_movement,"ne2wall5dd" ,"bo_newall5dd" , []),
    ("mm_new_wall_3_5ddd" ,sokf_static_movement,"ne2wall5ddd" ,"bo_newall5ddd" , []),
    ("mm_new_wall_3_6dd" ,sokf_static_movement,"ne2wall6dd" ,"bo_newall6dd" , []),
    ("mm_new_wall_3_6ddd" ,sokf_static_movement,"ne2wall6ddd" ,"bo_newall6ddd" , []),
    ("mm_new_wall_3_7dd" ,sokf_static_movement,"ne2wall7dd" ,"bo_newall7dd" , []),
    ("mm_new_wall_3_7ddd" ,sokf_static_movement,"ne2wall7ddd" ,"bo_newall7ddd" , []),
    ("mm_new_wall_3_8dd" ,sokf_static_movement,"ne2wall8dd" ,"bo_newall8dd" , []),
    ("mm_new_wall_3_8ddd" ,sokf_static_movement,"ne2wall8ddd" ,"bo_newall8ddd" , []),
    ("mm_new_wall_3_9dd" ,sokf_static_movement,"ne2wall9dd" ,"bo_newall9dd" , []),
    ("mm_new_wall_3_9ddd" ,sokf_static_movement,"ne2wall9ddd" ,"bo_newall9ddd" , []),
    ("mm_new_wall_3_10dd" ,sokf_static_movement,"ne2wall10dd" ,"bo_newall10dd" , []),
    ("mm_new_wall_3_10ddd" ,sokf_static_movement,"ne2wall10ddd" ,"bo_newall10ddd" , []),
    ("mm_new_wall_3_11dd" ,sokf_static_movement,"ne2wall11dd" ,"bo_newall11dd" , []),
    ("mm_new_wall_3_11ddd" ,sokf_static_movement,"ne2wall11ddd" ,"bo_newall11ddd" , []),
	
    ("mm_woodenwall1dd" ,sokf_static_movement,"woodenwall1dd" ,"bo_woodenwall1dd" , []),
    ("mm_woodenwallsnowy1dd" ,sokf_static_movement,"woodenwallsnowy1dd" ,"bo_woodenwallsnowy1dd" , []),
  
    ("mm_sp_poor_bridge1d" ,sokf_static_movement,"sp_poor_village_bridge1d" ,"bo_sp_poor_village_bridge1d" , []),
    ("mm_sp_rich_bridge2d" ,sokf_static_movement,"sp_rich_village_bridge11d" ,"bo_sp_rich_village_bridge11d" , []),
    ("mm_sp_rich_bridge3d", sokf_static_movement, "sp_rich_village_bridge12d", "bo_sp_rich_village_bridge12d" , []),

    ("mm_sp_rich_bridge4d" ,sokf_static_movement,"sp_rich_village_bridge13d" ,"bo_sp_rich_village_bridge13d" , []),
    
    ("mm_stockade_cannon_destroyed" ,sokf_static_movement,"stockade_cannon_destroyed" ,"stockade_cannon_destroyed_collision" , []),
    ("mm_stockade_destroyed" ,sokf_static_movement,"stockade_destroyed" ,"stockade_destroyed_collision" , []),
    ("mm_stakes_destroyed" ,sokf_static_movement,"stackes_destroyed" ,"0" , []),
    ("mm_stakes2_destroyed" ,sokf_static_movement,"mmstackesd" ,"bo_mmstackesd" , []),
    ("mm_dummy_destroyed",sokf_static_movement,"mm_dummy_destroyed","0", []),

    #Buildable/repairable palisade
    ("mm_palisadedd" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"mmpalisadedd" ,"bo_mmpalisadedd" , [
      check_common_constructable_prop_on_hit_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    #Short
    ("mm_constr_pontoon_short" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"pontoon_construct" ,"bo_pontoon_construct" , [
      check_common_constructable_prop_on_hit_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    #Med
    ("mm_constr_pontoon_med" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"pontoon_construct" ,"bo_pontoon_construct" , [
      check_common_constructable_prop_on_hit_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    #Long
    ("mm_constr_pontoon_long" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"pontoon_construct" ,"bo_pontoon_construct" , [
      check_common_constructable_prop_on_hit_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    #Watchtower contruct
    ("mm_constr_watchtower" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"watchtower_construct" ,"bo_watchtower_construct" , [
      check_common_constructable_prop_on_hit_trigger,
      (ti_on_scene_prop_use,[]),
    ]),

  ("mm_stakes_construct",sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"stackes_destroyed" ,"bo_stackes_destroyed" , [
      check_common_constructable_prop_on_hit_trigger,
      check_common_constructible_props_destroy_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    ("mm_stakes2_construct" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"mmstackesd" ,"bo_mmstackesd" , [  
      check_common_constructable_prop_on_hit_trigger,
      check_common_constructible_props_destroy_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    ("sandbags_construct" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"sandbags_destroy" ,"bo_sandbags_destroy" , [  
      check_common_constructable_prop_on_hit_trigger,
      check_common_constructible_props_destroy_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    ("chevaux_de_frise_tri_construct" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"chevaux_de_frise_tri_destroy" ,"bo_chevaux_de_frise_tri_destroy" , [  
      check_common_constructable_prop_on_hit_trigger,
      check_common_constructible_props_destroy_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    ("gabiondeploy_construct" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"hanskopf" ,"bo_hanskopf" , [
      check_common_constructable_prop_on_hit_trigger,
      check_common_constructible_props_destroy_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    ("mm_fence1d" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"mmfence1d" ,"bo_mmfence1d" , [
      check_common_constructable_prop_on_hit_trigger,
      check_common_constructible_props_destroy_trigger,
      (ti_on_scene_prop_use,[]),
    ]),
    ("plank_construct_dummy" ,sokf_static_movement|sokf_dont_move_agent_over|sokf_show_hit_point_bar|sokf_destructible,"mm_plank1" ,"bo_mm_plank1" , [
      check_common_constructable_prop_on_hit_trigger,
      (ti_on_scene_prop_use,[]),
      ]),
    ("earthwork1_construct_dummy" ,sokf_static_movement,"earthwork1" ,"bo_earthwork1" , [  
      check_common_constructable_prop_on_hit_trigger,
      check_common_constructible_props_destroy_trigger,
      (ti_on_scene_prop_use,[]),]),
    ("crate_explosive" ,sokf_static_movement,"barreltriangulated" ,"barreltriangulated_collision" , []),

  ("mm_crator_small",sokf_static_movement,"crator_small","0", []),
  ("mm_crator_crator_medium_very_small",sokf_static_movement,"crator_medium_very_small","0", []),
  ("mm_crator_medium_small",sokf_static_movement,"crator_medium_small","0", []),
  ("mm_crator_medium",sokf_static_movement,"crator_medium","0", []),
  ("mm_crator_big_medium",sokf_static_movement,"crator_big_medium","0", []),
  ("mm_crator_big",sokf_static_movement,"crator_big","0", []),
  ("mm_crator_explosion",sokf_static_movement,"crator_explosion","0", []),

  ("mm_wall_wood_planks1",sokf_static_movement,"splinters","0", []),
  ("mm_wall_wood_planks2",sokf_static_movement,"splinters2","0", []),
  ("mm_wall_wood_planks3",sokf_static_movement,"splinters3","0", []),
  ("mm_wall_stones1",sokf_static_movement,"wall_stones1","0", []),
  ("mm_wall_stones2",sokf_static_movement,"wall_stones2","0", []),
  ("mm_wall_stones3",sokf_static_movement,"wall_stones3","0", []),
  ("mm_wall_stones4",sokf_static_movement,"wall_stones4","0", []),
  ("mm_wall_stonesdesert1",sokf_static_movement,"desertBricks1","0", []),
  ("mm_wall_stonesdesert2",sokf_static_movement,"desertBricks2","0", []),

  ("mm_wallgate" ,0,"wallgate" ,"wallgate_collision" , []),
	  ("mm_walldesertgatedesert" ,0,"desertWallGatehouse" ,"bo_desertWallGatehouse" , []),
	  ("mm_wallwoodgatewood" ,0,"woodWallGatehouse" ,"bo_woodWallGatehouse" , []),
    ("mm_gunrack" ,0,"gunrack" ,"gunrack_collision" , []),
    ("mm_lantern" ,0,"lantern" ,"0" , []),
    ("mm_table1" ,0,"table1" ,"table1_collision" , []),
    ("mm_cupboard1" ,0,"cupboard1" ,"cupboard1_collision" , []),
    ("mm_cupboard2" ,0,"cupboard2" ,"bo_cupboard2" , []),
    ("mm_cupboard3" ,0,"cupboard3" ,"bo_cupboard3" , []),
    ("mm_french_barrel" ,0,"barreltriangulated" ,"barreltriangulated_collision" , []),
    ("mm_brit_barrel" ,0,"barreltriangulated_brit" ,"barreltriangulated_collision" , []),
    ("mm_coffin" ,0,"coffin" ,"coffin_collision" , []),
    ("mm_grave1" ,0,"grave1" ,"0" , []),
    ("mm_grave2" ,0,"grave2" ,"0" , []),
    ("mm_restroom" ,0,"restroom" ,"restroom_collision" , []),
    ("mm_sign" ,0,"sign" ,"sign_collision" , []),
    ("mm_bed" ,0,"bed" ,"bed_collision" , []),
    ("mm_chair1" ,0,"chair1" ,"chair_collision" , []),
    ("mm_little_table" ,0,"little_table" ,"little_table_collision" , []),
    ("mm_little_table2" ,0,"little_table2" ,"little_table2_collision" , []),
    ("mm_bank1" ,0,"bank" ,"bank_collision" , []),
    ("mm_crate1" ,0,"crate1" ,"bo_crate" , []),
    ("mm_crate2" ,0,"crate2" ,"bo_crate" , []),
    ("mm_wall82" ,0,"wall82" ,"wall82_collision" , []),
	("mm_walldesert82" ,0,"desertWall82" ,"bo_desertWall82" , []),
	("mm_wallwood82" ,0,"woodWall82" ,"bo_woodWall82" , []),
    ("mm_wall84" ,0,"wall84" ,"wall84_collision" , []),
    ("mm_fountain1" ,0,"brunnen" ,"brunnen_collision" , []),
    ("mm_fireplace1" ,0,"camin" ,"camin_collision" , []),
    ("mm_fireplace2" ,0,"camin2" ,"camin2_collision" , []),
    ("mm_bookcase" ,0,"bookcase" ,"bookcase_collision" , []),

  ("mm_piano",spr_use_time(0),"piano","bo_piano",
    [
      (ti_on_scene_prop_use,
      [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":instance_id"),
        
        (agent_is_active,":agent_id"),
        (agent_is_alive,":agent_id"),
        (agent_get_player_id,":player_id",":agent_id"),
        (player_is_active,":player_id"),
        (prop_instance_is_valid,":instance_id"),
        (assign,":in_use",0),
        (try_for_agents, ":cur_agent"),
          (agent_is_active,":cur_agent"),
          (agent_is_alive,":cur_agent"),
          (agent_get_slot,":cur_inst",":cur_agent",slot_agent_used_prop_instance),
          (eq,":cur_inst",":instance_id"), # same prop
          (neq,":cur_agent",":agent_id"), # and not meself
          (assign,":in_use",1),
        (try_end),
        (try_begin),
          (eq,":in_use",0),
          (call_script,"script_multiplayer_server_agent_stop_music",":agent_id"),
          (try_begin),
            (agent_get_horse, ":player_horse", ":agent_id"),
            (le, ":player_horse", 0),
            (try_begin),
              (set_fixed_point_multiplier, 100),
              (agent_get_position,pos33,":agent_id"),
              (prop_instance_get_position, pos40, ":instance_id"),
              (position_move_y,pos40,-200),
              (get_distance_between_positions,":dist",pos33,pos40),
              (lt, ":dist", 280),
              (prop_instance_get_scene_prop_kind,":prop_kind",":instance_id"),
              (agent_set_slot, ":agent_id", slot_agent_used_prop_instance, ":instance_id"),
              (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_return_server_action, server_action_force_music_selection, ":prop_kind"),
            (else_try),
              (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_show_multiplayer_message, multiplayer_message_type_error, "str_cannot_use_piano_angle"),
            (try_end),
          (else_try),
            (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_show_multiplayer_message, multiplayer_message_type_error, "str_cannot_use_piano"),
          (try_end),
        (else_try),
          (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_show_multiplayer_message, multiplayer_message_type_error, "str_piano_in_use"),
        (try_end)
      ]),
    ]),
    ("mm_organ",spr_use_time(0),"organ","bo_organ",
    [
      (ti_on_scene_prop_use,
      [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":instance_id"),
        
        (agent_is_active,":agent_id"),
        (agent_is_alive,":agent_id"),
        (agent_get_player_id,":player_id",":agent_id"),
        (player_is_active,":player_id"),
        
        (prop_instance_is_valid,":instance_id"),
        
        (assign,":in_use",0),
        (try_for_agents, ":cur_agent"),
          (agent_is_active,":cur_agent"),
          (agent_is_alive,":cur_agent"),
          (agent_get_slot,":cur_inst",":cur_agent",slot_agent_used_prop_instance),
          (eq,":cur_inst",":instance_id"), # same prop
          (neq,":cur_agent",":agent_id"), # and not meself
          (assign,":in_use",1),
        (try_end),
        
        # not in use by a other player.
        (try_begin),
          (eq,":in_use",0),
          
          # Always stop first.
          (call_script,"script_multiplayer_server_agent_stop_music",":agent_id"),
          
          # not on horseback
          (try_begin),
            (agent_get_horse, ":player_horse", ":agent_id"),
            (le, ":player_horse", 0),
            
            (try_begin),
              (set_fixed_point_multiplier, 100),
              
              (agent_get_position,pos33,":agent_id"),
              (prop_instance_get_position, pos40, ":instance_id"),
              
              (position_move_y,pos40,-250),
              (get_distance_between_positions,":dist",pos33,pos40),
              
              (lt, ":dist", 280),
              
              #(get_angle_between_positions, ":rotation", pos33, pos40),
              
            
              (prop_instance_get_scene_prop_kind,":prop_kind",":instance_id"),
              (agent_set_slot, ":agent_id", slot_agent_used_prop_instance, ":instance_id"),
              
              (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_return_server_action, server_action_force_music_selection, ":prop_kind"),
            (else_try),
              (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_show_multiplayer_message, multiplayer_message_type_error, "str_cannot_use_piano_angle"),
            (try_end),
          (else_try),
            (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_show_multiplayer_message, multiplayer_message_type_error, "str_cannot_use_organ"),
          (try_end),
        (else_try),
          (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_show_multiplayer_message, multiplayer_message_type_error, "str_organ_in_use"),
        (try_end),
      ]),
    ]),
    
    ("mm_shithouse_button",spr_use_time(1),"0","cannon_button_collision",
    [
      (ti_on_scene_prop_use,
      [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":instance_id"),
        
        (agent_is_active,":agent_id"),
        (agent_is_alive,":agent_id"),
        (agent_get_player_id,":player_id",":agent_id"),
        (player_is_active,":player_id"),
        
        (prop_instance_is_valid,":instance_id"),
        
        (assign,":in_use",0),
        (try_for_agents, ":cur_agent"),
          (agent_is_active,":cur_agent"),
          (agent_is_alive,":cur_agent"),
          (agent_get_slot,":cur_inst",":cur_agent",slot_agent_used_prop_instance),
          (eq,":cur_inst",":instance_id"), # same prop
          (neq,":cur_agent",":agent_id"), # and not meself
          (assign,":in_use",1),
        (try_end),
        
        # not in use by a other player.
        (try_begin),
          (eq,":in_use",0),
          
          # not on horseback
          (try_begin),
            (agent_get_horse, ":player_horse", ":agent_id"),
            (le, ":player_horse", 0),
            
            (try_begin),
              (call_script,"script_cf_agent_is_taking_a_shit",":agent_id"),
              # we stopped shitting.
              (call_script,"script_multiplayer_server_agent_stop_music",":agent_id"),
            (else_try),
              (agent_set_slot, ":agent_id", slot_agent_used_prop_instance, ":instance_id"),
              
              (agent_set_animation,":agent_id","anim_shitting",0),
              
              (agent_set_wielded_item,":agent_id",-1),  
        
              # put player on stool.
              (prop_instance_get_position,pos5,":instance_id"),
              (position_move_x,pos5,30),
              (agent_set_position,":agent_id",pos5),
            (try_end),
          (else_try),
            (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_show_multiplayer_message, multiplayer_message_type_error, "str_cannot_use_toilet"),
          (try_end),
        (else_try),
          (multiplayer_send_2_int_to_player, ":player_id", multiplayer_event_show_multiplayer_message, multiplayer_message_type_error, "str_toilet_in_use"),
        (try_end),
      ]),
    ]),
    
    ("mm_ammobox_cannon", sokf_static_movement|sokf_dont_move_agent_over, "ammobox_cannon" , "bo_ammobox", []),
    ("mm_ammobox_howitzer", sokf_static_movement|sokf_dont_move_agent_over, "ammobox_howitzer" , "bo_ammobox", []),
    
    ("mm_tent1",0,"mm_tent1","bo_mmtent1", []),
    ("mm_wood_heap1",0,"mm_wood_heap1","bo_mm_wood_heap1", []),
    ("mm_wood_heap2",0,"mm_wood_heap2","bo_mm_wood_heap2", []),
    ("mm_wood_heap3",0,"mm_wood_heap3","bo_mm_wood_heap3", []),
    ("mm_shrine",0,"mmshrine","bo_shrine", []),
    ("mm_shrine1",0,"mmshrine1","bo_shrine", []),
    ("mm_shrine2",0,"mmshrine2","bo_shrine", []),
    ("mm_shrine3",0,"mmshrine3","bo_shrine", []),
    ("mm_shrine4",0,"mmshrine4","bo_shrine", []),
    ("mm_arc",0,"arc","bo_arc", []),
    
    ("mm_redoubt1",0,"mmredoubts1","bo_mmredoubts1", []),
    ("mm_redoubt2",0,"mmredoubts2","bo_mmredoubts1", []),
    ("mm_redoubt3",0,"mmredoubts3","bo_mmredoubts1", []),
    ("mm_redoubt4",0,"mmredoubts4","bo_mmredoubts1", []),
    ("mm_redoubt5",0,"mmredoubts5","bo_mmredoubts1", []),
    ("mm_redoubt6",0,"mmredoubts6","bo_mmredoubts6", []),
    ("mm_redoubt7",0,"mmredoubts7","bo_mmredoubts6", []),
    ("mm_redoubt8",0,"mmredoubts8","bo_mmredoubts6", []),
    ("mm_redoubt9",0,"mmredoubts9","bo_mmredoubts6", []),
    
    ("mm_great_redoubt1",0,"greatredoubts","bo_greatredoubts", []),
    ("mm_great_redoubt2",0,"greatredoubts1","bo_greatredoubts", []),
    ("mm_smallredoubt1",0,"smallredoubts","bo_smallredoubts", []),
    ("mm_smallredoubt2",0,"smallredoubts1","bo_smallredoubts1", []),
    ("mm_smallredoubt3",0,"smallredoubts2","bo_smallredoubts1", []),
    ("mm_smallredoubt4",0,"smallredoubts3","bo_smallredoubts", []),

    ("mm_trenches1",0,"mmtrenches1","bo_mmtrenches1", []),
    ("mm_trenches2",0,"mmtrenches2","bo_mmtrenches2", []),
    
    ("mm_sp_small_fort",0,"testforts","bo_testforts", []),
    ("mm_sp_small_fort1",0,"testforts1","bo_testforts1", []),
    ("mm_sp_small_fort2",0,"testforts2","bo_testforts2", []),

    ("mm_sp_czech1",0,"czech","bo_czech", []),
    ("mm_sp_czech2",0,"czech1","bo_czech1", []),
    ("mm_sp_czech3",0,"czech2","bo_czech2", []),
    ("mm_sp_czech4",0,"czech3","bo_czech3", []),

  ("mm_oim_fortwall1",0,"euro_fort_wall_blasted","bo_euro_fort_wall_blasted", []),
    ("mm_oim_fortwall2",0,"euro_fort_wall","bo_euro_fort_wall", []),
    ("mm_oim_fortwall3",0,"euro_fort_stairs","bo_euro_fort_stairs", []),
    ("mm_oim_fortwall4",0,"euro_fort_gate_house","bo_euro_fort_gate_house", []),
    ("mm_oim_fortwall5",0,"euro_fort_tower","bo_euro_fort_tower", []),
    ("mm_oim_fortwall6",0,"euro_fort_tower_ugol","bo_euro_fort_tower_ugol", []),
    ("mm_oim_fortwall7",0,"euro_fort_wall_corner","bo_euro_fort_wall_corner", []),
    
    ("mm_oim_fortwall9",0,"euro_fort_wall_in","bo_euro_fort_wall_in", []),
    ("mm_oim_fortwall10",0,"euro_fort_wall_in_half","bo_euro_fort_wall_in_half", []),
    
    ("mm_oim_debris1",0,"zaval","bo_zaval", []),
    ("oim_church1",0,"oim_rus_wood_church_a","bo_oim_rus_wood_church_a", []),
    ("oim_church2",0,"polsc_chapel_1a","bo_pol_wood_church", []),
    ("oim_rus_house1",0,"rus_izba_c","bo_rus_izba_c", []),
    ("oim_rus_house2",0,"rus_izba_d","bo_rus_izba_d", []),
    ("oim_rus_house3",0,"rus_izba_e","bo_rus_izba_e", []),
    ("oim_rus_house4",0,"rus_izba_a","bo_rus_izba_a", []),
    ("oim_rus_house5",0,"rus_izba_b","bo_rus_izba_b", []),

    ("mm_sp_rich_house1",0,"sp_rich_village_houses1","bo_sp_rich_village_houses1", []),
    ("mm_sp_rich_house2",0,"sp_rich_village_houses2","bo_sp_rich_village_houses1", []),
    ("mm_sp_rich_house3",0,"sp_rich_village_houses3","bo_sp_rich_village_houses1", []),
    ("mm_sp_rich_house4",0,"sp_rich_village_houses4","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house5",0,"sp_rich_village_houses5","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house6",0,"sp_rich_village_houses6","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house7",0,"sp_rich_village_houses8","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house8",0,"sp_rich_village_houses9","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house9",0,"sp_rich_village_houses10","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house10",0,"sp_rich_village_houses11","bo_sp_rich_village_houses4", []),
    ("mm_sp_rich_house11",0,"sp_rich_village_houses12","bo_sp_rich_village_houses4", []),
    ("mm_sp_rich_house12",0,"sp_rich_village_houses13","bo_sp_rich_village_houses4", []),
    ("mm_sp_rich_church1",0,"sp_rich_village_houses7","bo_sp_rich_village_houses3", []),
    ("mm_sp_rich_street1",0,"sp_rich_village_street1","bo_sp_rich_village_street1", []),
    ("mm_sp_rich_street2",0,"sp_rich_village_street2","bo_sp_rich_village_street2", []),
    ("mm_sp_rich_street3",0,"sp_rich_village_street3","bo_sp_rich_village_street3", []),
    ("mm_sp_rich_street4",0,"sp_rich_village_street4","bo_sp_rich_village_street4", []),
    ("mm_sp_rich_street5",0,"sp_rich_village_street5","bo_sp_rich_village_street5", []),
   # ("mm_sp_rich_street6",0,"sp_rich_village_street6","bo_sp_rich_village_street6", []),
    ("mm_sp_poor_house6",0,"sp_poor_village_houses6","bo_sp_poor_village_houses6", []),
    ("mm_sp_poor_house7",0,"sp_poor_village_houses7","bo_sp_poor_village_houses7", []),
    ("mm_sp_poor_house9",0,"sp_poor_village_houses9","bo_sp_poor_village_houses9", []),
    ("mm_sp_poor_house10",0,"sp_poor_village_houses10","bo_sp_poor_village_houses10", []),
    ("mm_sp_poor_house11",0,"sp_poor_village_houses11","bo_sp_poor_village_houses11", []),

    
    ("mm_sp_rich_house14",0,"sp_rich_village_houses15","bo_sp_rich_village_houses1", []),
    ("mm_sp_rich_house15",0,"sp_rich_village_houses15","bo_sp_rich_village_houses1", []),
    ("mm_sp_rich_house16",0,"sp_rich_village_houses17","bo_sp_rich_village_houses1", []),
    ("mm_sp_rich_house17",0,"sp_rich_village_houses17","bo_sp_rich_village_houses1", []),
    ("mm_sp_rich_house18",0,"sp_rich_village_houses18","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house19",0,"sp_rich_village_houses19","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house20",0,"sp_rich_village_houses22","bo_sp_rich_village_houses4", []),
    ("mm_sp_rich_house21",0,"sp_rich_village_houses21","bo_sp_rich_village_houses4", []),
    ("mm_sp_rich_house22",0,"sp_rich_village_houses22","bo_sp_rich_village_houses4", []),
    ("mm_sp_rich_house23",0,"sp_rich_village_houses24","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house24",0,"sp_rich_village_houses24","bo_sp_rich_village_houses2", []),
    ("mm_sp_rich_house25",0,"sp_rich_village_houses25","bo_sp_rich_village_houses2", []),

    
    #Trenches
    ("mm_trench_straight",0,"mm_trench_straight","bo_mm_trench_straight", []),
    ("mm_trench_corner",0,"mm_trench_corner","bo_mm_trench_corner", []),
    ("mm_trench_curve",0,"mm_trench_curve","bo_mm_trench_curve", []),
    ("mm_trench_big_curve",0,"mm_trench_big_curve","bo_mm_trench_big_curve", []),
    ("mm_trench_cross",0,"mm_trench_cross","bo_mm_trench_cross", []),
    ("mm_trench_cross2",0,"mm_trench_cross2","bo_mm_trench_cross2", []),
    ("mm_trench_bastion",0,"mm_trench_bastion","bo_mm_trench_bastion", []),
    ("mm_trench_entrance1",0,"mm_trench_entrance1","bo_mm_trench_entrance1", []),
    ("mm_trench_entrance2",0,"mm_trench_entrance2","bo_mm_trench_entrance2", []),
    
    ("mm_brit_barrel_explosive" ,sokf_static_movement,"barreltriangulated_brit" ,"barreltriangulated_collision" , []),
    ("mm_french_barrel_explosive" ,sokf_static_movement|spr_use_time(2),"barreltriangulated" ,"barreltriangulated_collision" , [  
      (ti_on_scene_prop_use,
      [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":instance_id"),
        
        (scene_prop_get_slot,":cur_time",":instance_id",scene_prop_slot_time),
        (le,":cur_time",0),
        (scene_prop_set_slot,":instance_id", scene_prop_slot_time, 5), #Seconds until exploding
        (scene_prop_set_slot,":instance_id", scene_prop_slot_user_agent, ":agent_id"), #User agent
      ]),]),
    ("mm_prus_barrel_explosive" ,sokf_static_movement,"barreltriangulated_brit" ,"barreltriangulated_collision" , []),
    
    #("fans_end", 0,"0" ,"0" , []),
    #used as end fan!
    ("mm_cannon_aim_platform" ,sokf_static_movement|sokf_dont_move_agent_over,"0" ,"bo_gunplane_combined" , []), # test mesh: gunplane_combined
    
    # Cannon types for mappers to place on map, will be replaced with seperate bits.
    ("mm_cannon_12pdr" ,sokf_static_movement,"cannon_12pdr" ,"0" , []),
    ("mm_cannon_howitzer" ,sokf_static_movement,"cannon_howitzer" ,"0" , []),
    ("mm_cannon_mortar" ,sokf_static_movement,"cannon_mortar" ,"0" , []),
    ("mm_cannon_fort" ,sokf_static_movement,"cannon_fort" ,"0" , []),
    ("mm_cannon_naval" ,sokf_static_movement,"cannon_naval" ,"0" , []),
    ("mm_cannon_carronade" ,sokf_static_movement,"cannon_carronade" ,"0" , []),
    ("mm_cannon_swievel" ,sokf_static_movement,"cannon_swievel" ,"0" , []),
    ("mm_cannon_rocket" ,sokf_static_movement,"rocket_launcher" ,"0" , []),
    #("mm_cannons_end", 0,"0" ,"0" , []),
    
    # Used as cannons end!
    # Normal cannonballs for mappers
    ("mm_cannonball_6pd", 0, "cannonball_6pd" , "cannonball_collision" , []),
    ("mm_cannonball_12pd", 0, "cannonball_12pd" , "cannonball_collision" , []),
    ("mm_cannonball_24pd", 0, "cannonball_24pd" , "cannonball_collision" , []),
    ("mm_cannonball_36pd", 0, "cannonball_36pd" , "cannonball_collision" , []),
    ("mm_rocket", 0, "rocket_projectile" , "cannonball_collision" , []),
    
    # Static cannon bits.
    ("mm_cannon_mortar_static",sokf_static_movement,"cannon_mortar_wood_static","0",[]),
    ("mm_cannon_fort_static",sokf_static_movement,"cannon_fort_static","0",[]),
    ("mm_cannon_rocket_static",sokf_static_movement,"rocket_launcher_static","0",[]),
    
    # loaded ammo cannon bits.
    ("mm_cannon_mortar_loaded_ammo",sokf_static_movement,"mortar_cartdridge","0",[]),
    ("mm_cannon_rocket_loaded_ammo",sokf_static_movement,"rocket_projectile","0",[]),
    #("mm_loaded_ammos_end", 0, "0" , "0" , []),
    
    # used as loaded_ammo_end!
    # Code cannonballs for trajectory
    ("mm_cannonball_code_only_6pd",sokf_static_movement,"cannonball_6pd","0",[]),
    ("mm_cannonball_code_only_12pd",sokf_static_movement,"cannonball_12pd","0",[]),
    ("mm_cannonball_code_only_24pd",sokf_static_movement,"cannonball_24pd","0",[]),
    ("mm_cannonball_code_only_36pd",sokf_static_movement,"cannonball_36pd","0",[]),
    ("mm_rocket_code_only",sokf_static_movement, "rocket_projectile" , "0" , []),
    
    # Cannon bits :)
    ("mm_cannon_12pdr_wood",sokf_static_movement|sokf_dont_move_agent_over,"cannon_12pdr_wood","12wood_barrel",[check_cannon_animation_finished_trigger]),
    ("mm_cannon_howitzer_wood",sokf_static_movement|sokf_dont_move_agent_over,"cannon_howitzer_wood","howitzerwood_barrel",[check_cannon_animation_finished_trigger]),
    ("mm_cannon_mortar_wood" ,sokf_static_movement,"cannon_mortar_wood" ,"mortarwood" , []),
    ("mm_cannon_fort_wood" ,sokf_static_movement,"cannon_fort_movable" ,"0" , []),
    ("mm_cannon_naval_wood" ,sokf_static_movement,"cannon_naval_wood" ,"navalbarrel" , [check_cannon_animation_finished_trigger]),
    ("mm_cannon_carronade_wood" ,sokf_static_movement,"cannon_carronade_wood" ,"navalwheels" , []),
    ("mm_cannon_swievel_wood" ,sokf_static_movement,"cannon_swievel_wood" ,"0" , []),
    ("mm_cannon_rocket_wood" ,sokf_static_movement,"rocket_launcher_wood" ,"0" , []),
    
    ("mm_cannon_12pdr_wheels",sokf_static_movement,"cannon_12pdr_wheels","0",[]),
    ("mm_cannon_howitzer_wheels",sokf_static_movement,"cannon_12pdr_wheels","0",[]),
    ("mm_cannon_fort_wheels",sokf_static_movement,"cannon_fort_movable2","bo_cannon_fort",[check_cannon_wheels_animation_finished_trigger]),
    ("mm_cannon_naval_wheels",sokf_static_movement,"0","0",[]),
    
    ("mm_cannon_12pdr_barrel" ,sokf_static_movement,"cannon_12pdr_barrel" ,"0" , []),
    ("mm_cannon_howitzer_barrel" ,sokf_static_movement,"cannon_howitzer_barrel" ,"0" , []),
    ("mm_cannon_mortar_barrel" ,sokf_static_movement,"cannon_mortar_barrel" ,"0" , []),
    ("mm_cannon_fort_barrel" ,sokf_static_movement,"cannon_fort_barrel" ,"0" , []),
    ("mm_cannon_naval_barrel" ,sokf_static_movement,"cannon_naval_barrel" ,"0" , []),
    ("mm_cannon_carronade_barrel" ,sokf_static_movement,"cannon_carronade_barrel" ,"0" , []),
    ("mm_cannon_swievel_barrel" ,sokf_static_movement,"cannon_swievel_barrel" ,"0" , []),
    ("mm_cannon_rocket_barrel" ,sokf_static_movement,"rocket_launcher_barrel" ,"0" , []),
    
    ("mm_cannon_12pdr_limber_wheels",sokf_static_movement,"cannon_12pdr_limber_wheels","0",[]),
    ("mm_cannon_howitzer_limber_wheels",sokf_static_movement,"cannon_12pdr_limber_wheels","0",[]),
    
    # Limber part
    ("mm_limber_wood",sokf_static_movement|sokf_dont_move_agent_over,"limber_wood","bo_limber_wood",[]),
    ("mm_limber_wheels",sokf_static_movement,"limber_wheels","0",[]),
    
    # Buttons
    # ("mm_cannon1_limber" ,sokf_static_movement|spr_use_time(10),"cannon1_limber" ,"0" , [ # Only use for unlimber
      # check_mm_use_cannon_prop_start_trigger,
      # check_mm_use_cannon_prop_end_trigger,
      # check_mm_use_cannon_prop_cancel_trigger,
    # ]),
    
    ("mm_cannon_12pdr_limber" ,sokf_static_movement|sokf_dont_move_agent_over|spr_use_time(10),"cannon_12pdr_limber" ,"bo_cannon4_limber" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_cannon_howitzer_limber" ,sokf_static_movement|sokf_dont_move_agent_over|spr_use_time(10),"cannon_howitzer_limber" ,"bo_cannon4_limber" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_limber_button", sokf_static_movement|spr_use_time(5), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_pickup_rocket_button", sokf_static_movement|spr_use_time(5), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_aim_button", sokf_static_movement|spr_use_time(0), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_load_cartridge_button", sokf_static_movement|spr_use_time(2), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_load_bomb_button", sokf_static_movement|spr_use_time(2), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_load_rocket_button", sokf_static_movement|spr_use_time(5), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_reload_button", sokf_static_movement|spr_use_time(9), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_12pdr_push_button",sokf_static_movement|spr_use_time(1),"0","12wheels",[
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    ("mm_howitzer_push_button",sokf_static_movement|spr_use_time(1),"0","12wheels",[
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    ("mm_fort_push_button",sokf_static_movement|spr_use_time(1),"0","fortwheels",[
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    ("mm_naval_push_button",sokf_static_movement|spr_use_time(1),"0","navalwheels",[
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    # Taking of difirent ammo
    ("mm_round_button", sokf_static_movement|spr_use_time(2), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_shell_button", sokf_static_movement|spr_use_time(2), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_canister_button", sokf_static_movement|spr_use_time(2), "0" , "cannon_button_collision" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),
    
    ("mm_bomb_button", sokf_static_movement|spr_use_time(2), "mortar_bomb_stack" , "bo_ammobox" , [
      check_mm_use_cannon_prop_start_trigger,
      check_mm_use_cannon_prop_end_trigger,
      check_mm_use_cannon_prop_cancel_trigger,
    ]),

  ("mm_tunnel_wall" ,sokf_static_movement|sokf_destructible,"mm_shovel_earth3" ,"bo_mm_shovel_earth3" , [check_common_earth_on_hit_trigger,]),
  ("mm_earth_dig1" ,sokf_static_movement|sokf_destructible,"mm_shovel_earth" ,"bo_mm_shovel_earth" , [check_common_earth_on_hit_trigger,]),
  ("mm_earth_dig2" ,sokf_static_movement|sokf_destructible,"mm_shovel_earth1" ,"bo_mm_shovel_earth1" , [check_common_earth_on_hit_trigger,]),
  ("mm_earth_dig3" ,sokf_static_movement|sokf_destructible,"mm_shovel_earth2" ,"bo_mm_shovel_earth2" , [check_common_earth_on_hit_trigger,]),
  ("mm_earth_dig4" ,sokf_static_movement|sokf_destructible,"mm_shovel_earth4" ,"bo_mm_shovel_earth4" , [check_common_earth_on_hit_trigger,]),

  # ULTIMOS
  ("mm_ambience_sound_global_wind_snow",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_snow"),
    ]),]),  

  ("mm_ambience_sound_global_night",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_global_ambient_night"),
    ]),]),  

 ("mm_ambience_sound_global_beach",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_global_ambient_beach"),
    ]),]),  

 ("mm_ambience_sound_global_farmland",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_global_ambient_farmland"),
    ]),]),  

 ("mm_ambience_sound_global_farmland_evening",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_global_ambient_farmland_evening"),
    ]),]),  

 ("mm_ambience_sound_global_farmland_empty",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_global_ambient_farmland_empty"),
    ]),]),  
 
("mm_ambience_sound_global_city_empty",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_global_ambient_city_empty"),
    ]),]),  

 ("mm_ambience_sound_local_birds",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_birds"),
    ]), ]),  
 ("mm_ambience_sound_local_birds_many",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_birds_many"),
    ]), ]),  
 ("mm_ambience_sound_local_ocean",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_ocean"),
    ]), ]),  
  ("mm_ambience_sound_local_crickets",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_crickets_few"),
    ]), ]),  
  ("mm_ambience_sound_local_crickets_many",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_crickets_many"),
    ]), ]),     
  ("mm_ambience_sound_local_river",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_river"),
    ]), ]),   
  ("mm_ambience_sound_local_night",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_night"),
    ]), ]),  
  ("mm_ambience_sound_local_seagulls",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_seagulls"),
    ]), ]),  
  ("mm_ambience_sound_local_flys",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_fly"),
    ]), ]),    

 ("mm_ambience_sound_local_roof_rain",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_roof"),
    ]), ]), 
 ("mm_ambience_sound_local_stone_rain",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_stone"),
    ]), ]), 
 ("mm_ambience_sound_local_windmill",0,"0" ,"0" , [
  (ti_on_init_scene_prop,
    [
      (neg|multiplayer_is_dedicated_server),
      (play_sound,"snd_ambient_windmill"),
    ]), ]), 

  ("mm_ambience_sound_local_crow",0,"0","0",
   [
   (ti_on_scene_prop_init,
    [
      (store_trigger_param_1,":instance_id"),
      (store_random_in_range,":cur_time",1,31),
      (scene_prop_set_slot, ":instance_id", scene_prop_slot_time,":cur_time")
    ]),
  ]),

  ("mm_sp_crate_explosive",sokf_static_movement|sokf_destructible,"barreltriangulated" ,"barreltriangulated_collision" , [
  (ti_on_init_scene_prop,
    [
      (this_or_next|multiplayer_is_server), #In case someone wants them in a multi scene...
      (neg|game_in_multiplayer_mode),
      (store_trigger_param_1,":prop_id"),
      (scene_prop_set_hit_points,":prop_id",70),
      
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos5, 1500),
      (position_set_y, pos5, 80),
      (position_set_z, pos5, 0),
      (prop_instance_dynamics_set_properties, ":prop_id", pos5),
      (position_set_x, pos5, 300),
      (position_set_y, pos5, 300),
      (position_set_z, pos5, 300),
      (prop_instance_dynamics_set_omega, ":prop_id", pos5),
    ]), 
  (ti_on_scene_prop_hit,[]),
  (ti_on_scene_prop_destroy,
    [
      (this_or_next|multiplayer_is_server), #In case someone wants them in a multi scene...
      (neg|game_in_multiplayer_mode),
      (store_trigger_param_1,":prop_id"),
      (assign,":attacker_agent_no",-1),
      (set_fixed_point_multiplier, 100),
      (prop_instance_get_position,pos3,":prop_id"),
      (copy_position,pos47,pos3),
      (position_set_z,pos3,-3000),#patch1115 fix 29/1
      (prop_instance_set_position,":prop_id",pos3),
      (prop_instance_animate_to_position,":prop_id",pos3),
      (call_script,"script_explosion_at_position",":attacker_agent_no",300,500)
   ]),
  ]),

  #PN END ***************************************************************************************************************************

  ("code_freeze_agent",sokf_moveable,"0","bo_pw_freeze_agent", []),
  ("code_freeze_horse_agent",sokf_moveable,"0","bo_pw_freeze_horse_agent", []),

  ("custom_script_trigger_a",sokf_invisible|spr_use_time(1),"pw_invisible_chest","bo_pw_invisible_chest", []),
  ("custom_script_trigger_b",sokf_invisible|spr_use_time(1),"pw_invisible_chest","bo_pw_invisible_chest", []),
  ("custom_script_trigger_c",sokf_invisible|spr_use_time(1),"pw_invisible_chest","bo_pw_invisible_chest", []),
  ("custom_script_trigger_d",sokf_invisible|spr_use_time(1),"pw_invisible_chest","bo_pw_invisible_chest", []),
  ("custom_script_trigger_e",sokf_invisible|spr_use_time(1),"pw_invisible_chest","bo_pw_invisible_chest", []),
]

def fill_scene_props_list(list_var, trigger_id, modify_function):
  for scene_prop in scene_props:
    trigger_list = scene_prop[4]
    triggers_to_pop = []
    for i, trigger in enumerate(trigger_list):
      if trigger[0] == trigger_id:
        triggers_to_pop.append(i)
        list_var.append(modify_function(scene_prop[0], trigger[1:]))
    for i in reversed(triggers_to_pop):
      trigger_list.pop(i)

scene_props_to_link = []
def make_link_scene_prop_entry(spr_name, link_list):
  link_list = [spr_name] + [spr_name if x == link_scene_prop_self else x for x in link_list]
  link_list = [spr_tag(x) for x in link_list]
  for unused in range(len(link_list), linked_scene_prop_slot_count + 1):
    link_list.append(-1)
  return link_list
fill_scene_props_list(scene_props_to_link, link_scene_prop, make_link_scene_prop_entry)

scene_props_to_init = []
def make_init_scene_prop_entry(spr_name, link_list):
  return [spr_tag(spr_name)] + link_list
fill_scene_props_list(scene_props_to_init, init_scene_prop, make_init_scene_prop_entry)
