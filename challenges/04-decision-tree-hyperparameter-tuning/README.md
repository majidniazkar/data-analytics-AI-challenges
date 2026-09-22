# Challenge 4 - A decision tree model with hyperparameter tuning

**Topic:** Supervised classification &nbsp;|&nbsp; **Techniques:** Decision tree, hyperparameter tuning (max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes) &nbsp;|&nbsp;
**Data:** the same water quality dataset as [challenge 3](../03-classifier-comparison-water-quality/data)

## Description

The objective of this challenge is to develop a supervised Machine Learning (ML) model, i.e. a
decision tree model, to delineate the water quality status of a water sample. In this challenge, the
same data used in the third challenge can be employed. To be more precise, the dataset consists of 295
samples with nine water quality parameters as input data and Water Quality Index (WQI) as output data,
respectively. The decision tree should understand the relationship between WQI and all or a subset of
the water quality parameters. Table 1 lists different ranges of WQI with the corresponding water
quality status:

**Table 1 - Water quality status based on WQI values**

| Class | WQI value | Water quality status |
|-------|-----------|----------------------|
| A | < 50 | Excellent |
| B | 51-100 | Good |
| C | 101-200 | Poor water |
| D | 201-300 | Very poor water |
| E | > 300 | Water unsuitable for drinking |

For developing the decision tree models, 75% of the dataset can be used for training, and the rest of
the dataset can be utilized to test model performance. While training the decision tree, you should
opt for tuning at least one or more hyperparameters. The hyperparameters are:

1. `max_depth` - the maximum depth of the tree
2. `min_samples_split` - the minimum number of samples required to split an internal node
3. `min_samples_leaf` - the minimum number of samples required to be at a leaf node
4. `max_leaf_nodes` - the maximum number of trees

## Dataset

This challenge reuses the dataset from
[challenge 3](../03-classifier-comparison-water-quality/data).

## Deliverables

Your Python code file (not a Colab link) and a short report of at most two pages describing the data
preprocessing, data division, model development, and results of the hyperparameter tuning.

## Solutions

A reference solution exists but is kept in a separate private repository so the challenge stays
solvable. If you are an instructor or reviewer and need access, contact the author.
