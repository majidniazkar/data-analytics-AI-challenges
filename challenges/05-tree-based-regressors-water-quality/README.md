# Challenge 5 - Build regressors based on random tree and random forest

**Topic:** Supervised regression &nbsp;|&nbsp; **Techniques:** Random tree and random forest regressors, hyperparameter tuning, performance comparison &nbsp;|&nbsp;
**Data:** the same water quality dataset as [challenge 3](../03-classifier-comparison-water-quality/data)

## Description

The objective of this challenge is to develop two supervised Machine Learning (ML) models, i.e. a
random tree model and a random forest model, to predict the Water Quality Index (WQI) value. In this
challenge, the same data used in the third and fourth challenges can be employed. The dataset has 295
samples, while each sample consists of nine water quality parameters and a corresponding WQI. The
tree-based regressors should capture the relationship between water quality parameters and WQI so that
they can estimate WQI when the water quality parameters are known. Table 1 shows different water
quality statuses based on the WQI values:

**Table 1 - Water quality status based on different ranges of the WQI values**

| Class | WQI value | Water quality status |
|-------|-----------|----------------------|
| A | < 50 | Excellent |
| B | 51-100 | Good |
| C | 101-200 | Poor water |
| D | 201-300 | Very poor water |
| E | > 300 | Water unsuitable for drinking |

For developing the random tree model and random forest models, 75% of the dataset can be used for
training, while the rest can be exploited to compare their performances. When training tree-based
regressors, optimizing hyperparameters is recommended. The hyperparameters include:

1. tree maximum depth
2. minimum samples split
3. minimum samples leaf
4. maximum leaf nodes

## Dataset

This challenge reuses the dataset from
[challenge 3](../03-classifier-comparison-water-quality/data).

## Deliverables

Your Python code file (**not** a Colab link) and a short report of at most two pages describing the
data preprocessing, data division, model development, hyperparameter tuning, and results of comparing
the two regressors.

## Solutions

A reference solution exists but is kept in a separate private repository so the challenge stays
solvable. If you are an instructor or reviewer and need access, contact the author.
