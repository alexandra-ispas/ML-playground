# Simple Liniar Regression
> y = b_0 + b_1 * x_1
> * y: dependent variable
> * x_1: independent variable
> * b_0: constant (y-intercept)
> * b_1: coefficient (slope)

# Ordinary Least Squares
There are multiple slope lines that can be drawn for linear regression.
The best line is the one that minimizes the sum of the squared differences between the observed values and the predicted values.
This method is called Ordinary Least Squares (OLS).

epsilon (residual) = y - y_hat (the difference between the observed value and the predicted value)

y_hat = b_0 + b_1 * x_1, where b_0 and b_1 are chosen to minimize the sum of the squared differences between the observed values and the predicted values.

The regression line is the one that has the smallest value of the following sum:
> SUM(epsilon^2) = SUM(y - y_hat)^2 = SUM(y - (b_0 + b_1 * x_1))^2

# Dummy variables
For example, if we have a categorical variable with two categories, we can create a dummy variable that takes the value of 0 or 1 for each category.\
Let's say we have a variable called "Country" with two categories: France and Germany.\
We would have a column for France and a column for Germany, but the two columns would be redundant as `Germany = 1 - France` (multicoliniarity). \
You should always include `n-1` dummy variables for `n` categories.

# Statistical Significance