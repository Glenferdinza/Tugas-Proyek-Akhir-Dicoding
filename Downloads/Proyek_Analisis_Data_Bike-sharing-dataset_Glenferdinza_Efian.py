import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Header: Proyek Analisis Data: Bike Sharing Dataset
st.header("Proyek Analisis Data: Bike Sharing Dataset")

st.write("""
Nama: Glenferdinza Aghis Asyadda Rayndika Efian  
Email: glenferdinza21@gmail.com  
ID Dicoding: glenferdinza_efian
""")

# Header: Menentukan Pertanyaan Bisnis
st.header("Menentukan Pertanyaan Bisnis")

st.write("""
1. Bagaimana pengaruh faktor lingkungan dan cuaca (seperti suhu, kelembapan, dan kondisi cuaca) terhadap jumlah penyewaan sepeda harian atau jam-jam tertentu?  
2. Apakah terdapat pola anomali dalam jumlah penyewaan sepeda yang dapat dikaitkan dengan kejadian besar atau kondisi khusus, seperti bencana atau hari libur nasional?  
""")

# Header: Import Semua Packages/Library yang Digunakan
st.header("Import Semua Packages/Library yang Digunakan")
st.write("""
- import streamlit as st
- import pandas as pd
- import numpy as np
- import seaborn as sns
- import matplotlib.pyplot as plt
""")

# Header: Data Wrangling
st.header("Data Wrangling")

# Insight Data Wrangling
st.write("""Data wrangling adalah proses mempersiapkan data untuk analisis. 
Disini nanti aku akan memuat data lalu memeriksa informasi datanya, dan melakukan perubahan tipe data jika diperlukan.""")

# Load data
day_df = pd.read_csv("C:/Users/Lenovo/OneDrive/ドキュメント/Bike/day/day.csv")
hour_df = pd.read_csv("C:/Users/Lenovo/OneDrive/ドキュメント/Bike/hour/hour.csv")

# Informasi Data
st.write("Informasi singkat dari Data Day:")
st.write(day_df.head())
st.write("Informasi singkat dari Data Hour:")
st.write(hour_df.head())

# Missing values
st.write("Jumlah Missing Values di Data Day:")
st.write(day_df.isnull().sum())
st.write("Jumlah Missing Values di Data Hour:")
st.write(hour_df.isnull().sum())

# Mengubah tipe data kolom tanggal
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Cek kategori cuaca
st.write("Kategori cuaca yang ada dalam data:")
st.write(day_df['weathersit'].unique())

if 4 not in day_df['weathersit'].unique():
    st.write("Kategori 4 (badai) tidak ada dalam data.")
else:
    st.write("Kategori 4 (badai) ada dalam data.")

# Header: Exploratory Data Analysis (EDA)
st.header("Exploratory Data Analysis (EDA)")
st.write("Pada tahap ini, aku akan melakukan analisis deskriptif dan visualisasi data untuk memahami pola dan hubungan antara variabel, langsung aja sebagai berikut:")

# Statistik deskriptif
st.write("Statistik Deskriptif Data Day:")
st.write(day_df.describe())
st.write("Statistik Deskriptif Data Hour:")
st.write(hour_df.describe())

# Korelasi variabel numerik di Data Day
correlation = day_df[['temp', 'hum', 'cnt']].corr()
st.write("Korelasi Variabel Numerik (Harian):")
st.write(correlation)

# Deteksi anomali dengan Z-Score di Data Hour
mean_cnt = np.mean(hour_df['cnt'])
std_cnt = np.std(hour_df['cnt'])
hour_df['z_score'] = (hour_df['cnt'] - mean_cnt) / std_cnt

st.write("Z-Score untuk Deteksi Anomali (Beberapa Data Awal):")
st.write(hour_df[['cnt', 'z_score']].head())

st.write("Ditahap ini, aku akan melakukan visualisasi data untuk memahami pola dan hubungan antara variabel yaitu sebagai berikut:")

