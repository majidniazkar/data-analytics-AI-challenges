# Challenge 3 - Create three classifiers and compare their performances

**Topic:** Supervised classification &nbsp;|&nbsp; **Techniques:** Three classifiers compared, 75/25 train-test split, accuracy / precision / recall &nbsp;|&nbsp;
**Data:** 295 water samples, 9 quality parameters + WQI ([`data/`](data))

## Description

The objective of this challenge is to develop three supervised Machine Learning (ML) models to
delineate whether a water sample is drinkable or not. For this challenge, your input data includes
water quality parameters (like dissolved oxygen), while the output is a Water Quality Index (WQI).
You can develop three ML classifiers (like KNN, SVR, etc.) to understand the relationship between
water quality parameters and WQI. For clarification, the following table presents different ranges of
WQI and their associated water quality status:

**Table 1 - Water quality classification based on WQI values**

| Class | WQI value | Water quality status |
|-------|-----------|----------------------|
| A | < 50 | Excellent |
| B | 51-100 | Good |
| C | 101-200 | Poor water |
| D | 201-300 | Very poor water |
| E | > 300 | Water unsuitable for drinking |

The dataset includes 295 samples. It was adopted from an online repository. The input parameters are:

1. Temperature
2. Dissolved Oxygen
3. pH
4. Bio-Chemical Oxygen Demand (mg/L)
5. Faecal Streptococci (MPN/100 mL)
6. Nitrate (mg/L)
7. Faecal Coliform (MPN/100 mL)
8. Total Coliform (MPN/100 mL)
9. Conductivity (mho/cm)

You can use 75% of the dataset for training your ML models, while the rest of the dataset will be
utilized to compare the performance of different classifiers.

## Deliverables

Your Python code and a short report of at most two pages describing the data preprocessing, data
division, classifiers, and results of the comparative analysis for both train and test datasets using
proper metrics (like accuracy, recall, precision, etc.).

## Solutions

A reference solution exists but is kept in a separate private repository so the challenge stays
solvable. If you are an instructor or reviewer and need access, contact the author.
