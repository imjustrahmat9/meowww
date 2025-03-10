# -*- coding: utf-8 -*-
"""Proyek Analisis Data_Rahmat Hidayat.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FdK_krkm0zqGEZ9Nicpfk4RCfOSqEbqO

# Proyek Analisis Data: [E-Commerce]
- **Nama:** Rahmat Hidayat
- **Email:** mc013d5y1559@student.devacademy.id
- **ID Dicoding:** MC013D5Y1559

## Menentukan Pertanyaan Bisnis

- Pertanyaan 1 : Bagaimana pengaruh harga terhadap konversi pembelian produk di situs e-commerce?
- Pertanyaan 2 : Produk kategori mana yang memiliki tingkat retensi pelanggan tertinggi di platform e-commerce?

## Import Semua Packages/Library yang Digunakan
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive

"""DATA WRAGLING"""

#Menyiapkan data dan memanggil dataset

kucing = pd.read_csv('/content/drive/MyDrive/Rahmat Hidayat_Projek/order_items_dataset.csv')
kelinci = pd.read_csv('/content/drive/MyDrive/Rahmat Hidayat_Projek/customers_dataset.csv')
Anjing = pd.read_csv('/content/drive/MyDrive/Rahmat Hidayat_Projek/orders_dataset.csv')

#pengecekan data
print(kucing.shape, kelinci.shape, Anjing.shape)

kucing.head(10)

# Mengecek jumlah missing values di setiap dataset
print("Missing values di kucing:\n", kucing.isnull().sum())
print("\nMissing values di kelinci:\n", kelinci.isnull().sum())
print("\nMissing values di Anjing:\n", Anjing.isnull().sum())

# Menghapus duplikasi data
kucing_clean = kucing_clean.drop_duplicates()
kelinci_clean = kelinci_clean.drop_duplicates()
Anjing_clean = Anjing_clean.drop_duplicates()

# Membuat salinan dataset agar tidak mengubah dataset asli
kucing_clean = kucing.copy()
kelinci_clean = kelinci.copy()
Anjing_clean = Anjing.copy()

# Mengubah nama kolom agar lebih seragam dan mudah digunakan
kucing_clean.columns = kucing_clean.columns.str.lower().str.replace(' ', '_')
kelinci_clean.columns = kelinci_clean.columns.str.lower().str.replace(' ', '_')
Anjing_clean.columns = Anjing_clean.columns.str.lower().str.replace(' ', '_')

"""### Gathering Data"""

# Cek ukuran dataset
print(f"Order Items: {kucing.shape}")
print(f"Customers: {kelinci.shape}")
print(f"Orders: {Anjing.shape}")

# Cek 5 data pertama
print("\nOrder Items Dataset:")
display(kucing.head())

print("\nCustomers Dataset:")
display(kelinci.head())

print("\nOrders Dataset:")
display(Anjing.head())

# Cek tipe data
print("\nInfo Order Items Dataset:")
kucing.info()

print("\nInfo Customers Dataset:")
kelinci.info()

print("\nInfo Orders Dataset:")
Anjing.info()

"""**Insight:**
- xxx
- xxx

### Assessing Data
"""

# Menampilkan 5 data pertama
print("Order Items Dataset:")
display(kucing.head())

print("\nCustomers Dataset:")
display(kelinci.head())

print("\nOrders Dataset:")
display(Anjing.head())

# Melihat tipe data dan jumlah missing values
print("\nInformasi Order Items Dataset:")
print(kucing.info())

print("\nInformasi Customers Dataset:")
print(kelinci.info())

print("\nInformasi Orders Dataset:")
print(Anjing.info())

# Statistik deskriptif untuk melihat ringkasan data numerik
print("\nStatistik Order Items Dataset:")
print(kucing.describe())

print("\nStatistik Customers Dataset:")
print(kelinci.describe())

print("\nStatistik Orders Dataset:")
print(Anjing.describe())

# Mengecek jumlah missing values di setiap dataset
print("\nJumlah Missing Values:")
print("Order Items:\n", kucing.isnull().sum())
print("\nCustomers:\n", kelinci.isnull().sum())
print("\nOrders:\n", Anjing.isnull().sum())

# Mengecek jumlah duplikasi
print("\nJumlah Data Duplikat:")
print("Order Items:", kucing.duplicated().sum())
print("Customers:", kelinci.duplicated().sum())
print("Orders:", Anjing.duplicated().sum())

"""**Insight:**
- xxx
- xxx

### Cleaning Data
"""

# Melihat daftar kolom dalam DataFrame
print("Kolom dalam kucing:", kucing.columns)
print("Kolom dalam kelinci:", kelinci.columns)
print("Kolom dalam Anjing:", Anjing.columns)

# Pastikan hanya menghapus kolom yang benar-benar ada dalam DataFrame
columns_to_drop = ["order_id", "order_item_id", "product_id", "seller_id"]

kucing.drop(columns=[col for col in columns_to_drop if col in kucing.columns], inplace=True)
kelinci.drop(columns=[col for col in columns_to_drop if col in kelinci.columns], inplace=True)
Anjing.drop(columns=[col for col in columns_to_drop if col in Anjing.columns], inplace=True)

print("Kolom setelah dihapus:")
print("kucing:", kucing.columns)
print("kelinci:", kelinci.columns)
print("Anjing:", Anjing.columns)

