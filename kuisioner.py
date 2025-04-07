import streamlit as st  # Mengimpor library Streamlit untuk membuat antarmuka web interaktif

def evaluasi_kuisioner(jawaban):
    nilai = [int(j.split('.')[0]) for j in jawaban]

    # Hitung jumlah masing-masing skor
    skor_counter = {
        4: nilai.count(4),
        3: nilai.count(3),
        2: nilai.count(2),
        1: nilai.count(1)
    }

    # Ambil skor yang paling sering muncul
    skor_terbanyak = max(skor_counter, key=skor_counter.get)
    jumlah_terbanyak = skor_counter[skor_terbanyak]

    # Jika skor terbanyak muncul lebih dari 4 kali/ min 5 angka muncul, maka di nilai berdasarkan skor tertinggi dominan
    if jumlah_terbanyak > 3:
        if skor_terbanyak == 4:
            return "Sangat Puas"
        elif skor_terbanyak == 3:
            return "Puas"
        elif skor_terbanyak == 2:
            return "Kurang Puas"
        else:
            return "Tidak Puas"
    else:
        return "Tidak Puas"



# Inisialisasi state untuk mendeteksi apakah tombol submit sudah ditekan
if "submit_clicked" not in st.session_state:
    st.session_state.submit_clicked = False  # Set nilai defaultnya False

st.title("Kuisioner Kepuasan Pelayanan")  # Menampilkan judul utama halaman

# Fungsi untuk membuat pertanyaan dengan penanda anchor dan validasi jawaban
def pertanyaan(nomor, teks, opsi):
    st.markdown(f"<a name='{nomor}'></a>", unsafe_allow_html=True)  # Membuat anchor untuk navigasi ke pertanyaan
    jawaban = st.radio(teks, options=opsi, index=None, key=nomor)  # Menampilkan radio button pilihan jawaban

    # Jika tombol submit ditekan dan jawaban belum diisi, tampilkan peringatan merah
    if st.session_state.submit_clicked and jawaban is None:
        st.markdown(f"<span style='color:red'>❗Pertanyaan {nomor} belum dijawab.</span>", unsafe_allow_html=True)

    return jawaban  # Mengembalikan nilai jawaban

# Daftar pertanyaan, dan menggunakan \u00A0 untuk spasi non-breaking agar angka tidak hilang
u1 = pertanyaan("U1", "U1. Kejelasan Persyaratan: Bagaimana pendapat Anda tentang kesesuaian persyaratan pelayanan dengan jenis layanan?", [
    "4.\u00A0Sangat sesuai", "3.\u00A0Sesuai", "2.\u00A0Kurang sesuai", "1.\u00A0Tidak sesuai"
])
u2 = pertanyaan("U2", "U2. Kejelasan Prosedur: Bagaimana pendapat Anda tentang kejelasan prosedur pelayanan di BKPPD?", [
    "4.\u00A0Sangat jelas", "3.\u00A0Jelas", "2.\u00A0Kurang jelas", "1.\u00A0Tidak jelas"
])
u3 = pertanyaan("U3", "U3. Ketepatan Waktu Penyelesaian: Bagaimana pendapat Anda tentang kecepatan waktu dalam memberikan pelayanan?", [
    "4.\u00A0Sangat cepat", "3.\u00A0Cepat", "2.\u00A0Kurang cepat", "1.\u00A0Tidak cepat"
])
u4 = pertanyaan("U4", "U4. Ketentuan Biaya Pelayanan: Bagaimana pendapat Anda tentang biaya dalam pelayanan?", [
    "4.\u00A0Gratis", "3.\u00A0Murah", "2.\u00A0Cukup Mahal", "1.\u00A0Sangat Mahal"
])
u5 = pertanyaan("U5", "U5. Kesesuaian Hasil: Bagaimana pendapat Anda tentang kesesuaian produk pelayanan antara yang tercantum dalam standar pelayanan dengan hasil yang diberikan?", [
    "4.\u00A0Sangat Sesuai", "3.\u00A0Sesuai", "2.\u00A0Kurang Sesuai", "1.\u00A0Tidak Sesuai"
])
u6 = pertanyaan("U6", "U6. Kemampuan Petugas: Bagaimana pendapat Anda tentang kompetensi / kemampuan petugas dalam pelayanan?", [
    "4.\u00A0Sangat Kompeten", "3.\u00A0Kompeten", "2.\u00A0Kurang Kompeten", "1.\u00A0Tidak Kompeten"
])
u7 = pertanyaan("U7", "U7. Keramahan Petugas: Bagaimana pendapat Anda mengenai perilaku petugas dalam pelayanan terkait kesopanan dan keramahan?", [
    "4.\u00A0Sangat Sopan dan Ramah", "3.\u00A0Sopan dan Ramah", "2.\u00A0Kurang Sopan dan Ramah", "1.\u00A0Tidak Sopan dan Ramah"
])
u8 = pertanyaan("U8", "U8. Penanganan Pengaduan: Bagaimana pendapat Anda tentang penanganan pengaduan bagi pengguna layanan?", [
    "4.\u00A0Dikelola dengan baik", "3.\u00A0Kurang maksimal", "2.\u00A0Ada tapi tidak berfungsi", "1.\u00A0Tidak ada"
])
u9 = pertanyaan("U9", "U9. Sarana dan Prasarana: Bagaimana pendapat Anda tentang kualitas sarana dan prasarana yang ada di ruang pelayanan BKPPD?", [
    "4.\u00A0Sangat Baik", "3.\u00A0Baik", "2.\u00A0Cukup", "1.\u00A0Buruk"
])

jawaban = [u1, u2, u3, u4, u5, u6, u7, u8, u9]  # Menggabungkan semua jawaban dalam list
pertanyaan_ids = ["U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9"]  # List ID untuk membantu navigasi

# Tombol untuk melihat hasil
lihat_hasil = st.button("Lihat Hasil")  # Menampilkan tombol "Lihat Hasil"

if lihat_hasil:
    st.session_state.submit_clicked = True  # Mengaktifkan validasi error
    if None in jawaban:
        # Kalau masih ada jawaban yang kosong
        st.markdown("<span style='color:red'>❗Mohon lengkapi semua pertanyaan berikut:</span>", unsafe_allow_html=True)

        # Tampilkan daftar pertanyaan yang belum dijawab, bisa diklik untuk scroll ke bagian tersebut
        for idx, j in enumerate(jawaban):
            if j is None:
                st.markdown(f" ❗ [Jawab pertanyaan {pertanyaan_ids[idx]}](#{pertanyaan_ids[idx]})", unsafe_allow_html=True)
    else:
        hasil = evaluasi_kuisioner(jawaban)  # Proses evaluasi hasil
        st.success(f"Hasil: {hasil}")  # Menampilkan hasil evaluasi dengan tanda berhasil
