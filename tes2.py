import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import plotly.express as px
import joblib

st.title("Dashboard")
st.subheader("Student Dropout Analysis")

# load data
df_1 = pd.read_csv('data.csv', sep=';')
coef = pd.read_csv('coef_df.csv')

# Sidebar menu
st.sidebar.title("📊 Menu Visualisasi")
menu = st.sidebar.radio("Pilih Visualisasi:", [
    "Komposisi Status Mahasiswa",
    "Korelasi terhadap Status",
    "Koefisien Model",
    "Kesimpulan & Rekomendasi",
    "PREDICTOR"
])



# === Tampilan Tengah Berdasarkan Menu ===

if menu == "Komposisi Status Mahasiswa":
    st.subheader("📊 Komposisi Status Mahasiswa")
    data_1 = pd.read_csv('data.csv', sep=";")
        
    status_counts = df_1['Status'].value_counts()
    fig1 = px.pie(names=status_counts.index, values=status_counts.values, title='Komposisi Status Mahasiswa')
    st.plotly_chart(fig1)

    with st.expander("See explanation"):
        st.write('''
        Gambaran umum mengenai proporsi jumlah mahasiswa yang masih belajar, berhasil lulus, dan dropout.
        ''')

elif menu == "Korelasi terhadap Status":
    st.subheader("🎓 Korelasi Fitur Terhadap Status")

    selected_cols_num = [
        'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade',
        'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade',
        'Age_at_enrollment',
    ]

    for col in selected_cols_num:
        fig = px.box(df_1, x="Status", y=col, points="all",
                     title=f"Distribusi {col} terhadap Status")
        st.plotly_chart(fig)

    # Tambahan Countplot 1 & 2 → ganti dengan bar chart
    st.subheader("📊 Unit Tanpa Evaluasi per Semester")
    fig3a = px.histogram(df_1, x='Curricular_units_1st_sem_without_evaluations', color='Status',
                         barmode='group', title="Tanpa Evaluasi Semester 1")
    fig3b = px.histogram(df_1, x='Curricular_units_2nd_sem_without_evaluations', color='Status',
                         barmode='group', title="Tanpa Evaluasi Semester 2")

    st.plotly_chart(fig3a)
    st.plotly_chart(fig3b)

    # Countplot kategori
    st.subheader("📌 Fitur Kategori Terhadap Status")
    selected_cols_cat = ['Scholarship_holder', 'Debtor', 'Gender']

    for col in selected_cols_cat:
        fig = px.histogram(df_1, x=col, color='Status', barmode='group',
                           title=f"{col} terhadap Status")
        st.plotly_chart(fig)


    mode_mapping = {
    1: 'general_phase_contingent',
    17: 'general_phase_contingent',
    39: 'over_23_years',
    44: 'technological_specialization_diploma',
    43: 'change_of_course',
    7: 'holders_of_higher_course',
    99: 'Other'
}
    df_1['Application_mode_mapped'] = df_1['Application_mode'].map(mode_mapping).fillna('Unknown')

    fig = px.histogram(df_1, x='Application_mode_mapped', color='Status', barmode='group',
                   title="Application Mode terhadap Status")
    st.plotly_chart(fig)   

elif menu == "Koefisien Model":
    st.subheader("📦 Fitur Yang Sangat Mempengaruhi Dropout")

    coef_df = pd.DataFrame(coef)

    fig = px.bar(coef_df, x="Feature", y="Coefficient", title="Relasi Koefisien",
                 color="Coefficient", color_continuous_scale="Viridis")
    fig.update_layout(xaxis_title="Fitur", yaxis_title="Koefisien", xaxis_tickangle=-45)

    st.plotly_chart(fig)

    with st.expander("Penjelasan singkat"):
        st.write("""
        • Koefisien positif → menaikkan peluang mahasiswa lulus atau Graduate  
        • Koefisien negatif → menurunkan peluang mahasiswa lulus, artinya cenderung ke Dropout
        """)
