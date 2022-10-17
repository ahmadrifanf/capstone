import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.patches import ConnectionPatch

st.set_page_config(layout="wide")
st.image("banner.jpg")

st.title("Bangkitkan e-Commerce Indonesia")
st.caption("oleh: Ahmad RIfan Ferdiyansyah")

c1a, c1b = st.columns([2,1], gap="large")
with c1a:
    st.markdown("Pandemi COVID-19 telah mempengaruhi sebagian kegiatan bisnis mulai dari operasional, pemasaran, penjualan, hingga cara berkomunikasi dengan pelanggan. Situasi ini terbukti mampu mendorong e-commerce nasional. Menurut _Indonesia E-Commerce Assosiation_ (IdEA), penjualan e-commerce mengalami peningkatan sebesar 25% selama pandemi dan volume transaksi meningkat hingga 78% dibanding tahun 2019. Pertumbuhan e-commerce mendadak meningkat berkali-kali lipat dibandingkan yang diprediksi.")
    st.markdown("Meskipun demikian, ternyata hasil Survei Statistik e-Commerce tahun 2021 yang diselenggarakan oleh Badan Pusat Statistik (BPS) menunjukkan bahwa **sekitar 72,39% pelaku usaha e-commerce mengeluhkan pendapatan mereka yang menurun** pada tahun 2021. Mayoritas pelaku usaha e-commerce mengatakan bahwa penurunan pendapatan mereka berada pada rentang 50-75% jika dibandingkan tahun 2020. Kondisi ini masih sama dengan hasil survei tahun sebelumnya, dimana mayoritas pelaku usaha e-commerce juga mengeluhkan penurunan pendapatan akibat pandemi.")
    st.caption("Mengapa ini bisa terjadi?")
    st.markdown("Untuk menjawabnya mari kita lihat terlebih dahulu bagaimana profil dari e-commerce di Indonesia.")
    
with c1b:
    label1 =['Meningkat','Sama','Menurun']
    value1 = [9.72,17.89,72.39]
    explode1 = (0,0,0.1)
    color = plt.get_cmap('RdYlGn_r')(np.linspace(0.3,0.7,len(value1)))
    
    fig1, ax1 = plt.subplots()
    ax1.pie(value1,
            explode = explode1,
            labels = label1,
            autopct = '%1.1f%%',
            #shadow = TRUE,
            startangle = 90,
            colors = color,
            wedgeprops = {"linewidth":1, "edgecolor":"white"})
    ax1.set_title("Proporsi e-Commerce Menurut Dampak Pandemi\nTerhadap Pendapatan Usaha, 2021")
    ax1.set_xlabel("sumber: BPS (diolah)")
    st.pyplot(fig1)

st.markdown('''---''')
st.header("Profil e-Commerce Indonesia")    

st.markdown("_Electronic Commerce_ (e-Commerce) berdasarkan _Organization for Economic Co-Operation and Development_ (OECD, 2009) adalah penjualan atau pembelian barang atau jasa, yang dilakukan melalui jaringan komputer dengan metode yang secara spesifik dirancang untuk tujuan menerima atau melakukan pesanan. Barang atau jasa dipesan dengan metode tersebut, tetapi pembayaran dan pengiriman utama barang atau jasa tidak harus dilakukan secara online. Transaksi e-Commerce mencakup pemesanan melalui halaman website, ekstranet maupun _Electronic Data Interchange_ (EDI), e-mail, media sosial (Facebook, Instagram, dan lainnya), serta _instant messaging_ (WhatsApp, Line, dan lainnya) dan tidak mencakup pemesanan yang dibuat melalui telepon (baik _fixed-line_ maupun _mobile phone_) dan faksimili.")
st.markdown("Berangkat dari definisi tersebut, BPS kemudian memperkirakan jumlah usaha _e-commerce_ di Indonesia yaitu mencapai 2.361.423 usaha. Adapun sebaran usaha _e-commerce_ banyak terdapat di Pulau Jawa, yaitu sekitar 75,15% dari total usaha _e-commerce_. Fenomena ini tentunya berkaitan dengan lokasi yang dekat dengan pusat perekonomian dan ketersediaan fasilitas pendukung usaha seperti akses internet yang memadai.")

st.subheader("Proporsi Usaha e-Commerce Indonesia")

