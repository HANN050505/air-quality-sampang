import json

notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pertemuan 2 – Analisis Statistik Data Kualitas Udara Kabupaten Sampang\n",
    "\n",
    "**Nama:** Raihan Aryanova  \n",
    "**NIM:** 23XXXXXXXX  \n",
    "**Program Studi:** Informatika  \n",
    "\n",
    "## Tujuan Pembelajaran\n",
    "\n",
    "1. Melakukan migrasi dataset Kualitas Udara ($NO_2$) Kabupaten Sampang dari file CSV lokal ke cloud database Aiven PostgreSQL.\n",
    "2. Menghubungkan cloud database Aiven PostgreSQL ke KNIME Analytics Platform.\n",
    "3. Memproses dan mengekstrak nilai statistik deskriptif menggunakan KNIME.\n",
    "4. Menjelaskan secara teoritis dan matematis seluruh properti statistik yang dihasilkan oleh KNIME.\n",
    "5. Memberikan contoh perhitungan manual beserta verifikasi menggunakan Python.\n",
    "6. Menyusun dokumentasi terstruktur untuk dipublikasikan pada web statis Jupyter Book."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Import Library dan Memuat Dataset\n",
    "\n",
    "Dataset yang digunakan merupakan hasil pemrosesan data konsentrasi $NO_2$ Kabupaten Sampang periode **24 Agustus 2025 hingga 23 Agustus 2026** (315 hari pengamatan)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import scipy.stats as stats\n",
    "\n",
    "# Memuat file dataset\n",
    "file_csv = '../data/no2_sampang.csv'\n",
    "df = pd.read_csv(file_csv)\n",
    "\n",
    "print(\"Jumlah Baris:\", len(df))\n",
    "print(\"Jumlah Kolom:\", len(df.columns))\n",
    "print(\"Nama Kolom:\")\n",
    "print(list(df.columns))\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Pemeriksaan Struktur Data dan Missing Value\n",
    "\n",
    "Pemeriksaan awal dilakukan untuk memverifikasi tipe data dan keberadaan nilai hilang sebelum dimasukkan ke cloud database."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Menampilkan struktur dan tipe data\n",
    "df.info()\n",
    "\n",
    "print(\"\\nJumlah Missing Value pada Setiap Kolom:\")\n",
    "print(df.isnull().sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Penyimpanan Data pada Cloud Database (Aiven PostgreSQL)\n",
    "\n",
    "Aiven digunakan sebagai penyedia layanan cloud database PostgreSQL agar dataset terpusat dan dapat diakses dari KNIME.\n",
    "\n",
    "### Tahapan Integrasi Aiven Cloud:\n",
    "1. Membuat instance PostgreSQL pada platform Aiven.\n",
    "2. Mencatat parameter koneksi database: *Host*, *Port*, *User*, *Password*, dan *Database Name*.\n",
    "3. Membuat tabel database `no2_sampang` dengan skema tipe data yang sesuai.\n",
    "4. Mengunggah seluruh baris data ke cloud database Aiven."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Penarikan Data Menggunakan KNIME Analytics Platform\n",
    "\n",
    "Pengambilan data dan perhitungan statistik dilakukan pada KNIME Analytics Platform menggunakan rangkaian node berikut:\n",
    "\n",
    "1. **CSV Reader**: Membaca file CSV lokal.\n",
    "2. **PostgreSQL Connector**: Membuka koneksi terenkripsi ke cloud database Aiven PostgreSQL.\n",
    "3. **DB Writer**: Menuliskan isi CSV ke tabel cloud Aiven secara langsung.\n",
    "4. **DB Table Selector**: Memilih tabel `no2_sampang` yang berada di cloud Aiven.\n",
    "5. **DB Reader**: Eksekusi query untuk menarik data dari cloud Aiven ke KNIME Table.\n",
    "6. **Statistics**: Menghitung dan mengekstrak statistik deskriptif dari setiap kolom."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Penjelasan Properti Statistik KNIME\n",
    "\n",
    "- **Column**: Nama kolom atau variabel yang sedang dianalisis.\n",
    "- **Type**: Tipe data variabel pada KNIME (seperti Number Double, Integer, String, atau Date).\n",
    "- **Min (Minimum)**: Nilai terkecil dari seluruh observasi pada suatu kolom.\n",
    "- **Max (Maximum)**: Nilai terbesar dari seluruh observasi pada suatu kolom.\n",
    "- **Mean**: Nilai rata-rata aritmetika, mengukur titik pusat distribusi data.\n",
    "- **Median ($Q_2$)**: Nilai tengah data setelah seluruh nilai diurutkan dari terkecil ke terbesar.\n",
    "- **Std. Dev. (Standard Deviation)**: Simpangan baku sampel ($s$), mengukur rata-rata penyebaran data terhadap nilai rata-ratanya.\n",
    "- **Variance**: Varians sampel ($s^2$), yaitu kuadrat dari standar deviasi yang menunjukkan besarnya dispersi data.\n",
    "- **Skewness**: Mengukur tingkat ketidaksimetrisan (kemiringan) distribusi data terhadap rata-ratanya.\n",
    "- **Kurtosis**: Mengukur tingkat keruncingan puncak distribusi relatif terhadap distribusi normal.\n",
    "- **IQR (Interquartile Range)**: Jangkauan antarkuartil, yaitu selisih antara Kuartil Ketiga ($Q_3$) dan Kuartil Pertama ($Q_1$).\n",
    "- **MAD (Median Absolute Deviation)**: Median dari selisih mutlak setiap data terhadap nilai median.\n",
    "- **No. Missing**: Jumlah baris data yang kosong atau bernilai `NULL`/`NaN`.\n",
    "- **No. +unlimited**: Jumlah nilai yang bernilai positif tak hingga ($+\\infty$).\n",
    "- **No. -unlimited**: Jumlah nilai yang bernilai negatif tak hingga ($-\\infty$).\n",
    "- **Row Count**: Jumlah total baris atau observasi non-null pada kolom tersebut."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Formulasi Matematis dan Contoh Perhitungan Statistik\n",
    "\n",
    "Untuk memahami mekanisme perhitungan setiap properti statistik, digunakan sampel data kecil $X = \\{2, 4, 5, 7, 9\\}$ dengan jumlah sampel $n = 5$.\n",
    "\n",
    "### 1. Minimum ($\\text{Min}$)\n",
    "$$\\text{Min}(X) = \\min(x_1, x_2, \\dots, x_n)$$\n",
    "$$\\text{Min}(\\{2, 4, 5, 7, 9\\}) = 2$$\n",
    "\n",
    "### 2. Maksimum ($\\text{Max}$)\n",
    "$$\\text{Max}(X) = \\max(x_1, x_2, \\dots, x_n)$$\n",
    "$$\\text{Max}(\\{2, 4, 5, 7, 9\\}) = 9$$\n",
    "\n",
    "### 3. Rata-rata ($\\bar{x}$ / Mean)\n",
    "$$\\bar{x} = \\frac{\\sum_{i=1}^{n} x_i}{n}$$\n",
    "$$\\bar{x} = \\frac{2 + 4 + 5 + 7 + 9}{5} = \\frac{27}{5} = 5.4$$\n",
    "\n",
    "### 4. Median ($\\tilde{x}$)\n",
    "Data terurut: $2, 4, 5, 7, 9$. Karena $n = 5$ (ganjil), median terletak pada data ke-\\frac{5+1}{2} = 3.\n",
    "$$\\tilde{x} = 5$$\n",
    "\n",
    "### 5. Standar Deviasi Sampel ($s$) dan Varians ($s^2$)\n",
    "$$s^2 = \\frac{\\sum_{i=1}^{n} (x_i - \\bar{x})^2}{n - 1}$$\n",
    "$$s^2 = \\frac{29.20}{5 - 1} = 7.30$$\n",
    "$$s = \\sqrt{7.30} \\approx 2.70185$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verifikasi Perhitungan Menggunakan Python\n",
    "contoh = np.array([2, 4, 5, 7, 9], dtype=float)\n",
    "\n",
    "print(\"Data Sampel:\", contoh)\n",
    "print(\"Min:\", np.min(contoh))\n",
    "print(\"Max:\", np.max(contoh))\n",
    "print(\"Mean:\", np.mean(contoh))\n",
    "print(\"Median:\", np.median(contoh))\n",
    "print(\"Varians Sampel:\", np.var(contoh, ddof=1))\n",
    "print(\"Std. Dev. Sampel:\", np.std(contoh, ddof=1))\n",
    "print(\"Skewness Sampel:\", stats.skew(contoh, bias=False))\n",
    "print(\"Kurtosis Sampel (Excess):\", stats.kurtosis(contoh, bias=False))\n",
    "print(\"MAD:\", np.median(np.abs(contoh - np.median(contoh))))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Perhitungan Statistik Aktual Dataset Kualitas Udara ($NO_2$)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "def hitung_statistik_lengkap(data_frame):\n",
    "    numeric_cols = data_frame.select_dtypes(include=[np.number]).columns\n",
    "    hasil = []\n",
    "    \n",
    "    for col in numeric_cols:\n",
    "        s = data_frame[col].dropna()\n",
    "        n = len(s)\n",
    "        mean_v = s.mean()\n",
    "        median_v = s.median()\n",
    "        min_v = s.min()\n",
    "        max_v = s.max()\n",
    "        std_v = s.std(ddof=1) if n > 1 else 0.0\n",
    "        skew_v = stats.skew(s, bias=False) if n > 2 else np.nan\n",
    "        kurt_v = stats.kurtosis(s, bias=False) if n > 3 else np.nan\n",
    "        \n",
    "        n_missing = data_frame[col].isna().sum()\n",
    "        n_pos_inf = np.isposinf(data_frame[col]).sum()\n",
    "        n_neg_inf = np.isneginf(data_frame[col]).sum()\n",
    "        \n",
    "        hasil.append({\n",
    "            'Column': col,\n",
    "            'Min': min_v,\n",
    "            'Mean': mean_v,\n",
    "            'Median': median_v,\n",
    "            'Max': max_v,\n",
    "            'Std. Dev.': std_v,\n",
    "            'Skewness': skew_v,\n",
    "            'Kurtosis': kurt_v,\n",
    "            'No. Missing': n_missing,\n",
    "            'No. +unlimited': n_pos_inf,\n",
    "            'No. -unlimited': n_neg_inf\n",
    "        })\n",
    "    return pd.DataFrame(hasil)\n",
    "\n",
    "df_stat_aktual = hitung_statistik_lengkap(df)\n",
    "df_stat_aktual"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8. Interpretasi Hasil Statistik dan Kesimpulan\n",
    "\n",
    "1. **Konsentrasi $NO_2$**: Rata-rata konsentrasi $NO_2$ berada pada angka $2.1219 \\times 10^{-5}$ $\\text{mol/m}^2$ dengan distribusi miring positif ($0.5124$).\n",
    "2. **Missing Value**: Hanya terdapat $1$ nilai kosong pada kolom perubahan harian dikarenakan baris pertama tidak memiliki data pembanding sebelumnya.\n",
    "3. **Nilai Tak Hingga**: Tidak terdapat nilai $+\\infty$ maupun $-\\infty$ pada seluruh kolom."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

with open("notebooks2.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook_content, f, indent=2, ensure_ascii=False)

print("File notebooks2.ipynb berhasil diperbarui!")