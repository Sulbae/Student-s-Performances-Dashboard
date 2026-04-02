# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini mereka telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Jaya Jaya Institut memerlukan sebuah dashboard sebagai alat monitoring agar mudah dalam memahami data dan mengawasi performa belajar para siswanya.

### Permasalahan Bisnis

Berdasarkan kebutuhan bisnis yang sedang dihadapi, maka fokus utama pada proyek ini adalah membuat dashboard sebagai platform monitoring metrik-metrik penting untuk kebutuhan analisis screening siswa yang memerlukan bimbingan khusus sehingga dapat menurunkan peluang mereka terjerumus ke jalan dropout. Institusi juga perlu menyusun strategi yang tepat untuk dapat menjaga kualitas belajar para siswa. 

Berikut pertanyaan bisnis yang diharapkan dapat terjawab melalui proyek ini.
* Bagaimana pengaruh Kondisi Finansial Mahasiswa terhadap Status Kelulusan?
* Bagaimana pengaruh Kondisi Ekonomi Makro terhadap Status Kelulusan?
* Bagaimana pengaruh Capaian Akademik Mahasiswa terhadap Status Kelulusan?
* Apa saja 10 faktor yang berpengaruh signifikan terhadap tingginya probabilitas mahasiswa dapat mengalami dropout?
* Bagaimana strategi yang harus dijalankan oleh tim akademik dalam mengelola kualitas belajar siswa untuk menekan angka dropout mahasiswa?

### Cakupan Proyek

1) Pengumpulan dan Persiapan Data
2) Pengolahan dan Analisis Data
3) Visualisasi dan Interpretasi Data
5) Pembuatan Dashboard
6) Rekomendasi

### Persiapan

Sumber data: [Jaya Jaya Institut Dataset](https://raw.githubusercontent.com/Sulbae/Student-s-Performances-Dashboard/refs/heads/main/students_data.csv)

Setup environment:

1. Buat lingkungan virtual
    ```
    conda create --name penerapan-data-science python=3.10 -y
    ```
2. Aktifkan lingkungan virtual
    ```
    conda activate penerapan-data-science
    ```
3. Install dependensi
    ```
    conda install -r requirements.txt
    ```

Pengolahan dan Persiapan Data
``` 
Data Exploration
|---Karakteristik Data
|---Kelengkapan Data
|---Distribusi Data
Data Cleaning
|---Missing Value Handling
```
Eksplorasi dan Analisis Data
```
Analisis Korelasi Antar Variabel Data 
|---Observasi pengaruh Kondisi Ekonomi Mahasiswa terhadap Status Kelulusan
|---Observasi pengaruh Kondisi Ekonomi Makro terhadap Status Kelulusan
|---Observasi pengaruh Capaian Akademik Mahasiswa terhadap Status Kelulusan
```

## Business Dashboard

[Lihat Dashboard]()

Dashboard berisi informasi mengenai ringkasan metrik-metrik penting dan visualisasi data yang diperlukan dalam kegiatan monitoring terhadap berbagai aspek yang berkaitan dengan kondisi pengelolaan sumber daya manusia (talent) perusahaan seperti berikut:
1) Total Karyawan
    - Deskripsi: Jumlah seluruh karyawan yang terdata.
    - Kegunaan: Memberikan informasi mengenai besaran jumlah karyawan yang sedang/telah dikelola perusahaan.
2) Total Attrition
    - Deskripsi: Jumlah karyawan yang telah berhenti/diberhentikan dan tercatat pada database.
    - Kegunaan: Menjadi indikator tinggi-rendahnya tingkat pergantian karyawan (Attrition Rate).
3) Rata-rata Usia (Avg. Age)
    - Deskripsi: Usia rata-rata karyawan secara keseluruhan.
    - Kegunaan: Usia rata-rata dapat menjadi indikator dalam analisis demografi personel tim khususnya dalam monitoring komposisi tim hingga perencanaan promosi dan/atau suksesi.
4) Enviro Satisfaction Rate
    - Deskripsi: Tingkat kepuasan rata-rata karyawan terhadap kondisi lingkungan/budaya kerja perusahaan (Environment Satisfaction).
    - Kegunaan: Menjadi indikator awal dalam mengetahui tingkat kenyamanan perusahaan secara umum bagi seluruh karyawan.
5) Job Satisfaction Rate
    - Deskripsi: Tingkat kepuasan rata-rata karyawan terhadap pekerjaan yang diemban oleh mereka. 
    - Kegunaan: Menjadi indikator awal dalam mengetahui tingkat kesesuaian ekspektasi kerja karyawan dengan beban kerja nyata di kantor/lapangan. Informasi ini akan berguna sebagai early-warning dalam mendeteksi gejala burnout karyawan maupun pengelolaan organisasi yang tidak efisien.
6) Perfomance Rate
    - Deskripsi: Tingkat performa/kinerja rata-rata karyawan secara keseluruhan.
    - Kegunaan: Mengukur kinerja rata-rata karyawan dan sebagai tolak ukur awal yang menggambarkan tingkat produktivitas dari tenaga kerja perusahaan.
7) Rata-rata Pelatihan Yang Diikuti (Avg. Training (Last Year))
    - Deskripsi: Jumlah pelatihan rata-rata yang telah diikuti karyawan selama satu tahun terakhir.
    - Kegunaan: Menjadi indikator pembanding bagi metrik Performance Rate dalam mengukur tingkat produktivitas perusahaan. Jumlah pelatihan dapat menjadi nilai representatif dari besaran investasi yang telah perusahaan lakukan untuk memelihara kualitas talentanya, yakni melalui pemberian fasilitas kegiatan pelatihan bagi para karyawan.
