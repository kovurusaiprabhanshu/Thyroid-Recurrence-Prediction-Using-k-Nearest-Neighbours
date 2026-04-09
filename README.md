# Thyroid Cancer Risk Assessment and Recurrence Prediction

This project implements a multi-stage clinical decision-support system designed to predict thyroid cancer recurrence. By combining unsupervised clustering, optimized neighbor search algorithms, and ensemble learning, the project provides a granular assessment of patient risk.

## 1\. Project Overview

The core objective is to move beyond simple binary classification. This system categorizes patients into risk tiers using **KMeans**, optimizes spatial relationships via **k-Nearest Neighbors (kNN)** variants, and executes final recurrence predictions using a **Random Forest** ensemble. This hybrid approach ensures that clinical predictions are both statistically robust and contextually aware of patient sub-groups.

## 2\. Technical Methodology and Model Architecture

### Hybrid Pipeline Logic

1.  **Stage 1: Risk Stratification (KMeans)**: Patients are clustered into three distinct risk categories (Low, Medium, High) based on clinical similarities.
2.  **Stage 2: Spatial Analysis (kNN)**: The project explores kNN to identify local patterns in patient data, utilizing optimized indexing structures for efficiency.
3.  **Stage 3: Recurrence Prediction (Random Forest)**: The cluster assignment and spatial features are integrated into a Random Forest model to predict the final recurrence outcome and calculate probability scores.

### kNN Search Algorithms

To optimize neighbor search efficiency, the following spatial indexing structures are explored:

  * **KD-Tree Algorithm**: Partitions data space using hyperplanes perpendicular to coordinate axes; highly efficient for lower-dimensional clinical data.
  * **Ball-Tree Algorithm**: Organizes data into nested hyperspheres, providing superior performance in higher-dimensional feature spaces.
  * **Brute Force**: A baseline linear search used to validate the accuracy of the tree-based indexing methods.

## 3\. Techniques Used

  * **Machine Learning Modeling**: Implementation of the Supervised Learning paradigm for classification and Unsupervised Learning for stratification.
  * **Data Visualization**: Transformation of complex clinical datasets into interpretable graphs for feature correlation analysis.
  * **Data Preprocessing**: Advanced filtering, One-Hot Encoding via `get_dummies`, and feature reindexing to ensure model stability during deployment.
  * **Performance Evaluation**: Appraisal of models through multiple statistical benchmarks to ensure clinical reliability.

## 4\. Evaluation Metrics

In medical diagnostics, raw accuracy is insufficient. This project prioritizes a balanced appraisal through:

  * **Accuracy**: The proportion of total correct predictions.
  * **Precision**: Focuses on minimizing False Positives (predicting recurrence when it is not present).
  * **Sensitivity (Recall)**: The most vital metric in cancer detection; focuses on minimizing False Negatives (missing a recurrence).
  * **F1-Score**: The harmonic mean of Precision and Sensitivity, ensuring a balanced performance profile.

## 5\. Project Components

| Component | Feature | Description |
| :--- | :--- | :--- |
| Dataset | `Thyroid_Diff.csv` | Comprehensive clinical dataset sourced from Kaggle. |
| Core Logic | `predict.py` | Handles the hybrid inference (KMeans + Random Forest). |
| Deployment | `app.py` | Streamlit-based user interface for clinical data entry. |
| Models | `.pkl` Files | Serialized models, scalers, and feature column references. |

## 6\. Technologies and Libraries

  * **Python 3**: Primary programming language.
  * **Streamlit**: Web framework for clinical deployment.
  * **Scikit-Learn**: Framework for KMeans, kNN, and Random Forest implementations.
  * **Pandas and Numpy**: Data manipulation and numerical operations.
  * **Joblib**: For model serialization and persistence.

## 7\. Use Cases

  * **Individual Risk Assessment**: Assisting healthcare providers in predicting recurrence likelihood and risk levels for new patients.
  * **Clinical Forecasting Template**: Providing a standardized framework for oncological analytics.
  * **Medical Infrastructure Evaluation**: Generating insights into state-level medical outcomes and treatment effectiveness.

## 8\. Author

**Kovuru Sai Prabhanshu** [GitHub Profile](https://www.google.com/search?q=https://github.com/kovurusaiprabhanshu)
