import streamlit as st
from keras.models import load_model
import numpy as np


def convert_score(value):
    value = int(value)
    if value > 95:
        return 7
    if value > 90:
        return 6
    if value > 85:
        return 5
    if value > 80:
        return 4
    if value > 75:
        return 3
    if value > 70:
        return 2
    else:
        return 1


if __name__ == '__main__':
    # Memberi judul pada situs Streamlit
    st.title("Unitics")

    # Mendefinisikan halaman dari Streamlit
    select_pages = st.sidebar.selectbox(
        'Pages',
        ('Home', 'Science College Recommendation', 'Social College Recommendation')
    )

    # Seleksi kondisi halaman pada Streamlit
    if select_pages == "Home":
        # Berisi penjelasan singkat mengenai project yang dikerjakan
        st.subheader("About This Project")
        st.markdown(
            '<p style="color:Black;">The suitability between the choice of majors and universities with the interests '
            'and abilities of students in both academic and financial fields greatly affects the development of '
            'students potential and understanding of career plans for their future. Many of them follow their parents '
            'wishes and think that it is the right decision, so they don\'t have to bother with the dilemma of '
            'choosing majors and universities. Some students are determined to try their luck or follow the advice of '
            'the counseling teacher at their high school.</p>',
            unsafe_allow_html=True)
        st.text("")
        st.markdown('<p style="color:Black;"><b>Awards:</b> Build on Asean 2021 Finalist</p>', unsafe_allow_html=True)
        st.text("")
        st.markdown('<p style="color:Black;"><b>Machine Learning Engineer:</b> Joseph Ananda Sugihdharma</p>',
                    unsafe_allow_html=True)
        st.markdown('<p style="color:Black;"><b>UI/UX Designer:</b> Dina Noviana</p>', unsafe_allow_html=True)
        st.markdown('<p style="color:Black;"><b>Infrastructure Engineer:</b> Mohammad Zulfikar</p>',
                    unsafe_allow_html=True)
        st.markdown('<p style="color:Black;"><b>Web Developer (Frontend):</b> Rangga Adi Satria</p>',
                    unsafe_allow_html=True)
        st.markdown('<p style="color:Black;"><b>Web Developer (Backend):</b> M. Fikri Mustofa A.</p>',
                    unsafe_allow_html=True)
        st.markdown('<p style="color:Black;"><b>Last Updated: 18-Jan-2022</b></p>', unsafe_allow_html=True)

    if select_pages == "Science College Recommendation":
        # Subheader
        st.subheader("Science College Recommendation")

        # Text box untuk kata masukan dari pengguna
        mat1 = st.text_input("Enter 1st Semester Mathematics Score", "")
        mat2 = st.text_input("Enter 2nd Semester Mathematics Score", "")
        mat3 = st.text_input("Enter 3rd Semester Mathematics Score", "")
        mat4 = st.text_input("Enter 4th Semester Mathematics Score", "")
        mat5 = st.text_input("Enter 5th Semester Mathematics Score", "")
        ing1 = st.text_input("Enter 1st Semester English Score", "")
        ing2 = st.text_input("Enter 2nd Semester English Score", "")
        ing3 = st.text_input("Enter 3rd Semester English Score", "")
        ing4 = st.text_input("Enter 4th Semester English Score", "")
        ing5 = st.text_input("Enter 5th Semester English Score", "")
        ind1 = st.text_input("Enter 1st Semester Indonesian Score", "")
        ind2 = st.text_input("Enter 2nd Semester Indonesian Score", "")
        ind3 = st.text_input("Enter 3rd Semester Indonesian Score", "")
        ind4 = st.text_input("Enter 4th Semester Indonesian Score", "")
        ind5 = st.text_input("Enter 5th Semester Indonesian Score", "")
        fis1 = st.text_input("Enter 1st Semester Physics Score", "")
        fis2 = st.text_input("Enter 2nd Semester Physics Score", "")
        fis3 = st.text_input("Enter 3rd Semester Physics Score", "")
        fis4 = st.text_input("Enter 4th Semester Physics Score", "")
        fis5 = st.text_input("Enter 5th Semester Physics Score", "")
        kim1 = st.text_input("Enter 1st Semester Chemistry Score", "")
        kim2 = st.text_input("Enter 2nd Semester Chemistry Score", "")
        kim3 = st.text_input("Enter 3rd Semester Chemistry Score", "")
        kim4 = st.text_input("Enter 4th Semester Chemistry Score", "")
        kim5 = st.text_input("Enter 5th Semester Chemistry Score", "")
        bio1 = st.text_input("Enter 1st Semester Biology Score", "")
        bio2 = st.text_input("Enter 2nd Semester Biology Score", "")
        bio3 = st.text_input("Enter 3rd Semester Biology Score", "")
        bio4 = st.text_input("Enter 4th Semester Biology Score", "")
        bio5 = st.text_input("Enter 5th Semester Biology Score", "")

        if st.button("Predict"):
            score = [mat1, mat2, mat3, mat4, mat5, ing1, ing2, ing3, ing4, ing5, ind1, ind2, ind3, ind4, ind5,
                     fis1, fis2, fis3, fis4, fis5, kim1, kim2, kim3, kim4, kim5, bio1, bio2, bio3, bio4, bio5]

            converted_score = list(map(convert_score, score))

            model_ipa = load_model('ipa_v4.h5')
            prediction_ipa = model_ipa.predict([converted_score])
            prediction_ipa_idx = np.array(prediction_ipa[0]).argsort()[::-1][:5]

            labels_ipa = np.load('labels_ipa.npy', allow_pickle=True)
            result = labels_ipa[prediction_ipa_idx]
            st.subheader("TOP 5 RECOMMENDATIONS")
            st.text("Rank 1: " + result[0])
            st.text("Rank 2: " + result[1])
            st.text("Rank 3: " + result[2])
            st.text("Rank 4: " + result[3])
            st.text("Rank 5: " + result[4])

    if select_pages == "Social College Recommendation":
        # Subheader
        st.subheader("Social College Recommendation")

        # Text box untuk kata masukan dari pengguna
        mat1 = st.text_input("Enter 1st Semester Mathematics Score", "")
        mat2 = st.text_input("Enter 2nd Semester Mathematics Score", "")
        mat3 = st.text_input("Enter 3rd Semester Mathematics Score", "")
        mat4 = st.text_input("Enter 4th Semester Mathematics Score", "")
        mat5 = st.text_input("Enter 5th Semester Mathematics Score", "")
        ing1 = st.text_input("Enter 1st Semester English Score", "")
        ing2 = st.text_input("Enter 2nd Semester English Score", "")
        ing3 = st.text_input("Enter 3rd Semester English Score", "")
        ing4 = st.text_input("Enter 4th Semester English Score", "")
        ing5 = st.text_input("Enter 5th Semester English Score", "")
        ind1 = st.text_input("Enter 1st Semester Indonesian Score", "")
        ind2 = st.text_input("Enter 2nd Semester Indonesian Score", "")
        ind3 = st.text_input("Enter 3rd Semester Indonesian Score", "")
        ind4 = st.text_input("Enter 4th Semester Indonesian Score", "")
        ind5 = st.text_input("Enter 5th Semester Indonesian Score", "")
        eko1 = st.text_input("Enter 1st Semester Economics Score", "")
        eko2 = st.text_input("Enter 2nd Semester Economics Score", "")
        eko3 = st.text_input("Enter 3rd Semester Economics Score", "")
        eko4 = st.text_input("Enter 4th Semester Economics Score", "")
        eko5 = st.text_input("Enter 5th Semester Economics Score", "")
        geo1 = st.text_input("Enter 1st Semester Geography Score", "")
        geo2 = st.text_input("Enter 2nd Semester Geography Score", "")
        geo3 = st.text_input("Enter 3rd Semester Geography Score", "")
        geo4 = st.text_input("Enter 4th Semester Geography Score", "")
        geo5 = st.text_input("Enter 5th Semester Geography Score", "")
        sos1 = st.text_input("Enter 1st Semester Sociology Score", "")
        sos2 = st.text_input("Enter 2nd Semester Sociology Score", "")
        sos3 = st.text_input("Enter 3rd Semester Sociology Score", "")
        sos4 = st.text_input("Enter 4th Semester Sociology Score", "")
        sos5 = st.text_input("Enter 5th Semester Sociology Score", "")
        sej1 = st.text_input("Enter 1st Semester History Score", "")
        sej2 = st.text_input("Enter 2nd Semester History Score", "")
        sej3 = st.text_input("Enter 3rd Semester History Score", "")
        sej4 = st.text_input("Enter 4th Semester History Score", "")
        sej5 = st.text_input("Enter 5th Semester History Score", "")

        if st.button("Predict"):
            score = [mat1, mat2, mat3, mat4, mat5, ing1, ing2, ing3, ing4, ing5, ind1, ind2, ind3, ind4, ind5,
                     eko1, eko2, eko3, eko4, eko5, geo1, geo2, geo3, geo4, geo5, sos1, sos2, sos3, sos4, sos5,
                     sej1, sej2, sej3, sej4, sej5]

            converted_score = list(map(convert_score, score))

            model_ipa = load_model('ips_v4.h5')
            prediction_ipa = model_ipa.predict([converted_score])
            prediction_ipa_idx = np.array(prediction_ipa[0]).argsort()[::-1][:5]

            labels_ipa = np.load('labels_ips.npy', allow_pickle=True)
            result = labels_ipa[prediction_ipa_idx]
            st.subheader("TOP 5 RECOMMENDATIONS")
            st.text("Rank 1: " + result[0])
            st.text("Rank 2: " + result[1])
            st.text("Rank 3: " + result[2])
            st.text("Rank 4: " + result[3])
            st.text("Rank 5: " + result[4])
