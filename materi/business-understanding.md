# Business Understanding



## 1. Latar Belakang



Kualitas udara merupakan salah satu aspek penting dalam kondisi lingkungan karena berhubungan dengan kesehatan manusia, ekosistem, dan aktivitas masyarakat. Udara yang tercemar dapat mengandung berbagai zat atau partikel yang berbahaya apabila berada pada konsentrasi tertentu.



Untuk mengetahui kondisi kualitas udara, diperlukan data yang dapat digunakan untuk mengamati keberadaan dan perubahan polutan dari waktu ke waktu. Salah satu sumber data yang dapat digunakan adalah pengamatan satelit.



Pada proyek ini, pengamatan kualitas udara dilakukan pada wilayah **Kabupaten Sampang, Jawa Timur**, dengan memanfaatkan data observasi satelit **Sentinel-5P/TROPOMI** yang diperoleh melalui **Copernicus Data Space Ecosystem**.



Parameter yang menjadi fokus pengamatan pada tahap awal adalah **Nitrogen Dioxide (NO₂)**.



## 2. Indeks Kualitas Udara



Indeks Kualitas Udara atau **Air Quality Index (AQI)** merupakan suatu indeks yang digunakan untuk menggambarkan kondisi kualitas udara berdasarkan konsentrasi polutan tertentu. AQI membantu menerjemahkan data konsentrasi polutan menjadi kategori kualitas udara yang lebih mudah dipahami oleh masyarakat.



Secara umum, semakin tinggi konsentrasi polutan yang berbahaya bagi kesehatan, semakin buruk pula kondisi kualitas udara yang direpresentasikan oleh indeks tersebut.



Beberapa parameter polutan yang dapat digunakan dalam penilaian kualitas udara antara lain:



- **NO₂ (Nitrogen Dioxide)**

- **CO (Carbon Monoxide)**

- **SO₂ (Sulfur Dioxide)**

- **O₃ (Ozone)**

- **PM2.5 (Particulate Matter 2.5)**

- **PM10 (Particulate Matter 10)**



Namun, tidak semua parameter tersebut digunakan dalam analisis pada proyek ini. Pengamatan difokuskan pada parameter **NO₂** karena data parameter tersebut tersedia dari sumber satelit yang digunakan dan sesuai dengan tujuan pengamatan atmosfer pada wilayah Kabupaten Sampang.



> **Catatan:** Data NO₂ dari Sentinel-5P/TROPOMI yang digunakan dalam proyek ini tidak secara langsung merupakan nilai AQI. Data tersebut digunakan untuk mengamati karakteristik dan perubahan parameter NO₂ sebagai salah satu indikator polusi udara.



## 3. Polutan yang Diamati



### 3.1 Nitrogen Dioxide (NO₂)



Nitrogen Dioxide atau **NO₂** merupakan salah satu gas pencemar udara yang berasal terutama dari proses pembakaran bahan bakar pada kendaraan bermotor, pembangkit listrik, kegiatan industri, dan sumber pembakaran lainnya.



NO₂ termasuk salah satu polutan penting karena dapat berperan dalam pembentukan polutan sekunder di atmosfer dan dapat memberikan dampak terhadap kualitas udara serta kesehatan manusia.



Dalam proyek ini, NO₂ dipilih sebagai parameter utama untuk diamati menggunakan data Sentinel-5P/TROPOMI.



### 3.2 Carbon Monoxide (CO)



Carbon Monoxide atau **CO** merupakan gas yang dihasilkan terutama dari proses pembakaran yang tidak sempurna. Sumbernya dapat berasal dari kendaraan bermotor, pembakaran bahan bakar, serta aktivitas pembakaran lainnya.



CO merupakan salah satu parameter yang umum digunakan dalam pemantauan kualitas udara. Namun, parameter CO tidak menjadi fokus utama analisis pada tahap proyek ini.



### 3.3 Sulfur Dioxide (SO₂)



