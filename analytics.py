import pandas as pd

columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent',
           'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'attack_type']
df = pd.read_csv("DATA/KDDTrain+.txt", header=None, names=columns)

print(df.head())
print("Data shape:", df.shape)
# Adding Attack Flag
df['attack_flag'] = df[41].apply(lambda x: 0 if x=='normal' else 1)

print(df[['attack_flag']].head())
print(df['attack_flag'].value_counts())
import matplotlib.pyplot as plt
df['attack_flag'].value_counts().plot(kind='bar')
plt.title("Normal vs Attack Traffic")
plt.show()
attack_percentage = (df['attack_flag'].sum()/len(df))*100
print("Attack Traffic Percentage:", attack_percentage)
#count attacks per protocol
protocol_attack = pd.crosstab(df[1], df['attack_flag'])
print(protocol_attack)
#calculating protocol risk
protocol_attack['risk_score'] = protocol_attack[1]/(protocol_attack[0]+protocol_attack[1])
print(protocol_attack.sort_values(by='risk_score', ascending=False))
#count service attacks
service_attack = pd.crosstab(df[2], df['attack_flag'])
print(service_attack)
#calculating service risk
service_attack['risk_score']= service_attack[1]/(service_attack[0]+service_attack[1])
#finding most targeted services
print(service_attack.sort_values(by='risk_score', ascending=False).head(10))
#counting ports attacked
port_attack = pd.crosstab(df[3],df['attack_flag'])
print(port_attack)
#calculating port risk
port_attack['risk_score']= port_attack[1]/(port_attack[0]+port_attack[1])
#finding most targeted ports
print(port_attack.sort_values(by='risk_score', ascending=False).head(10))
#suspicious high data traffic
suspicious_data= df[(df['attack_flag']==1)&(df[4]>1000)]
print("Suspicious High Data Attacks:",suspicious_data.shape[0])

#detecting silent attacks 
silent_attacks = df[(df['attack_flag']==1)&(df[3]=='S0')]
print("Silent Attack Attempts:", silent_attacks.shape[0])

#detecting protocol-based suspicious activity
icmp_attacks = df[(df['attack_flag']==1)&(df[1]=='icmp')]
print("ICMP Based Attacks:", icmp_attacks.shape[0])

print("\n--- Final Threat Summary ---")
#overall attack level
if attack_percentage > 40:
    print("High Risk Network: Attack traffic is significant")

#Silent scanning detection 
if silent_attacks.shape[0] > 20000:
    print("Possible Scanning Activity Detected")

#Data-heavy attack detection
if suspicious_data.shape[0] > 3000:
    print("High Data Tranfer Attacks Present")

#ICMP reconnaissance detection 
if icmp_attacks.shape[0] > 5000:
    print("ICMP Based Reconnaissance Detected")

#exporting results to csv
df.to_csv("network_attack_data.csv", index=False)
protocol_attack.to_csv("protocol_risk.csv")
service_attack.to_csv("service_risk.csv")

print("CSV files created successfully!")

