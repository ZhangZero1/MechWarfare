


#Configuration Constants~~~~~~~~~~~~

#Designed for the default mech configuration in mind

# Calibration
Config_Fname = "myConfigLegs" # Name of the calibration config file for leg servos. This is a path to the file (although you can put the filename if it's in the same directory)

# Physcial Constants:
L1major = 4.5           # Length of the upper part of the leg (thigh), in cm.
L1minor = 3.9           # Length of the lower part of the leg (foot), in cm.
servo_base_extend = 3.0 # the amount the elevation servo protrudes from the base, in cm.
square_offset = 11.5    # Length of one side of the square that the chassis servos make. This code assumes the mech is in a square configuration.

# Software Constants:
effectDist = 1.5       # distance, in cm, before the leg starts to drop as it reaches its target. It follows a parabolic trajectory.
walkHeight = -6.0      # How far below the chassis the leg tip is when walking at normal height.
liftHeight = -3.5      # How far below the chassis the leg tip is when a leg is lifted up.
                       # A higher stride height allows the mech to overcome obstacles easier, but makes it less stable.
l_sweep = 90.0         # How much sweep angle the chassis servos have, in degrees.
                       # 90 is generally a good standard.
                       # Increasing this increases stride area, but can also run the risk of collision with other legs. Also tends to reduce stability.
l_extend = 9.5         # When the mech is standing at the standard walk height, how far can the legs extend from the chassis (in cm).
                       # This should be no longer than what the leg can physically extend to.
                       # Artificially smaller values can sometimes increase stability.
triangleExpand = 0.2   # Used to expand the stability triangle used in internal calculations slightly, in cm.
                       # Allows gait transition fluidity, but reduces stability. It should be a small value.
max_speed = 60.0       # Maximum translational speed the mech legs will be allowed to move. This effects ALL movements of the legs, so it should be a moderately high value.
                       # For reference, this dictates what 100% speed it will attempt to move if getting a movement command.
                       # Typically, set this moderately high, but have the client side limit the speed commands it sends from 15% to 50%
rad_max = 2.0          # Maximum Rotational speed the mech will attempt. Values greater than 2.5 tend to result in spastic motions.
aim_update_const = 5.0 # A multiplier on how fast the turret will pan. Slower values allow for greater stability, but less responsivity.
pitchMax = 2000        # Highest period the pitch servo will go. In Microseconds.
pitchMin = 1000        # Minimum period the pitch servo will go. In Microseconds.
yawMax = 2000          # Highest period the yaw servo will go. In Microseconds.
yawMin = 1000          # Minimum period the yaw servo will go. In Microseconds.

#Unused Constants (Some stuff used for the advanced linkage design)
u_Length = 5.25 
n_Length = 5.25
#servo2_x_offset = 2.7
#servo2_y_offset = 2.0

# Some other information (defined later in the code; not needed to edit during normal operation.)
#legPort = 8090 #Port where the mech listens for leg commands.
#turretPort = 8091 #port where the mech listens for turret commands.

#GLOBAL VARIABLES-----------------------------
#is our program running?
is_running = True

pitchVar = 1500 # These variables hold the pitch & yaw values for the turret.
yawVar = 1500
