import streamlit as st
import pandas as pd
from predict import predict_attack

st.title("Network Intrusion Detection System")
st.write ("""This system uses Machine Learning to detect malicious network activity based on connection features from the KDD dataset""")
duration = st.number_input("Duration",0)
protocol_type = st.selectbox("Protocol Type", ['tcp', 'udp', 'icmp'])
service = st.text_input("Service", 'http')
flag = st.text_input("Flag", 'SF')
src_bytes = st.number_input("Source Bytes",0)
dst_bytes = st.number_input("Destination Bytes",0)
count = st.number_input("Connection Count",0)
srv_count = st.number_input("Service Count",0)
same_srv_rate = st.number_input("Same Service Rate",0.0)
diff_srv_rate = st.number_input("Different Service Rate",0.0)
dst_host_count = st.number_input("Destination Host Count",0)
dst_host_srv_count = st.number_input("Destination Host Service Count",0)
if st.button("Detect Attack"):
    sample = pd.DataFrame([{
        'duration': duration,
        'protocol_type': protocol,
        'service': service,
        'flag': flag,
        'src_bytes': src_bytes,
        'dst_bytes': dst_bytes,
        'count': count,
        'srv_count': srv_count,
        'same_srv_rate': same_srv_rate,
        'diff_srv_rate': diff_srv_rate,
        'dst_host_count': dst_host_count,
        'dst_host_srv_count': dst_host_srv_count }])
    result = predict_attack(sample)

    st.subheader("Result:")
    if result == "Attack Detected":
        st.error("Attack Detected!")
    else:
        st.success("Normal Traffic")

st.markdown("---")
st.caption("Built using Machine Learning for Cybersecurity Threat Detection")
  