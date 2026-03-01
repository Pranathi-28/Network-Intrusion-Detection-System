# 🛡️ Network Intrusion Detection System (NIDS)

## 📌 Project Overview
This project presents a Machine Learning based Network Intrusion Detection System that identifies malicious network traffic by analyzing packet-level features.

It combines Cybersecurity + Data Analytics to classify network activity as normal or attack.

---

## 🎯 Objective
To detect and classify cyber attacks in network traffic using ML models trained on real-world intrusion datasets.

---

## ⚙️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- Machine Learning  
- Data Analytics  
- Cybersecurity  

---

## 🚨 Attack Types Detected
- DoS (Denial of Service)  
- Probe  
- R2L (Remote to Local)  
- U2R (User to Root)  

---

## 🧠 System Architecture
Network Data → Preprocessing → Feature Engineering → ML Model → Prediction → Dashboard

---

## ✨ Features
✔️ ML-based cyber attack detection  
✔️ Automated attack classification  
✔️ Predictive analytics  
✔️ Visualization support  

---

## 📊 Dataset Used
KDD Intrusion Detection Dataset

---

## 🛠️ Project Modules

| File | Description |
|------|-------------|
| preprocess.py | Data preprocessing |
| model.py | Model training |
| predict.py | Attack prediction |
| analytics.py | Data analysis |
| dashboard.py | Visualization |
| nids_model.pkl | Trained model |

---

## 📌 Use Cases
- SOC Teams  
- Network Security Engineers  
- Cybersecurity Researchers  
- IT Administrators  

---

## 🚀 Future Enhancements
- Real-time traffic monitoring  
- Streamlit live dashboard  
- Cloud deployment  

---

## 👩‍💻 Author
Developed by Pranathi  
Focused on Data Analytics & Cybersecurity

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

pip install pandas numpy scikit-learn

---

### Step 2: Run Preprocessing

python preprocess.py

---

### Step 3: Train Model

python model.py

---

### Step 4: Run Prediction

python predict.py

---

### Step 5: Run Dashboard

python dashboard.py

---

## 📊 Sample Output

The system analyzes network traffic and predicts whether the activity is:

✔️ Normal  
❌ Attack

Example Prediction:

Input Network Features → Processed → ML Model → Output:

Prediction: **DoS Attack Detected**

---

## 📈 Model Performance

- Accurate classification of malicious traffic  
- Detects multiple intrusion types  
- Supports automated threat detection
