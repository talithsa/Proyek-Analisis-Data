import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

hour_df = pd.read_csv('data/hour.csv')
day_df = pd.read_csv('data/day.csv')

def create_temp_df(df):
    temp_df = df.groupby('temp')['cnt'].mean().reset_index()
    return temp_df

def create_hum_df(df):
    hum_df = df.groupby('hum')['cnt'].mean().reset_index()
    return hum_df

def create_wind_df(df):
    wind_df = df.groupby('windspeed')['cnt'].mean().reset_index()
    return wind_df

def create_weekday_df(df):
    weekday_df = df.groupby('workingday')['cnt'].mean().reset_index()
    return weekday_df

def create_hour_df(df):
    hour_df = df.groupby('hr')['cnt'].mean().reset_index()
    return hour_df

temp_df = create_temp_df(hour_df)
hum_df = create_hum_df(hour_df)
wind_df = create_wind_df(hour_df)
weekday_df = create_weekday_df(hour_df)
hour_df = create_hour_df(hour_df)

st.title("Analisis Data 🚲 Bike Sharing Dataset")
st.caption("By Talitha Husna Salsabila")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])

with st.sidebar:
    st.subheader("Pilih Rentang Waktu Analisis Data")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=day_df['dteday'].min(),
        max_value=day_df['dteday'].max(),
        value=[day_df['dteday'].min(), day_df['dteday'].max()]
    )

st.subheader("⛅ Pengaruh Cuaca Terhadap Penggunaan Sepeda")
col1, col2, col3 = st.columns(3)
with col1:
    fig_temp = plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=temp_df)
    plt.title('Pengaruh Suhu terhadap Jumlah Pengguna Sepeda')
    plt.xlabel('Suhu')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig_temp)
with col2:
    fig_hum = plt.figure(figsize=(10, 6))
    sns.scatterplot(x='hum', y='cnt', data=hum_df)
    plt.title('Pengaruh Kelembaban terhadap Jumlah Pengguna Sepeda')
    plt.xlabel('Kelembaban')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig_hum)
with col3:
    fig_wind = plt.figure(figsize=(10, 6))
    sns.scatterplot(x='windspeed', y='cnt', data=wind_df)
    plt.title('Pengaruh Kecepatan Angin terhadap Jumlah Pengguna Sepeda')
    plt.xlabel('Kecepatan Angin')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig_wind)

hour_df['workingday'] = hour_df['hr'].apply(lambda x: 1 if x >= 8 and x <= 17 else 0)

st.subheader("🏕️ Pola Penggunaan Sepeda di Hari Kerja vs Hari Libur")
col1, col2 = st.columns(2)
with col1:
    fig_box = plt.figure(figsize=(10, 6))
    sns.boxplot(x='workingday', y='cnt', data=hour_df)
    plt.title('Pola Penggunaan Sepeda di Hari Kerja vs Hari Libur')
    plt.xlabel('Hari Kerja (1: Hari Kerja, 0: Hari Libur)')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig_box)
with col2:
    fig_line = plt.figure(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', hue='workingday', data=hour_df, ci=None)
    plt.title('Pola Penggunaan Sepeda Berdasarkan Jam di Hari Kerja dan Hari Libur')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig_line)

st.subheader("📌 Hasil dan Pembahasan")
st.write("""
- Faktor cuaca, seperti suhu, kelembaban, dan kecepatan angin, secara signifikan memengaruhi penggunaan sistem berbagi sepeda. Suhu yang hangat cenderung meningkatkan jumlah pengguna, sementara kelembaban tinggi dan kecepatan angin yang kuat menurunkan kenyamanan pengguna, yang menyebabkan penurunan jumlah penggunaan sepeda.
- Pola penggunaan sepeda di hari kerja dan hari libur sangat berbeda. Selama jam kerja, terutama di pagi dan sore hari, orang menggunakan sepeda paling banyak, menunjukkan betapa pentingnya untuk pergi ke tempat kerja atau sekolah. Sedangkan di hari libur, bagaimanapun, polanya lebih rata sepanjang hari, menunjukkan bahwa orang lebih banyak menggunakan sepeda untuk rekreasi atau bersantai.
- *Hasil diharapkan dapat membantu pengelolaan operasional dan strategi peningkatan layanan lebih lanjut, berdasarkan faktor cuaca dan pola temporal pengguna.*
""")

st.caption("Proyek Analisis Data - © Bangkit Academy 2024 Batch 2")