8) Monthly Rate Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Monthly Rate yang telah dikelompokkan ke dalam level tertentu.
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar dalam berbagai level gaji bulanan. Data ini digunakan untuk memahami pengaruh besaran gaji yang diterima terhadap tingkat Attrition karyawan.  
9) Percent Salary Hike Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan besaran Percent Salary Hike dalam satu tahun terakhir.
    - Kegunaan: Memberikan informasi besaran persentase kenaikan gaji bulanan dibandingkan dengan gaji sebelumnya. Data ini digunakan untuk memahami pengaruh besaran persentase kenaikan gaji terhadap tingkat Attrition karyawan.
10) Monthly Income Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Monthly Income yang telah dikelompokkan ke dalam level tertentu.
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar dalam berbagai level pendapatan total (gaji + pendapatan lain-lain) bulanan. Data ini digunakan untuk memahami pengaruh besaran pendapatan total bulanan yang mampu diperoleh terhadap tingkat Attrition karyawan.

## Conclusion

Berdasarkan hasil analisis dalam proyek ini, maka dapat disimpulkan bahwa:
1. Kompensasi Finansial merupakan Faktor Pendorong Utama Attrition
    * Karyawan dengan rasio kompensasi terhadap biaya hidup yang tidak seimbang (terutama yang menempuh jarak jauh dengan gaji yang relatif pas-pasan) memiliki kecenderungan lebih tinggi untuk resign. Dengan demikian, daya saing kompensasi dan pertimbangan biaya transportasi merupakan elemen kritis dalam keputusan retensi karyawan.
2. Masa Kerja dan Stabilitas Karir memiliki pengaruh yang signifikan terhadap Attrition Rate
    * Analisis terhadap NumCompaniesWorked, TotalWorkingYears, dan YearsAtCompany menunjukkan bahwa:
        - Karyawan dengan masa kerja kurang dari atau sama dengan 1 tahun merupakan segmen paling rentan terhadap Attrition (early-stage churn).
        - Karyawan dengan pengalaman kerja < 10 tahun dan riwayat perpindahan perusahaan yang cukup sering menunjukkan pola mobilitas karir yang cukup tinggi.
        - Sebaliknya, karyawan senior (masa kerja > 10 tahun atau dengan level jabatan yang tinggi) menunjukkan tingkat retensi yang lebih stabil.
3. Faktor Psikologis dan Lingkungan Kerja sebagai Pendorong Sekunder
    * Dapat dikatakan passion (JobInvolvement), lingkungan kerja (EnvironmentSatisfaction), dan kenyamanan dalam pekerjaan mereka (JobSatisfaction) memiliki korelasi moderat, tetapi konsisten terhadap attrition. Meskipun pengaruhnya tidak sekuat faktor-faktor lain. Aspek ini dapat menjadi faktor penguat yang akan mempercepat atau memperlambat keputusan resign, terutama ketika dikombinasikan dengan faktor ketidakpuasan terhadap kompensasi/benefit finansial.
4. Top 10 faktor yang berpengaruh signifikan terhadap Attration Rate
    * Berdasarkan hubungan pengaruh antar variabel yang telah dikalkulasi menggunakan metode perhitungan korelasi matrix. Aspek-aspek seperti DistanceFromHome, NumCompaniesWorked, MonthlyRate, PerformanceRating, dan PercentSalaryHike memiliki korelasi positif yang paling signifikan terhadap Attrition Karyawan dibandingkan dengan aspek-aspek lainnya. 
    * Menarik sekali bahwa PerfomanceRating memiliki korelasi positif terhadap Attrition. Beberapa alasan yang mungkin menjadi faktor penyebabnya antara lain:
        - Talent dengan performa tinggi seringkali memiliki nilai pasar (value) yang lebih kompetitif sehingga lebih mudah mendapat tawaran dari perusahaan lain.
        - Talent dengan performa tinggi memiliki ekspektasi promosi lebih cepat atau kenaikan gaji/kompensasi yang lebih tinggi. Jika ekspektasi tersebut tidak tercapai, maka dapat menjadi motivasi yang cukup kuat untuk pindah.
    * Sementara itu, aspek MonthlyIncome, StockOptionLevel, JobLevel, Age, TotalWorkingYears memiliki korelasi negatif yang paling signifikan terhadap Attrition Karyawan dibandingkan dengan aspek-aspek lainnya. Aspek Total Working Years dan Age biasanya saling berkaitan karena pada umumnya karyawan-karyawan yang sudah sangat senior memiliki peluang yang lebih rendah untuk berhenti/diberhentikan dari pekerjaannya karena berbagai alasan, misalnya sudah memiliki tanggungjawab yang besar atau sudah merasa nyaman dalam pekerjaannya. Hal ini sejalan dengan korelasi negatif yang ditunjukkan oleh aspek JobLevel, yang mana menandakan bahwa karyawan dengan level posisi yang lebih junior/rendah memiliki potensi Attrition yang lebih tinggi.

### Rekomendasi Action Items (Optional)

Berdasarkan temuan-temuan tersebut, berikut adalah rekomendasi strategis yang potensial untuk diterapkan:

1. Penerapan Early Support System
    - Apabila mahasiswa terindikasi sebagai Debtor dan/atau tercatat pernah telat melakukan pembayaran, segera lakukan intervensi dini seperti menyediakan layanan konseling untuk meminimalisir risiko Dropout akibat masalah finansial yang dihadapi.
        
2. Program Bantuan Finansial
    - * Pemberian keringanan khusus seperti skema pembayaran cicilan.

