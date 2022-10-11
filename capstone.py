pip install plotly

import streamlit as st
import pandas as pd
import plotly as pl

st.set_page_config(layout="wide")

st.title("e-Commerce Indonesia di Kala Pandemi")
c1a, c1b = st.columns(2)
with c1a:
    st.markdown("<div style='text-align: justify;'>"
        + "<p>Pandemi Covid-19 mempengaruhi sebagian besar kegiatan bisnis mulai dari kegiatan operasional, "
        + "pemasaran dan penjualan, serta cara kita berkomunikasi dengan customer. Permintaan dan kebutuhan customer juga terus berubah secara dinamis. "
        + "Menurut IdEA, penjualan e-commerce meningkat 25% selama pandemi. Volume transaksi meningkat hingga 78% dibandingkan tahun 2019. Pertumbuhan e-commerce "
        + "mendadak meningkat berkali-kali lipat dibandingkan yang diprediksi. Ini merupakan kesempatan yang dapat dimanfaatkan pelaku bisnis khususnya bisnis online, "
        + "tetapi juga menjadi tantangan yang perlu diantisipasi. Pebisnis harus bisa secara jeli melihat peluang dari pertumbuhan ini dan melakukan inovasi untuk "
        + "beradaptasi serta mengembangkan bisnisnya.</p>"
        + "</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>"
        + "<p>Berdasarkan data yang dimuat oleh iprice terlihat bahwa Tokopedia dan Shopee menjadi "
        + "<i>marketplace</i> yang paling banyak dikunjungi di indonesia dalam beberapa kuartal terakhir. "
        + "Meskipun sejak kuartal pertama tahun 2020 kita dilanda pandemi COVID-19, "
        + "Tokopedia dan Shopee ternyata mampu meningkatkan kunjungan situsnya dalam beberapa peride terakhir. Bahkan, kedua <i>marketplace</i> ini mampu meraih "
        + "kunjungan melebih 80% dari kelima <i>marketplace</i> tersebut pada kuartal pertama tahun 2022. Peningkatan ini tentunya sejalan dengan "
        + "perubahan pola konsumsi masyarakat yang beralih ke pembelian daring akibat adanya kebijakan pemerintah terkait penanganan pandemi. "
        + "Selain itu, inovasi dari <i>marketplace</i> juga mendorong minat para konsumen untuk melakukan transaksi di <i>marketplace</i> tersebut.</p>"
        + "</div>", unsafe_allow_html=True)
    
with c1b:
    df1 = pd.read_csv("marketplace_web_visits.csv")
    #filter_1 = st.select_slider("Pilih Periode", ["Q1 2019","Q2 2019","Q3 2019","Q4 2019",
    #                                              "Q1 2020","Q2 2020","Q3 2020","Q4 2020",
    #                                              "Q1 2021","Q2 2021","Q3 2021","Q4 2021",
    #                                              "Q1 2022"])
    #df1_filter = df1['period' == filter_1]
    #st.bar_chart(data = df1_filter, x = "period")
    st.markdown("**Gambar 1. Banyaknya kunjungan situs 5 besar marketplace, Q4 2019 - Q1 2022**")
    st.line_chart(data = df1, x = "period")
    st.markdown("_sumber: https://iprice.co.id/insights/mapofecommerce/en/_")


st.markdown('''---''')
st.subheader("Dampak Pandemi COVID-19 terhadap Usaha e-Commerce")
c2a, c2b = st.columns(2)
with c2a:
    category_1 =['Meningkat','Sama','Menurun']
    values_1 = [9.72,17.89,72.39]
    
    fig_1 = pl.graph_objects.Figure(
        pl.graph_objects.Pie(
            labels = category_1,
            values = values_1,
            hoverinfo = "label+percent",
            textinfo = "value"
        )
    )
    
    fig_1.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))
    
    st.markdown("**Gambar 2. Persentase Usaha e-Commerce menurut Dampak Pandemi COVID-19 terhadap Pendapatan Usaha, Tahun 2021**")
    st.plotly_chart(fig_1)
    st.markdown("_sumber: BPS, Statistik e-Commerce Tahun 2021_")
    
