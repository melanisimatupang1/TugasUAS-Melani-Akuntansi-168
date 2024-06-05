
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari CSV dengan separator ';'
df = pd.read_csv('data_penjualan.csv', sep=';')
print(df.columns)  # Untuk memeriksa nama kolom

#Melihat data frame
print(df.head())


# Total penjualan per kota
total_sales_per_city = df.groupby('Produk')['Jumlah Terjual'].sum().reset_index()

# Mengatur gaya seaborn
sns.set(style="whitegrid")

# Grafik total penjualan per jenis pelanggan
plt.figure(figsize=(10, 6))
sns.barplot(x='Produk', y='Jumlah Terjual', data=total_sales_per_city,  palette='viridis')
plt.title('Total Sales per Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Total Sales')
plt.show()

# Grafik total penjualan per kota
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Sales', data=total_sales_per_city, palette='viridis')
plt.title('Total Sales per City')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.show()

# Grafik total profit per kota
plt.figure(figsize=(6, 4))
sns.barplot(x='City', y='Profit', data=total_profit_per_city, palette='viridis')
plt.title('Total Profit per City')
plt.xlabel('City')
plt.ylabel('Total Profit')
plt.show()

# Visualisasi Profit per Jenis Pelanggan
plt.figure(figsize=(6, 4))
sns.barplot(x='Customer_Type', y='Profit', data=total_profit_per_customer_type, palette='viridis')
plt.title('Profit per Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Profit')
plt.show()