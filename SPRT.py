import numpy as np
import abc
import sys
import matplotlib.pyplot as plt

# SPRT test
class SPRT:

    __metaclass__ = abc.ABCMeta
    
    """Run sequential probability ratio test (SPRT) for bindary/normal endpoints"""
    # Init function
    def __init__(self, alpha = 0.05, beta = 0.2,
                 h0 = 0, h1 = 1, values = []):

        self.alpha = alpha
        self.beta = beta
        self.h0 = h0
        self.h1 = h1
        self.values = values
        self.upperCritical = np.log((1 - self.beta)/self.alpha)
        self.lowerCritical = np.log((1 - self.alpha)/self.beta)
        self.num_observation = len(values)
        self.seq_observation = np.array(range(1, self.num_observation + 1))
        # Check the arguments
        self.checkArgs()
        # Calculate boundary
        self.calBoundary()
        # Sequential test
        self.seqTest()
        
    # Plot the boundary and points
    def plot(self, boundaryColor = ["#b14a55", "#fe6b7a"]):

        upperBoundaryColor, lowerBoundaryColor = boundaryColor
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self.seq_observation, self.upperBoundary, color = upperBoundaryColor)
        ax.plot(self.seq_observation, self.lowerBoundary, color = lowerBoundaryColor)
        plt.show()

    # Plot only the boundary values
    def plot_boundary(self):

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self.seq_observation, self.upperBoundary, color="#b14a55")
        ax.plot(self.seq_observation, self.lowerBoundary, color="#fe6b7a")
        plt.show()
        
    # Abstract method, calculate the boundary by time
    @abc.abstractmethod
    def calBoundary(self):

        return 

    # Abstarct method, function to check the input argument
    def checkArgs(self):

        return 
            
    # Abstract method, calculate the boundary by time
    @abc.abstractmethod
    def seqTest(self):

        return 
        
# Binary Endpoint
class SPRTBinomial(SPRT):

    """Run sequential probability ratio test (SPRT) for bindary endpoints"""
    def calBoundary(self):

        self.denom = (np.log(self.h1/(1 - self.h1)) - np.log(self.h0/(1 - self.h0)))
        self.slope = (np.log(1 - self.h0) - np.log(1 - self.h1))/ self.denom
        self.upperIntercept, self.lowerIntercept = np.array([self.upperCritical, self.lowerCritical]) / self.denom
        self.upperBoundary = self.seq_observation * self.slope + self.upperIntercept
        self.lowerBoundary = self.seq_observation * self.slope + self.lowerIntercept

    def seqTest(self):

        self.cum_values = np.cumsum(self.values)


a = SPRTBinomial(alpha = 0.05, beta = 0.2, h0 = 0.1, h1 = 0.3, values = [1, 1, 0, 1, 0, 1])
a.plot_boundary()  
