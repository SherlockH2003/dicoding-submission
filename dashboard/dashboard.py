import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mp

st.caption("Dicoding Indonesia 2024")
# judulnya
st.title("Proyek Data Analyst Dicoding")
st.markdown(
    """
    ### Nama        : Farhan Abyan Putra Karim
    ### Email       : 2210631250049@student.unsika.ac.id
    ### Dicoding-ID : sherlockh2003
    """
)

# Untuk baca CSV
fileDay = pd.read_csv("../dashboard/day.csv")
fileHour = pd.read_csv("../dashboard/hour.csv")

tab1, tab2= st.tabs(["Day", "Hour"])

# tab1 untuk day.csv
with tab1 :
    # Show raw data
    st.write("Raw Data : day.csv")
    st.write(fileDay)
    
# tab2 untuk hour.csv
with tab2 :
    # Show raw data
    st.write("Raw Data : day.csv")
    st.write(fileHour)

with st.container():
    st.write("#### Last Rent : 12 Dec 2012")
    st.write(fileDay.tail())


with st.container():
    # Data tahunan
    st.markdown("### Data sewa sepeda tahunan (per bulan)")
    
    mp.figure(figsize=(10, 6))

    order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    fileDay['month'] = pd.Categorical(fileDay['month'], categories=order, ordered=True)

    mp.figure(figsize=(12, 6))
    mp.title('Rental per Month')

    casual = fileDay.groupby('month')['casual'].sum()
    registered = fileDay.groupby('month')['registered'].sum()

    mp.bar(casual.index, casual.values, label='Casual')
    mp.bar(registered.index, registered.values, bottom=casual.values, label='Registered')

    mp.xlabel('Month')
    mp.xticks(rotation=45)
    mp.ylabel('Number of Rentals')
    mp.legend()
    mp.tight_layout()
    st.pyplot(mp)
    
    st.markdown(
        """
        Pada data diatas, terlihat bahwa selama rentang waktu satu tahun,
        tren penyewaan sepeda selalu naik dari januari hingga juni,
        kemudian stagnan di bulan juni s.d. september,
        dan turun dari september hingga desember.
        \n
        Karena kenaikan itu lah, dapat kita asumsikan bahwa sebagian pengguna
        mendaftar menjadi member kita, untuk mengurangi potensi
        rebutan sepeda pada waktu-waktu aktif (active hour). Karena dari sini pun
        terlihat bahwa rental yang dilakukan oleh member naik drastis pada bulan
        mei hingga oktober.
        """
    )

with st.container() :
    # Data mingguan
    st.markdown( "### Data penyewaan sepeda mingguan (per hari)")
    fileDay['day'] = pd.Categorical(fileDay['day'], categories=[
        'Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday',
        'Saturday'], ordered=True)

    mp.figure(figsize=(12, 6))
    mp.title('Rental per Days')

    casual = fileDay.groupby('day')['casual'].sum()
    registered = fileDay.groupby('day')['registered'].sum()

    mp.bar(casual.index, casual.values, label='Casual')
    mp.bar(registered.index, registered.values, bottom=casual.values, label='Registered')

    mp.xlabel('Days')
    mp.xticks(rotation=45)
    mp.ylabel('Number of Rentals')
    mp.legend()
    mp.tight_layout()
    st.pyplot(mp)
    
    st.markdown(
        """
        Jika dilihat dari sudut pandang harian, peminjaman oleh member terbanyak dipegang oleh
        hari sabtu dan minggu. Sedangkan untuk orang kebanyakan, peminjaman
        ia lakukan pada hari selasa, rabu, dan kamis.
        \n
        Kita dapat simpulkan disini bahwa ada perbedaan motif penyewaan antara member dengan warga
        non-member. motif tersebut bisa didasari oleh tujuan ekonomi, tujuan entertainment, dst. 
        boleh jadi, mereka yang meminjam di hari kerja memang digunakan untuk keperluan kerja,
        sekolah, dan produktif lainnya. Sedangkan peminjam di hari libur, melakukan peminjaman
        untuk fasilitas hiburan.
        """
)

with st.container():    
    st.markdown( "### Data Hubungan Penyewa dengan Temperatur")
    mp.figure(figsize=(12,6)) # biar grafik sebelumnya ga ganggu
    mp.title('Temperature vs Rental')
    temper = fileDay['temperature'] * 41  # Ubah temperatur ke derajat C
    count = fileDay['count']  # banyak sepeda yang dirental

    # judul
    mp.title('Temperature vs Rental')

    # Korelasi
    sb.regplot(
        x=temper,
        y=count,
        scatter=True, 
        line_kws={"color": "orange"} 
    )

    # Labeel
    mp.xlabel("Temperature (in °C)")
    mp.ylabel("Number of bikes rented")
    
    st.pyplot(mp)

    mp.figure(figsize=(12,6))
    mp.title('Felt Temperature vs Rental')
    atemper = fileDay['atemp'] * 50
    count = fileDay['count']
    mp.subplot()
    sb.regplot(
        x=atemper,
        y=count,
        scatter=True, 
        line_kws={"color": "red"} 
    )
    mp.xlabel("Temperature (in °C)")
    mp.ylabel("Number of bikes rented")
    mp.show()
    st.pyplot(mp)
    st.markdown(
        """
        Jika dilihat dari sini, terlihat bahwa terdapat korelasi yang bersesuaian antara data
        cuaca dengan penyewaan sepeda. Pada grafik terlihat bahwa titik data mengikuti garis
        regresi linear meskipun tersimpang agak cukup jauh. Hal ini bisa menyimpulkan bahwa sebagian
        besar masyarakat portugal senang menyewa sepeda saat temperatur cuaca menunjukkan angka 15°C dan 30°C.
        2 jenis cluster data ini bisa menunjukkan perbedaan motif penyewaan juga. Cluster 15°C, bisa diasumsikan
        melakukan sewa sepeda karena suhunya sedang sejuk. Sedangkan cluster 30°C justru menyewa
        sepeda karena cuaca sedang panas. Entah mereka menyewa karena ingin berolahraga di musim panas,
        atau mereka ingin menyewa sepeda justru supaya cepat bermobilisasi.
        """
)
    
