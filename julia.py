import numpy as np
import time
import julia_core
import matplotlib.pyplot as plt
from functools import wraps

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print ("@timefn:" + fn.func_name + " took " + str(t2 - t1) + " seconds")
        return result
    return measure_time

def makegrid(lim, width):
	"""
	Creates a width-by-width grid of complex numbers between [-lim,+lim]
	"""

	zs = np.linspace(-lim, lim, width)
	zs = zs - 1j*zs[np.newaxis,:].T
	return zs

# @timefn
# @profile
def calculate_z(zs, c, maxiter):
    """
    Simplistic Python implementation of the Julia fractal computation.
    This is NOT a good implementation, but it is easy to understand.
    """

    zdim = zs.shape[0]
    zs = np.ravel(zs)
    mask = np.zeros(zs.shape, dtype=np.int32)

    for i in xrange(zs.size):
        n = 0
        z = zs[i]
        while abs(z)<2 and n<maxiter:
            z = z * z + c
            n += 1
        mask[i] = n

    return mask.reshape([zdim,zdim])

# def calculate_z(zs, c, maxiter):
#     """
#     This is a superior implementation of the Julia fractal computation
#     using numpy. This is a reference for the performance of our cythonised
#     code.
#     """
#
#     mask = maxiter*np.ones(zs.shape, dtype=np.int32)
#
#     for i in xrange(maxiter):
#         zs[mask==maxiter] = zs[mask==maxiter]**2 + c
#         mask[np.logical_and(mask==maxiter, np.abs(zs)>2)] = i
#
#     return mask

def julia_fract():

    grid_size = 512

    zs = makegrid(2, grid_size)

    # First res calculation is for functions in this file. Uncomment the second
    # and third lines to use the Cython code.

    # t0 = time.time()
    res = calculate_z(zs, -0.62772-0.42193j, 100)
    # res = julia_core.calculate_z(zs.ravel(), -0.62772-0.42193j, 100)
    # res = np.array(res).reshape(grid_size,grid_size)
    # print "Time taken to compute fractal: {} seconds".format(time.time() - t0)

    # plt.imshow(np.abs(res))
    # plt.show()

if __name__=="__main__":
    julia_fract()

# python -m timeit -n 5 -r 1 "import julia" "julia.julia_fract()"
# /usr/bin/time --verbose python julia.py
# python -m cProfile -s cumulative julia.py
# python -m cProfile -o profile.stats julia.py
# runsnake profile.stats
# python //usr/local/lib/python2.7/dist-packages/kernprof.py -l -v julia.py
# python -m memory_profiler julia.py
# perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
# cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
# minor-faults,cs,migrations -r 3 python diffusion_python_memory.py