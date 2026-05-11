# Python CLI Calculator with Unit Testing

Aplikasi kalkulator aritmetika berbasis Command Line Interface (CLI) yang dibangun dengan Python. Proyek ini difokuskan pada penerapan praktik *Software Engineering*, struktur proyek yang modular, dan pengujian otomatis (*Automated Testing*).

## Fitur Utama

* Operasi matematika dasar (Penjumlahan, Pengurangan, Perkalian, Pembagian).
* Arsitektur modular menggunakan *package* Python.
* Penanganan kesalahan (*Error Handling*) untuk input tidak valid dan pembagian dengan nol.
* Pengujian terotomatisasi menggunakan `unittest` dan `pytest`.

## Teknologi

* **Bahasa:** Python 3.x
* **Testing Framework:** `unittest`, `pytest`
* **Coverage Tool:** `pytest-cov`

## Instalasi

### 1. Clone repositori ini ke komputer lokal Anda

```bash
git clone https://github.com/ZippyNx/python-cli-calculator.git
```

### 2. Masuk ke direktori proyek

```bash
cd python-cli-calculator
```

### 3. (Opsional) Buat dan aktifkan virtual environment

#### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Instal dependensi yang dibutuhkan untuk pengujian

```bash
pip install pytest pytest-cov
```

## Menjalankan Aplikasi

Jalankan file utama melalui terminal:

```bash
python main.py
```

## Menjalankan Pengujian & Coverage

Proyek ini memiliki **Test Coverage sebesar 99%**.

Jalankan perintah berikut untuk mengeksekusi unit test dan melihat laporan coverage:

```bash
python -m pytest tests/ -v --cov --cov-report=html
```

Buka file `index.html` di dalam folder `htmlcov` untuk melihat laporan detail secara visual.