elif menu == "Kesimpulan & Rekomendasi":
    st.subheader("📦 kesimpulan dan rekomendasi berdasarkan data")

    with st.expander("strategi"):
        st.markdown("""
        • Fitur dengan Koefisien Positif (menurunkan risiko dropout)    
          Berarti fitur ini mengurangi kemungkinan dropout.  
          Strategi: diperkuat atau ditingkatkan.  
        • Fitur dengan Koefisien Negatif (meningkatkan risiko dropout).  
          Berarti fitur ini meningkatkan kemungkinan dropout. Strategi: dicegah atau ditangani.  
        """)

    
    with st.expander("kesimpulan"):
        st.write("""
    Faktor yang Mengurangi Risiko Dropout (koefisien positif):  
    •	avg_sem_approved (+1.40): Semakin banyak mata kuliah yang disetujui/berhasil dilalui, semakin kecil kemungkinan dropout.  
    •	Tuition_fees_up_to_date_Yes (+1.21): Mahasiswa yang rutin membayar SPP kuliah tepat waktu cenderung tidak dropout.  
    •	Scholarship_holder_Has Scholarship (+0.47): Penerima beasiswa lebih cenderung menyelesaikan kuliah atau graduate.  
    •	avg_sem_grade (+0.41): Nilai rata-rata yang tinggi juga menunjukkan kecenderungan untuk tetap kuliah dan graduate.  
    •	Debtor_No Debt (+0.40): Mahasiswa yang tidak memiliki utang atau mungkin uang kuliah yang berasal dari hutang berkorelasi dengan keberlanjutan studi hingga graduate.  
    •	Gender_Female (+0.09): Mahasiswa perempuan cenderung lebih bertahan dibanding laki-laki.  

    Faktor yang Meningkatkan Risiko Dropout (koefisien negatif)  
    •	Tuition_fees_up_to_date_No (−1.41): Mahasiswa yang tidak membayar SPP kuliah sangat berisiko tinggi dropout.  
    •	Scholarship_holder_No Scholarship (−0.67): Mahasiswa tanpa beasiswa memiliki rasio dropout lebih besar.  
    •	Debtor_Has Debt (−0.60): Mahasiswa yang memiliki utang menunjukkan kecenderungan dropout.  
    •	Application_mode (−0.36): Mode aplikasi tertentu (mungkin jalur tidak reguler) berisiko lebih tinggi dropout.    
    •	Gender_Male (−0.29): Mahasiswa laki-laki lebih cenderung dropout.  
    •	Age_at_enrollment (−0.20): Semakin tua usia masuk, semakin tinggi potensi dropout.  
    •	avg_sem_without_evaluation (−0.14): Banyaknya mata kuliah tanpa evaluasi (mungkin karena tidak hadir atau tidak ikut ujian) menunjukkan risiko dropout.  
        """)

    with st.expander("rekomendasi"):
        st.write("""
        •	Institusi dapat mengambil tidakan seperti adanya program remedial agar mahasiswa dapat memperbaiki nilai, program mentoring akademik yang bentuknya dapat disesuaikan sebagai sarana yang dapat digunakan untuk bisa lebih memahami pelajarannya.
        •	Institusi dapat menawarkan skema cicilan pembayaran, discount bila pelunasan di awal ataupun reminder pada mahasiswa yang telat  melakukan pembayaran.  
        •	Untuk mahasiswa yang sudah mengalami keterlambatan pembayaran institusi dapat  memberikan program bantuan finansial atau renegosiasi pembayaran.
        •	institusi dapat memperluas beasiswa terutama kepada mahasisa yang berisiko tinggi dropout. institusi juga bisa mencari donatur atau perusahaan yang berminat melakukan CSR dengan bantuan kepada mahasiswa yang beresiko.  
        •	Tambahkan kuota beasiswa bagi mahasiswa yang memiliki resiko tinggi atau yang menunjukkan kemajuan akademik.  sehingga lebih banyak mahasiswa yang mendapatkan beasiswa sehingga memperkecil potensi dropout
        •	institusi dapat memberikan seminar belajar efektif, bimbingan belajar , meningkatkan kualitas pengajar dan sarana agar proses belajar mengajar lebih berkualitas sehingga dapat meningkatkan nilai mahasiswa.  
        •	Hutang  berkaitan dengan pembayaran uang kuliah tepat waktu dan beasiswa, mahasiswa berbeasiswa yang bisa menentukan hutang mahasiswa. skema cicilan pembayaran dan perluasan cakupan beasiswa dapat mengurangi tingkat dropout
        •	Sediakan layanan konseling keuangan mencari donatur negeri ataupun swasta.  
        •	Menawarkan kelas kuliah flexible baik pilihan waktu dan kelas pembelajaran online. Membuat forum dengan melibatkan almamater untuk medapatnya informasi mengenai tantangan dan kendala yang dihadapi mahasiswa laki laki dan berusia diatas 23 tahun dalam perkuliahannya sehingga dapat diberikan solusinya.
        •	Application mode. Perluas jalur masuk melalui jalur seleksi umum yang memiliki otensi graduate yang paling besar. Untuk meningkatkan jumlah mahasiswa yang graduate
        """)


