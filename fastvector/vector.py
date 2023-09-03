"""
This module contains template Python code for implementing the Vector2D class.
"""
from __future__ import annotations

import numbers
from functools import total_ordering
from math import sqrt
from typing import SupportsFloat


@total_ordering
class Vector2D:
    """
    This is a sample class that demonstrates how to create a 2D vector.
    """

    def __init__(
        self, x_axis: SupportsFloat = 0.0, y_axis: SupportsFloat = 0.0
    ) -> None:
        """Create a vector with the given x and y values.

        Args:
            x: x-Value.
            y: y-Value.

        Raises:
            TypeError: If x or y are not a number.
        """
        if isinstance(x_axis, numbers.Real) and isinstance(
            y_axis, numbers.Real
        ):
            self.x_axis = x_axis
            self.y_axis = y_axis
        else:
            raise TypeError("You must pass in int/float value for x and y!")

    def __repr__(self) -> str:
        """Return the vector representation.

        Returns:
            The representation of the vector.
        """
        return f"vector.Vector2D({self.x_axis}, {self.y_axis})"

    def __str__(self) -> str:
        """The vector as a string.

        Returns:
            The vector as a string.
        """
        return f"({self.x_axis}, {self.y_axis})"

    def __abs__(self) -> float:
        """Return the length (magnitude) of the vector.

        Returns:
            Length of the vector.
        """
        return sqrt(pow(self.x_axis, 2) + pow(self.y_axis, 2))

    def __eq__(self, other_vector: object) -> bool:
        """Check if the vectors have the same values.

        Args:
            other_vector: Other vector (rhs)

        Returns:
            True, if the both vectors have the same values.
            False, else.
        """
        if not isinstance(other_vector, Vector2D):
            return False
        return (
            self.x_axis == other_vector.x_axis
            and self.y_axis == other_vector.y_axis
        )

    def __lt__(self, other_vector: Vector2D) -> bool:
        """Check if the self is less than the other vector.

        Args:
            other_vector: Other vector (rhs).

        Returns:
            True, if the self is less than the other vector.
            False, else.
        """
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        return abs(self) < abs(other_vector)

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        """Returns the addition vector of the self and the other vector.

        Args:
            other_vector: Other vector (rhs).

        Returns:
            The addition vector of the self and the other vector.
        """
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x_axis = self.x_axis + other_vector.x_axis
        y_axis = self.y_axis + other_vector.y_axis
        return Vector2D(x_axis, y_axis)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        """Return the subtraction vector of the self and the other vector.

        Args:
            other_vector: Other vector (rhs).

        Returns:
            The subtraction vector of the self and the other vector.
        """
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x_axis = self.x_axis - other_vector.x_axis
        y_axis = self.y_axis - other_vector.y_axis
        return Vector2D(x_axis, y_axis)

    def __mul__(
        self, other: Vector2D | SupportsFloat
    ) -> Vector2D | SupportsFloat:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scaler value (rhs)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and the other vector/number.
        """
        if isinstance(other, Vector2D):
            result: SupportsFloat = (
                self.x_axis * other.x_axis + self.y_axis * other.y_axis
            )
            return result
        if not isinstance(other, numbers.Real):
            raise TypeError("You must pass in an int/float!")
        return Vector2D(self.x_axis * other, self.y_axis * other)

    def __truediv__(self, other: SupportsFloat) -> Vector2D:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scaler value (rhs).

        Raises:
            ValueError: Division by zero.
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and the other vector/number.
        """
        if not isinstance(other, numbers.Real):
            raise TypeError("You must pass in an int/float!")
        return Vector2D(self.x_axis / other, self.y_axis / other)
