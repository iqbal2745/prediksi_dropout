#  Analisis Dropout Mahasiswa pada Institusi Pendidikan Edutech
##  Business Understanding
Tingkat dropout mahasiswa merupakan salah satu indikator utama kualitas dan efisiensi institusi pendidikan tinggi. Proyek ini bertujuan untuk menganalisis faktor-faktor utama yang memengaruhi gagalnya mahasiswa menyelesaikan kuliahnya sampai lulus dan berakhir dengan dropout. 
Tingginya tingkat dropout sangat penting ditangani. Hal ini karena merupakan faktor utama berhasil atau tidaknya suatu institusi pendidikan, bila institusi pendidikan gagal menekan tingkat dropout maka institusi pendidikan ini dapat dikatakan gagal dan mengancam keberlangsungan institusi pendidikan ini.
Sehinga institusi dapat memahami penyebab dropout dan mengambil tindakan intervensi intuk mencegah mahasiswa dropout dan meningkatkan tingkat graduate mahasiswa. 

## Permasalahan Bisnis
1.	Apa saja faktor yang dominan yang mendorng mahasiswa dropout 
2.	Apa saja faktor yang mendorong mahasiswa berhasil graduate 
3.	Menemukan pola pola mahasiswa yang dropout ataupun mahasiswa yang graduate

## Cakupan proyek
- Analisis deskriptif untuk memahami karakteristik mahasiswa dropout dan graduate
- Analisis korelasi antar fitur terhadap status mahasiswa 
- Pembangunan model klasifikasi (Logistic Regression)
- Visualisasi hasil (matplotlib, seaborn, plotly.express , streamlit)
- Prediksi menggunakan model tersimpan (`joblib`)
- membuat dashboard berisi visualisasi dan prototipe prediksi 

## Persiapan
Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md
Setup environment:
Membuat virtual environment (rekomendasi)
python -m venv env
source env/bin/activate        # Untuk macOS/Linux
env\Scripts\activate           # Untuk Windows


- Install semua dependensi dari requirements.txt
pip install -r requirements.txt

imbalanced_learn==0.13.0  
joblib==1.5.1  
matplotlib==3.8.4  
numpy==1.26.4  
pandas==2.3.0  
protobuf==6.31.1  
scikit-learn==1.7.0  
seaborn==0.13.2  
plotly==5.22.0  
streamlit==1.34.0  

## Business Dashboard
Dashboard interaktif dibangun menggunakan Streamlit dan terdiri dari dua komponen utama:
1. **Visualisasi Data**
   -  **Komposisi Status Mahasiswa**: Pie chart menunjukkan distribusi mahasiswa yang dropout dan graduate.
   - **Korelasi Fitur terhadap Status**: Boxplot (untuk fitur numerik) dan histogram (untuk fitur kategorikal) menunjukkan pengaruh masing-masing fitur terhadap status mahasiswa.
   -  **Koefisien Model**: Bar chart menggambarkan pengaruh tiap fitur terhadap prediksi model Logistic Regression.

2. **Prediksi Dropout (Model Prototipe)**
   - Mahasiswa dapat diinput berdasarkan fitur-fitur penting, dan sistem akan memprediksi kemungkinan dropout serta graduate beserta probabilitasnya.

## Menjalankan Sistem Machine Learning
Prototipe predictor berada di sidebar bagian kiri yaitu tombol paling bawah, yang bila di klik maka muncul predictor dibagian tengah streamlit.
Bagian input terdiri dari fitur fitur yang digunakan dalam model logistic regression, penyederhanaan fitur untuk hanya mengambil fitur yang memiliki korelesasi terkuat dengan corr() terhadap Status. Kemudian dilakukan feature engineering sederhana dengan membentuk 3 fitur average semester 1 dan semester 2 sehingga dari 6 fitur bisa dikurangi menjadi 3 fitur. 