c2a, c2b = st.columns([2,1], gap="large")
with c2a:
    value2 = {'media' : ['website','website','email','email','instant messaging','instant messaging','media sosial','media sosial','marketplace','marketplace'],
           'menggunakan': ['ya','tidak','ya','tidak','ya','tidak','ya','tidak','ya','tidak',],
           'persentase' : [2.38,97.62,10.42,89.58,93.98,6.02,54.66,45.34,21.64,78.36]}
    value2 = pd.DataFrame(value2)

    fig2 = px.bar(value2, x="media", y="persentase", color="menggunakan", title="Berdasarkan Media Penjualan")
    st.plotly_chart(fig2)

with c2b:
    filter3 = st.selectbox('Berdasarkan',
                          ['Total Pendapatan',
                           'Metode Pembayaran Utama',
                           'Usia Pemilik/Penanggungjawab',
                           'Pendidikan Pemilik/Penanggungjawab'])
    
    label3 =[]
    value3 = []
    explode3 = []
    color3 = ""
    
    if(filter3 == 'Total Pendapatan'):
        label3 = ['<300 juta', '300 juta - 2,5 miliar', '>2,5 miliar']
        value3 = [83.87, 13.85, 2.28]
        explode3 = [0.1,0,0]
        color3 = plt.get_cmap('Blues')(np.linspace(0.3,0.7,len(value3)))
    elif(filter3 == 'Metode Pembayaran Utama'):
        label3 = ['Debit/e-Wallet','Transfer Bank','COD']
        value3 = [4.95,16.33,78.72]
        explode3 = [0,0,0.1] 
        color3 = plt.get_cmap('Greens_r')(np.linspace(0.3,0.7,len(value3)))
    elif(filter3 == 'Usia Pemilik/Penanggungjawab'):
        label3 = ['15-24 tahun','25-34 tahun','35-44 tahun', '45-54 tahun', '>55 tahun']
        value3 = [6.13,24.79,33.07,24.31,11.70]
        explode3 = [0,0,0.1,0,0]
        color3 = plt.get_cmap('Oranges')(np.linspace(0.1,0.9,len(value3)))
    else:
        label3 = ['SMA/SMK ke bawah','DI/II/III', 'DIV/S1', 'S2/S3']
        value3 = [75.36,6.06,17.22,1.36]
        explode3 = [0.1,0,0,0]
        color3 = plt.get_cmap('Reds')(np.linspace(0.3,0.7,len(value3)))
    
    fig3, ax3 = plt.subplots()
    ax3.pie(value3,
            explode = explode3,
            labels = label3,
            autopct = '%1.1f%%',
            #shadow = TRUE,
            startangle = 90,
            colors = color3,
            wedgeprops = {"linewidth":1, "edgecolor":"white"})
    ax3.set_title(filter3)
    st.pyplot(fig3)
    
st.caption("sumber: BPS, 2021 (diolah)")
st.markdown("")

st.markdown("Dari grafik tersebut dapat kita simpukan bahwa sebagian besar pelaku usaha merupakan usaha e-commerce non-formal, dengan ciri-ciri:")
st.markdown("1. Mayoritas menggunakan _instant messaging_ dan media sosial sebagai media penjualan")
st.markdown("2. Nilai pendapatan total sebagian besar _e-commerce_ masih di bawah 300 juta rupiah")
st.markdown("3. Metode pembayaran yang paling sering digunakan yaitu _Cash on Delivery_ (COD) atau pembayaran secara tunai")
st.markdown("4. Mayoritas pemilik/penanggung jawab _e-commerce_ berusia 35-44 tahun")
st.markdown("5. 75,36 persen pemilik/penanggung jawab _e-commerce_ berpendidikan SMA/SMK sederajat ke bawah")
st.markdown("Jika kita merujuk pada Undang- Undang Nomor 20 Tahun 2008 tentang Usaha Mikro, Kecil dan Menengah (UMKM) maka dapat dikatakan bahwa e-commerce Indonesia masih didominasi oleh usaha mikro. Oleh sebab itu, untuk mengatasi keluhan penurunan pendapatan pelaku usaha _e-commerce_ harus diterakan kebijakan-kebijakan yang sangat mendukung keberlangsungan usaha mikro. Umumnya, kendala utama dari kegiatan mereka disebabkan oleh karena kurangnya permintaan atas barang dan jasa selama pandemi (48,74%).")
st.markdown("")

