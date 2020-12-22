"""Own implementation of a ND vector class.
"""
from __future__ import annotations

import array
import numbers
from functools import total_ordering
from math import sqrt
from typing import Any
from typing import Union

from .dtypes import Number
from .dtypes import float64


@total_ordering
class VectorND:
    """VectorND class to perform simple vector operations.
    """

    def __init__(self, *args: Any, dtype: Any = float64):
        """Create a vector instance with the given x and y values.

        Args:
            args (Any): The vector values.
            dtype (Any, optional): The dtype of the underlying array. Defaults to float64.

        Raises:
            TypeError: If x or y are not a number.
        """
        # Values are passed in as a list
        if len(args) == 1 and isinstance(args[0], list):
            self.values = array.array(dtype, args[0])
        # Values are passed in as optinal arguments
        elif len(args) > 0:
            values = [val for val in args]  # pylint: disable=unnecessary-comprehension
            self.values = array.array(dtype, values)
        else:
            raise TypeError('You must pass in an list of numbers, or numbers as a args tuple!')

    def __call__(self) -> str:
        """Callable for the vector instance representation.

        Returns:
            str: The representation of the vector instance.
        """
        return self.__repr__()

    def __repr__(self) -> str:
        """Return the vector instance representation.

        Returns:
            str: The representation of the vector instance.
        """
        return f'vector.VectorND({self.values})'

    def __str__(self) -> str:
        """The vector instance as a string.

        Returns:
            str: The vector instance as a string.
        """
        return f'({self.values})'

    def __len__(self) -> int:
        """Return the length of the vector.

        Returns:
            int: The vector length.
        """
        return len(self.values)

    def __getitem__(self, idx: int) -> Number:
        """Return the vector item at index idx.

        Args:
            idx (int): The index idx

        Raises:
            IndexError: If idx >= len.

        Returns:
            Number: If idx < len: returns the value. IndexError, else.
        """
        if 0 <= idx < len(self):
            return self.values[idx]
        raise IndexError('Invalid index value!')

    def __setitem__(self, idx: int, val: Number) -> None:
        """Returns the vector item at index idx.

        Args:
            idx (int): The index idx.
            val (Number): The new value at index idx.

        Raises:
            IndexError: If idx >= len.
        """
        if 0 <= idx < len(self):
            self.values[idx] = val
        else:
            raise IndexError('Invalid index value!')

    def __bool__(self) -> bool:
        """Return the truth value of the vector instance.

        Returns:
            bool: True, if the vector is not the Null-vector.
            False, else.
        """
        return bool(abs(self))

    def __abs__(self) -> float:
        """Return the length (magnitude) of the vector instance.

        Returns:
            float: Length of the vector instance.
        """
        square_sum = sum([val**2.0 for val in self.values])
        return sqrt(square_sum)

    def __eq__(self, other_vector: Any) -> bool:
        """Check if the vector instances have the same values.

        Args:
            other_vector (Any): Other vector instance (right-hand-side of the operator)

        Returns:
            bool: True, if the both vector instances have the same values.
            False, else.
        """
        self.check_vector_types(other_vector)
        is_equal = False
        if self.values == other_vector.values:
            is_equal = True
        return is_equal

    def __lt__(self, other_vector: VectorND) -> bool:
        """Check if the self instance is less than the other vector instance.

        Args:
            other_vector (VectorND): Other vector instance (right-hand-side of the operator).

        Returns:
            bool: True, if the self instance is less than the other vector instance.
            False, else.
        """
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector: VectorND) -> VectorND:
        """Returns the additon vector of the self and the other vector instance.

        Args:
            other_vector (VectorND): Other vector instance (right-hand-side of the operator).

        Returns:
            VectorND: The additon vector of the self and the other vector instance.
        """
        self.check_vector_types(other_vector)
        add_result = [self_val + other_val for self_val, other_val in zip(self.values, other_vector.values)]
        return VectorND(add_result)

    def __sub__(self, other_vector: VectorND) -> VectorND:
        """Return the subtraction vector of the self and the other vector instance.

        Args:
            other_vector (VectorND): Other vector instance (right-hand-side of the operator).

        Returns:
            VectorND: The subtraction vector of the self and the other vector instance.
        """
        self.check_vector_types(other_vector)
        sub_result = [self_val - other_val for self_val, other_val in zip(self.values, other_vector.values)]
        return VectorND(sub_result)

    def __mul__(self, other: Union[VectorND, Number]) -> Union[VectorND, Number]:
        """Return the multiplication of the self vector and the other vector(or number) instance.

        Args:
            other (Union[VectorND, Number]): Other vector instance or scaler value (right-hand-side of the operator)

        Raises:
            TypeError: [description]

        Returns:
            Union[VectorND, Number]: The multiplication of the self vector and the other vector(or number) instance.
        """
        if isinstance(other, VectorND):
            vector_dot = sum([self_val * other_val for self_val, other_val in zip(self.values, other.values)])
            return vector_dot
        if isinstance(other, numbers.Real):
            vector_mul = [val * other for val in self.values]
            return VectorND(vector_mul)
        raise TypeError('You must pass in a vector instance or an int/float number!',)

    def __truediv__(self, other: Number) -> VectorND:
        """Return the multiplication of the self vector and the other vector(or number) instance.

        Args:
            other (Number): Other vector instance or scaler value (right-hand-side of the operator).

        Raises:
            ValueError: [description]
            TypeError: [description]

        Returns:
            VectorND: The multiplication of the self vector and the other vector(or number) instance.
        """
        if isinstance(other, numbers.Real):
            if other != 0.0:
                vector_div = [val / other for val in self.values]
                return VectorND(vector_div)
            raise ValueError('You cannot divide by zero!')
        raise TypeError('You must pass in an int/float value!')

    @staticmethod
    def check_numeric_argument(argument: Number) -> None:
        """Check if the argument is a numeric value.

        Args:
            argument (Number): Argument to check.

        Raises:
            TypeError: If the argument is not of type numbers.Real.
        """
        if not isinstance(argument, numbers.Real):
            raise TypeError('You must pass in an int/float value!')

    @staticmethod
    def check_vector_types(vector: VectorND) -> None:
        """Check if the vector is an instance of the VectorND class.

        Args:
            vector (VectorND): A vector instance.

        Raises:
            TypeError: If vector is not an instance of the VectorND class.
        """
        if not isinstance(vector, VectorND):
            raise TypeError('You have to pass in two instances of the vector class!')
