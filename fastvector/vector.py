"""Own implementation of a 2D vector class.
"""
from __future__ import annotations

from functools import total_ordering
from math import sqrt


@total_ordering
class Vector2D:
    """Vector2D class to perform simple vector operations."""

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """Create a instance with the given x and y values.

        Args:
            x: x-Value.
            y: y-Value.

        Raises:
            TypeError: If x or y are not a number.
        """
        if isinstance(x, float | int) and isinstance(y, float | int):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must pass in int/float values for x and y!")

    def __call__(self) -> str:
        """Callable for the instance representation.

        Returns:
            The representation of the instance.
        """
        print("Calling the __call__ function!")
        return self.__repr__()

    def __repr__(self) -> str:
        """Return the instance representation.

        Returns:
            The representation of the instance.
        """
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        """The instance as a string.

        Returns:
            The instance as a string.
        """
        return f"({self.x}, {self.y})"

    def __bool__(self) -> bool:
        """Return the truth value of the instance.

        Returns:
            True, if the vector is not the Null-vector.
            False, else.
        """
        return bool(abs(self))

    def __abs__(self) -> float:
        """Return the length (magnitude) of the instance.

        Returns:
            Length of the instance.
        """
        return sqrt(self.x**2.0 + self.y**2.0)

    def __eq__(self, other_vector: object) -> bool:
        """Check if the instances have the same values.

        Args:
            other_vector: Other instance (rhs of the operator)

        Returns:
            True, if the both instances have the same values.
            False, else.
        """
        if not isinstance(other_vector, Vector2D):
            return False
        return self.x == other_vector.x and self.y == other_vector.y

    def __lt__(self, other_vector: Vector2D) -> bool:
        """Check if the self instance is less than the other instance.

        Args:
            other_vector: Other instance (rhs of the operator).

        Returns:
            True, if the self instance is less than the other instance.
            False, else.
        """
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        return abs(self) < abs(other_vector)

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        """Returns the addition vector of the self and the other instance.

        Args:
            other_vector: Other instance (rhs of the operator).

        Returns:
            The addition vector of the self and the other instance.
        """
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        """Return the subtraction vector of the self and the other instance.

        Args:
            other_vector: Other instance (rhs of the operator).

        Returns:
            The subtraction vector of the self and the other instance.
        """
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other: Vector2D | float) -> float | Vector2D:
        """Return the multiplication of self and left vector or number.

        Args:
            other: Other instance or scaler value (rhs of the operator)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and left vector or number.
        """
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        if not isinstance(other, float):
            raise TypeError("You must pass in an int/float!")
        return Vector2D(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> Vector2D:
        """Return the multiplication of self and left vector or number.

        Args:
            other: Other instance or scaler value (rhs of the operator).

        Raises:
            ValueError: Division by zero.
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and left vector or number.
        """
        if not isinstance(other, float):
            raise TypeError("You must pass in an int/float!")
        return Vector2D(self.x / other, self.y / other)
