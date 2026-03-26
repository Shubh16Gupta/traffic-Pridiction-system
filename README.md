# 🚦 Smart Urban Traffic Prediction System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

An intelligent machine learning system that predicts urban traffic congestion based on **time, day, and weather conditions**. It helps users make smarter travel decisions by forecasting traffic before they begin their journey.

---

## 📌 Table of Contents
- Features  
- Traffic Categories  
- Prerequisites  
- Installation  
- How to Run  
- Usage  
- Example Output  
- Project Structure  
- Technology Stack  
- How It Works  
- Model Performance  
- Dataset  
- Requirements  
- Future Scope  
- Author  
- License  

---

## 🌟 Features
- 🚗 Traffic prediction (0–100 score)  
- 📊 Traffic level classification (Low / Medium / High)  
- 🔁 What-if analysis  
- ⏰ Peak hour detection  
- 💡 Smart travel recommendations  
- ⚡ Fast predictions using Random Forest  

---

## 🎯 Traffic Categories
| Score | Level | Meaning |
|------|------|--------|
| 0–30 | 🟢 Low | Smooth traffic |
| 30–65 | 🟡 Medium | Moderate traffic |
| 65–100 | 🔴 High | Heavy congestion |

---

## 📋 Prerequisites
```text
Python 3.10 or 3.11
pip
Git
```

---

## ⚙️ Installation
```bash
git clone https://github.com/YOUR_USERNAME/traffic-prediction-system.git
cd traffic-prediction-system

python -m venv venv

# Activate environment
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

---

## 🚀 How to Run
```bash
python src/data_generator.py
python src/train_model.py
python main.py
```

---

## 📖 Usage
```text
1. Predict Traffic
2. What-if Analysis
3. Find Best Time
4. Peak Hours
5. Exit
```

**Predict Traffic**
```text
Input:
- Time (0–23)
- Day (Monday–Sunday)
- Weather (Clear, Rain, Cloudy)

Output:
- Traffic Score
- Traffic Level
- Recommendation
```

**What-if Analysis**
```text
Compare traffic across different times.
```

**Find Best Time**
```text
Suggests least congested time.
```

**Peak Hours**
```text
Displays high traffic time ranges.
```

---

## 📊 Example Output
```text
========================================================
📊 TRAFFIC PREDICTION RESULT
========================================================

Travel Time: 5 PM (17:00)
Day: Friday
Weather: Clear

Traffic Score: 78.3 / 100
Traffic Level: HIGH 🔴

Recommendation:
Avoid traveling between 4 PM – 7 PM

Peak Hours:
16:00 - 19:00

========================================================
```

---

## 🏗️ Project Structure
```text
traffic-prediction-system/
│
├── data/
│   └── traffic_data.csv
│
├── models/
│   └── traffic_model.pkl
│
├── src/
│   ├── data_generator.py
│   ├── train_model.py
│   ├── predict.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔧 Technology Stack
```text
Python
Scikit-learn
Pandas
NumPy
Joblib
```

---

## 🧠 How It Works
```text
1. Generate synthetic dataset
2. Encode features (time, day, weather)
3. Train Random Forest model
4. Take user input
5. Predict traffic score and category
```

---

## 📊 Model Performance
```text
Accuracy: ~99%
MAE: ~2.2
R² Score: ~0.98
Prediction Time: < 0.01 sec
```

---

## 📂 Dataset
```text
Type: Synthetic Dataset

Features:
- Hour
- Day
- Weather
- Traffic Score

Logic:
- Rush hours increase traffic
- Weekends reduce congestion
- Weather impacts traffic
```

---

## 🧪 Requirements
```text
pandas>=2.2
numpy>=1.26
scikit-learn>=1.4
joblib>=1.3
```

---

## 🔮 Future Scope
```text
- Web application (React + Node.js)
- Real-time traffic API
- Weather API integration
- Traffic heatmaps
- Mobile application
- Deep learning models (LSTM)
```

---

## 👨‍💻 Author
```text
Shubh Gupta
GitHub: https://github.com/Shubh16Gupta
```

---

## 📝 License
```text
MIT License
```

---

## 🎤 Viva Line
```text
This system predicts traffic proactively using machine learning, helping users plan travel efficiently.
```

---

## 📌 Status
```text
Completed
Web version planned
```

---

## ❤️
```text
Made with ❤️ for smarter cities 🚗
```