Sulfur Dioxide atau **SO₂** merupakan gas pencemar yang dapat dihasilkan dari pembakaran bahan bakar yang mengandung sulfur dan aktivitas industri tertentu.



SO₂ juga termasuk salah satu parameter yang dapat digunakan untuk menggambarkan kondisi pencemaran udara.



### 3.4 Ozone (O₃)



Ozone atau **O₃** merupakan salah satu komponen atmosfer yang memiliki karakteristik berbeda bergantung pada lokasinya di atmosfer. Ozon di permukaan dapat terbentuk melalui reaksi kimia yang melibatkan beberapa polutan dan paparan sinar matahari.



O₃ merupakan salah satu parameter yang juga dapat digunakan dalam pemantauan kualitas udara.



### 3.5 Particulate Matter (PM2.5 dan PM10)



PM2.5 dan PM10 merupakan partikel berukuran sangat kecil yang berada di udara. Partikel tersebut dapat berasal dari kendaraan, aktivitas industri, pembakaran, debu, dan berbagai sumber lainnya.



PM2.5 memiliki ukuran yang lebih kecil dibandingkan PM10 sehingga dapat masuk lebih jauh ke dalam sistem pernapasan.



## 4. Permasalahan



Permasalahan yang ingin dikaji melalui proyek ini adalah bagaimana karakteristik data NO₂ di Kabupaten Sampang selama periode pengamatan dan bagaimana perubahan nilai tersebut dari waktu ke waktu.



Selain itu, data hasil pengamatan perlu diperiksa untuk mengetahui:



1. Apakah terdapat data yang hilang (*missing values*).

2. Apakah terdapat nilai yang menyimpang (*outliers*).

3. Apakah terdapat indikasi *noise* pada data.

4. Bagaimana pola perubahan nilai NO₂ selama periode pengamatan.

5. Bagaimana distribusi nilai NO₂ pada wilayah Kabupaten Sampang.



## 5. Tujuan Analisis



Tujuan dari analisis ini adalah:



1. Mengumpulkan data NO₂ Kabupaten Sampang dari Copernicus Data Space Ecosystem.

2. Memahami karakteristik dataset yang diperoleh dari Sentinel-5P/TROPOMI.

3. Mengeksplorasi perubahan nilai NO₂ selama periode 24 Agustus 2025 sampai 24 Agustus 2026.

4. Menampilkan data dalam bentuk visualisasi grafik.

5. Menampilkan lokasi wilayah pengamatan menggunakan visualisasi peta.

6. Mengidentifikasi *missing values*, *outliers*, dan kemungkinan *noise* dalam dataset.

7. Menghasilkan dataset dan dokumentasi yang dapat digunakan untuk analisis pada pertemuan berikutnya.



## 6. Pertanyaan Analisis



Berdasarkan permasalahan tersebut, pertanyaan yang ingin dijawab dalam analisis ini adalah:



1. Bagaimana karakteristik data NO₂ di Kabupaten Sampang selama periode pengamatan?

2. Bagaimana perubahan nilai NO₂ dari waktu ke waktu?

3. Apakah terdapat *missing values* dalam dataset?

4. Apakah terdapat nilai NO₂ yang dapat dikategorikan sebagai *outlier*?

5. Bagaimana distribusi nilai NO₂ selama periode pengamatan?

6. Bagaimana kondisi data NO₂ secara keseluruhan berdasarkan hasil eksplorasi awal?



## 7. Wilayah dan Periode Pengamatan



Wilayah yang menjadi objek pengamatan adalah:



> **Kabupaten Sampang, Provinsi Jawa Timur, Indonesia**



Periode pengamatan yang digunakan adalah:



> **24 Agustus 2025 – 24 Agustus 2026**



Data diperoleh dari pengamatan satelit Sentinel-5P/TROPOMI melalui Copernicus Data Space Ecosystem.



Pada tahap berikutnya, dataset yang telah dikumpulkan akan diperiksa dan dieksplorasi untuk memahami struktur, kelengkapan, distribusi, serta karakteristik data sebelum dilakukan analisis lebih lanjut.

