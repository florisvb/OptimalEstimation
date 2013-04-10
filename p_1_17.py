# PROBLEM 1.17 and 1.18

from __future__ import division
import numpy as np
import scipy.stats
from nonlinear_least_squares import NonlinearLeastSquaresEstimator as NLSE

def generate_synthetic_data(Ar):
    '''
    Following the instructions in the book, this function calculates the noisy measurements, and the values of bj.
    
    Ar is a function of t
    '''
    
    interval = 5
    nvals = 1001
    ts = np.linspace(0,interval*nvals,nvals)
    
    c = np.matrix([0.5, 0.3, 0.6]).T
    
    def b(t):
        bj = Ar(t) + c
        return bj
        
    def y(t):
        # Note: rT r = rT AT A r = (A r)T A r
        eps = scipy.stats.norm(0, 0.05)
        epsmat = np.matrix([eps.rvs(), eps.rvs(), eps.rvs()]).T
        rTr = (Ar(t).T)*Ar(t)
        yj = 2*b(t).T*c - c.T*c + epsmat
        return yj
        
    ys = [y(t)[0,0] for t in ts]
    bs = np.matrix([(b(t).T).tolist()[0] for t in ts]).T
    
    return ys, bs
    

def do_p_1_17(Ar):
    print 'p 1.17: '
    
    # get noisy measurements and bj's
    ys, bs = generate_synthetic_data(Ar)
    
    
    # define functions for f and df/dx, these get used in the nonlinear least squares routine
    def f(x):
        return 2*bs.T*x - x.T*x
    def dfdx(x):
        val = 2*bs.T - x.T
        return val
        
    # initialize the estimator - this uses a module I wrote, see attached code
    nonlinear_least_squares_estimator = NLSE(f, dfdx)
    
    # run the iterative estimation routine with [0,0,0] initial condition
    nonlinear_least_squares_estimator.initialize_with_guess([0, 0, 0])
    xhat, iterations = nonlinear_least_squares_estimator.run_estimation(ys, stop_condition=0.0001, max_iterations=200)
    print xhat.T, iterations
    
    # run the iterative estimation routine with [-1,-1,-1] initial condition
    nonlinear_least_squares_estimator.initialize_with_guess([-100,-100,-100])
    xhat, iterations = nonlinear_least_squares_estimator.run_estimation(ys, stop_condition=0.0001, max_iterations=200)
    print xhat.T, iterations
        
    # run the iterative estimation routine with [10,10,10] initial condition
    nonlinear_least_squares_estimator.initialize_with_guess([100000,10000,10000])
    xhat, iterations = nonlinear_least_squares_estimator.run_estimation(ys, stop_condition=0.0001, max_iterations=200)
    print xhat.T, iterations    
    
    print
    print
    

def do_p_1_18(Ar):
    print 'p 1.18: '
    
    # get noisy measurements and bj's
    ys, bs = generate_synthetic_data(Ar)
    ys = np.matrix(ys).T
    
    # note: bs shape is 3x1001
    
    # get means
    ymean = np.mean(ys)
    bmean = np.mean(bs, axis=1) # take mean along rows, so we end up with a 3x1 matrix
    
    # calculate deviations from mean (crescent's in book)
    ycrescent = ys-ymean
    bmeanlist = np.hstack([bmean for i in range(bs.shape[1])]) # copy bmean 1001 times
    bcrescent = bs - bmean
    
    # calculate P, as defined in book
    P = (4*bs*bs.T).I
    
    # calculate xhat (aka chat), as defined in the book
    xhat = P*2*bs*ys
    print xhat.T
    
    print
    print
    
    
if __name__ == '__main__':

    ## PROBLEM 1.17
    
    # define Ar as in the book
    def Ar(t):
        Arj = np.matrix([10*np.sin(0.001*t), 5*np.sin(0.002*t), 10*np.cos(0.001*t)]).T
        return Arj
        
    # do the problem
    do_p_1_17(Ar)
        
    '''
    RESULTS:
    
    for initial condition of [0,0,0], the iterative process yields: [[ 0.49996038  0.29999508  0.60003693]], 5 iterations
    
    for initial condition of [-100,-100,-100], the iterative process yields: [[ 0.49996038  0.29999507  0.60003693]], 6 iterations
    
    for initial condition of [0,0,0], the iterative process yields: [[ 0.49996038  0.29999507  0.60003693]], 6 iterations

    All three of these (very different) initial conditions result in almost perfect estimates of xhat

    '''
    
    ## PROBLEM 1.18
    
    # define Ar as before
    def Ar(t):
        Arj = np.matrix([10*np.sin(0.001*t), 5*np.sin(0.002*t), 10*np.cos(0.001*t)]).T
        return Arj
        
    do_p_1_18(Ar)
    
    '''
    RESULTS:
    
    running this linearized method yields: xhat = [[ 0.47907049  0.24624506  0.62222234]]
    
    This is close to the real answer of [.5,.3,.6], but not as close as the nonlinear method
    
    '''
    
    # define Ar as a particular trajectory, as in the book:
    def Ar(t):
        Arj = np.matrix([10*np.sin(0.001*t), 5, 10*np.cos(0.001*t)]).T
        return Arj
    
    # do the nonlinear method
    do_p_1_17(Ar)
    
    # do the linear method
    do_p_1_18(Ar)
    
    '''
    RESULTS:
    
    Running the nonlinear iterative approach yields xhat = [[ 0.49996935  0.29993213  0.59995854]], 5 iterations
    
    Running the linear approach yields xhat = [[ 0.49991216  0.23378047  0.59990391]]
    
    This is somewhat closer than we got before with the linear approach, which is not surprising since the new system is a little more linear.
    
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
