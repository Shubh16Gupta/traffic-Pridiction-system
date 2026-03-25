# 🚦 Smart Urban Traffic Prediction System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

An intelligent machine learning system that predicts urban traffic congestion based on **time, day, and weather conditions**. This project uses Machine Learning to help users make smarter travel decisions by forecasting traffic before they travel.

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
- Future Scope  
- Author  
- License  

---

## 🌟 Features

- 🚗 Traffic prediction (0–100 score)  
- 📊 Traffic level classification (Low / Medium / High)  
- 🔁 What-if analysis (compare different times)  
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

- Python **3.10 or 3.11 recommended**
- pip installed
- Git

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

## 🚀 How to Run
- Step 1: Generate dataset → `python src/data_generator.py`
- Step 2: Train model → `python src/train_model.py`
- Step 3: Run app → `python main.py`

---

## 📖 Usage
When you run the program:
1. Predict Traffic  
2. What-if Analysis  
3. Find Best Time  
4. Peak Hours  
5. Exit  

**Predict Traffic:** Enter time (0–23), day, and weather 
**What-if Analysis:** Compare different travel times  
**Find Best Time:** Get least congested time  
**Peak Hours:** View high traffic periods  

---

## 📊 Example Output
========================================================  
📊 TRAFFIC PREDICTION RESULT  
========================================================  
Travel Time: 5 PM (17:00)  
Day: Friday  
Weather: Clear  

Traffic Score: 78.3 / 100  
Traffic Level: HIGH 🔴  

Recommendation: Avoid traveling between 4 PM – 7 PM  
Peak Hours: 16:00 - 19:00  
========================================================  

---

## 🏗️ Project Structure
traffic-prediction-system/  
│  
├── data/  
├── models/  
├── src/  
├── main.py  
├── requirements.txt  
└── README.md  

---

## 🔧 Technology Stack
Python, Scikit-learn, Pandas, NumPy, Joblib  

---

## 🧠 How It Works
Synthetic data → Feature encoding → Train Random Forest → Predict traffic  

---

## 📊 Model Performance
Accuracy ~99% | MAE ~2.2 | R² ~0.98 | Fast prediction  

---

## 🧪 Requirements
pandas>=2.2  
numpy>=1.26  
scikit-learn>=1.4  
joblib>=1.3  

---

## 🔮 Future Scope
Web app, Live APIs, Heatmaps, Mobile app  

---

## 👨‍💻 Author
Shubh Gupta  
GitHub: https://github.com/YOUR_USERNAME  

---

## 🎤 Viva Line
“This system predicts traffic proactively using machine learning.”  

---

## 📌 Status
Completed  

---

Made with ❤️ 🚗