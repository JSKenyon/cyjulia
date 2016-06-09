from cython.parallel import prange
import cython
import numpy as np
cimport numpy as np 

def calculate_z(zs, c, maxiter):
	"""
	This is identical to the first example in julia.py. It is here to
  demonstrate that it is possible to compile ordinary Python code.
	"""

	zdim = zs.shape[0]
	mask = np.empty(zs.shape, dtype=np.int32)

	for i in xrange(zs.size):
		n = 0
		z = zs[i]
		while abs(z)<2 and n<maxiter:
			z = z * z + c
			n = n + 1
		mask[i] = n

	return mask

# def calculate_z(double complex [:] zs, double complex c, int maxiter):
#     """
#     This is fairly typical Cythonised version of the basic Python
#     implementation. The major difference is the inclusion of types.
#     """
#
#     cdef int n, j
#     cdef int zdim = zs.size
#     cdef int [:] mask = np.empty(zdim, dtype=np.int32)
#
#     for j in xrange(zdim):
#         n = 0
#         while abs(zs[j]) < 2 and n < maxiter:
#             zs[j] = zs[j] * zs[j] + c
#             n = n + 1
#         mask[j] = n
#
#     return mask

# def calculate_z(double complex [:] zs, double complex c, int maxiter):
#     """
#     The following is an improved version of the above code. By replacing the
#     absolute value with some more explicit code which avoids taking the square
#     root, we gain a substantial speed-up.
#     """
#
#     cdef int n, j
#     cdef int zdim = zs.size
#     cdef int [:] mask = np.empty(zdim, dtype=np.int32)
#
#     for j in xrange(zdim):
#         n = 0
#         while (zs[j].real * zs[j].real + zs[j].imag * zs[j].imag) < 4 and n < maxiter:
#             zs[j] = zs[j] * zs[j] + c
#             n = n + 1
#         mask[j] = n
#
#     return mask

# def calculate_z(double complex [:] zs, double complex c, int maxiter):
#     """
#     This adds some multithreading. Note how simple it is to replace the
#     xrange with prange and surrender the GIL. This makes parallelism quite
#     easy.
#     """
#     cdef int n, j
#     cdef int zdim = zs.size
#     cdef int [:] mask = np.empty(zdim, dtype=np.int32)
#
#     for j in prange(zdim, nogil=True, schedule="guided"):
#         n = 0
#         while (zs[j].real * zs[j].real + zs[j].imag * zs[j].imag) < 4 and n < maxiter:
#             zs[j] = zs[j] * zs[j] + c
#             n = n + 1
#         mask[j] = n
#
#     return mask

# @cython.wraparound(False)
# @cython.boundscheck(False)
# @cython.nonecheck(False)
# def calculate_z(double complex [:] zs, double complex c, int maxiter):
#     """
#     This final version includes some decorators which tell the compiler to
#     ignore some standard checks. This can be dangerous, but well written code
#     will often not require these checks and removing them does increase speed.
#     """
#     cdef int n, j
#     cdef int zdim = zs.size
#     cdef int [:] mask = np.empty(zdim, dtype=np.int32)
#
#     for j in prange(zdim, nogil=True, schedule="guided"):
#         n = 0
#         while (zs[j].real * zs[j].real + zs[j].imag * zs[j].imag) < 4 and n < maxiter:
#             zs[j] = zs[j] * zs[j] + c
#             n = n + 1
#         mask[j] = n
#
#     return mask