with c2b:
    st.markdown("<div style='text-align: justify;'>"
        + "<p>Meskipun terjadi peningkatan kunjungan situs top <i>marketplace</i> di Indonesia, "
        + "ternyata hasil Survei Statistik <i>e-Commerce</i> tahun 2021 yang diselenggarakan oleh Badan Pusat Statistik "
        + "menunjukkan bahwa sekitar 72,39 persen pelaku usaha <i>e-commerce</i> mengeluh berkurangnya pendapatan mereka. "
        + "Mayoritas pelaku usaha <i>e-commerce</i> mengatakan bahwa penurunan pendapatan berada pada rentang 50-75% dibandingkan tahun 2020.</p>"
        + "</div>", unsafe_allow_html=True)
    
    st.caption("Mengapa ini bisa terjadi?")
    
    st.markdown("<div style='text-align: justify;'>"
        + "<p>Keluhan pelaku <i>e-commerce</i> yang tidak sejalan dengan jumlah kunjungan top <i>marketplace</i> tentunya "
        + "menjadi pertanyaan bagian sebagian orang. Untuk menjawabnya tentuk perlu kita lihat bagaimana profil dari pelaku usaha "
        + "<i>e-commerce</i> yang ada di Indonesia</p>"
        + "</div>", unsafe_allow_html=True)
    
    
    st.markdown("<div style='text-align: justify;'>"
        + "<p><i>Organization for Economic Co-Operation an Development</i> (OECD, 2019) mendefinisikan <i>e-commerce</i> "
        + "adalah penjualan atau pembelian barang dan jasa yang dilakukan melalui jaringan komputer dengan metode yang secara spesifik dirancang "
        + "untuk tujuan menerima dan melakukan pesanan. Dengan kata lain, <i>e-commerce</i> tidak hanya terbatas pada transaksi melalui <i>marketplace</i> "
        + "tetapi juga dapat dilakukan menggunakan media situs usaha, ekstranet maupun EDI (<i>Electronic Data Interchange</i>), <i>e-mail</i>, "
        + "media sosial (Facebook, Instagram, dan lainnya), serta <i>instant messaging</i> (Whatsapp, LINE, dan lainnya). Tidak termasuk "
        + "pemesanan yang dibuat melalui telepon dan faksimile.</p>"
        + "</div>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align: justify;'>"
        + "<p><b>Jadi, <i>e-commerce</i> sebenarnya tidak hanya terbatas pada transaksi melalui <i>marketplace</i> saja, tetapi mencakup seluruh yang dilakukan melalui jaringan komputer.</b></p>"
        + "</div>", unsafe_allow_html=True)
    
st.markdown('''---''')
st.subheader("Profil e-Commerce Indonesia")

filter_2 = st.selectbox("Berdasarkan", ["Total Pendapatan e-Commerce",
                                            "Metode Pembayaran",
                                            "Usia Pemilik/Penanggungjawab",
                                            "Pendidikan Terakhir Pemilik/Penanggungjawab",
                                            "Kategori Lapangan Usaha",])

category_2 = ["","","",""]
values_2 = [0,0,0,0]

if filter_2 == 'Total Pendapatan e-Commerce':
    category_2 = ['<300 juta', '300 juta - 2,5 miliar', '2,5 - 50 miliar', '>50 miliar'],
    values_2 = [83.87, 13.85, 2.09, 0.19]
elif filter_2 == 'Metode Pembayaran':
    category_2 = ['Kartu','e-Wallet','Transfer Bank','COD'],
    values_2 = [0.52,4.43,16.33,78.72]
elif filter_2 == 'Usia Pemilik/Penanggungjawab':
    category_2 = ['15-24 tahun','25-34 tahun','35-44 tahun', '45-54 tahun', 'lebih dari 55 tahun'],
    values_2 = [6.13,24.79,33.07,24.31,11.70]
