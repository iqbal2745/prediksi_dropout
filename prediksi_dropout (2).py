
# prediksi_attrition.py
import pandas as pd
import joblib
from imblearn.over_sampling import SMOTE


# 1. Load model
model_pipeline = joblib.load("model_dropout.joblib")

# 2. Data baru untuk prediksi
data_baru = pd.DataFrame([{
    "Tuition_fees_up_to_date": "No",
    "Scholarship_holder": "No Scholarship",
    "Age_at_enrollment": 28,
    "Debtor": "Has Debt",
    "Gender": "Male",
    "Application_mode": 17,
    "avg_sem_approved": 5.0,
    "avg_sem_grade": 10.0,
    "avg_sem_without_evaluation": "1.0"
}])

# 3. Prediksi
hasil = model_pipeline.predict(data_baru)[0]
hasil_str = "Dropout" if hasil == 0 else "Graduate"

# 4. Output
print("Prediksi Dropout:", hasil_str)
