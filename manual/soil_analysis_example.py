import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1. โหลดข้อมูลจากไฟล์ CSV ที่สร้างขึ้น (Synthetic Data 1,000 แถว)
file_path = '/Applications/XAMPP/xamppfiles/htdocs/farm_ai/manual/soil_data_sample.csv'
df = pd.read_csv(file_path)

# ตัด Sample_ID ออกเนื่องจากไม่ใช่ปัจจัยที่ใช้พยากรณ์
df = df.drop('Sample_ID', axis=1)

print(f"--- โหลดข้อมูลจาก: {file_path} ---")
print(f"จำนวนข้อมูลทั้งหมด: {len(df)} แถว")
print(df.head())

# 2. เตรียมข้อมูล (Features และ Target)
# ในตัวอย่างนี้เราจะพยากรณ์ Nitrogen_N โดยใช้ pH, Moisture, Temp และ EC
X = df[['pH', 'Moisture_pct', 'Soil_Temp_C', 'EC_ms_cm']] 
y = df['Nitrogen_N']


# แบ่งข้อมูลสำหรับ Train 80% และ Test 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. สร้างและฝึกสอนโมเดล Random Forest
# n_estimators คือจำนวนต้นไม้ในป่า AI (ยิ่งเยอะยิ่งละเอียดแต่ใช้เวลานาน)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. ทดสอบและประเมินผล
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n--- ผลการประเมินโมเดล ---")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f} (เข้าใกล้ 1 คือแม่นยำมาก)")

# 5. การพยากรณ์ข้อมูลใหม่ (ตัวอย่าง: มีดินตัวอย่างใหม่ที่วัดค่าได้ดังนี้)
new_soil_sample = pd.DataFrame([[6.2, 27, 28, 1.1]], columns=['pH', 'Moisture_pct', 'Soil_Temp_C', 'EC_ms_cm'])
prediction = model.predict(new_soil_sample)


print(f"\n--- การพยากรณ์ ---")
print(f"ดินที่มีค่า pH 6.2, ความชื้น 27% จะมีปริมาณ Nitrogen ประมาณ: {prediction[0]:.2f} mg/kg")

# 6. แสดงความสำคัญของแต่ละปัจจัย (Feature Importance)
importances = model.feature_importances_
for feature, importance in zip(X.columns, importances):
    print(f"ความสำคัญของ {feature}: {importance:.4f}")
