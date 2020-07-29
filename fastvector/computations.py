"""Own implementation of a vector computations.
"""
from .cython_computations import _naive_cython_clip_vector, _cython_clip_vector
from .dtypes import Number
from .vector import VectorND


def python_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND):
    """Clip the vector values by plain python code.

    Parameters
    ----------
    vector_in : VectorND
        Input vector
    min_value : Number
        Real number.
    max_value : Number
        Real number.
    vector_out : VectorND
        Output vector

    Raises
    ------
    ValueError
        If min_value is larger than max_value.
    """
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    VectorND.check_numeric_argument(min_value)
    VectorND.check_numeric_argument(max_value)
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    for i in range(len(vector_in)):
        vector_out[i] = min(max(vector_in[i], min_value), max_value)

def naive_cython_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND):
    """Clip the vector values by naive cython code.

    Parameters
    ----------
    vector_in : VectorND
        Input vector
    min_value : Number
        Real number.
    max_value : Number
        Real number.
    vector_out : VectorND
        Output vector

    Raises
    ------
    ValueError
        If min_value is larger than max_value.
    """
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    VectorND.check_numeric_argument(min_value)
    VectorND.check_numeric_argument(max_value)
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    _naive_cython_clip_vector(vector_in.values, min_value, max_value, vector_out.values)


def cython_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND):
    """Clip the vector values by optimized cython code.

    Parameters
    ----------
    vector_in : VectorND
        Input vector
    min_value : Number
        Real number.
    max_value : Number
        Real number.
    vector_out : VectorND
        Output vector

    Raises
    ------
    ValueError
        If min_value is larger than max_value.
    """
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    VectorND.check_numeric_argument(min_value)
    VectorND.check_numeric_argument(max_value)
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    _cython_clip_vector(vector_in.values, min_value, max_value, vector_out.values)
