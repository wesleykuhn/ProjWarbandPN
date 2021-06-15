from header_particle_systems import *

####################################################################################################################
#   Each particle system contains the following fields:
#
#  1) Particle system id (string):  Used for referencing particle systems in other files.
#     The prefix psys_ is automatically added before each particle system id.
#  2) Particle system flags (int).  See header_particle_systems.py for a list of available flags
#  3) mesh-name.
####
#  4) Num particles per second:     Number of particles emitted per second.
#  5) Particle life:                Each particle lives this long (in seconds).
#  6) Damping:                      How much particle's speed is lost due to friction.
#  7) Gravity strength:             Effect of gravity. (Negative values make the particles float upwards.)
#  8) Turbulence size:              Size of random turbulence (in meters)
#  9) Turbulence strength:          How much a particle is affected by turbulence.
####
# 10,11) Alpha keys:                Each attribute is controlled by two keys and
# 12,13) Red keys:                  each key has two fields: (time, magnitude)
# 14,15) Green keys:                For example scale key (0.3,0.6) means
# 16,17) Blue keys:                 scale of each particle will be 0.6 at the
# 18,19) Scale keys:                time 0.3 (where time=0 means creation and time=1 means end of the particle)
#
# The magnitudes are interpolated in between the two keys and remain constant beyond the keys.
# Except the alpha always starts from 0 at time 0.
####
# 20) Emit box size:                The dimension of the box particles are emitted from.
# 21) Emit velocity:                Particles are initially shot with this velocity.
# 22) Emit dir randomness
# 23) Particle rotation speed:      Particles start to rotate with this (angular) speed (degrees per second).
# 24) Particle rotation damping:    How quickly particles stop their rotation
####################################################################################################################

def psys(identifier, flags, mesh,
  number, life, damping=0.0, gravity=0.0, turbulence_size=0.0, turbulence_strength=0.0,
  alpha=[(1.0, 1.0), (1.0, 1.0)],
  red=[(1.0, 1.0), (1.0, 1.0)],
  green=[(1.0, 1.0), (1.0, 1.0)],
  blue=[(1.0, 1.0), (1.0, 1.0)],
  scale=[(1.0, 1.0), (1.0, 1.0)],
  emit_box=(1.0, 1.0, 1.0),
  emit_velocity=(0.0, 0.0, 0.0),
  emit_direction_randomness=0.0,
  rotation_speed=0.0,
  rotation_damping=0.0):
  return (identifier, flags, mesh, number, life, damping, gravity, turbulence_size, turbulence_strength,
    alpha[0], alpha[1], red[0], red[1], green[0], green[1], blue[0], blue[1], scale[0], scale[1],
    emit_box, emit_velocity, emit_direction_randomness, rotation_speed, rotation_damping)

