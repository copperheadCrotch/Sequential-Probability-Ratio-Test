import abc
import matplotlib.pyplot as plt
import numbers
import numpy as np
import sys

# Check if pandas is installed
try:

    import pandas as pd
    PANDAS_INSTALLED = True

except:

    PANDAS_INSTALLED = False
    

# SPRT test
class SPRT:

    __metaclass__ = abc.ABCMeta
    
    """Run sequential probability ratio test (SPRT) for bindary/normal endpoints"""
    # Init function
    def __init__(self, alpha = 0.05, beta = 0.2,
                 h0 = 0, h1 = 1, values = [], variance = 0):

        # Input arguments
        self.alpha = alpha
        self.beta = beta
        self.h0 = h0
        self.h1 = h1
        self.values = values
        self.cum_values = np.cumsum(self.values)
        self.variance = variance
        # Necessary arguments
        self.upperCritical = np.log((1 - self.beta)/self.alpha)
        self.lowerCritical = np.log(self.beta/(1 - self.alpha))
        self.num_observation = len(values)
        self._seq_observation = np.array(range(1, self.num_observation + 1))
        self.decision = None
        # Check the arguments
        self._checkCommonArgs()
        self._checkOtherArgs()
        # Calculate boundary
        self.calBoundary()
        # Sequential test
        self.seqTest()

    # Check common arguments in the fuction
    def _checkCommonArgs(self):

        if not all(0 < i <1 for i in [self.alpha, self.beta]):

            sys.stderr.write("Type I error rate and type II error rate are between 0 and 1!")
            sys.exit(1)

    # Plot the boundary and points
    def plot(self, boundaryColor = ["#cc181e", "#2793e8", 	"#559900"],  pointColor = "#3f5d7d", fill = True):

        upperBoundaryColor, lowerBoundaryColor, continueColor = boundaryColor
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self._seq_observation, self.upperBoundary, color = upperBoundaryColor, linewidth = 1, alpha = 0.95)
        ax.plot(self._seq_observation, self.lowerBoundary, color = lowerBoundaryColor,  linewidth = 1,  alpha = 0.95)
        ax.scatter(self._seq_observation, self.cum_values, color = pointColor, zorder = 1000)
        yticks, yticklabels = plt.yticks()
        ymin = yticks[0]
        ymax = yticks[-1]
        if fill:

            ax.fill_between(self._seq_observation, self.lowerBoundary, ymin, color = lowerBoundaryColor, alpha = 0.5)
            ax.fill_between(self._seq_observation, self.lowerBoundary, self.upperBoundary, color = continueColor, alpha = 0.5)
            ax.fill_between(self._seq_observation, self.lowerBoundary, ymax, color = upperBoundaryColor, alpha = 0.5)

        ax.spines["top"].set_visible(False)      
        ax.spines["right"].set_visible(False)      
        ax.get_xaxis().tick_bottom()    
        ax.get_yaxis().tick_left()
        xticks, xticklabels = plt.xticks()
        xmin = 0.95
        xmax = self.num_observation + 0.05 
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xticks(self._seq_observation)
        plt.xlabel("Observations")
        plt.ylabel("Cumulative Sum")
        plt.show()

    # Plot only the boundary values
    def plotBoundary(self, boundaryColor = ["#cc181e", "#2793e8", "#559900"], fill = True):

        upperBoundaryColor, lowerBoundaryColor, continueColor = boundaryColor
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self._seq_observation, self.upperBoundary, color="#b14a55", linewidth = 1)
        ax.plot(self._seq_observation, self.lowerBoundary, color="#fe6b7a", linewidth = 1)
        if fill:

            ax.fill_between()
            
        ax.spines["top"].set_visible(False)      
        ax.spines["right"].set_visible(False)      
        ax.get_xaxis().tick_bottom()    
        ax.get_yaxis().tick_left()
        plt.xlim(1, self.num_observation)
        plt.xticks(self._seq_observation)
        plt.xlabel("Observations")
        plt.ylabel("Cumulative Sum")
        plt.show()

    # Print test result
    def printResult(self):

        print("Decision:\t" + self.decision + "\n")
        if PANDAS_INSTALLED == True:

            output_dict = {'values': self.cum_values, 'lower': self.lowerBoundary, 'upper': self.upperBoundary, 'n': self._seq_observation}
            output_df = pd.DataFrame(output_dict, columns = ['values', 'lower', 'upper', 'n'])
            print(output_df)

        else:

            print('values\tlower\tupper\tn\n')
            for i in range(0, self.num_observation - 1):

                print('%.3f\t%.3f\t%.3f\t%d\n'%(self.cum_values[i], self.lowerBoundary[i], self.upperBoundary[i], self._seq_observation[i]))

        
    # Sequential test
    def seqTest(self):

        self.test_statistic = self.cum_values[self.num_observation - 1]
        if self.test_statistic > self.upperBoundary[self.num_observation - 1]:

            self.decision = "Reject"

        elif self.test_statistic < self.lowerBoundary[self.num_observation - 1]:

            self.decision = "Accept"

        else:

            self.decision = "Continue"

        self.printResult()
        
    # Abstract method, calculate the boundary by time
    @abc.abstractmethod
    def calBoundary(self):

        return

    # Abstarct method, function to check other input arguments
    @abc.abstractmethod
    def _checkOtherArgs(self):

        return 
        
# Binary Endpoint
class SPRTBinomial(SPRT):

    """Run sequential probability ratio test (SPRT) for bindary endpoints"""
    # Calculate boundary for binary outcome
    def calBoundary(self):

        self.denom = (np.log(self.h1/(1 - self.h1)) - np.log(self.h0/(1 - self.h0)))
        self.slope = (np.log(1 - self.h0) - np.log(1 - self.h1))/ self.denom
        self.upperIntercept, self.lowerIntercept = np.array([self.upperCritical, self.lowerCritical]) / self.denom
        self.upperBoundary = self._seq_observation * self.slope + self.upperIntercept
        self.lowerBoundary = self._seq_observation * self.slope + self.lowerIntercept

    # Check arguments
    def _checkOtherArgs(self):

        # Check h0 and h1
        if not all(0 < i <1 for i in [self.h0, self.h1]):

            sys.stderr.write("Null and alternative values are between 0 and 1!")
            sys.exit(1)

        # Check values
        if not all(i in [0, 1] for i in self.values):

            sys.stderr.write("Value is a Beroulli variable!")
            sys.exit(1)


# Normal Endpoint
class SPRTNormal(SPRT):

    """Run sequential probability ratio test (SPRT) for normal endpoints"""
    # Calculate boundary for normal outcome
    def calBoundary(self):

        self.slope = (self.h1 + self.h0)/2
        self.upperIntercept, self.lowerIntercept = np.array([self.upperCritical, self.lowerCritical]) * self.variance / (self.h1 - self.h0)
        self.upperBoundary = self._seq_observation * self.slope + self.upperIntercept
        self.lowerBoundary = self._seq_observation * self.slope + self.lowerIntercept

    # Check arguments
    def _checkOtherArgs(self):

        # Check variance
        if self.variance <= 0:

            sys.stderr.write("Variance of normal distribution is positive!")
            sys.exit(1)
