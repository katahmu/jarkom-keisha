# Analisis Protokol TCP & UDP - Wireshark

## Identitas

Nama: Keisha Hananta  
NIM: 103072400149  
Kelas: IF-04-01  

---

## Tujuan

Tujuan Praktikum:

Memahami perbedaan antara protokol TCP dan UDP  
Menganalisis komunikasi jaringan menggunakan Wireshark  
Mengamati proses pengiriman data antara client dan server  
Memahami cara kerja socket programming pada TCP dan UDP  

---

## Dasar Teori

### UDP (User Datagram Protocol)

UDP merupakan protokol pada layer transport yang bersifat:

Connectionless (tidak perlu koneksi terlebih dahulu)  
Tidak reliabel (tidak menjamin data sampai)  
Cepat dan ringan  

UDP tidak memiliki mekanisme:
- Handshake  
- Retransmission  
- Flow control  

Sehingga cocok untuk:
- DNS  
- Streaming  
- Game online  

---

### TCP (Transmission Control Protocol)

TCP merupakan protokol pada layer transport yang bersifat:

Connection-oriented (harus membangun koneksi terlebih dahulu)  
Reliable (menjamin data sampai)  

TCP menggunakan mekanisme:
- Three-way handshake (SYN, SYN-ACK, ACK)  
- Sequence number dan acknowledgment  
- Retransmission  

TCP digunakan pada:
- HTTP  
- FTP  
- Email  

---

## Metode

Langkah-langkah yang dilakukan:

Menjalankan UDP server  
![udp server](assets/asset1.png)

Menjalankan UDP client  
![udp client](assets/asset2.png)

Menjalankan TCP server  
![tcp server](assets/asset3.png)

Menjalankan TCP client  
![tcp client](assets/asset4.png)

Melakukan pengiriman data dari client ke server  
Mengamati hasil komunikasi yang terjadi  

---

## Hasil Analisis

Dari percobaan yang dilakukan:

### UDP
- Tidak terjadi koneksi awal (tanpa handshake)  
- Client langsung mengirim data ke server  
- Server langsung memberikan respon  
- Tidak ada jaminan data sampai  

### TCP
- Terjadi proses koneksi terlebih dahulu (handshake)  
- Data dikirim setelah koneksi terbentuk  
- Data lebih terjamin sampai ke tujuan  
- Komunikasi lebih stabil dibanding UDP  

---

## Kesimpulan

Dari praktikum ini dapat disimpulkan bahwa:

TCP dan UDP memiliki karakteristik yang berbeda pada layer transport  

UDP lebih cepat dan sederhana karena tidak memiliki mekanisme kontrol,  
namun tidak menjamin keandalan pengiriman data  

TCP lebih kompleks karena menggunakan mekanisme koneksi dan kontrol,  
tetapi mampu menjamin data sampai dengan benar dan berurutan  

Pemilihan penggunaan TCP atau UDP tergantung pada kebutuhan aplikasi,  
apakah lebih mengutamakan kecepatan atau keandalan  