from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track.
#  3) Track flags. See header_music.py for a list of available flags.
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags.
####################################################################################################################

# You must add mtf_module_track flag to the flags of the tracks located under module directory.

# Changed meanings of the different flags in PW:

# mtf_sit_victorious: after your faction captured a castle
# mtf_sit_encounter_hostile: after your faction lost a castle
# mtf_sit_fight: when many human agents have been recently killed nearby
# mtf_sit_killed: after the player was killed
# mtf_sit_ambushed: when in a faction hostile to any other, while near a friendly castle
# mtf_sit_siege: when in a faction hostile to any other, while near an enemy castle
# mtf_sit_tavern: when in a faction at peace with everyone, while near a friendly castle; or when near a tavern processing scene prop
# mtf_sit_town: when in a faction at peace with everyone, while near a castle owned by another faction; or somewhere not directly on terrain (probably a town)
# mtf_sit_town_infiltrate: after being outlawed, and when in town with a lock pick or poison dagger
# mtf_sit_travel: for all other situations, mostly when in alone in the countryside

# mtf_culture_1: as a commoner
# mtf_culture_2: as an outlaw
# mtf_culture_3: as a member of a faction

tracks = [
 ("ambushed_by_neutral", "elgar_pomp_and_circumstance_march_1.mp3", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_khergit", "liszt_les_preludes.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_nord", "strauss_radetzky_march.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_rhodok", "vivaldi_concerto_10_allegro_II.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_swadian", "vivaldi_concerto_flute_violin_continuo_allegro.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_vaegir", "vivaldi_summer_presto.mp3", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_sarranid", "vivaldi_winter_allegro.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("arena_1", "wagner_ride_of_the_valkyries.ogg", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
 ("armorer", "bach_cello_suite_1.ogg", mtf_sit_town, mtf_sit_tavern|mtf_sit_travel),
 ("calm_night_2", "bach_orchestral_suite_3_air.ogg", mtf_sit_travel|mtf_sit_night, mtf_sit_town|mtf_sit_tavern),
 ("captured", "claude_debussy_clair_de_lune.ogg", mtf_sit_killed|mtf_persist_until_finished, 0),
 ("coronation", "mazurek_dabrowskiego_polish_national_anthem.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("crazy_battle_music", "chopin_polonaise_military.ogg", mtf_sit_fight|mtf_sit_siege, mtf_sit_ambushed),
 ("defeated_by_neutral", "defeated_by_neutral.ogg", mtf_sit_encounter_hostile|mtf_persist_until_finished, 0),
 ("defeated_by_neutral_2", "defeated_by_neutral_2.ogg", mtf_sit_encounter_hostile|mtf_persist_until_finished, 0),
 ("defeated_by_neutral_3", "defeated_by_neutral_3.ogg", mtf_sit_encounter_hostile|mtf_persist_until_finished, 0),
 ("empty_village", "empty_village.ogg", mtf_sit_killed|mtf_persist_until_finished, 0),
 ("encounter_hostile_nords", "geminiani_concerto_grosso.ogg", mtf_persist_until_finished, 0),
 ("enter_the_juggernaut", "franz_schubert_marche_militaire.ogg", mtf_sit_fight|mtf_sit_siege, mtf_sit_ambushed),
 ("escape", "escape.ogg", mtf_sit_killed|mtf_persist_until_finished, 0),
 ("fight_1", "grieg_peer_gynt_in_the_hall_of_the_mountain_king.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_2", "rimsky_korsakov_the_flight_of_the_bumble_bee.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_3", "vivaldi_winter_presto.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_4", "percussion_battery.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_as_khergit", "beethoven_symphony_no_9_movement_4.ogg", mtf_culture_3|mtf_sit_fight, mtf_culture_all|mtf_sit_siege|mtf_sit_ambushed),
 ("fight_as_nord", "vivaldi_autumn_allegro.ogg", mtf_culture_3|mtf_sit_fight, mtf_culture_all|mtf_sit_siege|mtf_sit_ambushed),
 ("fight_as_rhodok", "vivaldi_concerto_grosso_8_allegro.ogg", mtf_culture_3|mtf_sit_fight, mtf_culture_all|mtf_sit_siege|mtf_sit_ambushed),
 ("fight_as_vaegir", "vivaldi_spring_allegro.ogg", mtf_culture_3|mtf_sit_fight, mtf_culture_all|mtf_sit_siege|mtf_sit_ambushed),
 ("fight_while_mounted_1", "fight_while_mounted_1.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_while_mounted_2", "fight_while_mounted_2.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("hearth_and_brotherhood", "tchaikovsky_overture_1812.ogg", mtf_sit_night|mtf_sit_travel, mtf_sit_town),
 ("infiltration_khergit", "infiltration_khergit.ogg", mtf_sit_town_infiltrate, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_fight),
 ("killed_by_khergit", "killed_by_khergit.ogg", mtf_culture_3|mtf_sit_killed|mtf_persist_until_finished, 0),
 ("killed_by_swadian", "claude_debussy_clair_de_lune.ogg", mtf_culture_3|mtf_sit_killed|mtf_persist_until_finished, 0),
 ("lords_hall_khergit", "brahms_hungarian_dance_5.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("lords_hall_nord", "mozart_eine_kleine_nachtmusik_allegro.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("lords_hall_swadian", "pachelbel_canon.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("lords_hall_rhodok", "elgar_pomp_and_circumstance_march_1.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("lords_hall_vaegir", "boccherini_minuet.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("mounted_snow_terrain_calm", "debussy_clair_de_lune.ogg", mtf_sit_travel, mtf_sit_night|mtf_sit_town|mtf_sit_tavern),
 ("neutral_infiltration", "hummel_rondo.ogg", mtf_sit_town_infiltrate, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_fight),
 ("outdoor_beautiful_land", "saint_saens_danse_macabre.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_tavern),
 ("retreat", "retreat.ogg", mtf_sit_killed|mtf_persist_until_finished, 0),
 ("siege_attempt", "dvorak_symphony_9_4.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_ambushed),
 ("tavern_1", "travel_swadian.ogg", mtf_sit_tavern, mtf_sit_town|mtf_sit_travel),
 ("tavern_2", "vivaldi_summer_allegro_adagio.ogg", mtf_sit_tavern, mtf_sit_town|mtf_sit_travel),
 ("town_khergit", "handel_queen_of_sheba.mp3", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("town_neutral", "mozart_symphony_40_molto_allegro.ogg", mtf_sit_town, mtf_sit_tavern|mtf_sit_travel),
 ("town_nord", "beethoven_symphony_5_1.ogg", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("town_rhodok", "william_boyce_sinfonia_1.mp3", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("town_swadian", "vivaldi_spring_allegro_2.ogg", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("town_vaegir", "grieg_peer_gynt_overture.ogg", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("tragic_village", "the_great_hall.ogg", mtf_culture_1|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_khergit", "bach_concerto_for_two_violins_first_movement.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_neutral", "bach_gavotte.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_nord",    "bach_brandenburg_concerto_movement_1.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_rhodok",  "strauss_radetzky_march.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_swadian", "bizet_carmen_overture.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_vaegir",  "rossini_william_tell_overture.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_sarranid",  "bizet_carmen_toreador.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("uncertain_homestead", "strauss_blue_danube_waltz.ogg", mtf_culture_1|mtf_culture_2|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("victorious_evil", "victorious_evil.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_neutral_1", "la_victoire_est_a_nous_short.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_neutral_2", "la_victoire_est_a_nous_short.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_neutral_3", "la_victoire_est_a_nous_short.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_swadian", "la_victoire_est_a_nous_short.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_vaegir", "la_victoire_est_a_nous_short.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_vaegir_2", "la_victoire_est_a_nous_short.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("main_menu_music", "main_menu_music.ogg", mtf_sit_main_title|mtf_start_immediately, 0),
 ("warband_siege", "bizet_carmen_aragonaise.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("wedding", "mendelssohn_wedding_march_recessional.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
]
