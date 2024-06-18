# geometry.py

"""
@file geometry.py
@brief Module de géométrie fournissant des fonctions pour calculer l'aire et le périmètre de formes simples.
"""

def rectangle_area(length, width):
    """
    @brief Calcule l'aire d'un rectangle.
    @param length Longueur du rectangle.
    @param width Largeur du rectangle.
    @return Aire du rectangle.
    """
    return length * width

def rectangle_perimeter(length, width):
    """
    @brief Calcule le périmètre d'un rectangle.
    @param length Longueur du rectangle.
    @param width Largeur du rectangle.
    @return Périmètre du rectangle.
    """
    return 2 * (length + width)

def circle_area(radius):
    """
    @brief Calcule l'aire d'un cercle.
    @param radius Rayon du cercle.
    @return Aire du cercle.
    """
    import math
    return math.pi * radius ** 2

def circle_circumference(radius):
    """
    @brief Calcule la circonférence d'un cercle.
    @param radius Rayon du cercle.
    @return Circonférence du cercle.
    """
    import math
    return 2 * math.pi * radius
