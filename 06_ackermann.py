"""Part 6 — Ackermann: four wheels, pose at rear axle, front steers (car-like)."""

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

#Tells Matplotlib to use the Agg backend if no other backend is set (e.g., in headless environments). 
#This allows us to create and save plots without requiring a display server.
os.environ.setdefault("MPLBACKEND", "Agg")

#This function creates a motion session with an ackermann kinematic model
#The robot is controlled using a combination of forward wheel commands and 
#time-based differential drive commands to create a specific motion pattern.
s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.ACKERMANN,
    dt=0.02,
    ackermann=amr.AckermannParams(wheelbase=0.000001, track_width=0.35, max_steering_angle=0.5, max_speed=1.0),
)
s.forward(1.0, 0.5)
s.turn_left(math.radians(30), 0.6)

#The robot path is animated, showing motion with time. poses are logged every 10 frames, and printed to console.
#A plot of the motion is created, showing path from initial to final position, and saved to a file.
fig, ax = plt.subplots(figsize=(5, 5))
amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
fig.savefig(os.path.join(os.path.dirname(__file__), "class_ackermann.png"), dpi=120)
print("Done. Final pose:", s.pose)
