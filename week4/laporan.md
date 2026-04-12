# Analisis Protokol DNS - Wireshark

## Identitas

Nama: Keisha Hananta  
NIM: 103072400149  
Kelas: IF-04-01  

---

## 4.1 Pengantar

DNS (Domain Name System) berfungsi untuk menerjemahkan nama domain menjadi alamat IP.  
Client akan mengirim permintaan ke server DNS dan menerima balasan berupa alamat IP.  

---

## 4.2 Nslookup

### Perintah 1: Mencari IP domain

```bash
nslookup www.mit.edu
```


---

### Perintah 2: Mencari DNS server otoritatif

```bash
nslookup -type=NS mit.edu
```

---

### Perintah 3: Query ke DNS tertentu

```bash
nslookup www.aiit.or.kr bitsy.mit.edu
```

![nslookup IP](assets/asset1.png)

---
### Analisa

#### 1. Web Asia (Tokyo)

```bash
nslookup -type=NS www.u-tokyo.ac.jp
```

![web asia](assets/asset2.png)

Hasil:
Server DNS untuk domain tersebut adalah:
- dns1.nc.u-tokyo.ac.jp  

---

#### 2. Web Eropa (Sweden)

```bash
nslookup -type=NS www.kth.se
```

![web eropa](assets/asset3.png)

Hasil:
Server DNS otoritatif:
- a.ns.kth.se  

---

#### 3. Server Email Yahoo Mail

Percobaan menggunakan DNS dari Sweden:

```bash
nslookup -type=MX yahoo.com a.ns.kth.se
```

![query refused](assets/asset4.png)

Hasil:
Query ditolak (**query refused**) karena server DNS tersebut tidak melayani permintaan dari luar domainnya.

---

Percobaan menggunakan DNS default:

```bash
nslookup -type=MX yahoo.com
```

![yahoo mx](assets/asset5.png)

Hasil:
Mail server Yahoo:
- mta5.am0.yahoodns.net  
- mta6.am0.yahoodns.net  
- mta7.am0.yahoodns.net  

Salah satu alamat IP server email Yahoo:
- **98.136.96.74** (contoh hasil lookup)

---

## 4.3 Ipconfig

### Menampilkan informasi jaringan

```bash
ipconfig /all
```

![ipconfig](assets/asset6.png)

---

### Menampilkan cache DNS

```bash
ipconfig /displaydns
```

![displaydns](assets/asset7.png)

---

### Menghapus cache DNS

```bash
ipconfig /flushdns
```

![flushdns](assets/asset8.png)

---

## 4.4 Tracing DNS dengan Wireshark

### Langkah 1: Bersihkan DNS cache

```bash
ipconfig /flushdns
```

![flushdns wireshark](assets/asset9.png)

---

### Langkah 2: Jalankan Wireshark dan set filter

```
ip.addr == [IP address]
```


---

### Langkah 3: Start capture lalu akses website

```
http://www.ietf.org
```


---

### Langkah 4: Stop capture dan filter DNS

```
dns
```

![dns filter](assets/asset10.png)

---

### Langkah 5: Nslookup dengan Wireshark

```bash
nslookup www.mit.edu
```

![nslookup wireshark](assets/asset11.png)

---

### Langkah 6: Nslookup type NS

```bash
nslookup -type=NS mit.edu
```

![nslookup ns wireshark](assets/asset12.png)

---

### Langkah 7: Nslookup ke server tertentu

```bash
nslookup www.aiit.or.kr bitsy.mit.edu
```

![nslookup custom wireshark](assets/asset13.png)

---
