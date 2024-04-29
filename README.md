# Summary Picker Function

## Description
The `summary_picker` function is designed to selectively print summary statistics from a fitted statistical model object. It allows the user to specify which statistics to display, such as coefficients, standard errors, R-squared values, adjusted R-squared values, and p-values. This function is useful for generating custom summary outputs tailored to specific needs, especially when analyzing statistical models.

## Function Parameters
- `model`: The fitted model object from which to extract summary statistics. This should be a fitted model from `statsmodels` or similar.
- `params` (list): A list of strings representing the names of the coefficients to display. Defaults to an empty list.
- `bse` (list): A list of strings indicating the names of the coefficients for which to display standard errors. Defaults to an empty list.
- `rsquared` (bool): If `True`, display the R-squared value of the model. Defaults to `False`.
- `rsquared_adj` (bool): If `True`, display the adjusted R-squared value of the model. Defaults to `False`.
- `pvalues` (list): A list of strings specifying the names of the coefficients for which to display p-values. Defaults to an empty list.

## Usage Example

```python
import statsmodels.api as sm
import numpy as np

# Generate sample data
np.random.seed(10)
X = np.random.rand(100, 2)  # 100 observations and 2 predictors
X = sm.add_constant(X)  # Adds a constant term to the predictor
y = X[:, 0] + 2 * X[:, 1] + 3 * X[:, 2] + np.random.randn(100)  # Generating response

# Fit an OLS model
model = sm.OLS(y, X)
results = model.fit()

# Use summary_picker to get selected summary details
custom_summary = summary_picker(model, params=['const', 'x1'], bse=['const', 'x1'], rsquared=True, rsquared_adj=True)
print(custom_summary)
