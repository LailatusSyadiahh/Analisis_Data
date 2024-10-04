import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set Seaborn style
sns.set(style='dark')

# Load the dataset
data = pd.read_csv("data/day.csv")

# Ensure 'dteday' is a datetime column
data['dteday'] = pd.to_datetime(data['dteday'])

# Helper functions
def create_weather_effects_df(df):
    return df.groupby('weathersit').agg({'cnt': 'mean'}).reset_index()

def create_weekday_weekend_df(df):
    df['is_weekend'] = df['weekday'].apply(lambda x: 1 if x in [5, 6] else 0)
    return df.groupby('is_weekend').agg({'cnt': 'mean'}).reset_index()

def create_daily_sales_df(df):
    return df.groupby('dteday').agg({'cnt': 'sum'}).reset_index()

# Create DataFrames for visualizations
weather_effects_df = create_weather_effects_df(data)
weekday_weekend_df = create_weekday_weekend_df(data)
daily_sales_df = create_daily_sales_df(data)

# Header for the dashboard
st.header('Bike Rental Analysis Dashboard :sparkles:')

# Visualization 1: Weather Effects on Bike Rentals
st.subheader('Weather Effects on Bike Rentals')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_effects_df, palette='Blues', ax=ax)
ax.set_title('Average Bike Rentals by Weather Situation', fontsize=20)
ax.set_xlabel('Weather Situation', fontsize=14)
ax.set_ylabel('Average Rentals', fontsize=14)
st.pyplot(fig)

# Conclusions about weather
st.markdown("""
**Conclusion:**
1. **Cuaca Cerah**: Penyewaan sepeda paling tinggi terjadi pada cuaca cerah atau berawan ringan, dengan rata-rata penyewaan mencapai 4,876 sepeda per hari.
2. **Cuaca Berkabut dan Mendung**: Penyewaan menurun ketika cuaca berkabut atau mendung, dengan rata-rata 4,035 sepeda per hari.
3. **Cuaca Buruk**: Pada cuaca hujan ringan atau salju, rata-rata penyewaan turun drastis menjadi 1,803 sepeda.
4. **Kesimpulan**: Cuaca cerah berperan besar dalam meningkatkan jumlah penyewaan sepeda, sedangkan cuaca buruk sangat menghambat penyewaan.
""")

# Visualization 2: Weekday vs Weekend Rentals
st.subheader('Bike Rentals: Weekday vs Weekend')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='is_weekend', y='cnt', data=weekday_weekend_df, palette='Oranges', ax=ax)
ax.set_xticklabels(['Weekday', 'Weekend'])
ax.set_title('Average Bike Rentals: Weekday vs Weekend', fontsize=20)
ax.set_xlabel('Day Type', fontsize=14)
ax.set_ylabel('Average Rentals', fontsize=14)
st.pyplot(fig)

# Conclusions about weekday and weekend rentals
st.markdown("""
**Kesimpulan:**
1. **Hari Kerja**: Rata-rata penyewaan sepeda pada hari kerja mencapai 193 sepeda per hari.
2. **Akhir Pekan**: Pada akhir pekan, rata-rata penyewaan sedikit lebih rendah, yaitu 181 sepeda per hari.
3. **Kesimpulan**: Meskipun terdapat lebih banyak penyewaan pada hari kerja dibandingkan akhir pekan, perilaku penyewaan pada akhir pekan tetap menunjukkan minat yang baik.
""")

# Visualization 3: Total Daily Rentals Over Time
st.subheader('Total Daily Bike Rentals Over Time')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='dteday', y='cnt', data=daily_sales_df, marker='o', color='green', ax=ax)
ax.set_title('Total Daily Bike Rentals Over Time', fontsize=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Total Rentals', fontsize=14)
plt.xticks(rotation=45)
st.pyplot(fig)

# Conclusions about daily rentals
st.markdown("""
**Kesimpulan:**
1. **Tren Penjualan**: Grafik menunjukkan total penyewaan sepeda per hari. Anda dapat melihat puncak permintaan yang terjadi pada hari-hari tertentu.
2. **Musiman**: Analisis lebih lanjut dapat dilakukan untuk mengidentifikasi pola musiman atau pengaruh faktor eksternal.
""")

st.caption('Copyright (c) Lailatus Syadiah')


