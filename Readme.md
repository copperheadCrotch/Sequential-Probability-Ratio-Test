sprt --- Wald's Sequential Probability Ratio Test
=========================
Installation
-----------------

```
pip install sprt
```

Class
-----------------

| Distribution  | Python Constructor | 
| ------------- |:-------------:| 
| Binomial      | SPRTBinomial  | 
| Normal        | SPRTNormal    | 
| Poisson       | SPRTPoisson    | 

Example
-----------

Wald's sequential probability ratio test
```python
import sprt as sprt
import numpy as np

test = sprt.SPRTNormal(alpha = 0.05, beta = 0.2, h0 = 0, h1 = 1, 
values = np.random.normal(0, 1, 10), 
variance = 1)
```
Obtain the boundary plot
```python
# Show plot
test.plot()
```

Docs
------------


Reference
------------
Wald, Abraham (June 1945). "Sequential Tests of Statistical Hypotheses". *Annals of Mathematical Statistics*. **16** (2): 117–186.
