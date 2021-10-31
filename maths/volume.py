"""
Find Volumes of Various Shapes.

Wikipedia reference: https://en.wikipedia.org/wiki/Volume
"""
from __future__ import annotations

from math import pi, pow


def vol_cube(side_length: int | float) -> float:
    """
    Calculate the Volume of a Cube.

    >>> vol_cube(1)
    1.0
    >>> vol_cube(3)
    27.0
    """
    return pow(side_length, 3)


def vol_spherical_cap(height: float, radius: float) -> float:
    """
    Calculate the Volume of the spherical cap.
    :return 1/3 pi * height ^ 2 * (3 * radius - height)

    >>> vol_spherical_cap(1, 2)
    5.235987755982988
    """
    return 1 / 3 * pi * pow(height, 2) * (3 * radius - height)


def vol_spheres_intersect(
    radius_1: float, radius_2: float, centers_distance: float
) -> float:
    """
    Calculate the volume of the intersection of two spheres.

    The intersection is composed by two spherical caps and therefore its volume is the
    sum of the volumes of the spherical caps.  First it calculates the heights (h1, h2)
    of the the spherical caps, then the two volumes and it returns the sum.
    The height formulas are
    h1 = (radius_1 - radius_2 + centers_distance)
       * (radius_1 + radius_2 - centers_distance)
       / (2 * centers_distance)
    h2 = (radius_2 - radius_1 + centers_distance)
       * (radius_2 + radius_1 - centers_distance)
       / (2 * centers_distance)
    if centers_distance is 0 then it returns the volume of the smallers sphere
    :return vol_spherical_cap(h1, radius_2) + vol_spherical_cap(h2, radius_1)

    >>> vol_spheres_intersect(2, 2, 1)
    21.205750411731103
    """
    if centers_distance == 0:
        return vol_sphere(min(radius_1, radius_2))

    h1 = (
        (radius_1 - radius_2 + centers_distance)
        * (radius_1 + radius_2 - centers_distance)
        / (2 * centers_distance)
    )
    h2 = (
        (radius_2 - radius_1 + centers_distance)
        * (radius_2 + radius_1 - centers_distance)
        / (2 * centers_distance)
    )

    return vol_spherical_cap(h1, radius_2) + vol_spherical_cap(h2, radius_1)


def vol_cuboid(width: float, height: float, length: float) -> float:
    """
    Calculate the Volume of a Cuboid.
    :return multiple of width, length and height

    >>> vol_cuboid(1, 1, 1)
    1.0
    >>> vol_cuboid(1, 2, 3)
    6.0
    """
    return float(width * height * length)


def vol_cone(area_of_base: float, height: float) -> float:
    """
    Calculate the Volume of a Cone.

    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    :return (1/3) * area_of_base * height

    >>> vol_cone(10, 3)
    10.0
    >>> vol_cone(1, 1)
    0.3333333333333333
    """
    return area_of_base * height / 3.0


def vol_right_circ_cone(radius: float, height: float) -> float:
    """
    Calculate the Volume of a Right Circular Cone.

    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    :return (1/3) * pi * radius^2 * height

    >>> vol_right_circ_cone(2, 3)
    12.566370614359172
    """
    return pi * pow(radius, 2) * height / 3.0


def vol_prism(area_of_base: float, height: float) -> float:
    """
    Calculate the Volume of a Prism.
    Wikipedia reference: https://en.wikipedia.org/wiki/Prism_(geometry)
    :return V = Bh

    >>> vol_prism(10, 2)
    20.0
    >>> vol_prism(11, 1)
    11.0
    """
    return float(area_of_base * height)


def vol_pyramid(area_of_base: float, height: float) -> float:
    """
    Calculate the Volume of a Pyramid.
    Wikipedia reference: https://en.wikipedia.org/wiki/Pyramid_(geometry)
    :return  (1/3) * Bh

    >>> vol_pyramid(10, 3)
    10.0
    >>> vol_pyramid(1.5, 3)
    1.5
    """
    return area_of_base * height / 3.0


def vol_sphere(radius: float) -> float:
    """
    Calculate the Volume of a Sphere.
    Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
    :return (4/3) * pi * r^3

    >>> vol_sphere(5)
    523.5987755982989
    >>> vol_sphere(1)
    4.1887902047863905
    """
    return 4 / 3 * pi * pow(radius, 3)


def vol_circular_cylinder(radius: float, height: float) -> float:
    """Calculate the Volume of a Circular Cylinder.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cylinder
    :return pi * radius^2 * height

    >>> vol_circular_cylinder(1, 1)
    3.141592653589793
    >>> vol_circular_cylinder(4, 3)
    150.79644737231007
    """
    return pi * pow(radius, 2) * height


def vol_ellipsoid(a_axis: float, b_axis: float, c_axis: float) -> float:
    """Calculate the Volume of a Ellipsoid.
    Wikipedia refrence: https://en.wikipedia.org/wiki/Ellipsoid
    :return 4/3 * pi * a_axis * b axis * c_axis
     
     >>> vol_ellipsoid(2.5, 5.2, 7.5)
     408.4070449666731
     >>> vol_ellipsoid(7.2, 2.2, 5.7)
     378.1974900097537
    """
    return float(4/3*pi*a_axis*b_axis*c_axis)


def vol_tetrahedron(edge: float) -> float:
    """Calculate the Volume of a Tetrahedron.
    Wikipedia refrence: https://en.wikipedia.org/wiki/Tetrahedron
    formula: edge**2/6√2
    :return edge**3 / (6 * pow(2, 1/2) )
    
    >>> vol_tetrahedron(2.7)
    2.319663795682469
    >>> vol_tetrahedron(7.752)
    54.900341245289894
    """
    



def main():
    """Print the Results of Various Volume Calculations."""
    print("Volumes:")
    print("Cube: " + str(vol_cube(2)))  # = 8
    print("Cuboid: " + str(vol_cuboid(2, 2, 2)))  # = 8
    print("Cone: " + str(vol_cone(2, 2)))  # ~= 1.33
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2)))  # ~= 8.38
    print("Prism: " + str(vol_prism(2, 2)))  # = 4
    print("Pyramid: " + str(vol_pyramid(2, 2)))  # ~= 1.33
    print("Sphere: " + str(vol_sphere(2)))  # ~= 33.5
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2)))  # ~= 25.1
    print("Spherical cap: " + str(vol_spherical_cap(1, 2)))  # ~= 5.24
    print("Spheres intersetion: " + str(vol_spheres_intersect(2, 2, 1)))  # ~= 21.21
    print("Ellipsoid: " + str(vol_ellipsoid(1, 2, 3)))  # ~= 25.13
    print("Tetrahedron: " + str(vol_tetrahedron(2)))  # ~= 0.94


if __name__ == "__main__":
    main()
