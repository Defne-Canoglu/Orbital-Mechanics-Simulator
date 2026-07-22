import numpy as np

# Universal gravitational constant
G = 6.67430e-11

# Earth parameters
EARTH_MASS = 5.972e24
EARTH_RADIUS = 6.371e6


def gravitational_acceleration(position):
    """
    Calculate gravitational acceleration acting on a spacecraft.

    Parameters
    ----------
    position : numpy array
        Spacecraft position vector [x, y] in meters

    Returns
    -------
    numpy array
        Acceleration vector [ax, ay] in m/s^2
    """

    distance = np.linalg.norm(position)

    acceleration = (
        -G * EARTH_MASS / distance**3
    ) * position

    return acceleration