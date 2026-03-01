from preprocess import load_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

df = load_data()
features = ['duration', 'src_bytes', 'dst_bytes', 'count', 'srv_count', 'same_srv_rate', 'diff_srv_rate', 'dst_host_count', 'dst_host_srv_count', 'protocol_encoded', 'service_encoded', 'flag_encoded']
X= df[features].fillna(0)
y= df['is_attack']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
joblib.dump(model, 'nids_model.pkl')
print("Model saved successfully!")