# Data Understanding



## 1. Gambaran Umum Data



Data yang digunakan dalam proyek ini merupakan data pengamatan kualitas udara yang diperoleh dari **Copernicus Data Space Ecosystem** dengan memanfaatkan data satelit **Sentinel-5P** dan instrumen **TROPOMI (TROPOspheric Monitoring Instrument)**.



Sentinel-5P merupakan satelit observasi bumi yang digunakan untuk memantau komposisi atmosfer. Salah satu parameter yang dapat diamati adalah **Nitrogen Dioxide (NO₂)**.



Pada proyek ini, data NO₂ digunakan untuk melakukan pengamatan terhadap kondisi atmosfer di wilayah **Kabupaten Sampang, Jawa Timur**.



## 2. Sumber Data



Sumber data yang digunakan adalah:



**Copernicus Data Space Ecosystem**



Platform tersebut menyediakan akses terhadap berbagai data observasi bumi dari program Copernicus, termasuk data Sentinel-5P.



Data yang digunakan dalam proyek ini berasal dari:



- Satelit: Sentinel-5P

- Instrumen: TROPOMI

- Parameter: NO₂

- Wilayah: Kabupaten Sampang

- Provinsi: Jawa Timur

- Negara: Indonesia



## 3. Parameter yang Digunakan



Parameter utama yang digunakan adalah:



### NO₂ — Nitrogen Dioxide



NO₂ merupakan salah satu gas yang digunakan sebagai indikator pencemaran atmosfer.



Dalam dataset yang digunakan, nilai NO₂ diperoleh dari hasil pengamatan Sentinel-5P/TROPOMI pada wilayah yang telah ditentukan.



Parameter ini digunakan untuk melihat:



- nilai NO₂ dari waktu ke waktu,

- perubahan nilai NO₂,

- distribusi nilai NO₂,

- nilai minimum dan maksimum,

- serta kemungkinan adanya nilai yang menyimpang.



## 4. Wilayah Pengamatan



Wilayah penelitian adalah **Kabupaten Sampang, Jawa Timur, Indonesia**.



Wilayah Kabupaten Sampang digunakan sebagai Area of Interest (AOI) dalam proses pengambilan data.



Secara geografis, Kabupaten Sampang merupakan salah satu kabupaten yang berada di Pulau Madura, Provinsi Jawa Timur.



Batas wilayah pengamatan digunakan untuk membatasi data satelit sehingga analisis berfokus pada wilayah Kabupaten Sampang.



## 5. Periode Pengamatan



Data dikumpulkan untuk periode:



> **24 Agustus 2025 – 24 Agustus 2026**



Periode tersebut digunakan untuk memperoleh data pengamatan selama kurang lebih satu tahun sehingga memungkinkan dilakukan analisis terhadap perubahan nilai NO₂ dari waktu ke waktu.



Data yang tersedia kemudian diperiksa berdasarkan tanggal pengamatan untuk mengetahui apakah seluruh tanggal dalam periode tersebut memiliki data.



## 6. Jenis Data



Data utama yang digunakan berupa data observasi atmosfer dari Sentinel-5P/TROPOMI.



Data kemudian diproses menjadi data deret waktu (*time series*) sehingga setiap pengamatan dapat dikaitkan dengan tanggal tertentu.



Bentuk data yang digunakan dalam analisis antara lain:



| Variabel | Keterangan |

|---|---|

| `t` | Tanggal/waktu pengamatan |

| `NO2` | Nilai parameter Nitrogen Dioxide |

| `feature` | Fitur/wilayah pengamatan |



Data tersebut kemudian digunakan untuk analisis statistik dan visualisasi.



## 7. Karakteristik Data



Dataset hasil pengambilan data perlu diperiksa sebelum dilakukan analisis. Pemeriksaan dilakukan untuk mengetahui:



1. Jumlah observasi.

2. Jumlah variabel.

3. Tipe data setiap variabel.

4. Rentang tanggal pengamatan.

5. Nilai minimum dan maksimum.

6. Nilai rata-rata.

7. Nilai median.

8. Distribusi data.

9. Data yang hilang.

10. Nilai yang berpotensi menjadi *outlier*.



Tahap pemeriksaan ini dilakukan untuk memastikan dataset dapat digunakan untuk proses analisis berikutnya.



## 8. Kualitas dan Kelengkapan Data



Tidak semua tanggal dalam periode pengamatan harus memiliki data yang tersedia. Oleh karena itu, dilakukan pemeriksaan terhadap tanggal pengamatan untuk mengetahui adanya *missing dates*.



Selain pemeriksaan tanggal, dilakukan pemeriksaan terhadap nilai NO₂ untuk mengetahui apakah terdapat nilai kosong (*missing values*).



Kelengkapan data akan dihitung dengan membandingkan jumlah tanggal yang tersedia dengan jumlah hari pada periode pengamatan.



## 9. Persiapan untuk Analisis



Setelah data berhasil dikumpulkan dan dipahami, tahap berikutnya adalah melakukan eksplorasi data.



Eksplorasi meliputi:



- pemeriksaan struktur dataset,

- statistik deskriptif,

- pemeriksaan *missing values*,

- identifikasi *outliers*,

- pemeriksaan kemungkinan *noise*,

- visualisasi data dalam bentuk grafik,

- serta visualisasi wilayah menggunakan peta.



Hasil eksplorasi tersebut akan menjadi dasar untuk menentukan langkah analisis pada tahap berikutnya.

