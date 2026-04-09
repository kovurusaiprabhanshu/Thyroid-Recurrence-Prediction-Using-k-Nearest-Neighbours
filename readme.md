# Thyroid Cancer Risk Assessment and Recurrence Prediction

This project is a clinical decision-support tool designed to predict the likelihood of thyroid cancer recurrence. It uses a hybrid machine learning approach, combining unsupervised clustering with supervised classification to provide multi-layered patient risk assessments.

## 1\. Live Demo

[Launch the Streamlit App](https://www.google.com/search?q=https://share.streamlit.io/kovurusaiprabhanshu/thyroid-risk-assesment-and-recurrence-prediction/main/app.py)

## 2\. Model Architecture

This project utilizes a dual-model pipeline:

1.  Stage 1: Risk Stratification (KMeans): Patients are clustered into three risk categories (Low, Medium, High) based on clinical similarities.
2.  Stage 2: Recurrence Prediction (Random Forest): The cluster assignment from Stage 1 is used as a feature, alongside original clinical data, to predict the binary recurrence outcome and calculate a probability score.

## 3\. Installation and Setup

### Prerequisites

  - Python 3.8 or higher
  - Pip (Python package manager)

### Local Execution

1.  Clone the repository:

    ```bash
    git clone https://github.com/kovurusaiprabhanshu/Thyroid-Risk-Assesment-and-Recurrence-Prediction.git
    cd Thyroid-Risk-Assesment-and-Recurrence-Prediction
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the application:

    ```bash
    streamlit run app.py
    ```

## 4\. Project Structure

  - app.py: The Streamlit frontend containing the user interface and input forms.
  - predict.py: The core logic file that handles data validation, encoding, scaling, and model inference.
  - models/: Directory containing serialized .pkl files for models, scalers, and feature column references.

## 5\. Features Analyzed

The model processes 14 clinical parameters, including:

  - Demographics: Age, Gender.
  - Clinical History: Smoking, Hx Radiotherapy.
  - Examinations: Physical Exam results, Adenopathy, Thyroid Function.
  - Pathological Data: Tumor Focality, Pathology type, TNM Staging, and overall Stage.

## 6\. Author

Kovuru Sai Prabhanshu [GitHub Profile](https://www.google.com/search?q=https://github.com/kovurusaiprabhanshu)
