'''VectorND class implementation.
'''
from __future__ import annotations

import array
import numbers
from functools import total_ordering
from math import sqrt
from typing import Any
from typing import Union

from .dtypes import Number
from .dtypes import float32


@total_ordering
class VectorND:
    '''VectorND class to perform simple vector operations.
    '''

    def __init__(self, *args: Any, dtype: Any = float32) -> None:
        '''Create a vector instance with the given x and y values.

        Args:
            args (Any): The vector values.
            dtype (Any): The dtype of the underlying arry. Defaults to 'float32'.

        Raises:
            TypeError: If x or y are not a number.
        '''
        if len(args) == 1 and isinstance(args[0], list):
            self.values = array.array(dtype, args[0])
        elif len(args) > 0:
            values = [val for val in args]
            self.values = array.array(dtype, values)
        else:
            raise TypeError('You must pass in a tuple or list of values!')

    def __call__(self) -> str:
        '''Callable for the vector instance representation.

        Returns:
            str: The representation of the vector instance.
        '''
        print('Calling the __call__ function!')
        return self.__repr__()

    def __repr__(self) -> str:
        '''Return the vector instance representation.

        Returns:
            str: The representation of the vector instance.
        '''
        return f'vector.VectorND({self.values})'

    def __str__(self) -> str:
        '''The vector instance as a string.

        Returns:
            str: The vector instance as a string.
        '''
        return f'({self.values})'

    def __len__(self) -> int:
        '''Return the length of the vector.

        Returns:
            int: The vector length.
        '''
        return len(self.values)

    def __getitem__(self, idx: int) -> Number:
        '''Return the vector item at index *idx*.

        Args:
            idx (int): The vector index.

        Raises:
            IndexError: If an invalid index is passed in.

        Returns:
            Number: Vector value at index *idx*.
        '''
        if 0 <= idx < len(self.values):
            return self.values[idx]
        else:
            raise IndexError('Invalid index!')

    def __setitem__(self, idx: int, val: Number) -> None:
        '''Set the vector item at index *idx*.

        Args:
            idx (int): The vector index.
            val (Number): The vector value to set.

        Raises:
            IndexError: If an invalid index is passed in.
        '''
        if 0 <= idx < len(self.values):
            self.values[idx] = val
        else:
            raise IndexError('Invalid index!')

    def __bool__(self) -> bool:
        '''Return the truth value of the vector instance.

        Returns:
            bool: True, if the vector is not the Null-vector. False, else.
        '''
        return bool(abs(self))

    def __abs__(self) -> float:
        '''Return the length (magnitude) of the vector instance.

        Returns:
            float: Length of the vector instance.
        '''
        square_sum = sum([val**2.0 for val in self.values])
        return sqrt(square_sum)

    def __eq__(self, other_vector: object) -> bool:
        '''Check if the vector instances have the same values.

        Args:
            other_vector (object): Other vector instance (right-hand-side of the operator)

        Returns:
            bool: True, if the both vector instances have the same values. False, else.
        '''
        is_equal = False
        if isinstance(other_vector, VectorND):
            if self.values == other_vector.values:
                is_equal = True
        return is_equal

    def __lt__(self, other_vector: VectorND) -> bool:
        '''Check if the self instance is less than the other vector instance.

        Args:
            other_vector (VectorND): Other vector instance (right-hand-side of the operator).

        Returns:
            bool: True, if the self instance is less than the other vector instance. False, else.
        '''
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector: VectorND) -> VectorND:
        '''Returns the additon vector of the self and the other vector instance.

        Args:
            other_vector (VectorND): Other vector instance (right-hand-side of the operator).

        Returns:
            VectorND: The additon vector of the self and the other vector instance.
        '''
        self.check_vector_types(other_vector)
        add_result = [self_val + other_val for self_val, other_val in zip(self.values, other_vector.values)]
        return VectorND(add_result)

    def __sub__(self, other_vector: VectorND) -> VectorND:
        '''Return the subtraction vector of the self and the other vector instance.

        Args:
            other_vector (VectorND): Other vector instance (right-hand-side of the operator).

        Returns:
            VectorND: The subtraction vector of the self and the other vector instance.
        '''
        self.check_vector_types(other_vector)
        sub_result = [self_val - other_val for self_val, other_val in zip(self.values, other_vector.values)]
        return VectorND(sub_result)

    def __mul__(self, other: Union[Number, VectorND]) -> Union[Number, VectorND]:
        '''Return the multiplication of the self vector and the other vector(or number) instance.

        Args:
            other (Union[Number, VectorND]): Other vector instance or scaler
                value (right-hand-side of the operator)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            Union[Number, VectorND]: The multiplication of the self vector and the other
                vector(or number) instance.
        '''
        if isinstance(other, VectorND):
            return sum([self_val * other_val for self_val, other_val in zip(self.values, other.values)])
        elif isinstance(other, numbers.Real):
            mul_result = [val * other for val in self.values]
            return VectorND(mul_result)
        else:
            raise TypeError('You must pass in a vector instance or an int/float number!')

    def __truediv__(self, other: Number) -> VectorND:
        '''Return the multiplication of the self vector and the other vector(or number) instance.

        Args:
            other: Other vector instance or scaler value (right-hand-side of the operator).

        Raises:
            ValueError: Division by zero.
            TypeError: Not int/float passed in.

        Returns:
            Number: The multiplication of the self vector and the other vector(or number) instance.
        '''
        if isinstance(other, numbers.Real):
            if other != 0.0:
                div_result = [val / other for val in self.values]
                return VectorND(div_result)
            else:
                raise ValueError('You cannot divide by zero!')
        else:
            raise TypeError('You must pass in an int/float value!')

    @staticmethod
    def check_vector_types(vector: object) -> None:
        '''Check if the vector is an instance of the VectorND class.

        Args:
            vector (object): A vector instance.

        Raises:
            TypeError: If vector is not an instance of the VectorND class.
        '''
        if not isinstance(vector, VectorND):
            raise TypeError('You have to pass in two instances of the vector class!')
