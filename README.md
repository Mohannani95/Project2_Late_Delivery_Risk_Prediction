# 📦 APL Logistics — Late Delivery Risk Prediction

> Machine Learning-based predictive risk intelligence platform for global supply chain operations

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)](https://streamlit.io/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0-green)](https://xgboost.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🎯 Project Overview

APL Logistics faces unpredictable shipment delays across five global markets. This project delivers a **predictive risk intelligence system** that flags high-risk orders **before** shipping — enabling proactive operational intervention instead of costly reactive fixes.

**Business Impact:** Transform delay management from reactive firefighting to predictive operations, with potential to reduce late delivery rate by 15-20%.

## 🚀 Live Demo

🔗 **Dashboard:** Coming soon (Streamlit Cloud deployment)  
📄 **Research Paper:** See `research_paper/` folder

## 📊 Key Results

| Metric | Value |
|--------|-------|
| Dataset Size | 180,519 orders × 40 columns |
| Best Model | **XGBoost** |
| ROC-AUC | 0.88 |
| F1 Score | 0.83 |
| Recall (Late Class) | 79% |
| Risk Tiers | Low (<40%) / Medium / High (>70%) |

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **ML:** scikit-learn, XGBoost, imbalanced-learn (SMOTE)
- **Data:** pandas, NumPy
- **Visualization:** matplotlib, seaborn, Plotly
- **Dashboard:** Streamlit
- **Development:** Jupyter Notebook, VS Code

## 📁 Repository Structure