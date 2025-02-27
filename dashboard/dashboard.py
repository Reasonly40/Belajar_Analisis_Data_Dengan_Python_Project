import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Data
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"File 'main_data.csv' tidak ditemukan di direktori: {file_path}")
        return None

# Memanggil fungsi load_data
all_df = load_data()

# --- Judul Dashboard
st.title("Bike Sharing Analysis Dashboard")

# Perbaikan fungsi create_hour_order_df
def create_hour_order_df(df):
    day_order_df = df.resample(rule='D', on='hour').agg({
        "instant": "nunique",
        "cnt": "sum"
    })
    day_order_df = day_order_df.reset_index()
    day_order_df.rename(columns={
        "instant": "order_count",
        "cnt": "revenue"
    }, inplace=True)
    
    return day_order_df

# Konversi kolom datetime
datetime_columns = ["dateDay"]
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# Pastikan dateDay dalam format datetime
all_df['dateDay'] = pd.to_datetime(all_df['dateDay'])

# Ambil rentang tanggal dari data
minDate = all_df['dateDay'].min().date()  # Konversi ke datetime.date
maxDate = all_df['dateDay'].max().date()

# Sidebar untuk memilih rentang tanggal
with st.sidebar:
    startDate, endDate = st.date_input(
        label='Jangka Waktu',
        min_value=minDate,
        max_value=maxDate,
        value=[minDate, maxDate]
    )

    # Pastikan pemfilteran bekerja dengan baik
    main_df = all_df[
        (all_df['dateDay'].dt.date >= startDate) & 
        (all_df['dateDay'].dt.date <= endDate)
    ]

# --- Perbandingan Penyewaan Sepeda antara Hari Kerja dan Hari Libur
st.header("Perbandingan Penyewaan Sepeda antara Hari Kerja dan Hari Libur")

# Menghitung total penyewaan berdasarkan jam dan hari kerja
hourly_working_day = main_df.groupby(['hour', 'workingday'])['cnt'].sum().unstack()

# Menghitung nilai minimum dan maksimum untuk masing-masing kategori (Hari Kerja & Hari Libur)
min_working = hourly_working_day[1].min() if 1 in hourly_working_day.columns else 0
max_working = hourly_working_day[1].max() if 1 in hourly_working_day.columns else 0
min_non_working = hourly_working_day[0].min() if 0 in hourly_working_day.columns else 0
max_non_working = hourly_working_day[0].max() if 0 in hourly_working_day.columns else 0

# Menentukan jam saat nilai minimum dan maksimum terjadi
hour_min_working = hourly_working_day[hourly_working_day[1] == min_working].index[0] if 1 in hourly_working_day.columns else None
hour_max_working = hourly_working_day[hourly_working_day[1] == max_working].index[0] if 1 in hourly_working_day.columns else None
hour_min_non_working = hourly_working_day[hourly_working_day[0] == min_non_working].index[0] if 0 in hourly_working_day.columns else None
hour_max_non_working = hourly_working_day[hourly_working_day[0] == max_non_working].index[0] if 0 in hourly_working_day.columns else None

# Menampilkan metrics
st.subheader("Statistik Penyewaan Sepeda")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Min Penyewaan (Hari Kerja)", value=min_working)
    st.metric(label="Jam Min Penyewaan (Hari Kerja)", value=hour_min_working)
    st.metric(label="Max Penyewaan (Hari Kerja)", value=max_working)
    st.metric(label="Jam Max Penyewaan (Hari Kerja)", value=hour_max_working)

with col2:
    st.metric(label="Min Penyewaan (Hari Libur)", value=min_non_working)
    st.metric(label="Jam Min Penyewaan (Hari Libur)", value=hour_min_non_working)
    st.metric(label="Max Penyewaan (Hari Libur)", value=max_non_working)
    st.metric(label="Jam Max Penyewaan (Hari Libur)", value=hour_max_non_working)
    
# Membuat visualisasi perbandingan jumlah penyewaan sepeda antara hari kerja dan hari libur
fig, ax = plt.subplots(figsize=(10, 6))
hourly_working_day.plot(kind='line', ax=ax, color=['skyblue', 'coral'])
ax.set_title('Total Penyewaan Sepeda Berdasarkan Jam dan Hari Kerja')
ax.set_xlabel('Jam Harian')
ax.set_ylabel('Total Penyewaan Sepeda')
ax.set_xticks(range(24))
ax.legend(title='Hari Kerja', labels=['Tidak (Libur)', 'Ya (Hari Kerja)'])
ax.grid(True)
st.pyplot(fig)

