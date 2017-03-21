sprt --- Wald's Sequential Probability Ratio Test
=========================

Data Distribution
-----------------

*Bernoulli
*Normal


Example
-----------

Wald's sequential probability ratio test
```python
test = SPRTNormal(alpha = 0.05, beta = 0.2, h0 = 0, h1 = 1, values = np.array([-0.57534696, 0.60796432, -1.61788271, -0.05556197, 0.51940720]), variance = 1)
# Show plot
test.plot()
```