elif filter_2 == 'Pendidikan Terakhir Pemilik/Penanggungjawab':
    category_2 = ['SMA/SMK sederajat ke bawah','Diploma I/II/III', 'Diploma IV/S1', 'S2/S3'],
    values_2 = [75.36,6.06,17.22,1.36]
else:
    category_2 = ['G Perdagangan dan Reparasi','C Industri Pengolahan','Akomodasi & Makan Minum', 'Lainnya'],
    values_2 = [46.05,17.1,15.81,(100-46.05-17.1-15.81)]
    
fig_2 = pl.graph_objects.Figure(
    pl.graph_objects.Pie(
        labels = category_2,
        values = values_2,
        hoverinfo = "label+percent",
        textinfo = "value"
    )
)
    
st.plotly_chart(fig_2)
st.markdown("_sumber: BPS, Statistik e-Commerce Tahun 2021_")

st.markdown("<div style='text-align: justify;'>"
    + "<p>Pada tahun 2021, BPS memperkirakan jumlah <i>e-commerce</i> di Indonesia mencapai 2,361 juta usaha. Sebagian besar "
    + "pelaku usaha merupakan usaha <i>e-commerce</i> non-formal, dengan ciri-ciri:</p>"
    + "<ul>"
    + "<li>Mayoritas menggunakan <i>instant messaging</i> dan media sosial sebagai media penjualan, hanya 21,64 persen usaha yang menggunakan marketplace</li>"
    + "<li>Nilai pendapatan total dari <i>e-commerce</i> di bawah 300 juta rupiah</li>"
    + "<li>Metode pembayaran yang paling sering digunakan yaitu <i>Cash on Delivery</i> (COD) atau pembayaran secara tunai</li>"
    + "<li>Mayoritas pemilik/penanggung jawab <i>e-commerce</i> berusia 35-44 tahun</li>"
    + "<li>75,36 persen pemilik/penanggung jawab <i>e-commerce</i> berpendidikan SMA/SMK sederajat ke bawah</li>"
    + "<li>Usaha yang dilakukan dalam <i>e-commerce</i> di dominasi oleh sektor perdagangan</li>"
    + "</ul>"
    + "</div>", unsafe_allow_html=True)

st.markdown('''---''')
st.subheader("Kesimpulan")
st.markdown("<div style='text-align: justify;'>"
    + "<p>Meskipun terdapat peningkatan kunjungan pada top <i>marketplace</i> ternyata belum mampu menyentuh pemulihan "
    + "ekonomi dari seluruh pelaku <i>e-commerce</i>. Hal ini wajar mengingat hanya 21,36 persen pelaku usaha yang menggunakan <i>marketplace</i> "
    + "sementara sebagian besar masih menggunakan <i>instant messaging</i> dan media sosial sebagai media penjualan, serta sebagian besar merupakan Usaha Mikro, Kecil, dan Menengah (UMKM) "
    + "karena pendapatannya yang bernilai dibawah 300 juta. "
    + "Program digitalisasi ekonomi tentunya perlu didorong dengan pengembangan UMKM kita sebab  tanpa dukungan kita, mereka belum tentu mampu "
    + "menyaingi perusahaan besar di <i>marketplace</i> yang sudah memiliki <i>rating</i> dan <i>history transaksi</i> yang terpercaya di mata pembeli. "
    + "Dalam konteks ini strategi pemasaran dari produk UMKM yang efektif diharapkan mampu mendorong peningkatan transaski jual-beli mereka.</p>"
    + "</div>", unsafe_allow_html=True)
    
st.markdown('''---''')
st.subheader("Referensi")
st.text("BPS. 2021. Statistik e-Commerce Tahun 2021. Jakarta.")
st.text("iPrice. 2022. Find Out E-commerce Competition in Indonesia. https://iprice.co.id/insights/mapofecommerce/en/. diakses 12 Oktober 2022 pukul 01.24 WIB.")
st.text("OECD. 2022. Electronic Commerce. https://stats.oecd.org/glossary/detail.asp?ID=4721. diakses 12 Oktober 2022 pukul 1.25 WIB")
