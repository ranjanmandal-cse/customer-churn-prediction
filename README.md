# 📡 Customer Churn Prediction — End-to-End ML Project

## Project Structure

```
churn_project/
├── CustomerChurn_Complete.ipynb   ← Full notebook (with markdown explanations)
├── app.py                          ← Streamlit app
├── Telco-Customer-Churn.csv       ← Dataset
├── models/
│   ├── best_churn_model.pkl       ← Tuned XGBoost (best model)
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── feature_info.json
└── plots/
    ├── 01_churn_distribution.png
    ├── 02_churn_by_contract.png
    ├── 03_correlation_heatmap.png
    ├── 04_distributions.png
    ├── 05_churn_by_tenure_group.png
    ├── 06_churn_by_addons.png
    ├── 07_roc_curves.png
    ├── 08_feature_importance.png
    ├── 09_model_comparison.png
    └── 10_confusion_matrix.png
```

---

## How to Run

### 1. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost streamlit plotly joblib imbalanced-learn
```

### 2. Run the Notebook
Open `CustomerChurn_Complete.ipynb` in Jupyter and run all cells.

### 3. Launch the Streamlit App
```bash
streamlit run app.py
```
The app will open at **http://localhost:8501**

---

## Model Results

| Model | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---|---|---|---|---|
| Logistic Regression | 0.739 | 0.505 | 0.791 | 0.617 | **0.847** |
| Random Forest | 0.787 | 0.631 | 0.476 | 0.543 | 0.826 |
| XGBoost (default) | 0.759 | 0.536 | 0.685 | 0.601 | 0.820 |
| **XGBoost (tuned)** | 0.740 | 0.507 | **0.810** | **0.624** | **0.847** |

> **Best Model:** Tuned XGBoost — highest Recall (catches 81% of churners) and tied best ROC-AUC (0.847)

---

## Key Findings from EDA

1. **Contract type** is the #1 churn driver — Month-to-month customers churn at ~43% vs 3% for 2-year contracts
2. **Tenure** matters — Customers in first 12 months churn at 48%, dropping to <10% after 4 years
3. **Add-on services** reduce churn — Customers with 4+ services churn at <15%
4. **Fiber optic** customers churn more despite paying more (service quality signal)
5. **Electronic check** payment method is associated with higher churn

---

## Skills Demonstrated
- Python, Pandas, NumPy
- Matplotlib, Seaborn (EDA & visualization)
- Scikit-learn (preprocessing pipelines, model training, evaluation)
- XGBoost (gradient boosting, hyperparameter tuning)
- Class imbalance handling (`class_weight`, `scale_pos_weight`)
- Streamlit (interactive web app)
- Plotly (interactive charts)
- joblib (model serialization)
