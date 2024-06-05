5 methods of building models:
1. All-in
2. Backward Elimination \
    a. select a significance level to stay in the model (e.g. SL = 0.05) \
    b. fit the full model with all possible predictors \
    c. consider the predictor with the highest P-value. If P > SL, go to step 4, otherwise go to FIN (model is ready)\
    d. remove the predictor \
    e. fit the model without this variable. Go back to step c
3. Forward Selection \
    a. select a significance level to enter the model (e.g. SL = 0.05) \
    b. fit all simple regression models y ~ x_n. Select the one with the lowest P-value \
    c. keep this variable and fit all possible models with one extra predictor added to the one(s) you already have \
    d. consider the predictor with the lowest P-value. If P < SL, go to step c, otherwise go to FIN (model is ready)\
What is special: keep the previous model. A new variable is added, if it doesn't pass the checks, then the last model is chosen.
4. Bidirectional Elimination \
    a. select a significance level to enter and to stay in the model (e.g. SLENTER = 0.05, SLSTAY = 0.05) \
    b. perform the next step of Forward Selection (new variables must have P < SLENTER to enter) \
    c. perform all steps of Backward Elimination (old variables must have P < SLSTAY to stay) \
    d. repeat the steps until no new variables can enter and no old variables can exit
5. All possible models/Score comparison (not recommended) \
    a. select a criterion of goodness of fit (e.g. Akaike criterion) \
    b. construct all possible regression models: 2^N - 1 total combinations \
    c. select the one with the best criterion \
   Example: 10 columns means 1023 models to check

2, 3, 4 <- stepwise regression
