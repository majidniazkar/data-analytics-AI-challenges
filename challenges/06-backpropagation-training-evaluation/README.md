# Challenge 6 - Understanding and evaluating backpropagation training

**Topic:** Training fundamentals &nbsp;|&nbsp; **Techniques:** Manual backpropagation, hyperparameter sensitivity study, MAE / RMSE &nbsp;|&nbsp;
**Data:** student-selected: almost-linear, 6-10 features

## Description

During the last lecture we introduced our first learning approach by showing how backpropagation can
be used to train a linear regressor. In Notebook 2 (Fundamentals) you can find the comparison between
the closed-form and deterministic regression supplied by scikit-learn (in the section *Regression
using a standard library*) and the newly introduced learning-based approach (in the section *Manual
linear regression*). Both are tested with the same dataset.

While a closed-form analytical solution is practically better for a problem of this simplicity, our
goal here is to peek under the hood. By applying backpropagation to a straightforward scenario, we can
easily observe and understand the fundamental mechanics of the learning process.

When analyzing the manual learning-based approach, several key hyperparameters clearly influence the
model's performance and the final weights it converges on. You will be testing the following factors:

- **Initial random initialization** - the starting values for weights (W) and bias (B)
- **Iterations** - the total number of backpropagation training cycles (epochs)
- **Batch size** - the number of training examples utilized in one iteration
- **Learning rate** - the step size taken during gradient descent

## Your task

You are challenged to design and execute a batch of tests to determine exactly how each of the factors
listed above influences your model's training.

1. **Select a new dataset.** Find a new dataset that exhibits an "almost linear" behavior and contains
   at least 6 to 10 distinct features.
2. **Design an experiment.** Create a testing methodology to isolate and evaluate the impact of each
   individual hyperparameter.
3. **Experiment with initialization.** For the W and B initialization tests, experiment with altering
   the initial probability distribution. For example, try shifting the average, adjusting the standard
   deviation, or swapping from a normal distribution to a uniform one.
4. **Evaluate and plot.** For each factor tested, plot the Mean Absolute Error (MAE) and Root Mean
   Squared Error (RMSE).

> **Crucial tip:** keep all other factors constant while testing a specific variable, so your results
> remain scientifically valid.

> **Course materials.** This statement refers to lecture notebooks that are distributed separately and
> are not part of this repository. If you are working the challenge independently, treat the reference
> as background and implement the pieces yourself.

## Solutions

A reference solution exists but is kept in a separate private repository so the challenge stays
solvable. If you are an instructor or reviewer and need access, contact the author.
