import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import streamlit as st

st.title("Milestone 1")
st.write("Muhamad Bagus Septian - FTDS Batch 13")

df = pd.read_csv("df_ads.csv")

@st.cache
def load_data(df):
    df = pd.read_csv("df_ads.csv")
    return df

data = load_data(df)

selected = st.sidebar.selectbox("Page", ("Data Visualisation", "Statistical Analysis"))

if selected == "Data Visualisation":
    st.title("Data Visualisation")

    col_1, col_2 = st.columns(2)

    with col_1 :
        st.subheader("Grafik Jenis Iklan")
        fig, ax = plt.subplots()
        sns.barplot(x=data["ad_type"].value_counts(), y=data["ad_type"].value_counts().index, orient="h")
        sns.set()
        st.pyplot(fig)

    with col_2 :
        st.subheader("Grafik Output Iklan")
        fig1, ax1 = plt.subplots()
        sns.barplot(data=data, x="average_impressions", y="ad_type", orient="h")
        st.pyplot(fig1)

    col_3, col_4 = st.columns(2)

    with col_3 :
        st.subheader("Grafik Lama Iklan")
        fig2, ax2 = plt.subplots()
        sns.barplot(data=data, x="num_of_days", y="ad_type", orient="h")
        st.pyplot(fig2)

    with col_4 :
        st.subheader("Grafik Biaya Iklan")
        fig3, ax3 = plt.subplots()
        sns.barplot(data=data, x="monthly_spend", y="ad_type", orient="h")
        st.pyplot(fig3)

    st.subheader("Grafik perbandingan biaya dan output iklan")

    tipe = st.selectbox(label="Pilih jenis iklan", options=list(data["ad_type"].unique()))

    fig4, ax4 = plt.subplots()
    sns.scatterplot(data=data[data["ad_type"]==tipe], x='average_impressions',y='num_of_days', ax=ax4)
    st.pyplot(fig4)

