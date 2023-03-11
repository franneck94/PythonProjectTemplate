from __future__ import annotations

import numbers
from functools import total_ordering
from math import sqrt
from typing import SupportsFloat
from typing import Union


@total_ordering
class Vector2D:
    def __init__(self, x: SupportsFloat = 0.0, y: SupportsFloat = 0.0) -> None:
        """Create a vector with the given x and y values.

        Args:
            x: x-Value.
            y: y-Value.

        Raises:
            TypeError: If x or y are not a number.
        """
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must pass in int/float value for x and y!")

    def __repr__(self) -> str:
        """Return the vector representation.

        Returns:
            The representation of the vector.
        """
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        """The vector as a string.

        Returns:
            The vector as a string.
        """
        return f"({self.x}, {self.y})"

    def __abs__(self) -> float:
        """Return the length (magnitude) of the vector.

        Returns:
            Length of the vector.
        """
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

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
        return self.x == other_vector.x and self.y == other_vector.y

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
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        """Return the subtraction vector of the self and the other vector.

        Args:
            other_vector: Other vector (rhs).

        Returns:
            The subtraction vector of the self and the other vector.
        """
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(
        self, other: Union[Vector2D, SupportsFloat]
    ) -> Union[Vector2D, SupportsFloat]:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scaler value (rhs)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and the other vector/number.
        """
        if isinstance(other, Vector2D):
            result: SupportsFloat = self.x * other.x + self.y * other.y
            return result
        if not isinstance(other, numbers.Real):
            raise TypeError("You must pass in an int/float!")
        return Vector2D(self.x * other, self.y * other)

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
        return Vector2D(self.x / other, self.y / other)
