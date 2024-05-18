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