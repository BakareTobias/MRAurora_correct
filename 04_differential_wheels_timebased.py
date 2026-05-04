"""Advanced: Differential drive — ``differential_drive_wheels`` (fixed wheel speeds, time-limited) and arcing.

Use this to script **tank-style** turns: unequal left/right for a fixed *duration* (seconds), not a spatial distance.
"""
#Makes Python store type annotations as strings and not evaluate them at definition time.
from __future__ import annotations

import math
import os
from pathlib import Path

import matplotlib.pyplot as plt

import AuroraMR as amr


#Tells Matplotlib to use the Agg backend if no other backend is set (e.g., in headless environments). 
#This allows us to create and save plots without requiring a display server.
os.environ.setdefault("MPLBACKEND", "Agg")

#store current directory as a variable 
here = Path(__file__).resolve().parent

def main() -> None:
    #This function creates a motion session with a  differential kinematic model
    #The robot is controlled using a combination of forward wheel commands and 
    #time-based differential drive commands to create a specific motion pattern.
    #A plot of the motion is created, showing path from initial to final position, and saved to a file.
    
    s = amr.MotionSession.create(
        amr.pose(0, 0, 0),
        amr.KinematicsModel.DIFFERENTIAL,
        dt=0.01,
        differential=amr.DifferentialParams(track_width=0.42, max_wheel_speed=2.5),
    )
    s.forward_wheels(0.7, 0.75)
    s.differential_drive_wheels(0.2, 1.1, duration=1.0)
    s.forward_wheels(0.3, 0.6)
    s.turn_left(math.pi / 5, 1.0)

    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    amr.plot_motion(s, ax=ax, show=False)
    ax.set_title("Differential: forward_wheels + time-based turn + turn_left")
    out = here / "adv_differential_wheels.png"
    fig.savefig(out, dpi=150)
    print("Wrote", out, "— final pose", s.pose)


if __name__ == "__main__":
    main()