print(kucing.isnull().sum())
print(kelinci.isnull().sum())
print(Anjing.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

# Memastikan ada kolom numerik untuk divisualisasikan
numeric_cols = kucing.select_dtypes(include=['float64', 'int64'])

if not numeric_cols.empty:
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=numeric_cols, palette="Set2")  # Menggunakan palet warna
    plt.xticks(rotation=45)  # Memutar label agar lebih mudah dibaca
    plt.title("Distribusi Data Numerik pada Dataset Kucing", fontsize=14)
    plt.xlabel("Fitur", fontsize=12)
    plt.ylabel("Nilai", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()
else:
    print("Tidak ada data numerik untuk divisualisasikan.")

"""**Insight:**
- xxx
- xxx

## Exploratory Data Analysis (EDA)

a. Statistik Deskriptif
"""

print(kucing.describe())
print(kelinci.describe())
print(Anjing.describe())

import seaborn as sns
import matplotlib.pyplot as plt

# Memeriksa tipe data dari setiap kolom
print(kucing.dtypes)

if 'shipping_limit_date' in kucing.columns:
    kucing['shipping_limit_date'] = pd.to_datetime(kucing['shipping_limit_date'], errors='coerce')

numeric_kucing = kucing.select_dtypes(include=['float64', 'int64'])

# Pastikan ada kolom numerik yang tersisa sebelum plotting
if not numeric_kucing.empty:
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_kucing.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Heatmap Korelasi Variabel Kucing")
    plt.show()
else:
    print("Tidak ada kolom numerik untuk dihitung korelasinya.")

plt.figure(figsize=(10, 5))
sns.histplot(kucing['price'], bins=30, kde=True, color='blue')
plt.title("Distribusi Harga Produk")
plt.xlabel("Harga")
plt.ylabel("Frekuensi")
plt.show()

"""## Visualization & Explanatory Analysis"""

kucing.hist(figsize=(12, 8), bins=30)
plt.show()

sns.scatterplot(x=kucing['price'], y=kucing['freight_value'])
plt.title("Hubungan Harga dengan Freight Value")
plt.xlabel("Harga")
plt.ylabel("Freight Value")
plt.show()

"""ANALISIS LANJUTAN (OPTIONAL)

### Pertanyaan 1: Bagaimana pengaruh harga terhadap konversi pembelian produk di situs e-commerce?

Jawaban :

Gambar ini menunjukkan hubungan antara harga produk dan biaya pengiriman (freight value) di sebuah platform e-commerce. Dari sebaran titik-titik data, kita bisa melihat bahwa sebagian besar produk yang dijual memiliki harga di bawah 2000 dan biaya pengiriman di bawah 100. Namun, ada juga beberapa produk yang harganya sangat tinggi (di atas 5000) dengan biaya pengiriman yang bervariasi, bahkan ada yang mencapai lebih dari 300.  

Dari pola yang terlihat, tidak ada hubungan yang jelas antara harga dan biaya pengiriman. Artinya, harga yang lebih tinggi tidak selalu berarti biaya pengiriman yang lebih mahal. Beberapa produk mahal tetap memiliki biaya pengiriman rendah, sementara ada juga produk yang justru punya ongkos kirim sangat tinggi. Ini bisa disebabkan oleh faktor lain, seperti ukuran dan berat produk, jarak pengiriman, atau kebijakan dari penjual itu sendiri.  

Bagi bisnis e-commerce, pola ini bisa menjadi bahan pertimbangan dalam strategi harga dan pengiriman. Jika biaya pengiriman yang terlalu tinggi membuat pembeli ragu, platform bisa menawarkan subsidi ongkir atau promo gratis ongkir untuk produk tertentu agar lebih menarik.  

Untuk analisis lebih lanjut, kita bisa mengecek seberapa kuat hubungan antara harga dan biaya pengiriman dengan perhitungan korelasi. Selain itu, melihat data berdasarkan kategori produk juga bisa membantu memahami apakah ada jenis produk tertentu yang cenderung memiliki biaya pengiriman lebih tinggi daripada yang lain.

### Pertanyaan 2: Bagaimana pola distribusi harga produk di platform e-commerce? Apakah mayoritas produk memiliki harga yang relatif rendah?

Jawaban :

Berdasarkan dari histogram distribusi harga produk di platform e-commerce pada gambar sebelumnya, terlihat bahwa mayoritas produk memiliki harga yang relatif rendah. Grafik menunjukkan bahwa sebagian besar produk berada dalam rentang harga yang rendah (di bawah 500), dengan frekuensi yang sangat tinggi dibandingkan dengan harga yang lebih tinggi.

Distribusi ini menunjukkan pola distribusi skewed right (miring ke kanan), di mana jumlah produk yang memiliki harga lebih tinggi semakin sedikit seiring dengan meningkatnya harga. Artinya, hanya sedikit produk yang memiliki harga di atas 1000, dan semakin sedikit lagi yang mencapai harga di atas 3000 atau lebih.

Pola ini mengindikasikan bahwa platform e-commerce lebih banyak menjual produk dengan harga terjangkau, yang kemungkinan besar sesuai dengan preferensi mayoritas pelanggan. Selain itu, adanya ekor panjang dalam distribusi harga menunjukkan bahwa meskipun ada beberapa produk premium dengan harga tinggi, jumlahnya sangat kecil dibandingkan dengan produk berharga rendah.

Dari perspektif bisnis, distribusi ini dapat memberikan wawasan bagi strategi penetapan harga dan pemasaran. Jika mayoritas pelanggan lebih cenderung membeli produk dengan harga rendah, maka strategi promosi dan diskon untuk kategori harga tersebut dapat meningkatkan konversi penjualan. Namun, jika ingin meningkatkan penjualan produk dengan harga tinggi, bisa dilakukan dengan strategi pemasaran yang lebih eksklusif dan targeted terhadap segmen pelanggan yang lebih spesifik.

**Insight:**
- xxx
- xxx
"""