# Visualisasi hubungan suhu dengan jumlah penyewaan sepeda
st.subheader("Hubungan Suhu dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_df, color='blue', ax=ax)
ax.set_title('Hubungan Suhu dengan Jumlah Penyewaan Sepeda')
ax.set_xlabel('Suhu (Celsius)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
st.write("Scatter plot menunjukkan adanya tren positif, di mana semakin tinggi suhu, jumlah penyewaan sepeda cenderung meningkat. Hal ini mengindikasikan suhu hangat mendorong aktivitas luar ruangan seperti bersepeda.")

# Visualisasi hubungan kelembapan dengan jumlah penyewaan sepeda
st.subheader("Hubungan Kelembapan dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='hum', y='cnt', data=day_df, color='green', ax=ax)
ax.set_title('Hubungan Kelembapan dengan Jumlah Penyewaan Sepeda')
ax.set_xlabel('Kelembapan (%)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
st.write("Scatter plot memperlihatkan tren negatif, menunjukkan bahwa kelembapan tinggi cenderung menurunkan minat untuk menyewa sepeda, mungkin karena kondisi yang kurang nyaman.")

# Visualisasi hubungan kondisi cuaca dengan jumlah penyewaan sepeda
st.subheader("Hubungan Kondisi Cuaca dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=day_df, palette='viridis', ax=ax)
ax.set_title('Hubungan Kondisi Cuaca dengan Jumlah Penyewaan Sepeda')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
st.write("Bar plot menunjukkan bahwa kondisi cuaca yang baik (kategori 1) memiliki jumlah penyewaan tertinggi, sementara kondisi yang lebih buruk (kategori 3) menyebabkan penurunan signifikan.")

# Visualisasi pola jumlah penyewaan sepeda per hari
st.subheader("Pola Jumlah Penyewaan Sepeda per Hari")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=hour_df['dteday'].dt.day, y='cnt', data=hour_df, color='purple', ax=ax)
ax.set_title('Pola Jumlah Penyewaan Sepeda per Hari')
ax.set_xlabel('Hari')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
st.write("Line plot menunjukkan fluktuasi jumlah penyewaan per hari. Puncak pada hari-hari tertentu bisa berkaitan dengan akhir pekan atau acara khusus.")

# Visualisasi pola jumlah penyewaan sepeda per jam
st.subheader("Pola Jumlah Penyewaan Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hour_df, color='orange', ax=ax)
ax.set_title('Pola Jumlah Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
st.write("Plot menunjukkan pola waktu puncak di pagi dan sore hari, menunjukkan penggunaan sepeda yang signifikan untuk perjalanan kerja atau sekolah.")

# Visualisasi deteksi anomali (Z-Score) per jam
st.subheader("Deteksi Anomali Jumlah Penyewaan Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='z_score', data=hour_df, color='red', ax=ax)
ax.set_title('Deteksi Anomali Jumlah Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Z-Score')
ax.axhline(y=3, color='black', linestyle='--', label='Threshold (3)')
ax.axhline(y=-3, color='black', linestyle='--')
ax.legend()
st.pyplot(fig)
st.write("Plot Z-Score menunjukkan adanya jam-jam tertentu dengan anomali ekstrem, seperti lonjakan besar yang mungkin disebabkan oleh event mendadak atau perubahan cuaca.")

# Visualisasi deteksi anomali (Z-Score) per hari
st.subheader("Deteksi Anomali Jumlah Penyewaan Sepeda per Hari")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=hour_df['dteday'].dt.day, y='z_score', data=hour_df, color='red', ax=ax)
ax.set_title('Deteksi Anomali Jumlah Penyewaan Sepeda per Hari')
ax.set_xlabel('Hari')
ax.set_ylabel('Z-Score')
ax.axhline(y=3, color='black', linestyle='--', label='Threshold (3)')
ax.axhline(y=-3, color='black', linestyle='--')
ax.legend()
st.pyplot(fig)
st.write("Anomali pada hari tertentu terlihat melalui nilai Z-Score tinggi atau rendah, yang memerlukan investigasi lebih lanjut untuk mengetahui penyebab seperti kondisi cuaca atau hari libur.")

# Header: Analisis Lanjutan (Opsional)
st.header("Analisis Lanjutan (Opsional)")
st.write("- None")

# Header: Conclusion
st.header("Conclusion")

# Insight Conclusion
st.write("Dari analisis yang telah dilakukan, dapat disimpulkan bahwa:")
st.write("1. Pengaruh faktor lingkungan dan cuaca (seperti suhu, kelembapan, dan kondisi cuaca) terhadap jumlah penyewaan sepeda harian atau jam-jam tertentu adalah signifikan.")
st.write("2. Terdapat pola anomali dalam jumlah penyewaan sepeda yang dapat dikaitkan dengan ke jadian besar atau kondisi khusus, seperti bencana atau hari libur nasional, namun tetap memerlukan investigasi lebih lanjut lagi mengenai penyebab-Nya")