# 🌧️ Rainfall Prediction using Machine Learning

This project predicts whether it will rain based on daily weather conditions using a Random Forest Classifier.

## 📊 Dataset

- **Total records**: 366  
- **Target column**: `rainfall` (`yes` → 1, `no` → 0)  
- **Features used**:  
  `pressure`, `dewpoint`, `humidity`, `cloud`, `sunshine`, `winddirection`, `windspeed`

## 🧼 Data Preprocessing

- Removed column name spaces  
- Handled missing values (`winddirection`, `windspeed`)  
- Dropped highly correlated temperature columns  
- Balanced the dataset using **downsampling**

## 🤖 Model Info

- **Model**: Random Forest Classifier  
- **Hyperparameter Tuning**: GridSearchCV (5-fold CV)  
- **Best Parameters**:  
  `n_estimators=50`, `max_features='sqrt'`, `min_samples_split=10`, `min_samples_leaf=1`, `max_depth=None`  
- **Test Accuracy**: ~74.5%  
- **Cross-Val Score**: ~81.9%

## 🚀 Deployment (Flask + Render)

- Web app built using **Flask**
- Trained model saved as `rainfall_prediction_model.pkl` using `pickle`
- Hosted live on **Render**

### 🔗 Live App URL
```
https://rainfall-prediction-system-bzs9.onrender.com
