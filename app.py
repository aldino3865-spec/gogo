import streamlit as st
import random

st.set_page_config(page_title="Number System Calculator", layout="wide")
st.title("Program Sistem Bilangan")

# =========================
# SIDEBAR MENU
# =========================

menu = st.sidebar.selectbox(
    "Pilih Fitur",
    ["Konversi", "Calculator", "BCD", "Komplemen", "Mini Game"]
)

base_map = {
    "Biner": 2,
    "Desimal": 10,
    "Oktal": 8,
    "Hexa": 16,
    "Hexadesimal": 16
}

# =========================
# 1 KONVERSI
# =========================
if menu == "Konversi":

    st.subheader("Konversi Sistem Bilangan")

    jenis = st.selectbox(
        "Jenis Bilangan Input",
        ["Biner", "Desimal", "Oktal", "Hexadesimal"]
    )

    bil = st.text_input("Masukkan bilangan")

    if st.button("Konversi"):

        try:
            desimal = int(bil, base_map[jenis])

            st.divider()

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write("Biner")
                st.success(format(desimal, 'b'))

            with col2:
                st.write("Desimal")
                st.success(desimal)

            with col3:
                st.write("Oktal")
                st.success(format(desimal, 'o'))

            with col4:
                st.write("Hexa")
                st.success(format(desimal, 'X'))

        except:
            st.error("Input tidak sesuai dengan jenis bilangan")

# =========================
# 2 CALCULATOR
# =========================
elif menu == "Calculator":

    st.subheader("Calculator Sistem Bilangan")

    col1, col2 = st.columns(2)

    with col1:
        jenis1 = st.selectbox(
            "Jenis Bilangan 1",
            ["Biner", "Desimal", "Oktal", "Hexa"]
        )
        bil1 = st.text_input("Bilangan 1")

    with col2:
        jenis2 = st.selectbox(
            "Jenis Bilangan 2",
            ["Biner", "Desimal", "Oktal", "Hexa"]
        )
        bil2 = st.text_input("Bilangan 2")

    operasi = st.selectbox("Operasi", ["+", "-", "*", "/"])

    hasil_basis = st.selectbox(
        "Tampilkan hasil dalam",
        ["Biner", "Desimal", "Oktal", "Hexa"]
    )

    if st.button("Hitung"):

        try:
            a = int(bil1, base_map[jenis1])
            b = int(bil2, base_map[jenis2])

            if operasi == "+":
                hasil = a + b
            elif operasi == "-":
                hasil = a - b
            elif operasi == "*":
                hasil = a * b
            else:
                hasil = a / b

            st.divider()
            st.subheader("Hasil")

            if hasil_basis == "Biner":
                st.success(format(int(hasil), 'b'))

            elif hasil_basis == "Desimal":
                st.success(hasil)

            elif hasil_basis == "Oktal":
                st.success(format(int(hasil), 'o'))

            else:
                st.success(format(int(hasil), 'X'))

        except:
            st.error("Input tidak valid")

# =========================
# 3 BCD
# =========================
elif menu == "BCD":

    st.subheader("Konversi Code Digital")

    jenis = st.selectbox(
        "Jenis Bilangan Input",
        ["Desimal", "Biner", "Oktal", "Hexa", "BCD"]
    )

    bil = st.text_input("Masukkan bilangan")

    # pilihan kode jika input BCD
    kode = None
    if jenis == "BCD":
        kode = st.selectbox(
            "Jenis Kode BCD",
            ["8421", "2421", "5421", "Excess-3"]
        )

    if st.button("Konversi"):

        try:

            # =========================
            # BCD -> DESIMAL
            # =========================
            if jenis == "BCD":

                digits = bil.split()
                desimal = ""

                tabel2421 = {
                    "0000":"0","0001":"1","0010":"2","0011":"3","0100":"4",
                    "1011":"5","1100":"6","1101":"7","1110":"8","1111":"9"
                }

                tabel5421 = {
                    "0000":"0","0001":"1","0010":"2","0011":"3","0100":"4",
                    "1000":"5","1001":"6","1010":"7","1011":"8","1100":"9"
                }

                for d in digits:

                    if kode == "8421":
                        desimal += str(int(d,2))

                    elif kode == "2421":
                        desimal += tabel2421[d]

                    elif kode == "5421":
                        desimal += tabel5421[d]

                    elif kode == "Excess-3":
                        desimal += str(int(d,2)-3)

                desimal = int(desimal)

                st.success(f"Desimal : {desimal}")

            # =========================
            # BASIS LAIN -> DESIMAL
            # =========================
            else:

                desimal = int(bil, base_map[jenis])

                if jenis != "Desimal":
                    st.info(f"{jenis} dikonversi ke Desimal : {desimal}")

            des_str = str(desimal)

            # =========================
            # 8421
            # =========================
            bcd = " ".join(format(int(i),'04b') for i in des_str)

            # =========================
            # 2421
            # =========================
            tabel2421 = {
                "0":"0000","1":"0001","2":"0010","3":"0011","4":"0100",
                "5":"1011","6":"1100","7":"1101","8":"1110","9":"1111"
            }

            code2421 = " ".join(tabel2421[i] for i in des_str)

            # =========================
            # 5421
            # =========================
            tabel5421 = {
                "0":"0000","1":"0001","2":"0010","3":"0011","4":"0100",
                "5":"1000","6":"1001","7":"1010","8":"1011","9":"1100"
            }

            code5421 = " ".join(tabel5421[i] for i in des_str)

            # =========================
            # Excess 3
            # =========================
            excess3 = " ".join(format(int(i)+3,'04b') for i in des_str)

            # =========================
            # Gray Code
            # =========================
            biner = format(desimal,'b')

            gray = biner[0]

            for i in range(1,len(biner)):
                gray += str(int(biner[i-1]) ^ int(biner[i]))

            st.divider()

            col1,col2,col3,col4,col5 = st.columns(5)

            with col1:
                st.write("BCD (8421)")
                st.success(bcd)

            with col2:
                st.write("2421 Code")
                st.success(code2421)

            with col3:
                st.write("5421 Code")
                st.success(code5421)

            with col4:
                st.write("Excess-3")
                st.success(excess3)

            with col5:
                st.write("Gray Code")
                st.success(gray)

        except:
            st.error("Input tidak valid")

# =========================
# 4 KOMPLEMEN
# =========================
elif menu == "Komplemen":

    st.subheader("Komplemen Biner")

    biner = st.text_input("Masukkan bilangan biner")

    if st.button("Hitung"):

        if set(biner) - {"0","1"}:
            st.error("Masukkan hanya angka 0 dan 1")

        else:

            k1 = "".join("1" if i=="0" else "0" for i in biner)
            k2 = format(int(k1,2)+1,'b')

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.write("Komplemen 1")
                st.success(k1)

            with col2:
                st.write("Komplemen 2")
                st.success(k2)

# =========================
# MINI GAME
# =========================
elif menu == "Mini Game":

    st.subheader("Mini Game Sistem Bilangan 🎮")

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "correct" not in st.session_state:
        st.session_state.correct = 0

    if "wrong" not in st.session_state:
        st.session_state.wrong = 0

    if st.button("Reset Score"):
        st.session_state.score = 0
        st.session_state.correct = 0
        st.session_state.wrong = 0

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("Score",st.session_state.score)

    with col2:
        st.metric("Benar",st.session_state.correct)

    with col3:
        st.metric("Salah",st.session_state.wrong)

st.divider()
st.caption("Number System Calculator • Kelompok 4")
