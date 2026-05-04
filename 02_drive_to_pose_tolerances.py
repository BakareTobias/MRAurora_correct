"""Advanced: ``drive_to_pose`` on TWO_WHEEL — goal pose, position/angle tolerances, then static plot.

``drive_to_pose`` chains rotate-then-drive segments until (x, y) and θ match the target.
It is *not* available for Ackermann (use explicit arcs in your own code).
"""
#Makes Python store type annotations as strings and not evaluate them at definition time.
from __future__ import annotations

import math
import os
from pathlib import Path

import matplotlib.pyplot as plt
from amr.kinematics.integration import wrap_pi
import AuroraMR as amr

#Tells Matplotlib to use the Agg backend if no other backend is set (e.g., in headless environments). 
#This allows us to create and save plots without requiring a display server.
os.environ.setdefault("MPLBACKEND", "Agg")

#store current directory as a variable 
here = Path(__file__).resolve().parent


def main() -> None:
    #This function creates a motion session with a two-wheel kinematic model
    #The robot has a goal defined, and drives towards it
    #The error between the final pose and the goal is calculated and printed,
    #along with a plot of the motion and the goal position.
    #A plot of the motion is created, with the goal position highlighted, and saved to a file.

    s = amr.MotionSession.create(
        amr.pose(0, 0, 0),
        amr.KinematicsModel.TWO_WHEEL,
        dt=0.015,
        unicycle=amr.TwoWheelParams(max_linear_speed=1.0, max_angular_speed=1.2),
    )
    goal = amr.pose(1.2, 0.8, math.radians(40))
    s.drive_to_pose(
        goal,
        linear_speed=0.55,
        angular_speed=0.9,
        position_tol=0.07,
        angle_tol=0.08,
    )
    err_xy = math.hypot(s.pose.x - goal.x, s.pose.y - goal.y)
    err_th = abs(wrap_pi(s.pose.theta - goal.theta))
    print("Goal:", goal)
    print("Final:", s.pose)
    print(f"Position error: {err_xy:.4f} m   angle error: {err_th:.4f} rad")

    fig, ax = plt.subplots(figsize=(6, 6))
    amr.plot_motion(s, ax=ax, show=False)
    ax.scatter([goal.x], [goal.y], c="magenta", s=40, zorder=10, label="goal (x, y)")
    ax.legend(loc="upper left")
    out = here / "adv_drive_to_pose.png"
    fig.savefig(out, dpi=150)
    print("Wrote", out)


if __name__ == "__main__":
    main()
