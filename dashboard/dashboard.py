import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
all_df = pd.read_csv('main_data.csv')

# --- Judul Dashboard
st.title("Bike Sharing Analysis Dashboard")

# --- Perbandingan Penyewaan Sepeda antara Hari Kerja dan Hari Libur
st.header("Perbandingan Penyewaan Sepeda antara Hari Kerja dan Hari Libur")

hourly_working_day = all_df.groupby(['hour', 'workingday'])['cnt'].sum().unstack()
fig, ax = plt.subplots(figsize=(10, 6))
hourly_working_day.plot(kind='line', ax=ax, color=['skyblue', 'coral'])
ax.set_title('Total Penyewaan Sepeda Berdasarkan Jam dan Hari Kerja')
ax.set_xlabel('Jam Harian')
ax.set_ylabel('Total Penyewaan Sepeda')
ax.set_xticks(range(24))
ax.legend(title='Hari Kerja', labels=['Ya', 'Tidak'])
ax.grid(True)
st.pyplot(fig)

st.markdown("""
- Pada hari kerja, peminjaman meningkat tajam pada jam 07.00 - 08.00 pagi dan jam 16.00 - 18.00 sore.
- Pada hari libur, jumlah peminjaman lebih tersebar merata sepanjang hari, dengan puncak lebih lambat sekitar pukul jam 12.00 - 15.00 siang.
""")

# --- Korelasi Variabel Cuaca dengan Jumlah Penyewaan Sepeda
st.header("Korelasi Variabel Cuaca dengan Jumlah Penyewaan Sepeda")
weather_vars = ['temp', 'atemp', 'hum', 'windspeed']

for var in weather_vars:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.regplot(x=all_df[var], y=all_df['cnt'], scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
    ax.set_title(f'{var} vs. Penyewaan Sepeda dengan Garis Regresi')
    ax.set_xlabel(var)
    ax.set_ylabel('Penyewaan Sepeda')
    ax.grid(True)
    st.pyplot(fig)

st.markdown("""
- Suhu (temp dan atemp) memiliki korelasi positif kuat dengan jumlah peminjaman.
- Kelembapan (hum) memiliki pengaruh negatif kecil.
- Kecepatan angin (windspeed) menunjukkan korelasi negatif lebih signifikan.
""")

# --- Analisis Lanjutan: Pengaruh Suhu dan Kecepatan Angin pada Kategori Penyewaan
st.header("Analisis Lanjutan: Pengaruh Suhu dan Kecepatan Angin pada Kategori Penyewaan")

bin_edges = [0, 1000, 2000, 3000, 4000, 5000, 10000]
bin_labels = ["Sangat Rendah", "Rendah", "Sedang", "Cukup Tinggi", "Tinggi", "Sangat Tinggi"]
all_df['cnt_bin'] = pd.cut(all_df['cnt'], bins=bin_edges, labels=bin_labels)

# Memfilter data untuk hanya menyertakan baris yang memiliki nilai kosong (NaN) di kolom hour
filtered_df = all_df[all_df['hour'].isna()]

# Melanjutkan analisis menggunakan filtered_df
filtered_df['cnt_bin'] = pd.cut(filtered_df['cnt'], bins=bin_edges, labels=bin_labels)

# Plot Rata-rata Suhu
fig, ax = plt.subplots(figsize=(8, 5))
filtered_df.groupby('cnt_bin')['temp'].mean().plot(kind='bar', color='royalblue', alpha=0.8, ax=ax)
ax.set_xlabel("Kategori Jumlah Penyewaan Sepeda")
ax.set_ylabel("Rata-rata Suhu (Normalisasi)")
ax.set_title("Rata-rata Suhu Berdasarkan Kategori Penyewaan Sepeda")
ax.set_xticklabels(bin_labels, rotation=45)
ax.set_ylim(0, 0.8)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Plot Rata-rata Kecepatan Angin
fig, ax = plt.subplots(figsize=(8, 5))
filtered_df.groupby('cnt_bin')['windspeed'].mean().plot(kind='bar', color='darkorange', alpha=0.8, ax=ax)
ax.set_xlabel("Kategori Jumlah Penyewaan Sepeda")
ax.set_ylabel("Rata-rata Kecepatan Angin")
ax.set_title("Rata-rata Kecepatan Angin Berdasarkan Kategori Penyewaan Sepeda")
ax.set_xticklabels(bin_labels, rotation=45)
ax.set_ylim(0, 0.35)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

st.markdown("""
- Penyewaan sepeda cenderung meningkat saat suhu lebih tinggi.
- Kecepatan angin yang tinggi cenderung menurunkan jumlah penyewaan.
""")

# --- Kesimpulan
st.header("Kesimpulan")
st.markdown("""
- Penyewaan sepeda di hari kerja dipengaruhi oleh mobilitas pekerja dan pelajar, sedangkan pada hari libur banyak penyewaan sepeda sebagai sarana rekreasi.
- Suhu memiliki korelasi positif terhadap penyewaan sepeda, sedangkan kelembapan dan kecepatan angin cenderung berkorelasi negatif.
""")