c3a, c3b = st.columns(2, gap="large")
with c3a:
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(121)
    ax5 = fig4.add_subplot(122)
    fig4.subplots_adjust(wspace=0)

    ratio4 = [0.08, 0.92]
    label4 = ['Pernah', 'Tidak Pernah']
    explode4 = [0.1, 0]
    
    angle = -180 * ratio4[0]
    ax4.pie(ratio4,
            autopct = '%1.1f%%',
            startangle = angle,
            labels = label4,
            explode = explode4,
            colors = plt.get_cmap('Set2')(np.linspace(0.1,0.9,2)))

    ratio5 = [0.6927, 0.2866, 0.1288]
    label5 = ['Dasar', 'Menengah', 'Ahli']
    width = .2

    ax5.pie(ratio5,
            autopct = '%1.1f%%',
            startangle = angle,
            labels = label5,
            radius = 0.5,
            textprops = {'size': 'smaller'},
            colors = plt.get_cmap('Set1')(np.linspace(0.1,0.9,3)))

    ax4.set_title('Keikutsertaan Pelatihan')
    ax5.set_title('Jenis Pelatihan')

    theta1, theta2 = ax4.patches[0].theta1, ax4.patches[0].theta2
    center, r = ax4.patches[0].center, ax4.patches[0].r

    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(- width / 2, .5), xyB=(x, y),
                        coordsA="data", coordsB="data", axesA=ax5, axesB=ax4)
    con.set_color([0, 0, 0])
    con.set_linewidth(2)
    ax5.add_artist(con)

    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(- width / 2, -.5), xyB=(x, y), coordsA="data",
                        coordsB="data", axesA=ax5, axesB=ax4)
    con.set_color([0, 0, 0])
    ax5.add_artist(con)
    con.set_linewidth(2)
    
    st.pyplot(fig4)

with c3b:
    st.markdown("Tingkat pendidikan yang tidak terlalu tinggi dan rendahnya keikutsertaan dalam pelatihan (25,36%) menjadikan pelaku usaha _e-commerce_ juga akan merasakan kesulitan dalam memasarkan produknya. Bahkan dari pelaku usaha yang telah mendapatkan pelatihan pemanfaatan teknologi informasi, sebagian besar masih berupa pelatihan dasar. Padahal, RedSeer telah memproyeksikan transaksi _e-commerce_ di Indonesia akan terus bertambah dari 67,4 miliar USD pada tahun 2021 menjad 137,5 miliar USD pada tahun 2025. Jika _e-commerce_ dengan usaha skala mikro tidak mampu memanfaatkan kesempatan ini, maka keuntungan tersebut hanya akan dirasakan oleh perusahaan besar saja.")

st.markdown('''---''')
st.subheader("Kesimpulan")
st.markdown("Peningkatan transaksi _e-commerce_ yang terjadi selama pandemi ternyata belum mampu menyentuh seluruh pelaku usaha _e-commerce_. Hal ini tampak dari banyaknya keluhan atas penurunan pendapatan dari para pelaku usaha, khususnya pada skala usaha mikro (pendapatan kurang dari 300 juta setahun). Selain itu, pendidikan pelaku usaha yang tidak terlalu tinggi dan rendahnya keikutsertaan dalam pelatihan menyebabkan mereka kesulitan dalam terus menarik minat konsumen untuk membeli produk mereka. Oleh sebab itu, diperlukan kebijakan perihal _e-commerce_ yang sangat mendukung keberlangsungan usaha mikro.")

st.markdown('''---''')
st.subheader("Saran")
st.markdown("Pengadaan pelatihan bagi pelaku usaha _e-commerce_ skala mikro dapat menjadi salah satu upaya untuk meningkatkan kemampuan pelaku usaha _e-commerce_, khususnya pemberian materi perihal promosi yang efektif dalam memasarkan produk mereka. Selain itu, pendampingan para ahli dalam proses pengembangan usaha juga mungkin diperlukan agar mereka dapat terus bertahan dalam menghadapi era digitalisasi ekonomi yang masih terus berkembang hingga saat ini.")
    
st.markdown('''---''')
st.subheader("Referensi")
st.markdown("_BPS. 2021. Statistik e-Commerce Tahun 2021. Jakarta._")
st.markdown("_iPrice. 2022. Find Out E-commerce Competition in Indonesia. https://iprice.co.id/insights/mapofecommerce/en/. diakses 12 Oktober 2022 pukul 01.24 WIB._")
st.markdown("_OECD. 2022. Electronic Commerce. https://stats.oecd.org/glossary/detail.asp?ID=4721. diakses 12 Oktober 2022 pukul 01.25 WIB._")
st.markdown("_Redseer. 2022. Consumer Internet in Indonesia. https://redseer.com/reports/consumer-internet-in-indonesia/. diakses 18 Oktober 2022 pukul 00.04 WIB._")
