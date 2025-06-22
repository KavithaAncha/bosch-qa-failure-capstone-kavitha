# Step 7 – Model Experimentation

This notebook explores multiple classification models to predict QA failures using the Bosch dataset.

---

## Models Tried
- Logistic Regression
- Random Forest
- XGBoost
- LightGBM
- Ensemble (VotingClassifier)

---

## Methodology
- Preprocessed Bosch dataset used (`train_numeric` sample with `Response` as target)
- Missing values handled using `SimpleImputer` (median)
- Baseline models trained and evaluated using F1 Score and ROC AUC
- XGBoost model tuned via GridSearchCV
- Cross-validation performed (5-fold)

---

## Final Model
**Model**: Tuned XGBoost  
**Performance**:
- F1 Score: `...` *(fill in based on output)*
- ROC AUC: `...`
- CV F1 Score: `...`
- Training time: ~ `...` seconds

---

## File Included
- [`Step7_Bosch_ModelExperimentation.ipynb`](./Step7_Bosch_ModelExperimentation.ipynb)

This file contains all code, markdown explanations, and evaluation outputs used in this step.

---

## Status
✔️ Completed as part of Capstone Step 7 submission.
