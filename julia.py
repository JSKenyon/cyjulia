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


def julia_fract():

    grid_size = 512

    zs = makegrid(2, grid_size)

    # t0 = time.time()
    res = calculate_z(zs, -0.62772-0.42193j, 100)
    # t1 = time.time()
    # print "Time taken to compute fractal: {} seconds".format(t1 - t0)

    # plt.imshow(np.abs(res))
    # plt.show()


if __name__=="__main__":
    julia_fract()

