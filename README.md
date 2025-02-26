# 🚴‍♂️ Bike Sharing Analytical Data Project

## 🚀 Panduan Menjalankan Streamlit Dashboard  
Dokumen ini berisi langkah-langkah untuk menginstal dependensi dan menjalankan **Streamlit Dashboard** untuk menganalisis data penyewaan sepeda.  

---

## 📌 1. Instalasi Dependensi  

### **a. Pastikan Python dan pip Sudah Terinstal**  
Jika belum, silakan unduh dan instal **Python** dari [python.org](https://www.python.org/).  
**pip** (package manager Python) biasanya sudah termasuk dalam instalasi Python. Untuk memeriksa, jalankan:  

`
python --version
`

`
pip --version
`

Jika pip belum terinstal, Anda dapat menginstalnya dengan perintah berikut:

`
python -m ensurepip --default-pip
`

### b. Buat Virtual Environment (Opsional, tetapi Direkomendasikan)
Untuk menghindari konflik dependensi, gunakan virtual environment dengan perintah:

`
python -m venv venv  # Membuat virtual environment bernama 'venv'
`

Aktifkan virtual environment:

Windows (PowerShell):

`
Set-ExecutionPolicy Unrestricted -Scope Process
`

`
.\venv\Scripts\activate
`

Mac/Linux:

`
source venv/bin/activate
`

### c. Instalasi Paket yang Dibutuhkan
Jalankan perintah berikut untuk menginstal Streamlit dan pustaka lainnya:

`
pip install streamlit pandas matplotlib seaborn
`

Simpan daftar paket ke dalam file requirements.txt untuk memudahkan instalasi ulang:

`
pip freeze > requirements.txt
`

Jika ingin menginstal ulang semua dependensi di masa depan, cukup jalankan:

`
pip install -r requirements.txt
`

## 📌 2. Menjalankan Streamlit Dashboard
Pastikan Anda berada di direktori proyek (misalnya, dashboard/), lalu jalankan:

`
cd dashboard  # Masuk ke folder dashboard
`

`
streamlit run dashboard.py  # Menjalankan dashboard
`

Jika berhasil, terminal akan menampilkan pesan seperti berikut:

`
You can now view your Streamlit app in your browser.
`

`
Local URL: http://localhost:8501
`

Buka http://localhost:8501 di browser untuk melihat dashboard.

## 📌 3. Mengunggah Dataset
Dashboard yang dijalankan secara lokal tidak perlu mengunggah dataset, tetapi jika dashboard dibuka melalui Streamlit Cloud, Anda perlu mengunggah dataset.

Klik tombol Upload Dataset di halaman dashboard.
Pilih file CSV yang akan dianalisis.
Data akan diproses dan divisualisasikan dalam bentuk grafik.
## 📌 4. Troubleshooting
Jika mengalami error, berikut beberapa solusi umum:

🔹 Error: Modul Tidak Ditemukan
Jalankan kembali perintah berikut:

`
pip install -r requirements.txt
`

🔹 Error: Port 8501 Sudah Digunakan
Gunakan port lain dengan perintah:

`
streamlit run dashboard.py --server.port 8502
`

🔹 Error: Virtual Environment Tidak Aktif
Pastikan sudah mengaktifkan virtual environment sebelum menjalankan Streamlit:

`
.\venv\Scripts\activate  # Windows (PowerShell)
`

`
source venv/bin/activate  # Mac/Linux
`
🔹 Nama Dataset Tidak Sesuai
Pastikan file CSV yang digunakan bernama main_data.csv.
