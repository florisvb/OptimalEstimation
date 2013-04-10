'''
Guide to understanding the python code I wrote for my homework:

I use python, because it's much more useful than matlab, and I know how to program more elegantly and quickly in python than in matlab. If you've never used python before, here are a few pointers to help you read my code:

A comment in the code looks like this:
'''
# I am a comment, and I am always going to be blue
'''
I also use block comments, which this text right here is an example of. They start and end with three of these: '
And they are pink; I hope you like pink, because there will be a lot of pink.

Each python script starts with some import statements such as:
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
'''
These import standard python modules, and rename them with something shorter. numpy is essentially matlab. matplotlib is a plotting library. scipy.stats has definitions of statistical pdf's, which I use for calculating gaussian noise. These modules give me access to standard functions that are, for example, built into matlab.

You will also see these statements:
'''
from least_squares import LeastSquaresEstimator
from least_squares import H_LTI
from nonlinear_least_squares import NonlinearLeastSquaresEstimator as NLSE
'''
These import class definitions from modules which **I wrote** for the homework that organize the least squares algorithms in such a way that I can reuse the code easily. I included a copy of these modules at the back of my homework.


For each problem I wrote a python script, which typically uses several functions and classes, either defined in the script, or in a model that is imported at the beginning. Within the code I have descriptive comments, and I tried to use intuitive variable names. I also included my results of running the code within the script itself, to keep things more organized. To read the code, start near the bottom. Look for this line:
'''
if __name__ == '__main__':
'''
That's where the script starts. In most of my problems this simply runs a function I wrote to do the homework problem, and is followed by the results of running the code.

If anything is unclear, please let me know so that I can make sure it is clearer in future homework assignments. You can also email me: florisvb@gmail.com
'''













