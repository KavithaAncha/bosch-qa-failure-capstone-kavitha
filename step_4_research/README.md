# 🔍 Step 4 – Reproducing Bosch QA Failure Prediction

As part of my Capstone project titled **"Early Prediction of QA Failures from Test Log Data"**, I reproduced a published baseline machine learning solution to understand the structure, challenges, and modeling strategies related to the Bosch Production Line dataset.

---

## 📂 Original Research Reference

- **GitHub Repo**: [liamculligan/bosch-production-line-performance](https://github.com/liamculligan/bosch-production-line-performance)
- **Kaggle Competition**: [Bosch Production Line Performance](https://www.kaggle.com/competitions/bosch-production-line-performance)

This repository demonstrated an XGBoost-based pipeline for binary classification using only numeric features in the dataset. I reproduced the workflow and results using Google Colab and a 100,000-row sample due to memory limitations.

---

## ✅ Reproduction Summary

- **Model**: XGBoost Classifier
- **Metric Used**: Matthews Correlation Coefficient (MCC)
- **Data Subset**: 100,000 rows from `train_numeric.csv.zip`
- **Notebook**: [`Step4_Bosch_Reproduction.ipynb`](./Step4_Bosch_Reproduction.ipynb)

---

## 📊 Results

| Metric | Value     |
|--------|-----------|
| MCC    | 0.1766    |

- Model successfully trained on sparse, high-dimensional numeric data.
- MCC was selected for its robustness in imbalanced classification problems.
- Basic preprocessing included:
  - Dropping `Id` column
  - Filling missing values with -999
  - 80/20 train/test split

---

## 🧠 Key Insights

- The model performed decently with minimal tuning on a subset of the dataset.
- The numeric data alone has signal, but performance could be improved by:
  - Adding **timestamp-derived features**
  - Including **categorical features** after encoding
  - Using **dimensionality reduction** (PCA or L1 regularization)
  - Trying **LightGBM** for speed and efficiency

---

## 🚀 Next Steps

- Use this XGBoost baseline as a performance reference.
- Enhance features using timestamps and time-series logic.
- Compare baseline against LightGBM and logistic regression with full feature sets.

---

## 🔗 Files

- [Step4_Bosch_Reproduction.ipynb](./Step4_Bosch_Reproduction.ipynb): Clean, reproducible Colab notebook with code, results, and commentary.