# --- Mengelompokkan Data ---  
if "season" in main_df.columns:  
    # Agregasi jumlah penyewaan berdasarkan musim  
    seasonal_data = main_df.groupby("season")["cnt"].sum()  

    # Nama musim 
    season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Salju"}  

    # Menampilkan Metrics
    st.subheader("Statistik Penyewaan Sepeda Berdasarkan Musim")  

    col1, col2 = st.columns(2)  

    with col1:  
        st.metric(label="Musim dengan Penyewaan Min",  
                  value=f"{season_labels[seasonal_data.idxmin()]} ({seasonal_data.min():,})")  

    with col2:  
        st.metric(label="Musim dengan Penyewaan Max",  
                  value=f"{season_labels[seasonal_data.idxmax()]} ({seasonal_data.max():,})")  

    # --- Visualisasi Data ---  
    st.subheader("Tren Penyewaan Sepeda Per Musim")  

    fig, ax = plt.subplots(figsize=(8, 6))  

    sns.barplot(x=[season_labels[i] for i in seasonal_data.index], y=seasonal_data.values, ax=ax, palette="Oranges")  
    ax.set_title("Total Penyewaan Sepeda Per Musim")  
    ax.set_xlabel("Musim")  
    ax.set_ylabel("Total Penyewaan")  
    ax.grid(axis='y', linestyle='--', alpha=0.7)  

    # Menampilkan visualisasi
    st.pyplot(fig)  
else:  
    st.error("Kolom 'season' tidak ditemukan dalam dataset.")  

# --- Korelasi Variabel Cuaca dengan Jumlah Penyewaan Sepeda
st.header("Korelasi Variabel Cuaca dengan Jumlah Penyewaan Sepeda")

filtered_df = main_df[main_df["hour"].isna()]

weather_vars = ['temp', 'atemp', 'hum', 'windspeed']

# Menghitung korelasi dan menampilkannya sebagai metrics di Streamlit
st.subheader("Nilai Korelasi")
col1, col2, col3, col4 = st.columns(4)

for i, var in enumerate(weather_vars):
    if var in filtered_df.columns and "cnt" in filtered_df.columns:
        correlation = filtered_df[[var, 'cnt']].corr().iloc[0, 1]  # Mengambil nilai korelasi
        with [col1, col2, col3, col4][i]:  # Menyesuaikan dengan kolom yang ada
            st.metric(label=f"Korelasi {var}", value=round(correlation, 3))

# Visualisasi hubungan dengan scatter plot dan regresi
for var in weather_vars:
    if var in filtered_df.columns and "cnt" in filtered_df.columns:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.regplot(x=filtered_df[var], y=filtered_df['cnt'], scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
        ax.set_title(f'{var} vs. Penyewaan Sepeda dengan Garis Regresi')
        ax.set_xlabel(var)
        ax.set_ylabel('Penyewaan Sepeda')
        ax.grid(True)
        st.pyplot(fig)

# --- Pengaruh Suhu dan Kecepatan Angin pada Kategori Penyewaan
st.header("Analisis Lanjutan: Pengaruh Suhu dan Kecepatan Angin pada Kategori Penyewaan")

# Menyaring hanya data yang TIDAK memiliki nilai pada kolom 'hour'
filtered_df = main_df[main_df["hour"].isna()]

if "cnt" in filtered_df.columns:
    bin_edges = [0, 1000, 2000, 3000, 4000, 5000, 10000]
    bin_labels = ["Sangat Rendah", "Rendah", "Sedang", "Cukup Tinggi", "Tinggi", "Sangat Tinggi"]
    filtered_df['cnt_bin'] = pd.cut(filtered_df['cnt'], bins=bin_edges, labels=bin_labels)

    if "temp" in filtered_df.columns and "cnt_bin" in filtered_df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        filtered_df.groupby('cnt_bin')['temp'].mean().plot(kind='bar', color='royalblue', alpha=0.8, ax=ax)
        ax.set_xlabel("Kategori Jumlah Penyewaan Sepeda")
        ax.set_ylabel("Rata-rata Suhu (Normalisasi)")
        ax.set_title("Rata-rata Suhu Berdasarkan Kategori Penyewaan Sepeda")
        ax.set_xticklabels(bin_labels, rotation=45)
        ax.set_ylim(0, 0.8)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    if "windspeed" in filtered_df.columns and "cnt_bin" in filtered_df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        filtered_df.groupby('cnt_bin')['windspeed'].mean().plot(kind='bar', color='darkorange', alpha=0.8, ax=ax)
        ax.set_xlabel("Kategori Jumlah Penyewaan Sepeda")
        ax.set_ylabel("Rata-rata Kecepatan Angin")
        ax.set_title("Rata-rata Kecepatan Angin Berdasarkan Kategori Penyewaan Sepeda")
        ax.set_xticklabels(bin_labels, rotation=45)
        ax.set_ylim(0, 0.35)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)
