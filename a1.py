import math
import re

def is_multiple_of_11(n):
    """Return True if n is a multiple of 11; False otherwise."""
    if n % 11 == 0:
        return True
    else:
        return False

def last_prime(m):
    """Return the largest prime number p that is less than or equal to m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    prime = m
    while prime > 1:
        if check_prime(prime):
            return prime
        prime -= 1
    return 0

def check_prime(n):
    """If n is not a prime number, return False; return True otherwise"""
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    if (b ** 2 - 4 * a * c) <= 0:
        x = "complex"
        return x
    else:
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return x1, x2

def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    Perfect shuffle means splitting a list into two halves and then interleaving
    them. For example, the perfect shuffle of [0, 1, 2, 3, 4, 5, 6, 7] is
    [0, 4, 1, 5, 2, 6, 3, 7]."""
    list1 = even_list[:len(even_list) // 2]
    list2 = even_list[len(even_list) // 2:]
    shuffle = []
    for i in range(len(list1)):
        shuffle.append(list1[i])
        shuffle.append(list2[i])
    if len(list2) > len(list1):
        shuffle.append(list2[len(list2) - 1])
    return shuffle


def five_times_list(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 5."""
    new_list = [i * 5 for i in input_list]
    return new_list

def triple_vowels(text):
    """Return a new version of text, with all the vowels tripled.
    For example:  "The *BIG BAD* wolf!" => "Theee "BIIIG BAAAD* wooolf!".
    For this exercise assume the vowels are
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    words = ''
    for letter in text:
        if letter in vowels:
            words += (3 * letter)
        else:
            words += letter
    return words


def count_words(text):
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', *', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
    Convert all the letters to lower-case before the counting."""
    text = text.lower()
    words = re.sub("[^a-zA-Z0-9#*+/@%'\n\-]", ' ', text)
    words = words.split()
    count = dict()

    for x in words:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    return count


def make_quartic_evaluator(a, b, c, d, e):
    """When called with 5 numbers, returns a function of one variable (x)
    that evaluates the quartic polynomial
    a x^4 + b x^3 + c x^2 + d x + e.
    For this exercise Your function definition for make_quartic_evaluator
    should contain a lambda expression."""
    return lambda x: a * (x ** 4) + b * (x ** 3) + c * (x ** 2) + d*x + e


class Polygon:
"""Represent a polygon with identifying function"""

    def __init__(self, n_sides, lengths=None, angles=None):
        """Initialize a new polygon from given numbers of side, length, and angle."""
        self.n_sides = n_sides
        self.lengths = lengths
        self.angles = angles

    def check_it(self, n_angles, sides, n_lengths):
        """Return different identifier base on given angles, sides, and lengths; if not
        enough conditions matched, return false"""
        if n_lengths is None:
            if sides == 4 & sum(n_angles) == 360 & len(set(n_angles)) == 1:
                """identified as rectangle"""
                return True
        if len(n_angles) == sides == len(n_lengths):
            n_lengths = n_lengths.sort()
            n_angles = n_angles.sort()
            if sides == 4 & sum(n_angles) == 360:
                if len(set(n_lengths)) == 1 & len(set(n_angles)) == 1:
                    """identified as square"""
                    return 1
                elif len(set(n_lengths)) == 1 & n_angles[0] == n_angles[1] & n_angles[2] == n_angles[3]:
                    """identified as rhombus"""
                    return 2
                else:
                    return False
            elif sides == 3 & sum(n_angles) == 180:
                if len(set(n_lengths)) == 1 & len(set(n_angles)) == 1:
                    """identified as equilateral triangle"""
                    return 3
                elif n_angles[0] == n_angles[1] | n_angles[1] == n_angles[2] & n_lengths[0] + n_lengths[1] > n_lengths[2]:
                    """identified as isosceles triangle"""
                    return 4
                else:
                    """identified as scalene triangle"""
                    return 5
            elif sides == 6 & sum(n_angles) == 720:
                if len(set(n_lengths)) == 1 & len(set(n_angles)) == 1:
                    """identified as regular hexagon"""
                    return 6
            else:
                return False
        return False

    def is_rectangle(self):
        """ returns True if the polygon is a rectangle,
        False if it is definitely not a rectangle, and None
        if the angle list is unknown (None)."""
        if self.angles is None:
            return None
        elif self.check_it(self.angles, self.n_sides, self.lengths):
            return True
        else:
            return False

    def is_rhombus(self):
        """ returns True if the polygon is a rhombus,
            False if it is definitely not a rhombus, and None
            if the angle and length list is unknown (None)."""
        if self.angles is None | self.lengths is None:
            return None
        elif self.check_it(self.angles, self.n_sides, self.lengths) == 2:
            return True
        else:
            return False

    def is_square(self):
        """ returns True if the polygon is a square,
            False if it is definitely not a square, and None
            if the angle and length list is unknown (None)."""
        if self.angles is None | self.lengths is None:
            return None
        elif self.check_it(self.angles, self.n_sides, self.lengths) == 1:
            return True
        else:
            return False

    def is_regular_hexagon(self):
        """ returns True if the polygon is a regular_hexagon,
            False if it is definitely not a regular_hexagon, and None
            if the angle and length list is unknown (None)."""
        if self.angles is None | self.lengths is None:
            return None
        elif self.check_it(self.angles, self.n_sides, self.lengths) == 6:
            return True
        else:
            return False

    def is_isosceles_triangle(self):
        """ returns True if the polygon is a isosceles_triangle,
            False if it is definitely not a isosceles_triangle, and None
            if the angle and length list is unknown (None)."""
        if self.angles is None | self.lengths is None:
            return None
        elif self.check_it(self.angles, self.n_sides, self.lengths) == 4:
            return True
        else:
            return False

    def is_equilateral_triangle(self):
        """ returns True if the polygon is a equilateral_triangle,
            False if it is definitely not a equilateral_triangle, and None
            if the angle and length list is unknown (None)."""
        if self.angles is None | self.lengths is None:
            return None
        elif self.check_it(self.angles, self.n_sides, self.lengths) == 3:
            return True
        else:
            return False

    def is_scalene_triangle(self):
        """ returns True if the polygon is a scalene_triangle,
            False if it is definitely not a scalene_triangle, and None
            if the angle and length list is unknown (None)."""
        if self.angles is None | self.lengths is None:
            return None
        elif self.check_it(self.angles, self.n_sides, self.lengths) == 5:
            return True
        else:
            return False