Input data
1.	Umur saat mendaftar, diisi dengan nilai interger umusur mahasiswa saat mendaftar.
2.	Jalur pendaftaran, dengan memilih jalur pendaftaran yang dilakukan mahasiswa saat mendaftar, tinggal memilih dari pilihan yang sudah ditampilkan.
3.	Rata-rata unit disetujui, yaitu banyaknya sks yang diasetujui, merupakan average jumlah sks semester 1 dan semester 2 yang disetujui, diisi dengan nilai integer.
4.	Rata-rata nilai semester, yaitu nilai avera semester 1 dan semester 2 mahasiswa, diisi nilai integer
5.	Rata-rata unit tanpa evaluasi, yaitu average sks yang tidak dievaluasi semester 1 dan semeter 2, diisi nilai integer
Setelah input data selesai, maka klik tombol prediksi untuk diproses. Hasilnya akan keluar dengan status dan probabilita dropout dan probabilita graduate

##  Conclusion

Model Logistic Regression menghasilkan performa yang baik:

- **Accuracy**: 88%
- **Precision**: 89%
- **Recall**: 91.5%
- **F1 Score**: 90%

Berikut  yang dapat disimpulkan (Kesimpulan Analisis Koefisien)

Koefisien positif = meningkatkan kemungkinan tidak dropout (lulus)
Koefisien negatif = meningkatkan kemungkinan dropout

Faktor yang Mengurangi Risiko Dropout (koefisien positif):
•	avg_sem_approved (+1.40): Semakin banyak mata kuliah yang disetujui/berhasil dilalui, semakin kecil kemungkinan dropout.  
•	Tuition_fees_up_to_date_Yes (+1.21): Mahasiswa yang rutin membayar SPP kuliah tepat waktu cenderung tidak dropout.  
•	Scholarship_holder_Has Scholarship (+0.47): Penerima beasiswa lebih cenderung menyelesaikan kuliah atau graduate.  
•	avg_sem_grade (+0.41): Nilai rata-rata yang tinggi juga menunjukkan kecenderungan untuk tetap kuliah dan graduate.  
•	Debtor_No Debt (+0.40): Mahasiswa yang tidak memiliki utang atau mungkin uang kuliah yang berasal dari hutang berkorelasi dengan keberlanjutan studi hingga graduate.  
•	Gender_Female (+0.09): Mahasiswa perempuan cenderung lebih bertahan dibanding laki-laki.  

Faktor yang Meningkatkan Risiko Dropout (koefisien negatif)  
•	Tuition_fees_up_to_date_No (−1.41): Mahasiswa yang tidak membayar SPP kuliah sangat berisiko tinggi dropout.  
•	Scholarship_holder_No Scholarship (−0.67): Mahasiswa tanpa beasiswa memiliki rasio dropout lebih besar  
•	Debtor_Has Debt (−0.60): Mahasiswa yang memiliki utang menunjukkan kecenderungan dropout.  
•	Application_mode (−0.36): Mode aplikasi tertentu (mungkin jalur tidak reguler) berisiko lebih tinggi dropout.     
•	Gender_Male (−0.29): Mahasiswa laki-laki lebih cenderung dropout.  
•	Age_at_enrollment (−0.20): Semakin tua usia masuk, semakin tinggi potensi dropout.  
•	avg_sem_without_evaluation (−0.14): Banyaknya mata kuliah tanpa evaluasi (mungkin karena tidak hadir atau tidak ikut ujian) menunjukkan risiko dropout.  

## rekomendasi action times
Akademik & Evaluasi  
•	Intervensi akademik untuk mahasiswa dengan jumlah mata kuliah gagal/ditinggalkan tinggi (avg_sem_approved & avg_sem_without_evaluation).  
•	Program bimbingan belajar atau remedial untuk mereka yang memiliki nilai rata-rata rendah  
Keuangan  
•	Monitor mahasiswa yang menunggak pembayaran (Tuition_fees_up_to_date_No) agar bisa ditindaklanjuti .  
•	Perluas akses beasiswa untuk mahasiswa dari latar belakang ekonomi rentan (Scholarship_holder_No Scholarship). Dengan bekerja sama dengan donatur atau CSR perusahaan atau pemerintah untuk membiayai mahasiswa yang memiliki kendala financial  
•	Program restrukturisasi atau penjadwalan utang mahasiswa bagi yang terdeteksi sebagai Debtor_Has Debt.  

