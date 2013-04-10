from __future__ import division
import numpy as np

class NonlinearLeastSquaresEstimator:
    def __init__(self, f, dfdx):
        '''
        f, df are functions of x
        '''
        self.f = f
        self.dfdx = dfdx
        
    def fit(self, y, W):
        xhat = self.xhat
        y = np.matrix(y).T
        
        deltay = y - self.f(xhat) 
        J = deltay.T*W*deltay
        H = self.dfdx(xhat)
        
        # update and save xhat
        deltax = (H.T*W*H).I*H.T*W*deltay
        self.xhat = self.xhat + deltax
        
        deltaJ = np.abs(J - self.J) / J
        self.J = J
        
        return deltaJ
        
    def initialize_with_guess(self, xhat):
        self.xhat = np.matrix(xhat).T
        self.J = 100000.
        self.iteration = 0
        
    def run_estimation(self, ylist, W=None, stop_condition=0.01, max_iterations=1000):
        i = 0
        if max_iterations > len(ylist):
            max_iterations = len(ylist)
            
        if W is None:
            W = np.matrix(np.eye(len(ylist)))
            
        while i < max_iterations:
        
            # run fitting routine, note, new xhat is stored 
            deltaJ = self.fit(ylist, W)
            
            # check end condition
            if deltaJ < stop_condition / np.linalg.norm(W):
                break
            i += 1
        
        return self.xhat, i
        
        
        
