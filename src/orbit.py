import numpy as np
from .physics import gravitational_acceleration


def simulate_orbit(
        initial_position,
        initial_velocity,
        timestep,
        steps
):
    """
    Simulate spacecraft trajectory.

    Parameters
    ----------
    initial_position : array
        Initial spacecraft position [x,y]

    initial_velocity : array
        Initial spacecraft velocity [vx,vy]

    timestep : float
        Simulation time step (seconds)

    steps : int
        Number of simulation steps

    Returns
    -------
    numpy array
        Spacecraft positions over time
    """

    position = np.array(
        initial_position,
        dtype=float
    )

    velocity = np.array(
        initial_velocity,
        dtype=float
    )


    trajectory = []


    for _ in range(steps):

        acceleration = gravitational_acceleration(
            position
        )

        velocity += acceleration * timestep

        position += velocity * timestep

        trajectory.append(
            position.copy()
        )


    return np.array(trajectory)