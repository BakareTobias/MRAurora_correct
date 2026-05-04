"""Part 5 — Differential drive: left/right wheel speeds, same (v, omega) world motion idea."""

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

#Tells Matplotlib to use the Agg backend if no other backend is set (e.g., in headless environments). 
#This allows us to create and save plots without requiring a display server.
os.environ.setdefault("MPLBACKEND", "Agg")

#This function creates a motion session with a  differential kinematic model
#The robot is controlled using a combination of forward wheel commands and 
#time-based differential drive commands to create a specific motion pattern.
s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.DIFFERENTIAL,
    dt=0.02,
    differential=amr.DifferentialParams(track_width=0.4, max_wheel_speed=2.0),
)
s.forward_wheels(1.0, 1.0)  # 1 m forward (both wheels same speed)
s.turn_left(math.pi / 4, 1.0)

#The robot path is animated, showing robot motion with time. poses are logged every 10 frames, and printed to console.
amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)

"""fig, ax = plt.subplots(figsize=(5, 5))
amr.plot_motion(s, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "class_differential.png"), dpi=120)
print("Done. Final pose:", s.pose)
"""