particle_systems = [

  # PN START *********************************************************************************************

  ("pistol_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
   40, 13, 0.9, -0.00003, 40, 1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
   (0.0, 0.75), (1, 0),       #alpha keys
   (0.0, 0.7), (1, 0.4),      #red keys
   (0.0, 0.7),(1, 0.4),       #green keys
   (0.0, 0.7), (1, 0.4),      #blue keys
   (0, 4.1),   (0.5, 12.0),   #scale keys
   (0.2, 0.45, 0.2),           #emit box size
   (0.0, 0.0, 0.0),                 #emit velocity
   0.0,                        #emit dir randomness
   100,                       #rotation speed
   0.5,                        #rotation damping
  ),
  ("cannon_ball_hit", psf_billboard_3d|psf_always_emit|psf_randomize_size,  "prtcl_dust_c",
     2000, 2, 15, -0.65, 12.0, 0.4,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (6.0, 6.7),   (7, 8.2),    #scale keys
     (0.45, 0.46, 3.2),         #emit box size
     (0, 0, 0.1),               #emit velocity
     4,                         #emit dir randomness
     15,                        #rotation speed
     0.1,                       #rotation damping
    ),
    ("cannon_blood", psf_billboard_3d |psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
     2000, 1.05, 3, 0.5, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (0.7, 0.7),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.1, 0.11),   (1.1, 0.028),  #scale keys
     (0.10, 0.10, 1),               #emit box size
     (0, 1.0, 0.3),                #emit velocity
     0.9,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),
    ("cannon_blood_2", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
     2000, 1, 3, 0.3, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.25), (0.7, 0.1),        #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.3, 0.75),   (1.2, 0.65),    #scale keys
     (0.11, 0.3, 0.11),             #emit box size
     (0.2, 0.3, 0),                 #emit velocity
     0.3,                         #emit dir randomness
     150,                       #rotation speed
     0,                       #rotation damping
     ),
     ("cannon_smoke", psf_billboard_3d, "prtcl_dust_a",
     1900, 11, 1.14, -0.006, 40, 1.75,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.90), (0.85, 0),       #alpha keys
     (0.0, 0.99), (1, 0.99),      #red keys
     (0.0, 0.99),(1, 0.99),       #green keys
     (0.0, 0.99), (1, 0.99),      #blue keys
     (-0.1, 6),   (1.0, 16.0),   #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (6.4, 0.2, 0),                 #emit velocity
     1.8,                        #emit dir randomness
     90,                       #rotation speed
     0.4,                        #rotation damping
    ),
    ("cannon_flash", psf_billboard_3d | psf_randomize_size , "prt_sparks_mesh_1",
     3000, 0.4, 0.1, -0.00003, 50.0, 1.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (-0.1, 3.1),   (0.9, 2.2),   #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (2.2, 0.26, 0),                 #emit velocity  #patch1115 fix 21/1
     0.05,                       #emit dir randomness
     100.0,                       #rotation speed
     0.5,                        #rotation damping
    ),
     ("musket_flash", psf_billboard_3d | psf_randomize_size , "prt_sparks_mesh_1",
     3000, 0.8, 0.1, -0.00003, 50.0, 1.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.0, 0.9),   (0.75, 0.1),   #scale keys
     (0.1, 0.2, 0.1),           #emit box size
     (0.6, 3.2, 0.6),                 #emit velocity
     0.05,                       #emit dir randomness
     100.0,                       #rotation speed
     0.5,                        #rotation damping
    ),
    ("musket_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     75, 22, 2, -0.006040, 90, 3.3,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.45), (0.449, 0),       #alpha keys
     (0.0, 0.99), (1, 0.99),      #red keys
     (0.0, 0.99),(1, 0.99),       #green keys
     (0.0, 0.99), (1, 0.99),      #blue keys
     (-0.01, 3.45),   (0.5, 12.7),   #scale keys
     (0.05, 0.05, 0.05),           #emit box size
     (0.0, 5.6, 0.0),                 #emit velocity
     0.85,                        #emit dir randomness
     90,                       #rotation speed
     0.25,                        #rotation damping
    ),
   ("pan_flash", psf_billboard_3d | psf_randomize_size , "prt_sparks_mesh_1",
     3000, 0.6, 0.1, -0.00003, 50.0, 1.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.0, 1.0),   (0.6, 0.7),   #scale keys
     (0.1, 0.1, 0.6),           #emit box size
     (0, 0, 0.6),                 #emit velocity
     0.05,                       #emit dir randomness
     100.0,                       #rotation speed
     0.5,                        #rotation damping
    ),
   ("pan_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     60, 10.6, 1.8, -0.0003, 90, 4,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.55), (0.549, 0),       #alpha keys
     (0.0, 0.99), (1, 0.99),      #red keys
     (0.0, 0.99),(1, 0.99),       #green keys
     (0.0, 0.99), (1, 0.99),      #blue keys
     (-0.07, 1.5),   (0.5, 3.75),   #scale keys
     (0.02, 0.02, 0.02),           #emit box size
     (-1.6, 0.6, 0.0),                 #emit velocity
     0.0,                        #emit dir randomness                       
    ),
  ("musket_sparks", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
     10, 0.7, 0.2, 0, 10.0, 0.02,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.1, 0.05),   (1, 0.05),  #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 0.9),               #emit velocity
     0.0,                       #emit dir randomness
     0,
     0,
    ),
    ("cannon_frizzle_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     40, 10, 1.8, -0.0003, 20, 1.75,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.75), (0.85, 0),       #alpha keys
     (0.0, 0.7), (1, 0.4),      #red keys
     (0.0, 0.7),(1, 0.4),       #green keys
     (0.0, 0.7), (1, 0.4),      #blue keys
     (-0.04, 1.5),   (0.5, 5.75),   #scale keys
     (0.02, 0.02, 0.02),           #emit box size
     (-1.6, 0.6, 0.0),                 #emit velocity
     0.0,                        #emit dir randomness
    ),
    ("bullet_hit_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     2000, 4, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 1.1),   (2, 4.2),    #scale keys
     (0.2, 0.2, 2.2),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     0.2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
    ("bottle_break", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_always_emit,  "prtcl_dust_g",
     850, 8, 0.1, 1.0, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
  (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 1),   (1.5, 1.5),    #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     50,                       #rotation speed
     0.5,                       #rotation damping
    ),
    ("bird_blood", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
     2000, 0.6, 3, 0.3, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.25), (0.7, 0.1),        #alpha keys
     (0.1, 22.7), (1, 0.7),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.0, 0.15),   (1, 0.35),    #scale keys
     (0.01, 0.2, 0.01),             #emit box size
     (0.2, 0.3, 0),                 #emit velocity
     0.3,                         #emit dir randomness
     150,                       #rotation speed
     0,                       #rotation damping
     ),
    ("explosion_flash", psf_billboard_3d | psf_randomize_size , "prt_sparks_mesh_1",
     3000, 0.8, 0.1, -0.00003, 50.0, 1.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
   (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.1, 7.1),   (1.0, 0.2),   #scale keys
     (0.4, 0.4, 4.1),           #emit box size
     (0.0, 0.0, 0.0),                 #emit velocity
     0.05,                       #emit dir randomness
     100.0,                       #rotation speed
     0.5,                        #rotation damping
    ),
    ("explosion_smoke", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_a",
     800, 13, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.6, 13.2),   (1, 10.0),    #scale keys
     (0.5, 0.5, 5.5),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     0.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("explosion_smoke2", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_a",
     1000, 11, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (10.0, 12.2),   (1, 10.0),    #scale keys
     (1.7, 1.7, 1.4),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     1.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("explosion_particles", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     4000, 20, 2, 0.58, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (1.7, 1.7, 4.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    ("cannon_ball_hit_particles", psf_randomize_size | psf_randomize_rotation,  "prtcl_dust_c",
     8000, 20, 1.5, 0.58, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1.8),   (1, 1.3),    #scale keys
     (1.7, 1.7, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    ("cannonball_ground_smoke", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_c",
     800, 3, 11, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.6, 3.2),   (1, 2.0),    #scale keys
     (0.2, 0.2, 3.8),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     0.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("cannonball_ground_smoke2", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_c",
     1000, 4, 11, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (10.0, 5.2),   (1, 2.0),    #scale keys
     (0.7, 0.7, 1.8),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     1.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("explosives_fuse_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     10, 1, 1.8, -0.0003, 20, 1.75,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.75), (0.85, 0),       #alpha keys
     (0.0, 0.7), (1, 0.4),      #red keys
     (0.0, 0.7),(1, 0.4),       #green keys
     (0.0, 0.7), (1, 0.4),      #blue keys
     (-0.04, 1.5),   (0.5, 5.75),   #scale keys
     (0.02, 0.02, 0.02),           #emit box size
     (-1.6, 0.6, 0.0),                 #emit velocity
     0.0,                        #emit dir randomness
    ),
   ("wallhit_smoke", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_a",
     800, 15, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.6, 19.2),   (1, 7.0),    #scale keys
     (1.5, 1.5, 5.5),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     0.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("wallhit_smoke2", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_a",
     900, 13, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (10.0, 9.2),   (1, 7.0),    #scale keys
     (1.7, 1.7, 2.4),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     1.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("wallhit_particles", psf_randomize_size | psf_randomize_rotation,  "prtcl_dust_d",
     250, 5, 2, 0.58, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1.3),   (1, 1.3),    #scale keys
     (1.1, 1.1, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    ("walldeserthit_particles", psf_randomize_size | psf_randomize_rotation,  "prtcl_dust_l",
     250, 5, 2, 0.58, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1.3),   (1, 1.3),    #scale keys
     (1.1, 1.1, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    
   ("fort_wallhit_smoke", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_a",
     20, 15, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.6, 9.2),   (1, 6.0),    #scale keys
     (0.5, 0.5, 5.5),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     0.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("fort_wallhit_smoke2", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_a",
     23, 13, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (10.0, 8.2),   (1, 6.0),    #scale keys
     (1.7, 1.7, 1.4),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     1.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("fort_wallhit_particles", psf_randomize_size | psf_randomize_rotation,  "prtcl_dust_e",
     10, 15, 2, 0.58, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1.3),   (1, 1.3),    #scale keys
     (1.1, 1.1, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    ("woodwallhit_particles", psf_randomize_size | psf_randomize_rotation,  "prtcl_dust_f",
     50, 5, 2, 0.58, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1.3),   (1, 1.3),    #scale keys
     (1.1, 1.1, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    ("musket_hit", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation| psf_global_emit_dir, "prtcl_dust_a",
      500, 3, 8, 0.2, 2, 20, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
      (0.0, 1), (1, 0),     #alpha keys
      (0.0, 0.95), (1, 0.95),          #red keys
      (0.0, 0.90), (1, 0.90),           #green keys
      (0.0, 0.70), (1, 0.70),          #blue keys
      (0, 3), (0.8, 5),  #scale keys
      (0, 0, 0),         #emit box size
      (0, 0, 10),               #emit velocity
      3,                      #emit dir randomness
      100,                     #rotation speed
      0.2,                       #rotation damping
    ),
	("musket_hit_particle", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation| psf_global_emit_dir, "prt_mesh_mud_1",
	2000, 2, 0.2, 2, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
      (0.0, 1), (1, 1),     #alpha keys
      (0.0, 0.1), (1, 0.1),          #red keys
      (0.0, 0.1), (1, 0.1),           #green keys
      (0.0, 0.1), (1, 0.1),          #blue keys
      (0.0, 0.125), (0.8, 0.125),  #scale keys
      (0, 0, 0),         #emit box size
      (0, 0, 8),               #emit velocity
      3,                      #emit dir randomness
      100,                     #rotation speed
      0.1,                       #rotation damping
    ),
	("musket_hit_objects", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
        500, 3.5, 6, 0, 2, 40, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 0),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.90), (1, 0.90),           #green keys
        (0.0, 0.80), (1, 0.80),          #blue keys
        (0, 1), (0.75, 10),  #scale keys
        (0, 0, 0),         #emit box size
        (0, -15, 0),               #emit velocity
        1,                      #emit dir randomness
        100,                     #rotation speed
        0.2,                       #rotation damping
    ),
    ("water_hit_a", psf_billboard_3d | psf_randomize_size | psf_randomize_rotation | psf_global_emit_dir, "prtcl_splash_b",
        80, 1.5, 4, 0.8, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 0),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.90), (1, 0.90),           #green keys
        (0.0, 0.70), (1, 0.70),          #blue keys
        (0, 0.3), (1, 2),  #scale keys
        (0, 0, 0),         #emit box size
        (0, 0, 6),               #emit velocity
        0,                      #emit dir randomness
        100,                     #rotation speed
        0.2,                       #rotation damping
        ),
		
		("water_hit_b",psf_randomize_size | psf_randomize_rotation | psf_turn_to_velocity|psf_global_emit_dir, "prtcl_splash_b",
      4, 3, 0, 0, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
      (0.0, 1), (1, 0),     #alpha keys
      (0.0, 0.95), (1, 0.95),          #red keys
      (0.0, 0.90), (1, 0.90),           #green keys
      (0.0, 0.70), (1, 0.70),          #blue keys
      (0, 1), (1, 5),  #scale keys
      (0.1, 0.1, 0),         #emit box size
      (0, 0, -0.01),               #emit velocity
      0,                      #emit dir randomness
      25,                     #rotation speed
      0.15,                       #rotation damping
    ),
    
    ("cannonball_water_hit_a", psf_billboard_3d | psf_randomize_size | psf_randomize_rotation | psf_global_emit_dir, "prtcl_splash_b",
        110, 2.5, 4, 0.5, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 0),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.90), (1, 0.90),           #green keys
        (0.0, 0.70), (1, 0.70),          #blue keys
        (0, 0.3), (1, 7),  #scale keys
        (0, 0, 0),         #emit box size
        (0, 0, 13),               #emit velocity
        0,                      #emit dir randomness
        100,                     #rotation speed
        0.2,                       #rotation damping
        ),
		
    ("cannonball_water_hit_b",psf_randomize_size | psf_randomize_rotation | psf_turn_to_velocity|psf_global_emit_dir, "prtcl_splash_b",
      4, 4, 0, 0, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
      (0.0, 1), (1, 0),     #alpha keys
      (0.0, 0.95), (1, 0.95),          #red keys
      (0.0, 0.90), (1, 0.90),           #green keys
      (0.0, 0.70), (1, 0.70),          #blue keys
      (0, 1), (1, 12),  #scale keys
      (0.1, 0.1, 0),         #emit box size
      (0, 0, -0.01),               #emit velocity
      0,                      #emit dir randomness
      25,                     #rotation speed
      0.15,                       #rotation damping
    ),
    
   ("mm_rain_drop",psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prtcl_drop",
      1, 0.288, 0, 0, 10.5, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
      (0.0, 0.8), (1, 0),     #alpha keys
      (0.0, 0.8), (1, 1),          #red keys
      (0.0, 0.8), (1, 1),           #green keys
      (0.0, 1), (1, 1),          #blue keys
      (0, 0.05), (1, 2.9),  #scale keys
      (0.3, 0.3, 0.03),         #emit box size
      (0, 0, 0),               #emit velocity
      0,                      #emit dir randomness
      0,                     #rotation speed
      0.5,                       #rotation damping
    ),

    ("mm_rain_wave",psf_randomize_size | psf_randomize_rotation | psf_turn_to_velocity|psf_global_emit_dir, "prtcl_splash_b",
      1, 1, 0, 0, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
      (0.0, 1), (1, 0),     #alpha keys
      (0.0, 0.95), (1, 0.95),          #red keys
      (0.0, 0.90), (1, 0.90),           #green keys
      (0.0, 0.70), (1, 0.70),          #blue keys
      (0, 1), (1, 1.5),  #scale keys
      (0.1, 0.1, 0),         #emit box size
      (0, 0, -0.01),               #emit velocity
      0,                      #emit dir randomness
      25,                     #rotation speed
      0.15,                       #rotation damping
    ),


    ("mm_watersplash", psf_emit_at_water_level , "prt_mesh_water_wave_1",
     5, 2.0, 0, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.03, 0.2), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 3),   (1.0, 10),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5,                        #rotation damping
    ),
  ("mm_bug_fly_1", psf_billboard_2d | psf_always_emit, "prtcl_dust_i",
     2, 18, 0.02, -0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 1.25),   (1, 1.25),    #scale keys
     (10, 5, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
      0.01,                        #emit dir randomness
      10,                        #rotation speed
      0,                         #rotation damping
    ),
  ("mm_bug_fly_2", psf_billboard_2d | psf_always_emit, "prtcl_dust_j",
     2, 18, 0.02, -0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 1.25),   (1, 1.25),    #scale keys
     (10, 5, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
      0.01,                        #emit dir randomness
      10,                        #rotation speed
      0,                         #rotation damping
    ),
  ("mm_bug_fly_3", psf_billboard_2d | psf_always_emit, "prtcl_dust_k",
     2, 18, 0.02, -0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 1.25),   (1, 1.25),    #scale keys
     (10, 5, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
      0.01,                        #emit dir randomness
      10,                        #rotation speed
      0,                         #rotation damping
    ),
    ("cannon_ball_hit_particles_snow", psf_randomize_size | psf_randomize_rotation,  "prtcl_dust_h",
     9000, 20, 1.5, 0.58, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1.8),   (1, 1.3),    #scale keys
     (1.7, 1.7, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    ("cannonball_ground_smoke_snow", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_h",
     1000, 3, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.6, 3.2),   (1, 2.0),    #scale keys
     (0.2, 0.2, 3.8),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     0.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("cannonball_ground_smoke2_snow", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_h",
     1300, 4, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (10.0, 5.2),   (1, 2.0),    #scale keys
     (0.7, 0.7, 1.8),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     1.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
    ("rocket_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_always_emit, "prtcl_dust_a", # psf_global_emit_dir psf_billboard_3d | psf_randomize_size psf_always_emit
     80, 12.6, 1.9, -0.0003, 90, 4,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.55), (0.549, 0),       #alpha keys
     (0.0, 0.99), (1, 0.99),      #red keys
     (0.0, 0.99),(1, 0.99),       #green keys
     (0.0, 0.99), (1, 0.99),      #blue keys
     (-0.07, 1.5),   (0.5, 3.75),   #scale keys
     (0.02, 0.02, 0.02),           #emit box size
     (-1.6, 0.6, 0.0),                 #emit velocity
     0.0,                        #emit dir randomness                       
    ),
  ("fort_complete_wallhit_smoke", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_a",
     20, 15, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.6, 9.2),   (1, 6.0),    #scale keys
     (0.5, 0.5, 5.5),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     0.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("fort_complete_wallhit_smoke2", psf_billboard_3d|psf_randomize_size,  "prtcl_dust_a",
     23, 13, 15, -0.04, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (10.0, 8.2),   (1, 6.0),    #scale keys
     (1.7, 1.7, 1.4),           #emit box size
     (-1.2, 0, 0.05),               #emit velocity
     1.8,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
   ("fort_complete_wallhit_particles", psf_randomize_size | psf_randomize_rotation,  "prtcl_dust_e",
     10, 15, 2, 0.58, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1.3),   (1, 1.3),    #scale keys
     (1.1, 1.1, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

  # PN END ***********************************************************************************************

  psys("game_rain", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
    number=500.0, life=0.5, damping=0.33, gravity=1.0, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(1.0, 0.3), (1.0, 0.3)],
    red=  [(1.0, 1.0), (1.0, 1.0)],
    green=[(1.0, 1.0), (1.0, 1.0)],
    blue= [(1.0, 1.0), (1.0, 1.0)],
    scale=[(1.0, 1.0), (1.0, 1.0)],
    emit_box=     (8.2, 8.2, 0.2),
    emit_velocity=(0.0, 0.0, -10.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.5),

  psys("game_snow", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_snow_fall_1",
    number=150.0, life=2.0, damping=0.2, gravity=0.1, turbulence_size=30.0, turbulence_strength=20.0,
    alpha=[(0.2, 1.0), (1.0, 1.0)],
    red=  [(1.0, 1.0), (1.0, 1.0)],
    green=[(1.0, 1.0), (1.0, 1.0)],
    blue= [(1.0, 1.0), (1.0, 1.0)],
    scale=[(1.0, 1.0), (1.0, 1.0)],
    emit_box=     (10.0, 10.0, 0.5),
    emit_velocity=(0.0, 0.0, -5.0),
    emit_direction_randomness=1.0,
    rotation_speed=200.0,
    rotation_damping=0.5),

  psys("game_blood", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
    number=500.0, life=0.65, damping=3.0, gravity=0.5, turbulence_size=0.0, turbulence_strength=0.0,
    alpha=[(0.0, 0.7), (0.7, 0.7)],
    red=  [(0.1, 0.7), (1.0, 0.7)],
    green=[(0.1, 0.7), (1.0, 0.7)],
    blue= [(0.1, 0.7), (1.0, 0.7)],
    scale=[(0.0, 0.015), (1.0, 0.018)],
    emit_box=     (0.0, 0.05, 0.0),
    emit_velocity=(0.0, 1.0, 0.3),
    emit_direction_randomness=0.9,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("game_blood_2", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_3",
    number=2000.0, life=0.6, damping=3.0, gravity=0.3, turbulence_size=0.0, turbulence_strength=0.0,
    alpha=[(0.0, 0.25), (0.7, 0.1)],
    red=  [(0.1, 0.7), (1.0, 0.7)],
    green=[(0.1, 0.7), (1.0, 0.7)],
    blue= [(0.1, 0.7), (1.0, 0.7)],
    scale=[(0.0, 0.15), (1.0, 0.35)],
    emit_box=     (0.01, 0.2, 0.01),
    emit_velocity=(0.2, 0.3, 0.0),
    emit_direction_randomness=0.3,
    rotation_speed=150.0,
    rotation_damping=0.0),

  psys("game_hoof_dust", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",
    number=5.0, life=2.0, damping=10.0, gravity=0.05, turbulence_size=10.0, turbulence_strength=39.0,
    alpha=[(0.2, 0.5), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 1.0)],
    green=[(0.0, 0.9), (1.0, 0.9)],
    blue= [(0.0, 0.78), (1.0, 0.78)],
    scale=[(0.0, 2.0), (1.0, 3.5)],
    emit_box=     (0.2, 0.3, 0.2),
    emit_velocity=(0.0, 0.0, 3.9),
    emit_direction_randomness=0.5,
    rotation_speed=130.0,
    rotation_damping=0.5),

  psys("game_hoof_dust_snow", psf_billboard_3d|psf_randomize_size, "prt_mesh_snow_dust_1",
    number=6.0, life=2.0, damping=3.5, gravity=1.0, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.2, 1.0), (1.0, 1.0)],
    red=  [(0.0, 1.0), (1.0, 1.0)],
    green=[(0.0, 1.0), (1.0, 1.0)],
    blue= [(0.0, 1.0), (1.0, 1.0)],
    scale=[(0.5, 4.0), (1.0, 5.7)],
    emit_box=     (0.2, 1.0, 0.1),
    emit_velocity=(0.0, 0.0, 1.0),
    emit_direction_randomness=2.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("game_hoof_dust_mud", psf_billboard_2d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_mud_1",
    number=5.0, life=.7, damping=10.0, gravity=3.0, turbulence_size=0.0, turbulence_strength=0.0,
    alpha=[(0.0, 1.0), (1.0, 1.0)],
    red=  [(0.0, 0.7), (1.0, 0.7)],
    green=[(0.0, 0.6), (1.0, 0.6)],
    blue= [(0.0, 0.4), (1.0, 0.4)],
    scale=[(0.0, 0.2), (1.0, 0.22)],
    emit_box=     (0.15, 0.5, 0.1),
    emit_velocity=(0.0, 0.0, 15.0),
    emit_direction_randomness=6.0,
    rotation_speed=200.0,
    rotation_damping=0.5),

  psys("game_water_splash_1", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_drop",
    number=20.0, life=0.85, damping=0.25, gravity=0.9, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.3, 0.5), (1.0, 0.0)],
    red=  [(1.0, 1.0), (1.0, 1.0)],
    green=[(1.0, 1.0), (1.0, 1.0)],
    blue= [(1.0, 1.0), (1.0, 1.0)],
    scale=[(0.0, 0.3), (1.0, 0.18)],
    emit_box=     (0.3, 0.2, 0.1),
    emit_velocity=(0.0, 1.2, 2.3),
    emit_direction_randomness=0.3,
    rotation_speed=50.0,
    rotation_damping=0.5),

  psys("game_water_splash_2", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_splash_b",
    number=30.0, life=0.4, damping=0.7, gravity=0.5, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.3, 1.0), (1.0, 0.3)],
    red=  [(1.0, 1.0), (1.0, 1.0)],
    green=[(1.0, 1.0), (1.0, 1.0)],
    blue= [(1.0, 1.0), (1.0, 1.0)],
    scale=[(0.0, 0.25), (1.0, 0.7)],
    emit_box=     (0.4, 0.3, 0.1),
    emit_velocity=(0.0, 1.3, 1.1),
    emit_direction_randomness=0.1,
    rotation_speed=50.0,
    rotation_damping=0.5),

  psys("game_water_splash_3", psf_emit_at_water_level, "prt_mesh_water_wave_1",
    number=5.0, life=2.0, damping=0.0, gravity=0.0, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.03, 0.2), (1.0, 0.0)],
    red=  [(1.0, 1.0), (1.0, 1.0)],
    green=[(1.0, 1.0), (1.0, 1.0)],
    blue= [(1.0, 1.0), (1.0, 1.0)],
    scale=[(0.0, 3.0), (1.0, 10.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.5),

  psys("torch_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
    number=50.0, life=0.35, damping=0.2, gravity=0.03, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.5, 0.8), (1.0, 0.0)],
    red=  [(0.5, 1.0), (1.0, 0.9)],
    green=[(0.5, 0.7), (1.0, 0.3)],
    blue= [(0.5, 0.2), (1.0, 0.0)],
    scale=[(0.0, 0.15), (0.4, 0.3)],
    emit_box=     (0.04, 0.04, 0.01),
    emit_velocity=(0.0, 0.0, 0.5),
    emit_direction_randomness=0.0,
    rotation_speed=200.0,
    rotation_damping=0.5),

  psys("fire_glow_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_fire_2",
    number=2.0, life=0.55, damping=0.2, gravity=0.0, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.5, 0.9), (1.0, 0.0)],
    red=  [(0.0, 0.9), (1.0, 0.9)],
    green=[(0.0, 0.7), (1.0, 0.7)],
    blue= [(0.0, 0.4), (1.0, 0.4)],
    scale=[(0.0, 2.0), (1.0, 2.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("fire_glow_fixed", psf_billboard_3d|psf_global_emit_dir, "prt_mesh_fire_2",
    number=4.0, life=100.0, damping=0.2, gravity=0.0, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(-0.01, 1.0), (1.0, 1.0)],
    red=  [(0.0, 0.9), (1.0, 0.9)],
    green=[(0.0, 0.7), (1.0, 0.7)],
    blue= [(0.0, 0.4), (1.0, 0.4)],
    scale=[(0.0, 2.0), (1.0, 2.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("torch_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prtcl_dust_a",
    number=15.0, life=0.5, damping=0.2, gravity=-0.2, turbulence_size=10.0, turbulence_strength=0.1,
    alpha=[(0.5, 0.25), (1.0, 0.0)],
    red=  [(0.0, 0.2), (1.0, 0.1)],
    green=[(0.0, 0.2), (1.0, 0.09)],
    blue= [(0.0, 0.2), (1.0, 0.08)],
    scale=[(0.0, 0.5), (0.8, 2.5)],
    emit_box=     (0.1, 0.1, 0.1),
    emit_velocity=(0.0, 0.0, 1.5),
    emit_direction_randomness=0.1,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("flue_smoke_short", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
    number=15.0, life=1.5, damping=0.1, gravity=-0.0, turbulence_size=10.0, turbulence_strength=12.0,
    alpha=[(0.0, 0.3), (1.0, 0.0)],
    red=  [(0.0, 0.2), (1.0, 0.1)],
    green=[(0.0, 0.2), (1.0, 0.09)],
    blue= [(0.0, 0.2), (1.0, 0.08)],
    scale=[(0.0, 1.5), (1.0, 7.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 1.5),
    emit_direction_randomness=0.1,
    rotation_speed=150.0,
    rotation_damping=0.8),

  psys("flue_smoke_tall", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
    number=15.0, life=3.0, damping=0.5, gravity=-0.0, turbulence_size=15.0, turbulence_strength=12.0,
    alpha=[(0.0, 0.35), (1.0, 0.0)],
    red=  [(0.0, 0.3), (1.0, 0.1)],
    green=[(0.0, 0.3), (1.0, 0.1)],
    blue= [(0.0, 0.3), (1.0, 0.1)],
    scale=[(0.0, 2.0), (1.0, 7.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 1.5),
    emit_direction_randomness=0.1,
    rotation_speed=150.0,
    rotation_damping=0.5),

  psys("war_smoke_tall", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
    number=5.0, life=12.0, damping=0.0, gravity=0.0, turbulence_size=7.0, turbulence_strength=7.0,
    alpha=[(0.0, 0.25), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 0.8)],
    green=[(0.0, 1.0), (1.0, 0.8)],
    blue= [(0.0, 1.0), (1.0, 0.8)],
    scale=[(0.0, 2.2), (1.0, 15.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 2.2),
    emit_direction_randomness=0.1,
    rotation_speed=100.0,
    rotation_damping=0.2),

  psys("ladder_dust_6m", psf_billboard_3d, "prt_mesh_smoke_1",
    number=700.0, life=0.9, damping=0.0, gravity=0.0, turbulence_size=7.0, turbulence_strength=7.0,
    alpha=[(0.0, 0.25), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 0.8)],
    green=[(0.0, 1.0), (1.0, 0.8)],
    blue= [(0.0, 1.0), (1.0, 0.8)],
    scale=[(0.0, 1.0), (1.0, 2.0)],
    emit_box=     (0.75, 0.75, 3.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.1,
    rotation_speed=100.0,
    rotation_damping=0.2),

  psys("ladder_dust_8m", psf_billboard_3d, "prt_mesh_smoke_1",
    number=900.0, life=0.9, damping=0.0, gravity=0.0, turbulence_size=7.0, turbulence_strength=7.0,
    alpha=[(0.0, 0.25), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 0.8)],
    green=[(0.0, 1.0), (1.0, 0.8)],
    blue= [(0.0, 1.0), (1.0, 0.8)],
    scale=[(0.0, 1.0), (1.0, 2.0)],
    emit_box=     (0.75, 0.75, 4.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.1,
    rotation_speed=100.0,
    rotation_damping=0.2),

  psys("ladder_dust_10m", psf_billboard_3d, "prt_mesh_smoke_1",
    number=1100.0, life=0.9, damping=0.0, gravity=0.0, turbulence_size=7.0, turbulence_strength=7.0,
    alpha=[(0.0, 0.25), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 0.8)],
    green=[(0.0, 1.0), (1.0, 0.8)],
    blue= [(0.0, 1.0), (1.0, 0.8)],
    scale=[(0.0, 1.0), (1.0, 2.0)],
    emit_box=     (0.75, 0.75, 5.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.1,
    rotation_speed=100.0,
    rotation_damping=0.2),

  psys("ladder_dust_12m", psf_billboard_3d, "prt_mesh_smoke_1",
    number=1300.0, life=0.9, damping=0.0, gravity=0.0, turbulence_size=7.0, turbulence_strength=7.0,
    alpha=[(0.0, 0.25), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 0.8)],
    green=[(0.0, 1.0), (1.0, 0.8)],
    blue= [(0.0, 1.0), (1.0, 0.8)],
    scale=[(0.0, 1.0), (1.0, 2.0)],
    emit_box=     (0.75, 0.75, 6.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.1,
    rotation_speed=100.0,
    rotation_damping=0.2),

  psys("ladder_dust_14m", psf_billboard_3d, "prt_mesh_smoke_1",
    number=1500.0, life=0.9, damping=0.0, gravity=0.0, turbulence_size=7.0, turbulence_strength=7.0,
    alpha=[(0.0, 0.25), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 0.8)],
    green=[(0.0, 1.0), (1.0, 0.8)],
    blue= [(0.0, 1.0), (1.0, 0.8)],
    scale=[(0.0, 1.0), (1.0, 2.0)],
    emit_box=     (0.75, 0.75, 7.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.1,
    rotation_speed=100.0,
    rotation_damping=0.2),

  psys("ladder_straw_6m", psf_randomize_size|psf_randomize_rotation, "prt_mesh_straw_1",
    number=700.0, life=1.0, damping=2.0, gravity=0.9, turbulence_size=10.0, turbulence_strength=2.0,
    alpha=[(0.1, 1.0), (1.0, 1.0)],
    red=  [(0.1, 0.6), (1.0, 0.6)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.4), (1.0, 0.4)],
    scale=[(0.0, 0.3), (1.0, 0.3)],
    emit_box=     (0.75, 0.75, 3.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=2.3,
    rotation_speed=200.0,
    rotation_damping=0.0),

  psys("ladder_straw_8m", psf_randomize_size|psf_randomize_rotation, "prt_mesh_straw_1",
    number=900.0, life=1.0, damping=2.0, gravity=0.9, turbulence_size=10.0, turbulence_strength=2.0,
    alpha=[(0.1, 1.0), (1.0, 1.0)],
    red=  [(0.1, 0.6), (1.0, 0.6)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.4), (1.0, 0.4)],
    scale=[(0.0, 0.3), (1.0, 0.3)],
    emit_box=     (0.75, 0.75, 4.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=2.3,
    rotation_speed=200.0,
    rotation_damping=0.0),

  psys("ladder_straw_10m", psf_randomize_size|psf_randomize_rotation, "prt_mesh_straw_1",
    number=1100.0, life=1.0, damping=2.0, gravity=0.9, turbulence_size=10.0, turbulence_strength=2.0,
    alpha=[(0.1, 1.0), (1.0, 1.0)],
    red=  [(0.1, 0.6), (1.0, 0.6)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.4), (1.0, 0.4)],
    scale=[(0.0, 0.3), (1.0, 0.3)],
    emit_box=     (0.75, 0.75, 5.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=2.3,
    rotation_speed=200.0,
    rotation_damping=0.0),

  psys("ladder_straw_12m", psf_randomize_size|psf_randomize_rotation, "prt_mesh_straw_1",
    number=1300.0, life=1.0, damping=2.0, gravity=0.9, turbulence_size=10.0, turbulence_strength=2.0,
    alpha=[(0.1, 1.0), (1.0, 1.0)],
    red=  [(0.1, 0.6), (1.0, 0.6)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.4), (1.0, 0.4)],
    scale=[(0.0, 0.3), (1.0, 0.3)],
    emit_box=     (0.75, 0.75, 6.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=2.3,
    rotation_speed=200.0,
    rotation_damping=0.0),

  psys("ladder_straw_14m", psf_randomize_size|psf_randomize_rotation, "prt_mesh_straw_1",
    number=1500.0, life=1.0, damping=2.0, gravity=0.9, turbulence_size=10.0, turbulence_strength=2.0,
    alpha=[(0.1, 1.0), (1.0, 1.0)],
    red=  [(0.1, 0.6), (1.0, 0.6)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.4), (1.0, 0.4)],
    scale=[(0.0, 0.3), (1.0, 0.3)],
    emit_box=     (0.75, 0.75, 7.5),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=2.3,
    rotation_speed=200.0,
    rotation_damping=0.0),

  psys("torch_fire_sparks", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_sparks_mesh_1",
    number=10.0, life=0.7, damping=0.2, gravity=0.0, turbulence_size=10.0, turbulence_strength=0.02,
    alpha=[(0.66, 1.0), (1.0, 0.0)],
    red=  [(0.1, 0.7), (1.0, 0.7)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.1), (1.0, 0.1)],
    scale=[(0.1, 0.05), (1.0, 0.05)],
    emit_box=     (0.1, 0.1, 0.1),
    emit_velocity=(0.0, 0.0, 0.9),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("fire_sparks_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_sparks_mesh_1",
    number=10.0, life=1.5, damping=0.2, gravity=0.0, turbulence_size=3.0, turbulence_strength=10.0,
    alpha=[(0.6, 1.0), (1.0, 1.0)],
    red=  [(0.1, 0.7), (1.0, 0.7)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.1), (1.0, 0.1)],
    scale=[(0.1, 0.07), (1.0, 0.03)],
    emit_box=     (0.17, 0.17, 0.01),
    emit_velocity=(0.0, 0.0, 1.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("brazier_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
    number=25.0, life=0.5, damping=0.1, gravity=0.0, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.5, 0.4), (1.0, 0.0)],
    red=  [(0.5, 1.0), (1.0, 0.9)],
    green=[(0.5, 0.7), (1.0, 0.3)],
    blue= [(0.5, 0.2), (1.0, 0.0)],
    scale=[(0.1, 0.2), (1.0, 0.5)],
    emit_box=     (0.1, 0.1, 0.01),
    emit_velocity=(0.0, 0.0, 0.4),
    emit_direction_randomness=0.0,
    rotation_speed=100.0,
    rotation_damping=0.2),

  psys("cooking_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
    number=25.0, life=0.35, damping=0.1, gravity=0.03, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.5, 0.8), (1.0, 0.0)],
    red=  [(0.5, 0.5*1.0), (1.0, 0.3*0.9)],
    green=[(0.5, 0.5*0.7), (1.0, 0.3*0.3)],
    blue= [(0.5, 0.5*0.2), (1.0, 0.0)],
    scale=[(0.1, 0.5), (1.0, 1.0)],
    emit_box=     (0.05, 0.05, 0.01),
    emit_velocity=(0.0, 0.0, 1.0),
    emit_direction_randomness=0.0,
    rotation_speed=200.0,
    rotation_damping=0.0),

  psys("cooking_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
    number=4.0, life=4.0, damping=0.1, gravity=0.0, turbulence_size=3.0, turbulence_strength=5.0,
    alpha=[(0.2, 0.20), (1.0, 0.0)],
    red=  [(0.0, 0.8), (1.0, 1.0)],
    green=[(0.0, 0.8), (1.0, 1.0)],
    blue= [(0.0, 0.85), (1.0, 1.0)],
    scale=[(0.0, 0.65), (1.0, 3.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 1.2),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("food_steam", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_steam_1",
    number=3.0, life=1.0, damping=0.0, gravity=0.0, turbulence_size=8.0, turbulence_strength=1.0,
    alpha=[(0.5, 0.1), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 0.1)],
    green=[(0.0, 1.0), (1.0, 0.1)],
    blue= [(0.0, 1.0), (1.0, 0.1)],
    scale=[(0.0, 0.2), (0.9, 0.5)],
    emit_box=     (0.05, 0.05, 0.0),
    emit_velocity=(0.0, 0.0, 0.1),
    emit_direction_randomness=0.0,
    rotation_speed=100.0,
    rotation_damping=0.5),

  psys("candle_light", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_candle_fire_1",
    number=7.0, life=1.1, damping=0.6, gravity=-0.0, turbulence_size=10.0, turbulence_strength=0.2,
    alpha=[(0.1, 0.5), (1.0, 0.0)],
    red=  [(0.5, 1.0), (1.0, 0.9)],
    green=[(0.5, 0.6), (1.0, 0.1)],
    blue= [(0.5, 0.2), (1.0, 0.0)],
    scale=[(0.3, 0.2), (1.0, 0.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 0.09),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("candle_light_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_candle_fire_1",
    number=4.0, life=1.1, damping=0.6, gravity=-0.0, turbulence_size=10.0, turbulence_strength=0.2,
    alpha=[(0.1, 0.8), (1.0, 0.0)],
    red=  [(0.5, 1.0), (1.0, 0.9)],
    green=[(0.5, 0.6), (1.0, 0.1)],
    blue= [(0.5, 0.2), (1.0, 0.0)],
    scale=[(0.3, 0.13), (1.0, 0.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 0.06),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("lamp_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
    number=10.0, life=0.8, damping=0.6, gravity=-0.0, turbulence_size=10.0, turbulence_strength=0.4,
    alpha=[(0.1, 0.5), (1.0, 0.0)],
    red=  [(0.5, 1.0), (1.0, 0.9)],
    green=[(0.5, 0.8), (1.0, 0.1)],
    blue= [(0.5, 0.4), (1.0, 0.0)],
    scale=[(0.3, 0.35), (0.9, 0.5)],
    emit_box=     (0.01, 0.01, 0.0),
    emit_velocity=(0.0, 0.0, 0.35),
    emit_direction_randomness=0.03,
    rotation_speed=100.0,
    rotation_damping=0.5),

  ("dummy_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 3, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 0.7),   (1, 2.2),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("dummy_straw", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     500, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("dummy_smoke_big", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 9, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.9), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 5),   (1, 15.0),    #scale keys
     (3, 3, 5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("dummy_straw_big", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     500, 3, 2, 2.0, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.8),   (1, 0.8),    #scale keys
     (3, 3, 3),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

  ("gourd_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 3, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 0.5),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("gourd_piece_1", psf_randomize_rotation,  "prt_gourd_piece_1",
     15, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    
    ("gourd_piece_2", psf_randomize_size | psf_randomize_rotation,  "prt_gourd_piece_2",
     50, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

  ("fire_fly_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_sparks_mesh_1",
     2, 5, 1.2, 0, 50, 7,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0.2),        #alpha keys
     (0.5, .7), (1, 0.7),      #red keys
     (0.5, 0.8), (1, 0.8),      #green keys
     (0.5, 1), (1, 1),      #blue keys
     (0, 0.1),   (1, 0.1),    #scale keys
     (20, 20, 0.5),             #emit box size
     (0, 0, 0),              #emit velocity
      5,                        #emit dir randomness
      0,                        #rotation speed
      0,                         #rotation damping
    ),

     ("bug_fly_1", psf_billboard_2d | psf_always_emit, "prt_mesh_rose_a",
     20, 8, 0.02, 0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (10, 5, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
      0.01,                        #emit dir randomness
      10,                        #rotation speed
      0,                         #rotation damping
    ),

  ("moon_beam_1", psf_billboard_2d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_mesh_moon_beam",#prt_mesh_moon_beam
     2, 4, 1.2, 0, 0, 0,          #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1), (1, 0),            #alpha keys
     (0, 0.4), (1, 0.4),                #red keys
     (0, 0.5), (1, 0.5),                #green keys
     (0, 0.6), (1, 0.6),                #blue keys
     (0, 2),   (1, 2.2),        #scale keys
     (1, 1, 0.2),                 #emit box size
     (0, 0, -2),                     #emit velocity
      0,                            #emit dir randomness
      100,                          #rotation speed
      0.5,                          #rotation damping
       ),

   psys("moon_beam_particle_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_sparks_mesh_1",
    number=10.0, life=1.5, damping=1.5, gravity=0.0, turbulence_size=10.0, turbulence_strength=10.0,
    alpha=[(0.5, 1.0), (1.0, 0.0)],
    red=  [(0.5, 0.5), (1.0, 0.5)],
    green=[(0.5, 0.7), (1.0, 0.7)],
    blue= [(0.5, 1.0), (1.0, 1.0)],
    scale=[(0.0, 0.1), (1.0, 0.1)],
    emit_box=     (1.0, 1.0, 4.0),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.5,
    rotation_speed=0.0,
    rotation_damping=0.0),

  ("night_smoke_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_dust_1",
     5, 10, 1.5, 0, 50, 2,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 0.1), (1, 0),        #alpha keys
     (0.5, 0.5), (1, 0.5),      #red keys
     (0.5, 0.5), (1, 0.5),      #green keys
     (0.5, 0.5), (1, 0.6),      #blue keys
     (0, 10),   (1, 10),        #scale keys
     (25, 25, 0.5),               #emit box size
     (0, 1, 0),                 #emit velocity
      2,                        #emit dir randomness
      20,                       #rotation speed
      1,                         #rotation damping
       ),
#-*-*-*- Fire For Fireplace -*-*-*-#
    ("fireplace_fire_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.8, 0.2, -0.1, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.2),   (1, 0.7),   #scale keys
     (0.2, 0.1, 0.01),      #emit box size
     (0, 0, 0.2),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5,                        #rotation damping
    ),
    ("fireplace_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     35, 0.6, 0.2, -0.2, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.4),   (1, 1),   #scale keys
     (0.4, 0.2, 0.01),            #emit box size
     (0, 0, 0.4),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5,                        #rotation damping
    ),

  psys("village_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
    number=50.0, life=1.0, damping=0.0, gravity=-1.2, turbulence_size=25.0, turbulence_strength=10.0,
    alpha=[(0.2, 0.7), (1.0, 0.0)],
    red=  [(0.2, 1.0), (1.0, 0.9)],
    green=[(0.2, 0.7), (1.0, 0.3)],
    blue= [(0.2, 0.2), (1.0, 0.0)],
    scale=[(0.0, 2.0), (1.0, 6.0)],
    emit_box=     (2.2, 2.2, 0.2),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.0,
    rotation_speed=250.0,
    rotation_damping=0.3),

  psys("village_fire_smoke_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
    number=30.0, life=2.0, damping=0.3, gravity=-1.0, turbulence_size=50.0, turbulence_strength=10.0,
    alpha=[(0.5, 0.15), (1.0, 0.0)],
    red=  [(0.2, 0.4), (1.0, 0.2)],
    green=[(0.2, 0.4), (1.0, 0.2)],
    blue= [(0.2, 0.4), (1.0, 0.2)],
    scale=[(0.0, 6.0), (1.0, 8.0)],
    emit_box=     (2.0, 2.0, 1.0),
    emit_velocity=(0.0, 0.0, 5.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.1),

  psys("map_village_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
    number=20.0, life=1.0, damping=0.0, gravity=-0.2, turbulence_size=3.0, turbulence_strength=3.0,
    alpha=[(0.2, 0.7), (1.0, 0.0)],
    red=  [(0.2, 1.0), (1.0, 0.9)],
    green=[(0.2, 0.7), (1.0, 0.3)],
    blue= [(0.2, 0.2), (1.0, 0.0)],
    scale=[(0.0, 0.15), (1.0, 0.45)],
    emit_box=     (0.2, 0.2, 0.02),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.0,
    rotation_speed=250.0,
    rotation_damping=0.3),

  psys("map_village_fire_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
    number=25.0, life=2.5, damping=0.3, gravity=-0.15, turbulence_size=3.0, turbulence_strength=3.0,
    alpha=[(0.5, 0.15), (1.0, 0.0)],
    red=  [(0.2, 0.4), (1.0, 0.3)],
    green=[(0.2, 0.4), (1.0, 0.3)],
    blue= [(0.2, 0.4), (1.0, 0.3)],
    scale=[(0.0, 0.6), (1.0, 0.9)],
    emit_box=     (0.2, 0.2, 0.1),
    emit_velocity=(0.0, 0.0, 0.03),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.1),

  psys("map_village_looted_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
    number=20.0, life=3.0, damping=0.3, gravity=-0.11, turbulence_size=3.0, turbulence_strength=2.0,
    alpha=[(0.5, 0.15), (1.0, 0.0)],
    red=  [(0.2, 0.5), (1.0, 0.5)],
    green=[(0.2, 0.5), (1.0, 0.5)],
    blue= [(0.2, 0.5), (1.0, 0.5)],
    scale=[(0.0, 0.7), (1.0, 1.3)],
    emit_box=     (0.2, 0.2, 0.1),
    emit_velocity=(0.0, 0.0, 0.015),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.1),

  ("dungeon_water_drops", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
     1, 1, 0.33, 0.8, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (1.0, 0.2), (1, 0.2),      #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 0.8),   (1.0, 0.8),  #scale keys
     (0.05, 0.05, 0.5),         #emit box size
     (0, 0, -5.0),              #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
     ),

  psys("wedding_rose", psf_billboard_2d|psf_always_emit, "prt_mesh_rose_a",
    number=50.0, life=8.0, damping=0.02, gravity=0.025, turbulence_size=1.0, turbulence_strength=5.0,
    alpha=[(0.0, 1.0), (1.0, 1.0)],
    red=  [(0.0, 0.5), (1.0, 0.5)],
    green=[(0.0, 0.5), (1.0, 0.5)],
    blue= [(0.0, 0.5), (1.0, 0.5)],
    scale=[(0.0, 0.25), (1.0, 0.25)],
    emit_box=     (4.0, 4.0, 0.1),
    emit_velocity=(0.0, 0.0, -0.9),
    emit_direction_randomness=0.01,
    rotation_speed=10.0,
    rotation_damping=0.0),

  ("sea_foam_a", psf_turn_to_velocity | psf_always_emit|psf_randomize_size, "prt_foam_a",
     1, 3.0, 1, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.7, 0.1), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 4),   (1.0, 4.5),   #scale keys
     (10.0, 1.0, 0),           #emit box size
     (0, 1, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5,                        #rotation damping
    ),
    ("fall_leafs_a", psf_billboard_2d | psf_always_emit, "prt_mesh_yrellow_leaf_a",
     1, 9, 0, 0.025, 4, 4,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),            #alpha keys
     (0, 0.5), (1, 0.5),        #red keys
     (0, 0.5), (1, 0.5),        #green keys
     (0, 0.5), (1, 0.5),        #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (4, 4, 4),                 #emit box size
     (0, 0.01, -0.9),           #emit velocity
      0.02,                     #emit dir randomness
      15,                       #rotation speed
      0,                        #rotation damping
    ),

  psys("wood_heap_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
    number=50.0, life=0.7, damping=0.0, gravity=-0.8, turbulence_size=25.0, turbulence_strength=10.0,
    alpha=[(0.2, 0.7), (1.0, 0.0)],
    red=  [(0.2, 1.0), (1.0, 0.9)],
    green=[(0.2, 0.7), (1.0, 0.3)],
    blue= [(0.2, 0.2), (1.0, 0.0)],
    scale=[(0.0, 1.0), (1.0, 3.0)],
    emit_box=     (1.0, 1.0, 0.3),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.0,
    rotation_speed=250.0,
    rotation_damping=0.3),

  psys("wood_heap_fire_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
    number=30.0, life=3.0, damping=0.3, gravity=-0.2, turbulence_size=50.0, turbulence_strength=10.0,
    alpha=[(0.5, 0.15), (1.0, 0.0)],
    red=  [(0.2, 0.4), (1.0, 0.2)],
    green=[(0.2, 0.4), (1.0, 0.2)],
    blue= [(0.2, 0.4), (1.0, 0.2)],
    scale=[(0.0, 3.0), (1.0, 3.0)],
    emit_box=     (1.0, 1.0, 1.0),
    emit_velocity=(0.0, 0.0, 3.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.1),

  psys("wood_heap_fire_sparks", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
    number=10.0, life=1.5, damping=0.2, gravity=0.1, turbulence_size=3.0, turbulence_strength=10.0,
    alpha=[(0.6, 1.0), (1.0, 1.0)],
    red=  [(0.1, 0.7), (1.0, 0.7)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.1), (1.0, 0.1)],
    scale=[(0.1, 0.1), (1.0, 0.03)],
    emit_box=     (0.7, 0.7, 0.3),
    emit_velocity=(0.0, 0.0, 3.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("cut_wood", psf_randomize_size|psf_randomize_rotation, "prt_mesh_straw_1",
    number=100.0, life=10.0, damping=2.0, gravity=0.9, turbulence_size=7.0, turbulence_strength=2.0,
    alpha=[(0.1, 1.0), (1.0, 1.0)],
    red=  [(0.1, 0.6), (1.0, 0.6)],
    green=[(0.1, 0.5), (1.0, 0.5)],
    blue= [(0.1, 0.4), (1.0, 0.4)],
    scale=[(0.0, 0.3), (1.0, 0.3)],
    emit_box=     (0.5, 0.1, 0.1),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=2.3,
    rotation_speed=200.0,
    rotation_damping=0.0),

  psys("fish_rise", 0, "pw_water_splash",
    number=1.0, life=3.0, damping=0.0, gravity=0.0, turbulence_size=10.0, turbulence_strength=0.0,
    alpha=[(0.1, 0.2), (1.0, 0.0)],
    red=  [(1.0, 1.0), (1.0, 1.0)],
    green=[(1.0, 1.0), (1.0, 1.0)],
    blue= [(1.0, 1.0), (1.0, 1.0)],
    scale=[(0.0, 1.0), (1.0, 10.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("throw_wheat", psf_randomize_rotation, "pw_thrown_wheat",
    number=300.0, life=2.0, damping=0.01, gravity=0.3, turbulence_size=15.0, turbulence_strength=5.0,
    alpha=[(0.1, 1.0), (1.0, 1.0)],
    red=  [(0.1, 1.0), (1.0, 1.0)],
    green=[(0.1, 1.0), (1.0, 1.0)],
    blue= [(0.1, 1.0), (1.0, 1.0)],
    scale=[(0.1, 1.0), (1.0, 1.0)],
    emit_box=     (0.1, 0.0, 0.0),
    emit_velocity=(0.0, 8.0, 0.0),
    emit_direction_randomness=2.0,
    rotation_speed=100.0,
    rotation_damping=0.2),

  psys("grape_leaf", psf_billboard_2d|psf_randomize_size|psf_always_emit, "pw_grape_leaf",
    number=1.0, life=5.0, damping=0.0, gravity=0.2, turbulence_size=4.0, turbulence_strength=4.0,
    alpha=[(0.0, 1.0), (1.0, 1.0)],
    red=  [(0.0, 0.5), (1.0, 0.5)],
    green=[(0.0, 0.5), (1.0, 0.5)],
    blue= [(0.0, 0.5), (1.0, 0.5)],
    scale=[(0.0, 0.25), (1.0, 0.25)],
    emit_box=     (0.1, 0.1, 0.1),
    emit_velocity=(0.2, 0.2, -0.5),
    emit_direction_randomness=0.03,
    rotation_speed=30.0,
    rotation_damping=0.0),

  psys("wine_press_fill", 0, "pw_wine_press_wine",
    number=1.0, life=5.0, damping=0.0, gravity=0.0, turbulence_size=0.0, turbulence_strength=0.0,
    alpha=[(0.3, 1.0), (1.0, 1.0)],
    red=  [(0.1, 1.0), (1.0, 1.0)],
    green=[(0.1, 1.0), (1.0, 1.0)],
    blue= [(0.1, 1.0), (1.0, 1.0)],
    scale=[(0.1, 1.0), (1.0, 1.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 0.06),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("brewing_steam", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_steam_1",
    number=3.0, life=5.0, damping=0.1, gravity=0.0, turbulence_size=8.0, turbulence_strength=1.0,
    alpha=[(0.5, 0.3), (1.0, 0.0)],
    red=  [(0.0, 1.0), (1.0, 0.1)],
    green=[(0.0, 1.0), (1.0, 0.1)],
    blue= [(0.0, 1.0), (1.0, 0.1)],
    scale=[(0.0, 0.2), (0.9, 1.5)],
    emit_box=     (0.05, 0.05, 0.0),
    emit_velocity=(0.0, 0.0, 0.4),
    emit_direction_randomness=0.0,
    rotation_speed=100.0,
    rotation_damping=0.5),

  psys("target_agent", psf_global_emit_dir, "pw_target_agent",
    number=5.0, life=0.5, damping=0.5, gravity=-0.1, turbulence_size=0.0, turbulence_strength=0.0,
    alpha=[(0.8, 1.0), (1.0, 0.0)],
    red=  [(0.2, 1.0), (1.0, 0.5)],
    green=[(0.2, 0.1), (1.0, 0.1)],
    blue= [(0.2, 0.1), (1.0, 0.1)],
    scale=[(0.0, 2.0), (1.0, 1.0)],
    emit_box=     (0.0, 0.0, 0.0),
    emit_velocity=(0.0, 0.0, 0.0),
    emit_direction_randomness=0.0,
    rotation_speed=0.0,
    rotation_damping=0.0),

  psys("dynamic_rain", psf_billboard_2d|psf_global_emit_dir, "prtcl_rain",
    number=3.0, life=1.0, damping=0.3, gravity=1.0,
    alpha=[(0.0, 0.0), (0.4, 0.3)],
    emit_box=     (2.0, 2.0, 0.2),
    emit_velocity=(0.0, 0.0, -10.0),
    emit_direction_randomness=0.01),

  psys("dynamic_snow", psf_billboard_3d|psf_global_emit_dir|psf_randomize_size|psf_randomize_rotation, "prt_mesh_snow_fall_1",
    number=1.0, life=2.0, damping=0.2, gravity=0.1, turbulence_size=30.0, turbulence_strength=20.0,
    alpha=[(0.2, 1.0), (1.0, 1.0)],
    emit_box=     (2.0, 2.0, 0.2),
    emit_velocity=(0.0, 0.0, -5.0),
    emit_direction_randomness=1.0,
    rotation_speed=200.0,
    rotation_damping=0.5),

]
