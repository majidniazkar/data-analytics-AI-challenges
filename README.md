# Data Analytics & AI Challenges

Ten self-contained challenges in data analytics and artificial intelligence. Each one is a
realistic brief with a real, messy dataset - work them in any language you like.

[![Validate](https://github.com/<your-github-username>/data-analytics-ai-challenges/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-github-username>/data-analytics-ai-challenges/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## What this is

Each challenge gives you a scenario, a genuine export from a public platform, and a set of
requirements. Because the datasets are real they contain duplicates, missing values, and
off-topic records that have to be handled before any modelling starts. The statements
deliberately leave the modelling and scoring choices open - there is no single correct
answer.

The challenges are ordered by difficulty but each stands alone.

## Challenges

| # | Challenge | Topic | Techniques | Data |
|---|-----------|-------|------------|------|
| 1 | [A recommender system for online shops](challenges/01-recommender-system-online-shops) | Recommender systems | Data cleaning, language detection, weighted multi-criteria scoring | 500 books from [Open Library](https://openlibrary.org) (CSV) |
| 2 | [Building an unsupervised optical character recognizer](challenges/02-unsupervised-ocr-clustering) | Unsupervised learning | K-Means, agglomerative clustering, cluster-label assignment, confusion matrix | Handwritten digits, 1797 x 64 (bundled with scikit-learn) |
| 3 | [Create three classifiers and compare their performances](challenges/03-classifier-comparison-water-quality) | Supervised classification | Three classifiers compared, 75/25 split, accuracy / precision / recall | 295 water samples, 9 parameters + WQI |
| 4 | [A decision tree model with hyperparameter tuning](challenges/04-decision-tree-hyperparameter-tuning) | Supervised classification | Decision tree, hyperparameter tuning | Water quality dataset (shared with challenge 3) |
| 5 | [Build regressors based on random tree and random forest](challenges/05-tree-based-regressors-water-quality) | Supervised regression | Random tree and random forest regressors, hyperparameter tuning | Water quality dataset (shared with challenge 3) |
| 6 | [Understanding and evaluating backpropagation training](challenges/06-backpropagation-training-evaluation) | Training fundamentals | Manual backpropagation, hyperparameter sensitivity study, MAE / RMSE | Student-selected: almost-linear, 6-10 features |
| 7 | [Deep Learning on real data](challenges/07-deep-learning-on-real-data) | Deep learning from scratch | Network topology, custom activation functions, epoch sensitivity | Student-selected: at least 10 features |
| 8 | [Fine tuning](challenges/08-deep-network-fine-tuning) | Deep learning from scratch | Softmax cross-entropy, LR decay, momentum, Glorot init, dropout | Student-selected: at least 10 features, 2-3+ classes |
| 9 | [PyTorch](challenges/09-pytorch) | Deep learning frameworks | PyTorch, data preparation, architecture selection | Student-selected: tabular, text, image or audio |
| 10 | [Keras](challenges/10-keras) | Deep learning frameworks | Keras, data preparation, architecture selection | Student-selected: tabular, text, image or audio |

## Layout

```
challenges/
  01-recommender-system-online-shops/
    README.md          the challenge statement
    challenge.pdf      the original brief, as handed out
    data/              input dataset
```

## Getting started

```bash
git clone https://github.com/majidniazkar/data-analytics-ai-challenges.git
cd data-analytics-ai-challenges

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` is a suggested starting point, not a constraint - add whatever your
approach needs.

## Solutions

Reference solutions for all ten challenges are kept in a separate private repository so the
challenges stay solvable. Instructors and reviewers can request access from the author.

## Data provenance

Every dataset is a real export from a public source, credited in the challenge it belongs
to. No dataset contains personal or sensitive information. Open Library publishes its
catalogue data under CC0; check the terms of each source before redistributing a dataset
beyond this repository.

## License

Released under the [MIT License](LICENSE).
