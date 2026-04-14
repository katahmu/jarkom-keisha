# TCP

## Identitas

Nama: Keisha Hananta  
NIM: 103072400149  
Kelas: IF-04-01  

---

## Tujuan

Tujuan Praktikum:

Memahami cara kerja protokol TCP (Transmission Control Protocol)  
Menganalisis komunikasi HTTP yang berjalan di atas TCP menggunakan Wireshark  
Mengidentifikasi alamat IP dan port pada komunikasi client-server  
Memahami proses pengiriman data (upload) melalui TCP  

---

## Dasar Teori

TCP (Transmission Control Protocol) merupakan protokol pada layer transport yang bersifat:

Connection-oriented (harus membangun koneksi terlebih dahulu)  
Reliable (menjamin data sampai ke tujuan)  
Menggunakan mekanisme kontrol seperti acknowledgment dan retransmission  

TCP memiliki karakteristik:

Menggunakan Sequence Number dan Acknowledgment  
Melakukan Three-way Handshake (SYN, SYN-ACK, ACK)  
Melakukan segmentasi data menjadi beberapa bagian  

Dalam komunikasi HTTP:

Client mengirim request ke server  
Server mengirim response ke client  
Server HTTP umumnya menggunakan port 80  

---

## Metode

Langkah-langkah yang dilakukan:

Membuka Wireshark  
Memilih interface jaringan (Wi-Fi)  
Memulai capture paket  

Membuka website:
http://gaia.cs.umass.edu/wireshark-labs/alice.txt  
![buka alice](assets/asset1.png)

Membuka:
http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html  
![buka tcp lab](assets/asset2.png)

Melakukan upload file alice.txt  

Menghentikan capture  

Memfilter paket menggunakan: http
![filter http](assets/asset3.png)

Kemudian filter: tcp
![filter tcp](assets/asset4.png)

---

## Hasil Analisis

## 1. Alamat IP dan port TCP client

Dari hasil analisis:

IP Client = 10.218.10.29  
Port Client = 51056  

Client menggunakan port sementara (ephemeral port) untuk komunikasi  

---

## 2. Alamat IP dan port server

Dari hasil analisis:

IP Server = 128.119.245.12  
Port Server = 80  

Port 80 digunakan untuk layanan HTTP  

---

## 3. Alamat IP dan port TCP client (konfirmasi)

Dari koneksi yang sama:

IP Client = 10.218.10.29  
Port Client = 51056  

Port ini tetap digunakan selama koneksi berlangsung   

---

## Kesimpulan

TCP merupakan protokol yang andal karena menjamin pengiriman data  
Komunikasi terjadi antara client dan server menggunakan IP dan port tertentu  
Client menggunakan port acak (ephemeral port)  
Server HTTP menggunakan port 80  

TCP mampu mengirim data besar dengan cara membaginya menjadi beberapa segmen  
dan menyusunnya kembali di sisi penerima  