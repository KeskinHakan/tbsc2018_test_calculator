# This app prepared for the test calculation amounts for the TBSC 2018

import pandas as pd
import streamlit as st
import math

st.set_page_config(page_title="Site Test Numbers According to TBSC 2018", page_icon="🖖")
pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)


language = st.sidebar.selectbox("App Language", {"Turkish", "English"})


# Calculation of the Test Amounts.

# Test Results

if language == "English":

    # st.title("Rule Based Classification of Customer's Data")
    st.markdown("<h2 style='text-align: center; color: grey;'>Test Numbers Calculator According to TBSC 2018 </h2>",
                unsafe_allow_html=True)
    """
    This app prepared to calculate the test numbers according to Turkish Building Seismic Code 2018 Chapter 15.

    To use this app please consider the these items below;

        1- Type of Structural System (Concrete or Precast),
        2- Knowledge Level,
        3- Is the project available?,
        4- Typical floor area in m2,
        5- Number of Floors, 
        6- Number of Columns for each story,
        7- Number of Beams for each story,
        8- Number of Shear Wall for each story(If existing)

    After these choices this app will give the minimum test numbers according to TBSC 2018.

    """

    # Inputs for the calculation
    st.sidebar.header("Project Inputs")
    system = st.sidebar.selectbox("Type of Structural System: ", {"Concrete", "Precast"})
    knowledge_level = st.sidebar.selectbox("Knowledge Level: ", {"Limited", "Comprehensive"})
    project = st.sidebar.selectbox("Is the project available?: ", {"Yes", "No"})
    area = st.sidebar.number_input("Typical Floor Area (m2)", value=300, step=1)
    n_of_floors = st.sidebar.number_input("Number of Floors", value=3, step=1)
    n_of_columns = st.sidebar.number_input("Number of Columns for each story", value=15, step=1)
    n_of_beams = st.sidebar.number_input("Number of Beams for each story", value=30, step=1)
    n_of_shear_wall = st.sidebar.number_input("Number of Shear Wall for each story(If existing)", value=3, step=1)
    st.subheader("Test Results")
    if knowledge_level == "Limited":
        min_exp_col = 1
        min_exp_beam = 1
        min_exp_sw = 1
        min_cct_col_sw = 3

        n_of_cct = st.sidebar.number_input("Number of Concrete Core Test for the each Floor", value=4, step=1)

        min_exp_col_code = math.ceil((n_of_columns * 0.05))
        min_exp_sw_code = math.ceil((n_of_shear_wall * 0.05))

        min_cmt_col_code = math.ceil((n_of_columns-min_exp_col_code)*0.20)
        min_cmt_sw_code = math.ceil((n_of_shear_wall - min_exp_sw_code) * 0.20)

        exp_test_col = max(min_exp_col, min_exp_col_code)
        exp_test_sw = max(min_exp_sw, min_exp_sw_code)

        cct_for_floor = max(min_cct_col_sw,n_of_cct)

        st.info("Total Concrete Exposure Test for Columns: " + str(int(exp_test_col*n_of_floors)))
        st.info("Total Concrete Exposure Test for Beams: " + str(int(min_exp_beam * n_of_floors)))
        st.info("Total Concrete Exposure Test for Shear Walls: " + str(int(exp_test_sw*n_of_floors)))

        st.info("Total Cover Meter Test for Columns: " + str(int(min_cmt_col_code*n_of_floors)))
        st.info("Total Cover Meter Test for Shear Walls: " + str(int(min_cmt_sw_code*n_of_floors)))

        st.info("Total Concrete Core Test: " + str(int(cct_for_floor*n_of_floors)))

    else:
        if project == "Yes":
            min_exp_col = 1
            min_exp_beam = 1
            min_exp_sw = 1

            min_cct_col_sw_ground = 3
            min_cct_col_sw_normal = 2


            if system == "Precast":
                min_code_cct = math.ceil(area/600)
                min_cct = 5
            else:
                min_code_cct = math.ceil(area / 400)
                min_cct = 9

            cct_for_ground = max(min_cct_col_sw_ground,min_code_cct)
            cct_for_floor = max(min_cct_col_sw_normal,min_code_cct)
            cct_code = cct_for_ground + cct_for_floor*(n_of_floors-1)

            if min_cct_col_sw_ground < min_code_cct:
                st.info("Total Concrete Core Test for Ground Floor: " + str(min_code_cct))
            else:
                st.info("Total Concrete Core Test for Ground Floor: " + str(min_cct_col_sw_ground))

            if cct_for_floor < min_code_cct:
                st.info("Total Concrete Core Test for Normal Floors: " + str(min_code_cct))
            else:
                st.info("Total Concrete Core Test for Normal Floors: " + str(cct_for_floor))

            if cct_code < min_cct:
                st.info("Total Concrete Core Test: " + str(min_cct))
            else:
                st.info("Total Concrete Core Test: " + str(cct_code))

            min_exp_col_code = math.ceil((n_of_columns * 0.05))
            min_exp_sw_code = math.ceil((n_of_shear_wall * 0.05))

            exp_test_col = max(min_exp_col, min_exp_col_code)
            exp_test_sw = max(min_exp_sw, min_exp_sw_code)

            min_cmt_col_code = math.ceil((n_of_columns-min_exp_col_code)*0.20)
            min_cmt_sw_code = math.ceil((n_of_shear_wall - min_exp_sw_code) * 0.20)
            min_cmt_beam_code = math.ceil((n_of_beams-min_exp_beam) * 0.10)

            st.info("Total Concrete Exposure Test for Columns: " + str(int(exp_test_col * n_of_floors)))
            st.info("Total Concrete Exposure Test for Beams: " + str(int(min_exp_beam * n_of_floors)))
            st.info("Total Concrete Exposure Test for Shear Walls: " + str(int(exp_test_sw * n_of_floors)))

            st.info("Total Cover Meter Test for Columns: " + str(int(min_cmt_col_code * n_of_floors)))
            st.info("Total Cover Meter Test for Columns: " + str(int(min_cmt_beam_code * n_of_floors)))
            st.info("Total Cover Meter Test for Shear Walls: " + str(int(min_cmt_sw_code * n_of_floors)))

        else:
            min_exp_col = 1
            min_exp_sw = 1
            min_exp_beam = 1
            min_cct_col_sw_ground = 3
            min_cct_col_sw_normal = 2

            if system == "Precast":
                min_code_cct = math.ceil(area/600)
                min_cct = 5
            else:
                min_code_cct = math.ceil(area / 400)
                min_cct = 9

            min_exp_col_code = math.ceil((n_of_columns * 0.1))
            min_exp_sw_code = math.ceil((n_of_shear_wall * 0.1))

            min_cmt_col_code = math.ceil((n_of_columns-min_exp_col_code)*0.30)
            min_cmt_sw_code = math.ceil((n_of_shear_wall - min_exp_sw_code) * 0.30)
            min_cmt_beam_code = math.ceil((n_of_beams-min_exp_beam) * 0.15)

            exp_test_col = max(min_exp_col, min_exp_col_code)
            exp_test_sw = max(min_exp_sw, min_exp_sw_code)


            cct_for_ground = max(min_cct_col_sw_ground,min_code_cct)
            cct_for_floor = max(min_cct_col_sw_normal,min_code_cct)
            cct_code = cct_for_ground + cct_for_floor*(n_of_floors-1)

            if min_cct_col_sw_ground < min_code_cct:
                st.info("Total Concrete Core Test for Ground Floor: " + str(min_code_cct))
            else:
                st.info("Total Concrete Core Test for Ground Floor: " + str(min_cct_col_sw_ground))

            if cct_for_floor < min_code_cct:
                st.info("Total Concrete Core Test for Normal Floor: " + str(min_code_cct))
            else:
                st.info("Total Concrete Core Test for Normal Floor: " + str(cct_for_floor))

            if cct_code < min_cct:
                st.info("Total Concrete Core Test: " + str(min_cct))
            else:
                st.info("Total Concrete Core Test: " + str(cct_code))

            st.info("Total Concrete Exposure Test for Columns: " + str(int(exp_test_col * n_of_floors)))
            st.info("Total Concrete Exposure Test for Beams: " + str(int(min_exp_beam * n_of_floors)))
            st.info("Total Concrete Exposure Test for Shear Walls: " + str(int(exp_test_sw * n_of_floors)))

            st.info("Total Cover Meter Test for Columns: " + str(int(min_cmt_col_code * n_of_floors)))
            st.info("Total Cover Meter Test for Beams: " + str(int(min_cmt_beam_code * n_of_floors)))
            st.info("Total Cover Meter Test for Shear Walls: " + str(int(min_cmt_sw_code * n_of_floors)))
