link tutorial untuk mempermudah deploy:

```bash
https://www.youtube.com/watch?v=Q4-k2E9Wb3w&t=3369s
```

Berikut adalah contoh README.md yang menjelaskan cara melakukan deploy aplikasi Python ke Heroku berdasarkan informasi yang diberikan dalam gambar:

```markdown
# Deploy Aplikasi Python ke Heroku

Panduan ini menjelaskan langkah-langkah untuk melakukan deploy aplikasi Python ke Heroku.

## Langkah 1: Buat Environment di Folder Aplikasi

Buat environment Python di folder aplikasi Anda. Gunakan perintah berikut:
```

```bash
conda create --name <namanya> python=3.?
```

Gantilah `<namanya>` dengan nama environment yang Anda inginkan dan saya menggunakan `python 3.8` dengan versi Python yang sesuai.

## Langkah 2: Aktifkan Environment

Setelah environment berhasil dibuat, aktifkan environment tersebut dengan perintah berikut:

```bash
conda activate <namanya>
```

Gantilah `<namanya>` dengan nama environment yang telah Anda buat.

## Langkah 3: Install Perangkat yang Dibutuhkan

Install semua dependencies atau perangkat yang diperlukan menggunakan perintah berikut:

```bash
pip install -r requirements.txt
```

Gantilah `<namafiledaftarperangkat>` dengan nama file yang berisi daftar dependencies (biasanya `requirements.txt`).

## Langkah 4: Test Aplikasi di Lokal

Sebelum melakukan deploy, pastikan aplikasi berjalan dengan baik di lokal. Jalankan aplikasi Anda dengan perintah berikut:

```bash
python app.py
```

## Langkah 5: Masuk ke Heroku dan Buat Aplikasi Baru

Masuk ke akun Heroku Anda, kemudian buat aplikasi baru melalui menu:

```plaintext
Create -> New App
```

## Langkah 6: Login ke CLI Heroku

Gunakan Heroku CLI untuk login ke akun Heroku Anda dengan perintah berikut:

```bash
heroku login -i
```

## Langkah 7: Proses Mengupload Aplikasi ke Server Heroku Lewat Git

Setelah login, ikuti langkah-langkah berikut untuk mengupload aplikasi Anda ke Heroku:

1. Inisialisasi Git di folder proyek Anda (jika belum dilakukan):

   ```bash
   git init heroku
   ```

2. Tambahkan remote Heroku ke Git:

   ```bash
   git remote add heroku <namaaplikasidiHeroku>
   ```

   Gantilah `<namaaplikasidiHeroku>` dengan nama aplikasi yang telah Anda buat di Heroku.

3. Tambahkan semua file ke Git:

   ```bash
   git add .
   ```

4. Commit perubahan:

   ```bash
   git commit -am "Deploy aplikasi python"
   ```

5. Push ke Heroku:

   ```bash
   git push heroku master
   ```

## Catatan Tambahan

- Pastikan file `Procfile` ada di root folder proyek Anda dengan format yang benar untuk menjalankan aplikasi di Heroku.
- Jika menggunakan database, pastikan konfigurasi environment variables (seperti `DATABASE_URL`) sudah diatur dengan benar di Heroku.

Setelah semua langkah di atas selesai, aplikasi Anda seharusnya sudah berhasil dideploy ke Heroku dan bisa diakses melalui URL aplikasi yang disediakan oleh Heroku.
```

Anda dapat menyesuaikan README.md ini sesuai dengan kebutuhan spesifik proyek Anda. Pastikan juga untuk menyertakan informasi tambahan jika ada pengaturan atau konfigurasi khusus yang diperlukan.



(stag-app-thrive) D:\Hari Ini\Semester 8\Tugas\Thrive\fix-app-finance-dashboard\backup\updateMasFrendi\OOP_flask>tree
Folder PATH listing for volume DATA
Volume serial number is FEE0-2270
D:.
├───app
│   ├───logs
│   ├───models
│   │   └───__pycache__
│   ├───resources
│   │   ├───css
│   │   ├───cssbundle
│   │   │   └───font
│   │   ├───fourth
│   │   │   └───vendor
│   │   │       └───fancybox
│   │   │           └───source
│   │   ├───js
│   │   │   └───bundle
│   │   ├───main
│   │   │   └───css
│   │   ├───second
│   │   │   └───cssbundle
│   │   │       └───font
│   │   ├───thridJS
│   │   │   └───js
│   │   │       └───bundle
│   │   └───vendor
│   │       └───fancybox
│   │           └───source
│   ├───routes
│   │   └───__pycache__
│   ├───services
│   │   └───__pycache__
│   ├───templates
│   └───__pycache__
└───logs

