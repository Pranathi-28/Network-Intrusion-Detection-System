import pandas as pd
from predict import predict_attack

sample = pd.DataFrame([{
    'duration': 0,
    'protocol_type': 'tcp',
    'service': 'http',
    'flag': 'SF',
    'src_bytes': 181,
    'dst_bytes': 5450,
    'count': 2,
    'srv_count': 2,
    'same_srv_rate': 1.0,
    'diff_srv_rate': 0.0,
    'dst_host_count': 150,
    'dst_host_srv_count': 25 }])
result = predict_attack(sample)
print(result)