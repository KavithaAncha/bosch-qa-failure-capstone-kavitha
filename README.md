# Bosch QA Failure Capstone – Sample Data & Extraction Script

This repository contains data and scripts for Step 2 of my Capstone Project.

##  Project Overview

**Capstone Theme:** Predicting QA Failures from Test Log Data  
**Main Dataset:** [Bosch Production Line Performance – Kaggle](https://www.kaggle.com/competitions/bosch-production-line-performance/data)

In real-world manufacturing or embedded QA workflows (like aerospace and defense software testing), failure patterns can often be predicted from early-stage logs. 
This project aims to explore machine learning methods to model those patterns using real-world industrial data.

---

## Contents

### `data/` folder includes:

| File | Description |
|------|-------------|
| `sample_train_numeric.csv` | First 1000 rows from `train_numeric.csv` – used for initial exploration and testing |
| `sample_train_date.csv` | First 1000 rows from `train_date.csv` – includes timestamp-based features |
| `sample_train_categorical.csv` | First 1000 rows from `train_categorical.csv` – includes encoded categorical features |
| `Bosch dataset files.py` | Python script used to load the original files and extract these 1000-row samples |

---

## Original Dataset Source

The full dataset (14GB+) is available from Kaggle at:  
🔗 https://www.kaggle.com/competitions/bosch-production-line-performance/data

Due to size, only small samples are committed to this repository.

---

## 🔧 Script Usage

To generate the smaller sample datasets from the original Bosch files, run the following command from your project root:

```bash
python "data/Bosch dataset files.py"

## Step 5 – Data Wrangling & EDA

Notebook: [`Step5_DataWrangling_Bosch.ipynb`](step_5_wrangling/Step5_DataWrangling_Bosch.ipynb)

This step focused on preparing the Bosch dataset for modeling:
- Removed constant and high-missing-value features
- Imputed missing values using median strategy
- Created a 100K-row sampled subset to enable efficient model prototyping
- (Optional) Performed exploratory data analysis (EDA) to identify top features correlated with QA failures
