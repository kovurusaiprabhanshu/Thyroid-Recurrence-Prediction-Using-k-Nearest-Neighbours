import joblib
import pandas as pd

# Load models
kmeans_model = joblib.load("models/kmeans_model.pkl")
rf_model = joblib.load("models/rf_model.pkl")

# Load scalers
scaler_kmeans = joblib.load("models/scaler_kmeans.pkl")
scaler_rf = joblib.load("models/scaler_rf.pkl")

# Load columns
kmeans_columns = joblib.load("models/columns_kmeans.pkl")
rf_columns = joblib.load("models/columns_rf.pkl")

def predict(input_data: pd.DataFrame):

    # -------------------------
    # STEP 0: Validate input
    # -------------------------
    required_cols = [
        'Age', 'Gender', 'Smoking', 'Hx Smoking', 'Hx Radiothreapy',
        'Thyroid Function', 'Physical Examination', 'Adenopathy',
        'Pathology', 'Focality', 'T', 'N', 'M', 'Stage'
    ]
    
    missing = set(required_cols) - set(input_data.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # -------------------------
    # STEP 1: Encode for KMeans
    # -------------------------
    encoded = pd.get_dummies(input_data)

    kmeans_input = encoded.reindex(columns=kmeans_columns, fill_value=0)
    kmeans_scaled = scaler_kmeans.transform(kmeans_input)

    cluster = kmeans_model.predict(kmeans_scaled)

    # -------------------------
    # STEP 2: Add cluster feature
    # -------------------------
    input_with_cluster = input_data.copy()
    input_with_cluster["Cluster"] = cluster

    # -------------------------
    # STEP 3: Encode for RF
    # -------------------------
    encoded_rf = pd.get_dummies(input_with_cluster)

    rf_input = encoded_rf.reindex(columns=rf_columns, fill_value=0)
    rf_scaled = scaler_rf.transform(rf_input)

    recurrence = rf_model.predict(rf_scaled)
    recurrence_proba = rf_model.predict_proba(rf_scaled)[:, 1]

    # ------------------------
    # STEP 4: Make output readable
    # -------------------------
    cluster_map = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk"
    }

    recurrence_map = {
        0: "No Recurrence",
        1: "High Chance of Recurrence"
    }

    result = input_data.copy()
    result["Predicted_Cluster"] = cluster
    result["Risk_Level"] = [cluster_map.get(c, c) for c in cluster]
    result["Recurrence_Prediction"] = [recurrence_map.get(r, r) for r in recurrence]
    result["Recurrence_Probability"] = recurrence_proba.round(3)

    return result
