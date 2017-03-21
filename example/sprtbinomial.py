# Example
import numpy as np
from sprt import SPRTBinomial

binomial_data = np.random.binomial(1, 0.52, size = 10)
test = SPRTBinomial(alpha = 0.05, beta = 0.2, h1 = 0.55, h0 = 0.5, values = binomial_data)
test.plotBoundary()
test.plot()
