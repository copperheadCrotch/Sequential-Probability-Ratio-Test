sprt --- Wald's Sequential Probability Ratio Test
=========================

Data Distribution
-----------------

..*Bernoulli
..*Normal


Example
-----------

Wald's sequential probability ratio test
```python
import sprt as sprt
import numpy as np

test = sprt.SPRTNormal(alpha = 0.05, beta = 0.2, h0 = 0, h1 = 1, 
values = np.random.normal(10, 0, 1), 
variance = 1)
```
Obtain the boundary plot
```python
# Show plot
test.plot()
```
