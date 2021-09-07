from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
  ("mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_score_b", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mp_ingame_menu", 0, "mp_ingame_menu", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_left", 0, "mp_inventory_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_right", 0, "mp_inventory_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_choose", 0, "mp_inventory_choose", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_glove", 0, "mp_inventory_slot_glove", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_horse", 0, "mp_inventory_slot_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_armor", 0, "mp_inventory_slot_armor", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_helmet", 0, "mp_inventory_slot_helmet", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_boot", 0, "mp_inventory_slot_boot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_empty", 0, "mp_inventory_slot_empty", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_equip", 0, "mp_inventory_slot_equip", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_left_arrow", 0, "mp_inventory_left_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_right_arrow", 0, "mp_inventory_right_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_main", 0, "mp_ui_host_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mp_ui_host_maps_randomp", 0, "mp_ui_host_maps_randomp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_panel", 0, "mp_ui_command_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_l", 0, "mp_ui_command_border_l", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_r", 0, "mp_ui_command_border_r", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_welcome_panel", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("tableau_mesh_shield_round_1",  0, "fixed_tableau_mesh_shield_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_2",  0, "fixed_tableau_mesh_shield_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_3",  0, "fixed_tableau_mesh_shield_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_4",  0, "fixed_tableau_mesh_shield_round_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_5",  0, "fixed_tableau_mesh_shield_round_5", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_1",  0, "fixed_tableau_mesh_shield_small_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_2",  0, "fixed_tableau_mesh_shield_small_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_3",  0, "fixed_tableau_mesh_shield_small_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_1",   0, "fixed_tableau_mesh_shield_kite_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_2",   0, "fixed_tableau_mesh_shield_kite_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_3",   0, "fixed_tableau_mesh_shield_kite_3",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_4",   0, "fixed_tableau_mesh_shield_kite_4",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_heater_1", 0, "fixed_tableau_mesh_shield_heater_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_heater_2", 0, "fixed_tableau_mesh_shield_heater_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_pavise_1", 0, "fixed_tableau_mesh_shield_pavise_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_pavise_2", 0, "fixed_tableau_mesh_shield_pavise_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("heraldic_armor_bg", 0, "heraldic_armor_bg",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("tableau_mesh_heraldic_armor_a", 0, "fixed_tableau_mesh_heraldic_armor_a",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_b", 0, "fixed_tableau_mesh_heraldic_armor_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_c", 0, "fixed_tableau_mesh_heraldic_armor_c",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_d", 0, "fixed_tableau_mesh_heraldic_armor_d",  0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("banner_a01", 0, "pw_banner_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a02", 0, "pw_banner_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a03", 0, "pw_banner_m13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a04", 0, "pw_banner_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a05", 0, "pw_banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a06", 0, "pw_banner_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a07", 0, "pw_banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a08", 0, "pw_banner_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a09", 0, "pw_banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a10", 0, "pw_banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a11", 0, "pw_banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a12", 0, "pw_banner_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a13", 0, "pw_banner_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a14", 0, "pw_banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a15", 0, "pw_banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a16", 0, "pw_banner_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a17", 0, "pw_banner_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a18", 0, "pw_banner_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a19", 0, "pw_banner_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a20", 0, "pw_banner_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a21", 0, "pw_banner_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_b01", 0, "pw_banner_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b02", 0, "pw_banner_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b03", 0, "pw_banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b04", 0, "pw_banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b05", 0, "pw_banner_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b06", 0, "pw_banner_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b07", 0, "pw_banner_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b08", 0, "pw_banner_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b09", 0, "pw_banner_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b10", 0, "pw_banner_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b11", 0, "pw_banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b12", 0, "pw_banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b13", 0, "pw_banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b14", 0, "pw_banner_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b15", 0, "pw_banner_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b16", 0, "pw_banner_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b17", 0, "pw_banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b18", 0, "pw_banner_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b19", 0, "pw_banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b20", 0, "pw_banner_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b21", 0, "pw_banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_c01", 0, "pw_banner_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c02", 0, "pw_banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c03", 0, "pw_banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c04", 0, "pw_banner_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c05", 0, "pw_banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c06", 0, "pw_banner_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c07", 0, "pw_banner_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c08", 0, "pw_banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c09", 0, "pw_banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c10", 0, "pw_banner_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c11", 0, "pw_banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c12", 0, "pw_banner_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c13", 0, "pw_banner_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c14", 0, "pw_banner_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c15", 0, "pw_banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c16", 0, "pw_banner_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c17", 0, "pw_banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c18", 0, "pw_banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c19", 0, "pw_banner_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c20", 0, "pw_banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c21", 0, "pw_banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_d01", 0, "pw_banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d02", 0, "pw_banner_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d03", 0, "pw_banner_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d04", 0, "pw_banner_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d05", 0, "pw_banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d06", 0, "pw_banner_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d07", 0, "pw_banner_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d08", 0, "pw_banner_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d09", 0, "pw_banner_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d10", 0, "pw_banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d11", 0, "pw_banner_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d12", 0, "pw_banner_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d13", 0, "pw_banner_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d14", 0, "pw_banner_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d15", 0, "pw_banner_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d16", 0, "pw_banner_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d17", 0, "pw_banner_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d18", 0, "pw_banner_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d19", 0, "pw_banner_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d20", 0, "pw_banner_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d21", 0, "pw_banner_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_e01", 0, "pw_banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e02", 0, "pw_banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e03", 0, "pw_banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e04", 0, "pw_banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e05", 0, "pw_banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e06", 0, "pw_banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e07", 0, "pw_banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e08", 0, "pw_banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e09", 0, "pw_banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e10", 0, "pw_banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e11", 0, "pw_banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e12", 0, "pw_banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e13", 0, "pw_banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e14", 0, "pw_banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e15", 0, "pw_banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e16", 0, "pw_banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e17", 0, "pw_banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e18", 0, "pw_banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e19", 0, "pw_banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e20", 0, "pw_banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e21", 0, "pw_banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_f01", 0, "pw_banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f02", 0, "pw_banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f03", 0, "pw_banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f04", 0, "pw_banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f05", 0, "pw_banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f06", 0, "pw_banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f07", 0, "pw_banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f08", 0, "pw_banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f09", 0, "pw_banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f10", 0, "pw_banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f11", 0, "pw_banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f12", 0, "pw_banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f13", 0, "pw_banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f14", 0, "pw_banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f15", 0, "pw_banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f16", 0, "pw_banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f17", 0, "pw_banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f18", 0, "pw_banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f19", 0, "pw_banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f20", 0, "pw_banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f21", 0, "pw_banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_g01", 0, "pw_banner_g01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g02", 0, "pw_banner_g02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g03", 0, "pw_banner_g03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g04", 0, "pw_banner_g04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g05", 0, "pw_banner_g05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g06", 0, "pw_banner_g06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g07", 0, "pw_banner_g07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g08", 0, "pw_banner_g08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g09", 0, "pw_banner_g09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g10", 0, "pw_banner_g10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g11", 0, "pw_banner_g11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g12", 0, "pw_banner_g12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g13", 0, "pw_banner_g13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g14", 0, "pw_banner_g14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g15", 0, "pw_banner_g15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g16", 0, "pw_banner_g16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g17", 0, "pw_banner_g17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g18", 0, "pw_banner_g18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g19", 0, "pw_banner_g19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g20", 0, "pw_banner_g20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g21", 0, "pw_banner_g21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_h01", 0, "pw_banner_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h02", 0, "pw_banner_h02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h03", 0, "pw_banner_h03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h04", 0, "pw_banner_h04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h05", 0, "pw_banner_h05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h06", 0, "pw_banner_h06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h07", 0, "pw_banner_h07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h08", 0, "pw_banner_h08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h09", 0, "pw_banner_h09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h10", 0, "pw_banner_h10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h11", 0, "pw_banner_h11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h12", 0, "pw_banner_h12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h13", 0, "pw_banner_h13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h14", 0, "pw_banner_h14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h15", 0, "pw_banner_h15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h16", 0, "pw_banner_h16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h17", 0, "pw_banner_h17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h18", 0, "pw_banner_h18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h19", 0, "pw_banner_h19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h20", 0, "pw_banner_h20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_h21", 0, "pw_banner_h21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_i01", 0, "pw_banner_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i02", 0, "pw_banner_i02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i03", 0, "pw_banner_i03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i04", 0, "pw_banner_i04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i05", 0, "pw_banner_i05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i06", 0, "pw_banner_i06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i07", 0, "pw_banner_i07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i08", 0, "pw_banner_i08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i09", 0, "pw_banner_i09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i10", 0, "pw_banner_i10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i11", 0, "pw_banner_i11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i12", 0, "pw_banner_i12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i13", 0, "pw_banner_i13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i14", 0, "pw_banner_i14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i15", 0, "pw_banner_i15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i16", 0, "pw_banner_i16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i17", 0, "pw_banner_i17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i18", 0, "pw_banner_i18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i19", 0, "pw_banner_i19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i20", 0, "pw_banner_i20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_i21", 0, "pw_banner_i21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_j01", 0, "pw_banner_j01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j02", 0, "pw_banner_j02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j03", 0, "pw_banner_j03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j04", 0, "pw_banner_j04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j05", 0, "pw_banner_j05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j06", 0, "pw_banner_j06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j07", 0, "pw_banner_j07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j08", 0, "pw_banner_j08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j09", 0, "pw_banner_j09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j10", 0, "pw_banner_j10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j11", 0, "pw_banner_j11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j12", 0, "pw_banner_j12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j13", 0, "pw_banner_j13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j14", 0, "pw_banner_j14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j15", 0, "pw_banner_j15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j16", 0, "pw_banner_j16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j17", 0, "pw_banner_j17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j18", 0, "pw_banner_j18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j19", 0, "pw_banner_j19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j20", 0, "pw_banner_j20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_j21", 0, "pw_banner_j21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_k01", 0, "pw_banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k02", 0, "pw_banner_k02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k03", 0, "pw_banner_k03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k04", 0, "pw_banner_k04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k05", 0, "pw_banner_k05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k06", 0, "pw_banner_k06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k07", 0, "pw_banner_k07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k08", 0, "pw_banner_k08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k09", 0, "pw_banner_k09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k10", 0, "pw_banner_k10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k11", 0, "pw_banner_k11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k12", 0, "pw_banner_k12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k13", 0, "pw_banner_k13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k14", 0, "pw_banner_k14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k15", 0, "pw_banner_k15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k16", 0, "pw_banner_k16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k17", 0, "pw_banner_k17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k18", 0, "pw_banner_k18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k19", 0, "pw_banner_k19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k20", 0, "pw_banner_k20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_k21", 0, "pw_banner_k21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_l01", 0, "pw_banner_l01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l02", 0, "pw_banner_l02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l03", 0, "pw_banner_l03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l04", 0, "pw_banner_l04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l05", 0, "pw_banner_l05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l06", 0, "pw_banner_l06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l07", 0, "pw_banner_l07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l08", 0, "pw_banner_l08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l09", 0, "pw_banner_l09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l10", 0, "pw_banner_l10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l11", 0, "pw_banner_l11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l12", 0, "pw_banner_l12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l13", 0, "pw_banner_l13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l14", 0, "pw_banner_l14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l15", 0, "pw_banner_l15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l16", 0, "pw_banner_l16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l17", 0, "pw_banner_l17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l18", 0, "pw_banner_l18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l19", 0, "pw_banner_l19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l20", 0, "pw_banner_l20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_l21", 0, "pw_banner_l21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_m01", 0, "pw_banner_m01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m02", 0, "pw_banner_m02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m03", 0, "pw_banner_m03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m04", 0, "pw_banner_m04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m05", 0, "pw_banner_m05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m06", 0, "pw_banner_m06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m07", 0, "pw_banner_m07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m08", 0, "pw_banner_m08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m09", 0, "pw_banner_m09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m10", 0, "pw_banner_m10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m11", 0, "pw_banner_m11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m12", 0, "pw_banner_m12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_m13", 0, "pw_banner_m13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_kingdom_a", 0, "pw_banner_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_b", 0, "pw_banner_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_c", 0, "pw_banner_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_d", 0, "pw_banner_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_e", 0, "pw_banner_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_f", 0, "pw_banner_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_g", 0, "pw_banner_kingdom_g", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banners_default_a", 0, "banners_default_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_b", 0, "banners_default_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_c", 0, "banners_default_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_d", 0, "banners_default_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_e", 0, "banners_default_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("troop_label_banner",  0, "troop_label_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("main_menu_background", 0, "main_menu_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("loading_background", 0, "load_screen_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mp_ui_order_button", 0, "mp_ui_order_button", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("tableau_mesh_pw_banner_pole", 0, "tableau_mesh_pw_banner_pole",  0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("tableau_mesh_heraldic_leather_vest_a", 0, "tableau_mesh_heraldic_leather_vest_a",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_padded_cloth_a", 0, "tableau_mesh_heraldic_padded_cloth_a",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_padded_cloth_b", 0, "tableau_mesh_heraldic_padded_cloth_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_tabard_b", 0, "tableau_mesh_heraldic_tabard_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_brigandine_b", 0, "tableau_mesh_heraldic_brigandine_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_coat_of_plates", 0, "tableau_mesh_heraldic_coat_of_plates",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_lamellar_armor_d", 0, "tableau_mesh_heraldic_lamellar_armor_d",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_mail_long_surcoat", 0, "tableau_mesh_heraldic_mail_long_surcoat",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_surcoat_over_mail", 0, "tableau_mesh_heraldic_surcoat_over_mail",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_colored_arena_tunic", 0, "tableau_mesh_colored_arena_tunic",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_colored_arena_armor", 0, "tableau_mesh_colored_arena_armor",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_colored_lamellar_leather", 0, "tableau_mesh_colored_lamellar_leather",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_colored_lamellar_vest_b", 0, "tableau_mesh_colored_lamellar_vest_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_colored_helmets_new_b", 0, "tableau_mesh_colored_helmets_new_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_colored_helmets_new_d", 0, "tableau_mesh_colored_helmets_new_d",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_colored_helmets_new_e", 0, "tableau_mesh_colored_helmets_new_e",  0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("pw_stats_chart_commoners", 0, "pw_stats_chart_commoners", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pw_stats_chart_outlaws", 0, "pw_stats_chart_outlaws", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pw_stats_chart_banner", 0, "pw_stats_chart_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("pw_stats_chart_war", 0, "pw_stats_chart_war", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pw_stats_chart_all", 0, "pw_stats_chart_all", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pw_stats_chart_selected", 0, "pw_stats_chart_selected", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("pw_status_background_player", 0, "pw_status_background_player", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pw_status_food_bar", 0, "pw_status_food_bar", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("pw_progress_bar", 0, "pw_progress_bar", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pw_progress_bar_fill", 0, "pw_progress_bar_fill", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  # PN START ***********************************************************************
  #Construct props stuff
  ("construct_mesh_stakes", 0, "ui_construct_cdf", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_stakes2", 0, "ui_construct_stakes", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_sandbags", 0, "ui_construct_bags", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_cdf_tri", 0, "ui_construct_cdf_tri", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_gabion", 0, "ui_construct_gabion", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_fence", 0, "ui_construct_fence", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_earthwork", 0, "ui_construct_dig", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  #Bonus icons
  ("bonus_icon_melee", 0, "bonus_icon_melee", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_accuracy", 0, "bonus_icon_accuracy", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_speed", 0, "bonus_icon_speed", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_reload", 0, "bonus_icon_reload", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_artillery", 0, "bonus_icon_artillery", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_commander", 0, "bonus_icon_commander", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #Artillery icons
  ("arty_icon_take_ammo", 0, "arty_icon_take_ammo", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("arty_icon_put_ammo", 0, "arty_icon_put_ammo", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("arty_icon_ram", 0, "arty_icon_ram", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("arty_icon_move_up", 0, "arty_icon_move_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("arty_icon_take_control", 0, "arty_icon_take_control", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #Medic icons
  ("medic_icon_heal", 0, "medic_icon_heal", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("medic_icon_medic", 0, "medic_icon_medic", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #Stuff
  ("item_select_no_select", 0, "cb_ui_title_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mm_spyglass_ui", 0, "mm_spyglass_ui_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("custom_mp_ui_order_button", 0, "mp_ui_order_button", 0, 0, 0, 0, 0, 0, 0.8, 0.6, 0.6),

  ("target_plate", 0, "target_plate", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  # PN END *************************************************************************
]