else:
    # st.title("Rule Based Classification of Customer's Data")
    st.markdown("<h2 style='text-align: center; color: grey;'>TBDY 2018'e göre Saha Test Sayısı Hesaplayıcı </h2>",
                unsafe_allow_html=True)
    """
    Bu uygulama, Türkiye Bina Deprem Yönetmeliği 2018 - Bölüm 15'e göre test sayılarının hesaplanması için hazırlanmıştır.

    Uygulamayı kullanmak için lütfen aşağıdaki maddeleri dikkate alınız;

        1- Yapı Taşıyıcı Tipi (Betonarme or Önüretimli),
        2- Bilgi Düzeyi,
        3- Proje Mevcut mu?,
        4- Tipik kat alanı m2 cinsinden,
        5- Toplam kat sayısı, 
        6- Her kat için toplam kolon adeti,
        7- Her kat için toplam kiriş adeti,
        8- Her kat için toplam perde duvar adeti (eğer mevcutsa)

    Bu seçeneklerden sonra uygulama, toplam minimum test sayısını TBDY 2018'e göre hesaplayacaktır.

    """

    # Inputs for the calculation
    st.sidebar.header("Proje Girdileri")
    system = st.sidebar.selectbox("Yapı Taşıyıcı Tipi: ", {"Betonarme", "Önüretimli"})
    knowledge_level = st.sidebar.selectbox("Bilgi Düzeyi: ", {"Sınırlı", "Kapsamlı"})
    project = st.sidebar.selectbox("Proje Mevcut mu?: ", {"Evet", "Hayır"})
    area = st.sidebar.number_input("Tipik kat alanı m2 cinsinden", value=300, step=1)
    n_of_floors = st.sidebar.number_input("Toplam kat sayısı", value=3, step=1)
    n_of_columns = st.sidebar.number_input("Her kat için toplam kolon adeti", value=15, step=1)
    n_of_beams = st.sidebar.number_input("Her kat için toplam kiriş adeti", value=30, step=1)
    n_of_shear_wall = st.sidebar.number_input("Her kat için toplam perde duvar adeti (eğer mevcutsa)", value=3, step=1)
    st.subheader("Test Sonuçları")
    if knowledge_level == "Sınırlı":
        min_exp_col = 1
        min_exp_beam = 1
        min_exp_sw = 1
        min_cct_col_sw = 3

        n_of_cct = st.sidebar.number_input("Her kat için toplam beton karot numune testi adeti", value=4, step=1)

        min_exp_col_code = math.ceil((n_of_columns * 0.05))
        min_exp_sw_code = math.ceil((n_of_shear_wall * 0.05))

        min_cmt_col_code = math.ceil((n_of_columns-min_exp_col_code)*0.20)
        min_cmt_sw_code = math.ceil((n_of_shear_wall - min_exp_sw_code) * 0.20)

        exp_test_col = max(min_exp_col, min_exp_col_code)
        exp_test_sw = max(min_exp_sw, min_exp_sw_code)

        cct_for_floor = max(min_cct_col_sw,n_of_cct)

        st.info("Kolonlar için Toplam Beton Sıyırma Test Adeti: " + str(int(exp_test_col*n_of_floors)))
        st.info("Kirişler için Toplam Beton Sıyırma Test Adeti: " + str(int(min_exp_beam * n_of_floors)))
        st.info("Perdeler için Toplam Beton Sıyırma Test Adeti: " + str(int(exp_test_sw*n_of_floors)))

        st.info("Kolonlar için Toplam Donatı Tespit Cihazı Testi: " + str(int(min_cmt_col_code*n_of_floors)))
        st.info("Perdeler için Toplam Donatı Tespit Cihazı Testi: " + str(int(min_cmt_sw_code*n_of_floors)))

        st.info("Toplam Beton Karot Testi: " + str(int(cct_for_floor*n_of_floors)))

    else:
        if project == "Evet":
            min_exp_col = 1
            min_exp_beam = 1
            min_exp_sw = 1

            min_cct_col_sw_ground = 3
            min_cct_col_sw_normal = 2

            if system == "Önüretimli":
                min_code_cct = math.ceil(area/600)
                min_cct = 5
            else:
                min_code_cct = math.ceil(area / 400)
                min_cct = 9

            cct_for_ground = max(min_cct_col_sw_ground,min_code_cct)
            cct_for_floor = max(min_cct_col_sw_normal,min_code_cct)
            cct_code = cct_for_ground + cct_for_floor*(n_of_floors-1)

            if min_cct_col_sw_ground < min_code_cct:
                st.info("Zemin Kat için Toplam Beton Karot Testi: " + str(min_code_cct))
            else:
                st.info("Zemin Kat için Toplam Beton Karot Testi: " + str(min_cct_col_sw_ground))

            if cct_for_floor < min_code_cct:
                st.info("Normal Katlar için Toplam Beton Karot Testi: " + str(min_code_cct))
            else:
                st.info("Normal Katlar için Toplam Beton Karot Testi: " + str(cct_for_floor))

            if cct_code < min_cct:
                st.info("Toplam Beton Karot Testi: " + str(min_cct))
            else:
                st.info("Toplam Beton Karot Testi: " + str(cct_code))

            min_exp_col_code = math.ceil((n_of_columns * 0.05))
            min_exp_sw_code = math.ceil((n_of_shear_wall * 0.05))

            exp_test_col = max(min_exp_col, min_exp_col_code)
            exp_test_sw = max(min_exp_sw, min_exp_sw_code)

            min_cmt_col_code = math.ceil((n_of_columns-min_exp_col_code)*0.20)
            min_cmt_sw_code = math.ceil((n_of_shear_wall - min_exp_sw_code) * 0.20)
            min_cmt_beam_code = math.ceil((n_of_beams-min_exp_beam) * 0.10)

            st.info("Kolonlar için Toplam Beton Sıyırma Test Adeti: " + str(int(exp_test_col * n_of_floors)))
            st.info("Kirişler için Toplam Beton Sıyırma Test Adeti: " + str(int(min_exp_beam * n_of_floors)))
            st.info("Perdeler için Toplam Beton Sıyırma Test Adeti: " + str(int(exp_test_sw * n_of_floors)))

            st.info("Kolonlar için Toplam Donatı Tespit Cihazı Testi: " + str(int(min_cmt_col_code * n_of_floors)))
            st.info("Kirişler için Toplam Donatı Tespit Cihazı Testi: " + str(int(min_cmt_beam_code * n_of_floors)))
            st.info("Perdeler için Toplam Donatı Tespit Cihazı Testi: " + str(int(min_cmt_sw_code * n_of_floors)))


        else:
            min_exp_col = 1
            min_exp_sw = 1
            min_exp_beam = 1
            min_cct_col_sw_ground = 3
            min_cct_col_sw_normal = 2

            if system == "Önüretimli":
                min_code_cct = math.ceil(area/600)
                min_cct = 5
            else:
                min_code_cct = math.ceil(area / 400)
                min_cct = 9

            min_exp_col_code = math.ceil((n_of_columns * 0.1))
            min_exp_sw_code = math.ceil((n_of_shear_wall * 0.1))

            min_cmt_col_code = math.ceil((n_of_columns-min_exp_col_code)*0.30)
            min_cmt_sw_code = math.ceil((n_of_shear_wall - min_exp_sw_code) * 0.30)
            min_cmt_beam_code = math.ceil((n_of_beams-min_exp_beam) * 0.15)

            exp_test_col = max(min_exp_col, min_exp_col_code)
            exp_test_sw = max(min_exp_sw, min_exp_sw_code)

            cct_for_ground = max(min_cct_col_sw_ground,min_code_cct)
            cct_for_floor = max(min_cct_col_sw_normal,min_code_cct)
            cct_code = cct_for_ground + cct_for_floor*(n_of_floors-1)

            if min_cct_col_sw_ground < min_code_cct:
                st.info("Zemin Kat için Toplam Beton Karot Testi: " + str(min_code_cct))
            else:
                st.info("Zemin Kat için Toplam Beton Karot Testi: " + str(min_cct_col_sw_ground))

            if cct_for_floor < min_code_cct:
                st.info("Normal Katlar için Toplam Beton Karot Testi: " + str(min_code_cct))
            else:
                st.info("Normal Katlar için Toplam Beton Karot Testi: " + str(cct_for_floor))

            if cct_code < min_cct:
                st.info("Toplam Beton Karot Testi: " + str(min_cct))
            else:
                st.info("Toplam Beton Karot Testi: " + str(cct_code))

            st.info("Kolonlar için Toplam Beton Sıyırma Test Adeti: " + str(int(exp_test_col * n_of_floors)))
            st.info("Kirişler için Toplam Beton Sıyırma Test Adeti: " + str(int(min_exp_beam * n_of_floors)))
            st.info("Perdeler için Toplam Beton Sıyırma Test Adeti: " + str(int(exp_test_sw * n_of_floors)))

            st.info("Kolonlar için Toplam Donatı Tespit Cihazı Testi: " + str(int(min_cmt_col_code * n_of_floors)))
            st.info("Kirişler için Toplam Donatı Tespit Cihazı Testi: " + str(int(min_cmt_beam_code * n_of_floors)))
            st.info("Perdeler için Toplam Donatı Tespit Cihazı Testi: " + str(int(min_cmt_sw_code * n_of_floors)))
            
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
