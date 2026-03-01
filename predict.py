import joblib
import pandas as pd

model = joblib.load('nids_model.pkl')
def predict_attack(sample):
    sample['protocol_encoded'] = sample['protocol_type'].astype('category').cat.codes
    sample['service_encoded'] = sample['service'].astype('category').cat.codes  
    sample['flag_encoded'] = sample['flag'].astype('category').cat.codes
    features = ['duration', 'src_bytes', 'dst_bytes', 'count', 'srv_count', 'same_srv_rate', 'diff_srv_rate', 'dst_host_count', 'dst_host_srv_count', 'protocol_encoded', 'service_encoded', 'flag_encoded']
    X= sample[features].fillna(0)
    prediction = model.predict(X)
    if prediction[0]==0:
        return "Normal Traffic"
    else:
        return "Attack Detected"