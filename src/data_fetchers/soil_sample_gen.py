import pandas as pd
import numpy as np

# ตั้งค่า Seed เพื่อให้ได้ข้อมูลเดิมทุกครั้งที่รัน (เพื่อการทดสอบ)
np.random.seed(42)

# จำนวนข้อมูลที่ต้องการ
n_samples = 1000

# 1. สร้าง Features (ปัจจัยนำเข้า)
data = {
    'Sample_ID': [f'S_{i+1:04d}' for i in range(n_samples)],
    'pH': np.random.uniform(4.5, 8.5, n_samples).round(2),
    'Moisture_pct': np.random.uniform(10, 50, n_samples).round(2),
    'Soil_Temp_C': np.random.uniform(22, 38, n_samples).round(2),
    'EC_ms_cm': np.random.uniform(0.5, 3.0, n_samples).round(2)
}

# 2. สร้าง Target (ผลลัพธ์) โดยใช้สูตรสมมติที่มีความสัมพันธ์กับ Features
# Nitrogen (N) จะสูงถ้า EC สูง และ Moisture เหมาะสม
data['Nitrogen_N'] = (data['EC_ms_cm'] * 25 + data['Moisture_pct'] * 0.5 + np.random.normal(0, 5, n_samples)).round(2)

# Phosphorus (P) จะสัมพันธ์กับ pH (ช่วง 6-7 จะสูง)
data['Phosphorus_P'] = (20 + (10 - abs(data['pH'] - 6.5) * 5) + np.random.normal(0, 3, n_samples)).round(2)

# Potassium (K) 
data['Potassium_K'] = (data['EC_ms_cm'] * 40 + np.random.normal(0, 10, n_samples)).round(2)

# จัดการค่าที่อาจติดลบให้เป็นค่าต่ำสุด (เช่น 0)
data['Nitrogen_N'] = np.clip(data['Nitrogen_N'], 0, None)
data['Phosphorus_P'] = np.clip(data['Phosphorus_P'], 0, None)
data['Potassium_K'] = np.clip(data['Potassium_K'], 0, None)

# 3. สร้าง DataFrame และบันทึกเป็น CSV
df = pd.DataFrame(data)
file_path = '/Applications/XAMPP/xamppfiles/htdocs/farm_ai/data/raw/soil_data_sample.csv'
df.to_csv(file_path, index=False)


print(f"สร้างไฟล์ข้อมูลจำลองเรียบร้อยแล้วที่: {file_path}")
print(df.head())
