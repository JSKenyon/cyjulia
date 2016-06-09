This is the readme for the Julia fractal example. To run the Cython code, 
comment out all but one calculate_z function and compile from command line 
using:

python setup.py build_ext --inplace -f

Requirements: 
cython (0.23.4)
numpy (1.10.1)
matplotlib (1.3.1)
gcc (4.8.4)

NOTE: These were the versions on my laptop, but others will likely work too.
I would recommend pip installing what you do not already have.
