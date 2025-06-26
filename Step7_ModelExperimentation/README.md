# Bosch QA Failure Prediction – Step 7: Model Experimentation


This specific notebook focuses on **model experimentation**, evaluating various machine learning techniques to handle a highly imbalanced classification problem.

---

## Notebook Purpose

In this step, the objective was to:

- Train and evaluate multiple models on the Bosch dataset
- Explore strategies to deal with class imbalance
- Diagnose overfitting through performance metrics and confusion matrices
- Apply mentor feedback regarding model behavior and result interpretation

---

## Techniques Applied

- Models: Logistic Regression, Random Forest, XGBoost, LightGBM
- Imbalance handling: `class_weight='balanced'`, SMOTE
- Evaluation: Accuracy, F1 Score, ROC AUC, Confusion Matrix
- Improvements: GridSearchCV for tuning, Ensemble (VotingClassifier)

---

## Feedback Loop

This notebook includes an explicit response to mentor guidance on:
- Overfitting diagnosis using confusion matrices
- Revisiting evaluation metrics for minority class (Response = 1)
- Planning for next-stage improvements

---

## What's Next

Follow-up actions are proposed at the end of the notebook, including:

- Cost-sensitive learning
- Anomaly detection techniques
- Undersampling strategies
- Feature engineering and threshold tuning

These will be explored in Step 8: **Scaling the Prototype**.

---

## Files

```bash
.
├── Bosch_Step7_ModelExperimentation.ipynb
├── README.md
