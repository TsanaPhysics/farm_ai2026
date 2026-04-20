import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. โหลดข้อมูลจาก GitHub (AgriTech Sample Soil Data)
url = "https://raw.githubusercontent.com/omroy07/AgriTech/main/examples/data/sample_soil_data.csv"
print(f"--- กำลังโหลดข้อมูลจาก: {url} ---")
df = pd.read_csv(url)

# 2. เตรียมข้อมูล (ปรับปรุงชื่อคอลัมน์ให้ตรงกับ Dataset จริง)
features = ['pH', 'EC', 'organic_matter', 'moisture', 'temperature', 'zinc', 'iron', 'manganese', 'copper', 'boron']
X = df[features]
y = df['N'] # เปลี่ยนจาก Nitrogen เป็น N ตามชื่อคอลัมน์ในไฟล์

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. สร้างและฝึกสอนโมเดล
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. ประเมินผล
y_pred = model.predict(X_test)
print(f"R-squared Score: {r2_score(y_test, y_pred):.4f}")

# --- Visualization: Actual vs Predicted ---
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color='green')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual Nitrogen (N)')
plt.ylabel('Predicted Nitrogen (N)')
plt.title('Actual vs Predicted Nitrogen (AgriTech Dataset)')
plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/farm_ai/output/images/agritech_actual_vs_pred.png')
plt.close()

# --- Visualization: Feature Importance ---
importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=True)
plt.figure(figsize=(10, 6))
importances.plot(kind='barh', color='orange')
plt.title('Key Factors Affecting Nitrogen (N) Levels')
plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/farm_ai/output/images/agritech_feature_importance.png')
plt.close()

