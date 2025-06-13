# Step 4 – Reproducing Bosch QA Failure Prediction

This notebook reproduces an XGBoost-based model to predict QA test failures using numeric sensor data from the Bosch Production Line dataset.

- Original notebook: [liamculligan GitHub](https://github.com/liamculligan/bosch-production-line-performance)
- My notebook: [Step4_Bosch_Reproduction.ipynb](./Step4_Bosch_Reproduction.ipynb)

##  Summary

- Used 100,000 rows from `train_numeric.csv.zip` due to Colab memory limits
- Dropped `Id`, separated `Response`, and filled missing values
- Trained XGBoost classifier with MCC as the evaluation metric

##  Results

- **Matthews Correlation Coefficient (MCC)**: 0.1766

##  Insights

- MCC is more effective than accuracy in imbalanced datasets
- The numeric-only baseline is a good starting point
- Plan to use timestamp features, try LightGBM, and apply dimensionality reduction in Step 5
