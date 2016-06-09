from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

setup(
	cmdclass = {'build_ext': build_ext},
    	ext_modules=[Extension("julia_core", ["julia_core.pyx"],
               	include_dirs=[np.get_include()],
		extra_compile_args=['-fopenmp'],
		extra_link_args=['-lgomp'])]
	)