else :
    st.title("Statistical Analysis")
    st.subheader("Analisis Statistik Deskriptif")
    st.write("Peneliti melakukan analisis statistik desktiptif untuk melihat gambaran keseluruhan iklan di Google Ads")

    num_columns = data.select_dtypes(include=np.number).columns.tolist()

    data_mean = data[num_columns].mean().rename('mean')
    data_median = data[num_columns].median().rename('median')
    data_mode = data[num_columns].mode().iloc[0].rename('mode')

    central_tendency = pd.concat([data_mean, data_median, data_mode], axis=1)
    central_tendency

    modus = {"Label" :["advertiser_name", "ad_type", "impressions_range"], "Mode" : ["TURNING POINT USA, NFP", "VIDEO", "0-1000"]}
    modus = pd.DataFrame(modus)
    modus

    col_5, col_6, col_7 = st.columns(3)

    with col_5 :
        st.write("Grafik distribusi output")
        fig5, ax5 = plt.subplots()
        impress = data['average_impressions']
        density = stats.gaussian_kde(impress)
        n, x, _ = plt.hist(impress, histtype='step', bins=25)  
        plt.plot(x, density(x)*7)
        plt.axvline(impress.mean(), color='magenta', linestyle='dashed', linewidth=2)
        plt.axvline(impress.median(), color='green', linestyle='dashed', linewidth=2)
        plt.show()
        st.pyplot(fig5)

    with col_6 :
        st.write("Grafik distribusi lama iklan")
        fig6, ax6 = plt.subplots()
        days = data['num_of_days']
        density = stats.gaussian_kde(impress)
        n, x, _ = plt.hist(days, histtype='step', bins=25)  
        plt.plot(x, density(x)*7)
        plt.axvline(days.mean(), color='magenta', linestyle='dashed', linewidth=2)
        plt.axvline(days.median(), color='green', linestyle='dashed', linewidth=2)
        plt.show()
        st.pyplot(fig6)

    with col_7 :
        st.write("Grafik distribusi biaya")
        fig7, ax7 = plt.subplots()
        spend = data['monthly_spend']
        density = stats.gaussian_kde(impress)
        n, x, _ = plt.hist(spend, histtype='step', bins=25)  
        plt.plot(x, density(x)*7)
        plt.axvline(spend.mean(), color='magenta', linestyle='dashed', linewidth=2)
        plt.axvline(spend.median(), color='green', linestyle='dashed', linewidth=2)
        plt.show()
        st.pyplot(fig7)

    st.write("Berdasarkan analisis central tendency diketahui :")
    st.write("- Rata-rata iklan di Google Ads mendapatkan impression selama 17 hari")
    st.write("- Nilai tengah iklan di Google Ads mendapatkan impression adalah 5 hari")
    st.write("- Lama iklan paling sering mendapatkan impression adalah selama 1 hari")
    st.write("- Rata-rata penegeluaran per bulan yang diperlukan untuk memasang iklan di Google Ads adalah \$ 510406.8")
    st.write("- Nilai tengah pengeluaran per bulan yang diperlukan untuk memasang iklan di Google Ads adalah \$ 2400.0")
    st.write("- Pengeluaran per bulan yang paling sering diperlukan untuk memasang iklan di Google Ads adalah \$ 400.0")
    st.write("- Rata-rata impression yang didapat iklan yang di pasang di Google Ads adalah sebesar 173265 kali")
    st.write("- Nilai tengah jumlah impression yang didapat iklan yang di pasang di Google Ads adalah sebesar 500 kali")
    st.write("- Impression paling sering yang didapatkan iklan yang dipasang di Google Ads adalah sebesar 500 kali")
    st.write("- Pengiklan yang paling sering memasang iklan adalah TURNING POINT USA, NFP")
    st.write("- Jenis iklan yang paling sering dipasang di Google Ads adalah video")
    st.write("- Rentang impression yang paling sering didapat di Google Ads adalah 0-1000 kali")

    st.subheader("Analisis Statistik Inferensial")
    st.write("Diketahui jenis iklan termurah adalah iklan jenis image dan alternatif termurah ke dua adalah iklan jenis video. Peneliti ingin melakukan hipotesis apakah terdapat perbedaan yang signifikan pada rata-rata pengeluaran dari kedua jenis iklan tersebut.")

    image = data[data["ad_type"]=="IMAGE"][["monthly_spend"]]
    video = data[data["ad_type"]=="VIDEO"][["monthly_spend"]]

    st.write("Rata-rata pengeluaran jenis iklan jenis image adalah $ {}".format(np.round(image["monthly_spend"].mean())))
    st.write("Rata-rata pengeluaran jenis iklan jenis video adalah $ {}".format(np.round(video["monthly_spend"].mean())))

    st.write("Berdasarkan temuan tersebut maka peneliti akan merumuskan hipotesis sebagai berikut :")
    st.write("**H0: μ_image = μ_video**")
    st.write("**H1: μ_image != μ_video**")

    st.write("Hasil perhitungan statistik :")
    t_stat, p_val = stats.ttest_ind(image["monthly_spend"],video["monthly_spend"])
    st.write('P-value: {}'.format(p_val))
    st.write('t-statistics: {}'.format(t_stat))

    st.write("Grafik uji hipotesis")
    st.image("output.png")
    
    st.write("Berdasarkan uji hipotesis testing diketahui nilai p > α, berati H0 gagal ditolak. Oleh karena itu dapat disimpulkan bahwa tidak terdapat perbedaan yang signifikan antara mean image dan mean video.")
    st.write("Karena secara hasil uji hipotesis tidak terdapat perbedaan yang signifikan maka peneliti mengusulkan untuk menggunakan iklan dengan jenis image")

    st.write("Peneliti akan menggunakan analisis confidence interval untuk mengetahui estimasi biaya yang akan dikeluarkan untuk memasang iklan jenis image")

    st.write("Hasil analisis confidence interval")
    z = stats.norm.ppf(0.975)
    margin_error = z*image["monthly_spend"].std()/np.sqrt(len(image))

    ci_lower = image["monthly_spend"].mean() - margin_error
    ci_upper = image["monthly_spend"].mean() + margin_error

    st.write(f"Batas bawah confidence interval adalah {np.round(ci_lower)}")
    st.write(f"Batas atas confidence interval adalah {np.round(ci_upper)}")

    st.write("Grafik analisis confidence interval")
    st.image("ci.png")

    st.write("Berdasarkan hasil analisis dengan confidence interval maka diperkirakan dengan 95% keyakinan bahwa biaya per bulan yang dibutuhkan untuk memasang iklan dengan jenis image pada Google Ads berkisar antara \$ 45671.0   hingga  \$ 47943.0 ")

    st.subheader("Kesimpulan")
    st.write("Berdasarkan hasil eksplorasi data ditemukan :")
    st.write("- Terdapat tiga jenis iklan yang dipasang di Google Ads yaitu **text**, **image** dan **video**. Dari ketiga jenis iklan tersebut yang paling sering dipasang adalah jenis iklan **video**")
    st.write("- Jenis iklan dengan rata-rata impression paling banyak adalah iklan dengan jenis **image**.")
    st.write("- Jenis iklan dengan rata-rata lama mendapatkan impressions terbanyak adalah iklan dengan jenis **image**.")
    st.write("- Jenis iklan dengan biaya rata-rata paling murah adalah iklan dengan jenis **image**.")
    st.write("- Diketahui terdapat dua jenis iklan yang mendapatkan impression terbanyak adalah iklan jenis **video** dan **image**. Namun terdapat iklan dengan jenis **image** yang memerlukan biaya lebih murah dari pada iklan dengan jenis **video**.")

    st.write("Dari hasil eksplorasi data tersebut dapat disimpulkan bahwa memasang iklan dengan tipe image adalah strategi kampanye yang paling baik. Meskipun demikian diperlukan analisis lebih lanjut untuk dapat memberikan usulan yang lebih matang.")
    st.write("Berdasarkan hasil analisis statistik deskriptif :")
    st.write("- Rata-rata iklan di Google Ads mendapatkan impression selama 17 hari")
    st.write("- Nilai tengah iklan di Google Ads mendapatkan impression adalah 5 hari")
    st.write("- Lama iklan paling sering mendapatkan impression adalah selama 1 hari")
    st.write("- Rata-rata penegeluaran per bulan yang diperlukan untuk memasang iklan di Google Ads adalah $ 510406.8")
    st.write("- Nilai tengah pengeluaran per bulan yang diperlukan untuk memasang iklan di Google Ads adalah $ 2400.0")
    st.write("- Pengeluaran per bulan yang paling sering diperlukan untuk memasang iklan di Google Ads adalah $ 400.0")
    st.write("- Rata-rata impression yang didapat iklan yang di pasang di Google Ads adalah sebesar 173265 kali")
    st.write("- Nilai tengah jumlah impression yang didapat iklan yang di pasang di Google Ads adalah sebesar 500 kali")
    st.write("- Impression paling sering yang didapatkan iklan yang dipasang di Google Ads adalah sebesar 500 kali")
    st.write("- Pengiklan yang paling sering memasang iklan adalah TURNING POINT USA, NFP")
    st.write("- Jenis iklan yang paling sering dipasang di Google Ads adalah video")
    st.write("- Rentang impression yang paling sering didapat di Google Ads adalah 0-1000 kali")

    st.write("Dari hasil analisis statistik deskriptif diketahui bahwa rata-rata lama iklan mendapatkan impression untuk iklan dengan jenis image yaitu 35 hari. Sedangkan rata-rata keseluruhan lama iklan mendapat impression adalah 17 hari. Oleh karena itu dapat disimpulkan bahwa rata-rata lama iklan jenis image lebih besar dari rata-rata iklan keseluruhan.")
    st.write("Selain itu rata-rata biaya yang diperlukan untuk memasang iklan dengan jenis image sebesar \$ 46807.0 juga lebih kecil dari rata-rata biaya pemasangan iklan keseluruhan yaitu \$ 510406.8. Terakhir rata-rata impression untuk iklan jenis image sebesar 1353905 kali juga lebih besar dari rata-rata impression iklan keseluruhan yaitu sebesar 173265 kali.")

    st.write("Pada hasil uji hipotesis untuk membandingkan dua iklan dengan biaya yang paling murah yaitu iklan dengan jenis image dan juga jenis video tidak ditemukan perbedaan yang signifikan sehingga dengan mempertimbangankan temuan analisis yang sudah dilakukan sebelumnya, maka strategi kampanye yang paling efektif di Google Ads adalah dengan menggunakan iklan dengan jenis image. Selain itu dari hasil analisis yang sudah dilakukan peneliti menemukan estimasi biaya per bulan yang diperlukan untuk memasang data dengan jenis image berkisar antara \$ 45671.0   hingga  \$ 47943.0")