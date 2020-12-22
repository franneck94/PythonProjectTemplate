cimport cython

ctypedef fused vector_type:
    unsigned char
    char
    short
    unsigned short
    int
    unsigned int
    long long
    unsigned long long
    float
    double

def _naive_cython_clip_vector(list_in, min_value, max_value, list_out):
    for i in range(len(list_in)):
        list_out[i] = min(max(list_in[i], min_value), max_value)

@cython.boundscheck(False) # Deactivate bounds checking
@cython.wraparound(False) # Deactivate negative indexing
# cpef: def + cdef (python + c/c++)
cpdef _cython_clip_vector(vector_type[:] list_in, vector_type min_value, vector_type max_value, vector_type[:] list_out):
    for i in range(len(list_in)):
        list_out[i] = min(max(list_in[i], min_value), max_value)