elif menu == "PREDICTOR":
    st.subheader("🧠 Prediksi Dropout Mahasiswa")

    # Load pipeline yang sudah kamu simpan
    model_pipeline = joblib.load("model_dropout.joblib")

    # Mapping nama mode pendaftaran ke angka (sesuai data latih)

    mode_mapping= {
        'general_phase_contingent':1,
        'general_phase_contingent':17,
        'over_23_years':39,
        'technological_specialization_diploma':44,
        'change_of_course':43,
        'holders_of_higher_course':7,
        'Other': 99
    }
    # Judul Aplikasi
    st.title("Student Dropout Predictor")

    # Input Fitur
    age = st.number_input("Umur saat mendaftar", min_value=15, max_value=80, value=20)
    application_mode_str = st.selectbox("Jalur Pendaftaran", list(mode_mapping.keys()))
    application_mode = mode_mapping[application_mode_str]
    avg_sem_approved = st.number_input("Rata-rata Unit Disetujui", min_value=0.0, value=5.0)
    avg_sem_grade = st.number_input("Rata-rata Nilai Semester", min_value=0.0, value=12.0)
    avg_sem_without_eval = st.number_input("Rata-rata Unit Tanpa Evaluasi", min_value=0.0, value=0.0)

    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    debtor = st.selectbox("Status Hutang", ["Has Debt", "No Debt"])
    scholarship = st.selectbox("Beasiswa", ["Has Scholarship", "No Scholarship"])
    tuition = st.selectbox("Pembayaran Biaya Tepat Waktu", ["Yes", "No"])

    # Buat DataFrame input
    input_df = pd.DataFrame({
    "Age_at_enrollment": [age],
    "Application_mode": [application_mode],
    "avg_sem_approved": [avg_sem_approved],
    "avg_sem_grade": [avg_sem_grade],
    "avg_sem_without_evaluation": [avg_sem_without_eval],
    "Gender": [gender],
    "Debtor": [debtor],
    "Scholarship_holder": [scholarship],
    "Tuition_fees_up_to_date": [tuition]
    })

    # Tombol Prediksi
    if st.button("Prediksi"):
        prediction = model_pipeline.predict(input_df)[0]
        probability = model_pipeline.predict_proba(input_df)[0]

        st.write("### Hasil Prediksi:")
        st.write(f"*Status:* {prediction}")
        st.write(f"*Probabilitas Dropout:* {round(probability[0]*100, 2)}%")
        st.write(f"*Probabilitas Lulus:* {round(probability[1]*100, 2)}%")
