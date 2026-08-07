# Decision Tree Case Study

Minimal project scaffold for an ML case study focused on:

- EDA
- data preprocessing
- feature engineering
- Decision Tree classification
- pre-pruning
- post-pruning

## Suggested structure

```text
.
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/
├── reports/
│   └── figures/
├── src/
│   ├── __init__.py
│   ├── data/
│   ├── features/
│   └── models/
├── models/
├── .gitignore
└── README.md
```

## How to use

- Put the original dataset in `data/raw/`
- Save cleaned or transformed data in `data/interim/` or `data/processed/`
- Use `notebooks/` for EDA and experimentation
- Put reusable code in `src/`
- Store trained model artifacts in `models/`
- Save plots and charts in `reports/figures/`

## Recommended workflow

1. Explore the data in a notebook.
2. Clean and preprocess the dataset.
3. Engineer features.
4. Train a Decision Tree classifier.
5. Tune pre-pruning settings such as `max_depth`, `min_samples_split`, and `min_samples_leaf`.
6. Evaluate post-pruning using cost-complexity pruning where supported.

