
# coding: utf-8

# In[1]:

# SPRT 
# Binomial Endpoints
import sprt as sprt
import numpy as np

# Null value
h0 = 0.5
# Alternative value
h1 = 0.55
# Type I error rate = 0.05
alpha = 0.05
# Type II error rate = 0.2
beta = 0.2
# Values
values = np.random.binomial(1, 0.55, 100)
test = sprt.SPRTBinomial(h0 = h0, h1 = h1, alpha = alpha, beta = beta, values = values)


# In[2]:

test.plot()


# In[3]:

# Plot the boundary only
test.plotBoundary()


# In[4]:

# Plot the data and boundary but without fill the color
test.plot(fill = False)

