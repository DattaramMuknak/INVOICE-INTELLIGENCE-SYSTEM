import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"
SCALER_PATH = "models/scaler.pkl"

def load_model(model_path: str = MODEL_PATH, scaler_path: str = SCALER_PATH):
    """
    Load trained classifier model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    with open(scaler_path, "rb") as f:
        scaler = joblib.load(f)
    return model, scaler


def predict_invoice_flag(input_data):
    """
    Predict invoice flag for new vendor invoices.
    
    Parameters
    ----------
    input_data : dict
    
    Returns
    -------
    pd.DataFrame with predicted flag
    """    
    model,scaler  = load_model()
    input_df = pd.DataFrame(input_data)
    scaled_input = scaler.transform(input_df)
    input_df['Predicted_Flag'] = model.predict(scaled_input).round()
    return input_df

if __name__ == "__main__":
    
    # Example inference run (local testing)
    sample_data = {'invoice_quantity': [50,34773],
                 'invoice_dollars': [352.95, 225706.96],
                 'Freight': [1.73, 1196.25],
                 'total_item_quantity': [162, 34773],
                 'total_item_dollars': [2476, 225706]}
    
    prediction = predict_invoice_flag(sample_data)
    print(prediction)