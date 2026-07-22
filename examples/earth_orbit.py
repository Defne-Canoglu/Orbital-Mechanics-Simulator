import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import numpy as np
import matplotlib.pyplot as plt

from src.orbit import simulate_orbit

# Earth parameters
EARTH_RADIUS = 6.371e6
EARTH_MASS = 5.972e24
G = 6.67430e-11


# Low Earth Orbit altitude (similar to ISS)
altitude = 400000  # meters


# Initial spacecraft position
initial_position = np.array([
    EARTH_RADIUS + altitude,
    0
])


# Circular orbital velocity
orbital_velocity = np.sqrt(
    G * EARTH_MASS /
    (EARTH_RADIUS + altitude)
)


# Initial spacecraft velocity
initial_velocity = np.array([
    0,
    orbital_velocity
])


# Run simulation
trajectory = simulate_orbit(
    initial_position,
    initial_velocity,
    timestep=1,
    steps=6000
)


# Create plot
plt.figure(figsize=(8, 8))


plt.plot(
    trajectory[:, 0],
    trajectory[:, 1],
    label="Satellite trajectory"
)


# Draw Earth
earth = plt.Circle(
    (0, 0),
    EARTH_RADIUS,
    alpha=0.3
)

plt.gca().add_patch(earth)


plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")

plt.title(
    "Low Earth Orbit Simulation"
)

plt.axis("equal")
plt.grid()
plt.legend()


# Save result
plt.savefig(
    "results/orbit.png",
    dpi=300
)


plt.show()