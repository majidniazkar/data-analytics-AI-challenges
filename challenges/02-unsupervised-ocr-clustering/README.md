# Challenge 2 - Building an unsupervised optical character recognizer

**Topic:** Unsupervised learning &nbsp;|&nbsp; **Techniques:** K-Means, agglomerative clustering, cluster-label assignment, confusion matrix &nbsp;|&nbsp;
**Data:** `sklearn.datasets.load_digits` (1797 samples, 64 features) - no file needed

## Description

The objective of this challenge is to build an unsupervised optical character recognizer (OCR)
using a classic handwritten digits dataset, called National Institute of Standards and Technology
(NIST). The NIST dataset includes 1797 samples with 64 features (8x8 grayscale images). Generally,
the task entails clustering the images, visualizing the cluster centroids, and evaluating how well
clustering alone can detect digits. This challenge helps you to explore the data structure without
any supervision. The interesting part is to delineate which cluster is which number. Should we
utilize a cluster-label alignment or do we need to check the digit matching with our own eyes?

For developing an unsupervised OCR, first you need to load the data. You can visualize a few samples
in the dataset and store true labels of the images. Without using any labels, you need to cluster the
images so that each cluster consists of a digit. The key step is to develop two clustering methods:

1. K-Means
2. Agglomerative Clustering

You can explore different hyperparameters and settings for these two unsupervised methods, while the
recommendation is to use 10 clusters as we have only 10 digits (0-9).

After applying the clustering methods, you can visualize cluster centroids for K-Means. Do the 10
centroids resemble digits? If the clusters and digits do not match, you should compute the optimal
assignment between clusters and true digits. This way you can apply the mapping to all clusters and
compute accuracy through a confusion matrix. This helps you to evaluate how well clustering alone can
reveal digit identity. Which digits can be recovered better, and why? Finally, you can visualize a
few examples of digits and check their clustering.

## Dataset

The digits dataset ships with scikit-learn, so there is no file to download:

```python
from sklearn.datasets import load_digits
digits = load_digits()
```

## Deliverables

A short report of at most two pages describing the clustering results and answering the questions
raised above, accompanied by your Python code.

## Solutions

A reference solution exists but is kept in a separate private repository so the challenge stays
solvable. If you are an instructor or reviewer and need access, contact the author.
