🚴‍♂️ Bike Sharing Analytical Data Project
🚀 Panduan Menjalankan Streamlit Dashboard
Dokumen ini berisi langkah-langkah untuk menginstal dependensi dan menjalankan Streamlit Dashboard untuk menganalisis data penyewaan sepeda.

📌 1. Instalasi Dependensi
a. Pastikan Python dan pip Sudah Terinstal
Jika belum, silakan unduh dan instal Python dari python.org.
pip (package manager Python) biasanya sudah termasuk dalam instalasi Python. Untuk memeriksa, jalankan:

bash
Copy
Edit
python --version
pip --version
Jika pip belum terinstal, Anda dapat menginstalnya dengan perintah berikut:

bash
Copy
Edit
python -m ensurepip --default-pip
b. Buat Virtual Environment (Opsional, tetapi Direkomendasikan)
Untuk menghindari konflik dependensi, gunakan virtual environment dengan perintah:

bash
Copy
Edit
python -m venv venv  # Membuat virtual environment bernama 'venv'
Aktifkan virtual environment:

Windows (PowerShell):
bash
Copy
Edit
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate
Mac/Linux:
bash
Copy
Edit
source venv/bin/activate
c. Instalasi Paket yang Dibutuhkan
Jalankan perintah berikut untuk menginstal Streamlit dan pustaka lainnya:

bash
Copy
Edit
pip install streamlit pandas matplotlib seaborn
Simpan daftar paket ke dalam file requirements.txt untuk memudahkan instalasi ulang:

bash
Copy
Edit
pip freeze > requirements.txt
Jika ingin menginstal ulang semua dependensi di masa depan, cukup jalankan:

bash
Copy
Edit
pip install -r requirements.txt
📌 2. Menjalankan Streamlit Dashboard
Pastikan Anda berada di direktori proyek (misalnya, dashboard/), lalu jalankan:

bash
Copy
Edit
cd dashboard  # Masuk ke folder dashboard
streamlit run dashboard.py  # Menjalankan dashboard
Jika berhasil, terminal akan menampilkan pesan seperti berikut:

bash
Copy
Edit
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
Buka http://localhost:8501 di browser untuk melihat dashboard.

📌 3. Mengunggah Dataset
Dashboard yang dijalankan di lokal tidak perlu mengunggah dataset, tapi untuk membuka dashboard melalui streamlit cloud perlu melakukan ini.
Klik tombol Upload Dataset di halaman dashboard.
Pilih file CSV yang akan dianalisis.
Data akan diproses dan divisualisasikan dalam bentuk grafik.

📌 4. Troubleshooting
Jika mengalami error, berikut beberapa solusi umum:

🔹 Error: Modul Tidak Ditemukan
Jalankan kembali perintah berikut:

bash
Copy
Edit
pip install -r requirements.txt
🔹 Error: Port 8501 Sudah Digunakan
Gunakan port lain dengan perintah:

bash
Copy
Edit
streamlit run dashboard.py --server.port 8502
🔹 Error: Virtual Environment Tidak Aktif
Pastikan sudah mengaktifkan virtual environment sebelum menjalankan Streamlit:

bash
Copy
Edit
.\venv\Scripts\activate  # Windows (PowerShell)
source venv/bin/activate  # Mac/Linux
🔹 Nama Dataset Tidak Sesuai
Pastikan file CSV yang digunakan bernama main_data.csv.
