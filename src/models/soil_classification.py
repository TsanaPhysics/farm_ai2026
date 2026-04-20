import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# 1. โหลดข้อมูลจาก GitHub (Crop Recommendation Dataset)
url = "https://raw.githubusercontent.com/Pratham-gupta-235/ML-and-DL-Projects/main/Crop%20Recomendation%20System/Crop_recommendation.csv"
print(f"--- กำลังโหลดข้อมูลจาก: {url} ---")
df = pd.read_csv(url)

print(f"จำนวนข้อมูล: {len(df)} แถว")

# --- Visualization 1: Heatmap ความสัมพันธ์ของข้อมูล ---
plt.figure(figsize=(10, 6))
sns.heatmap(df.drop('label', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Soil Nutrients')
plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/farm_ai/output/images/crop_rec_heatmap.png')
plt.close()


# 2. เตรียมข้อมูล
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. สร้างและฝึกสอนโมเดล
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. ประเมินผล
y_pred = model.predict(X_test)
print("\n--- ผลการทดสอบ (Accuracy) ---")
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")

# --- Visualization 2: Feature Importance ---
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=True)
plt.figure(figsize=(10, 6))
importances.plot(kind='barh', color='skyblue')
plt.title('Factors Influencing Crop Choice (Feature Importance)')
plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/farm_ai/output/images/crop_rec_feature_importance.png')
plt.close()


# 5. ตัวอย่างการทำนาย
sample = pd.DataFrame([[90, 42, 43, 20.8, 82, 6.5, 202]], columns=X.columns)
prediction = model.predict(sample)
print(f"\nผลการพยากรณ์: พืชที่เหมาะสมคือ '{prediction[0]}'")
