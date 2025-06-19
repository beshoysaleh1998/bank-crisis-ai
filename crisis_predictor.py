
import streamlit as st
import pickle
import numpy as np

# تحميل النموذج المدرب
model = pickle.load(open("crisis_model.pkl", "rb"))

st.title("نظام التنبؤ بالأزمات المالية 💰⚠️")
st.subheader("أدخل البيانات الخاصة بيوم معين:")

clients = st.number_input("عدد العملاء", min_value=1000, step=100)
late_loans = st.number_input("عدد القروض المتأخرة", min_value=0)
usd_rate = st.number_input("سعر الدولار", min_value=0.0, format="%.2f")
complaints = st.number_input("عدد الشكاوى", min_value=0)
abnormal_withdrawals = st.number_input("عدد السحب غير الطبيعي", min_value=0)

if st.button("تنبؤ"):
    input_data = np.array([[clients, late_loans, usd_rate, complaints, abnormal_withdrawals]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ تحذير: هناك احتمال حدوث أزمة مالية!")
    else:
        st.success("✅ الوضع مستقر ولا يوجد خطر في الوقت الحالي.")
