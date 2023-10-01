"""
Mass-energy equivalence
Reference: https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence
"""
import math as m

""" Function to calculate energy(in joules) equivalent of a given
mass(in kilograms) using Einstein's equation E=mc^2"""


def calculate_energy(mass: float) -> float:
    """
    get energy equivalent of given mass in joules:
    >>> calculate_energy(1.2)
    1.0785062144841811e+17
    >>> calculate_energy(3.0)
    2.6962655362104528e+17
    >>> calculate_energy(5)
    4.493775893684088e+17
    >>> calculate_energy(-5)
    Traceback (most recent call last):
      ...
        raise TypeError("Mass cannot be negative")
    TypeError: Mass cannot be negative
    """
    if mass < 0:
        raise TypeError("Mass cannot be negative")
    # Speed of light in meters per second (approximately)
    speed_of_light = 299792458
    # Calculate energy using the equation E=mc^2
    energy = mass * speed_of_light**2
    # return value has unit Joules
    return energy


if __name__ == "__main__":
    mass = float(input("Enter mass (in kilograms): "))
    energy = calculate_energy(mass)
    print(f"Energy equivalent: {energy} joules")
