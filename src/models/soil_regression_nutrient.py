import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. โหลดข้อมูลจาก GitHub (Soil Nutrient Predictor Dataset)
url = "https://raw.githubusercontent.com/tej049/soil-nutrient-predictor-app/main/soil_nutrient_dataset%20(1).csv"
print(f"--- กำลังโหลดข้อมูลจาก: {url} ---")
df = pd.read_csv(url)

# --- Visualization: การกระจายตัวของ Nitrogen ---
plt.figure(figsize=(10, 6))
sns.histplot(df['N'], kde=True, color='purple')
plt.title('Distribution of Nitrogen (N) in Dataset')
plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/farm_ai/output/images/nutrient_pred_distribution.png')
plt.close()


# 2. เตรียมข้อมูล
features = ['temperature', 'humidity', 'ph', 'ec', 'organic_carbon']
X = df[features]
y = df['N']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. สร้างและฝึกสอนโมเดล
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. ประเมินผล
y_pred = model.predict(X_test)
print(f"R-squared Score: {r2_score(y_test, y_pred):.4f}")

# --- Visualization: Feature Importance ---
importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=True)
plt.figure(figsize=(10, 6))
importances.plot(kind='barh', color='purple')
plt.title('Environmental Factors affecting Nitrogen')
plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/farm_ai/output/images/nutrient_pred_feature_importance.png')
plt.close()


# 5. ตัวอย่างการพยากรณ์
sample = [[25.5, 60.2, 6.5, 1.2, 0.8]]
prediction = model.predict(sample)
print(f"\nผลการพยากรณ์ปริมาณ Nitrogen: {prediction[0]:.2f} mg/kg")
