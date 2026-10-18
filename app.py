import streamlit as st

# ==============================================================================
# KONFIGURASI HALAMAN & TEMA VISUAL MATH DETECTIVE
# ==============================================================================
st.set_page_config(
    page_title="Math Detective - LKPD Logika TKA",
    page_icon="🕵️‍♂️",
    layout="wide"
)

# Kustomisasi CSS untuk Tema Gelap / Papan Detektif
st.markdown("""
<style>
    .stApp {
        background-color: #1a1a1d;
        color: #e6e6e6;
    }
    .detective-title {
        font-family: 'Courier New', Courier, monospace;
        color: #ff4b4b;
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        letter-spacing: 2px;
        margin-bottom: 0px;
    }
    .doc-code {
        font-family: 'Courier New', Courier, monospace;
        color: #888888;
        text-align: center;
        font-size: 0.9rem;
        margin-bottom: 25px;
    }
    .case-card {
        background-color: #25262a;
        border-left: 5px solid #ff4b4b;
        padding: 15px 20px;
        border-radius: 5px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .case-header {
        font-family: 'Courier New', Courier, monospace;
        color: #fca311;
        font-size: 1.3rem;
        font-weight: bold;
    }
    .evidence-box {
        background-color: #141416;
        border: 1px dashed #4a4d52;
        padding: 12px;
        border-radius: 4px;
        font-style: italic;
        color: #d1d5db;
        margin-top: 8px;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# BANK SOAL LENGKAP (15 SOAL TKA LOGIKA SMA)
# ==============================================================================
BANK_SOAL = [
    {
        "id": 1,
        "judul": "Rahasia Sertifikat Robotik",
        "materi": "Penarikan Kesimpulan (Silogisme)",
        "stimulus": "Di SMA Nusantara, semua siswa yang mengikuti ekstrakurikuler Robotik wajib menguasai bahasa pemrograman Python. Beberapa siswa yang menguasai Python juga menyukai Catur.",
        "pertanyaan": "Berdasarkan bukti di atas, kesimpulan yang PASTI BENAR adalah...",
        "pilihan": [
            "A. Semua siswa yang menyukai Catur adalah anggota ekstrakurikuler Robotik.",
            "B. Beberapa siswa yang mengikuti ekstrakurikuler Robotik menyukai Catur.",
            "C. Semua siswa yang menguasai bahasa pemrograman Python adalah anggota Robotik.",
            "D. Tidak dapat disimpulkan hubungan pasti antara anggota Robotik dan penyuka Catur."
        ],
        "kunci": "D",
        "pembahasan": "Kuantor 'Beberapa siswa Python menyukai Catur' tidak menjamin bahwa siswa Python yang menyukai Catur tersebut adalah siswa di Robotik. Tidak ada hubungan pasti yang dapat disimpulkan."
    },
    {
        "id": 2,
        "judul": "Pernyataan Palsu Saksi Ujian",
        "materi": "Negasi Pernyataan Berkuantor",
        "stimulus": "Pengawas ujian menyatakan: 'Semua peserta TKA mengisi lembar jawaban menggunakan pensil 2B.'",
        "pertanyaan": "Bentuk pernyataan yang paling tepat untuk mematahkan (menegasikan) pernyataan pengawas adalah...",
        "pilihan": [
            "A. Semua peserta TKA tidak mengisi lembar jawaban menggunakan pensil 2B.",
            "B. Tidak ada peserta TKA yang mengisi lembar jawaban menggunakan pensil 2B.",
            "C. Ada peserta TKA yang tidak mengisi lembar jawaban menggunakan pensil 2B.",
            "D. Beberapa peserta TKA mengisi lembar jawaban menggunakan pulpen."
        ],
        "kunci": "C",
        "pembahasan": "Negasi dari kuantor universal 'Semua P adalah Q' (∀x P(x)) adalah kuantor eksistensial 'Ada/Beberapa P yang Bukan Q' (∃x ~P(x)). Cukup 1 peserta tidak memakai pensil 2B untuk membantah kata 'Semua'."
    },
    {
        "id": 3,
        "judul": "Syarat Beasiswa Penuh",
        "materi": "Logika Implikasi (Kontraposisi)",
        "stimulus": "Aturan Sekolah: 'Jika siswa memenangkan Olimpiade Matematika, maka siswa mendapatkan Beasiswa Penuh.'",
        "pertanyaan": "Pernyataan yang secara logika EKUIVALEN (setara) dengan aturan di atas adalah...",
        "pilihan": [
            "A. Jika siswa tidak memenangkan Olimpiade Matematika, maka siswa tidak mendapatkan Beasiswa Penuh.",
            "B. Jika siswa tidak mendapatkan Beasiswa Penuh, maka siswa tidak memenangkan Olimpiade Matematika.",
            "C. Jika siswa mendapatkan Beasiswa Penuh, maka siswa pasti memenangkan Olimpiade Matematika.",
            "D. Siswa tidak memenangkan Olimpiade Matematika atau tidak mendapatkan Beasiswa Penuh."
        ],
        "kunci": "B",
        "pembahasan": "Suatu implikasi (P -> Q) secara logika ekuivalen dengan KONTRAPOSISI-nya (~Q -> ~P). Pernyataan ~Q -> ~P berarti 'Jika siswa tidak mendapatkan Beasiswa Penuh, maka siswa tidak memenangkan Olimpiade Matematika'."
    },
    {
        "id": 4,
        "judul": "Posisi Duduk Tersangka",
        "materi": "Penalaran Analitis (Posisi)",
        "stimulus": "Lima siswa (Andi, Budi, Cici, Dini, Eko) duduk berderet dari posisi 1 (kiri) ke posisi 5 (kanan). Andi di sebelah kiri Budi. Cici di antara Dini dan Eko. Dini di posisi 5 (paling kanan). Budi tepat di sebelah kiri Eko.",
        "pertanyaan": "Siapakah yang berada di posisi paling kiri (posisi 1)?",
        "pilihan": [
            "A. Andi",
            "B. Budi",
            "C. Cici",
            "D. Eko"
        ],
        "kunci": "A",
        "pembahasan": "Rangkaian posisi dari kiri ke kanan (1 ke 5):\n- Dini di posisi 5 [ _ , _ , _ , _ , Dini ]\n- Cici di antara Dini dan Eko [ _ , _ , Eko , Cici , Dini ]\n- Budi di sebelah kiri Eko [ _ , Budi , Eko , Cici , Dini ]\n- Andi di sebelah kiri Budi [ Andi , Budi , Eko , Cici , Dini ]\nPosisi paling kiri (posisi 1) adalah Andi."
    },
    {
        "id": 5,
        "judul": "Misteri Mati Lampu",
        "materi": "Penarikan Kesimpulan (Modus Tollens)",
        "stimulus": "Premis 1: Jika listrik padam, maka pendingin ruangan (AC) tidak berfungsi.\nPremis 2: Hari ini pendingin ruangan (AC) berfungsi dengan baik.",
        "pertanyaan": "Kesimpulan yang sah (valid) berdasarkan dua premis di atas adalah...",
        "pilihan": [
            "A. Listrik tidak padam.",
            "B. Listrik sedang padam.",
            "C. Pendingin ruangan dalam keadaan rusak.",
            "D. Tidak ada kesimpulan yang dapat diambil."
        ],
        "kunci": "A",
        "pembahasan": "Prinsip Modus Tollens: [(P -> Q) DAN ~Q] menyimpulkan ~P. P = Listrik padam, Q = AC tidak berfungsi. Karena AC berfungsi (~Q), maka kesimpulannya adalah Listrik tidak padam (~P)."
    },
    {
        "id": 6,
        "judul": "Dilema Belajar Budi",
        "materi": "Logika Disjungsi & Implikasi",
        "stimulus": "Pernyataan: 'Budi belajar dengan tekun atau Budi gagal dalam ujian TKA.'",
        "pertanyaan": "Bentuk implikasi yang ekuivalen (setara) dengan pernyataan di atas adalah...",
        "pilihan": [
            "A. Jika Budi belajar dengan tekun, maka Budi gagal dalam ujian TKA.",
            "B. Jika Budi tidak belajar dengan tekun, maka Budi gagal dalam ujian TKA.",
            "C. Jika Budi gagal dalam ujian TKA, maka Budi belajar dengan tekun.",
            "D. Jika Budi lulus ujian TKA, maka Budi tidak belajar dengan tekun."
        ],
        "kunci": "B",
        "pembahasan": "Sifat ekuivalensi disjungsi ke implikasi: (P OR Q) ≡ (~P -> Q). Misal P = 'Budi belajar dengan tekun' dan Q = 'Budi gagal ujian'. Bentuk ~P -> Q adalah 'Jika Budi tidak belajar dengan tekun, maka Budi gagal dalam ujian TKA'."
    },
    {
        "id": 7,
        "judul": "Jadwal Pelajaran Laboratorium",
        "materi": "Penalaran Analitis (Jadwal)",
        "stimulus": "Empat mata pelajaran (Matematika, Fisika, Kimia, Biologi) dijadwalkan Senin hingga Kamis. Fisika sebelum Kimia. Matematika pada hari Rabu. Biologi diajarkan Kamis.",
        "pertanyaan": "Pelajaran apa yang diajarkan pada hari Senin?",
        "pilihan": [
            "A. Matematika",
            "B. Fisika",
            "C. Kimia",
            "D. Biologi"
        ],
        "kunci": "B",
        "pembahasan": "Rabu = Matematika, Kamis = Biologi. Tersisa Senin dan Selasa untuk Fisika dan Kimia. Karena Fisika harus sebelum Kimia, maka Fisika = Senin dan Kimia = Selasa."
    },
    {
        "id": 8,
        "judul": "Pola Hidup Sehat",
        "materi": "Penarikan Kesimpulan (Silogisme Hipotetis)",
        "stimulus": "Premis 1: Jika seseorang rajin berolahraga, maka daya tahan tubuhnya meningkat.\nPremis 2: Jika daya tahan tubuh seseorang meningkat, maka ia tidak mudah terserang penyakit.",
        "pertanyaan": "Kesimpulan yang sah dari kedua premis di atas adalah...",
        "pilihan": [
            "A. Jika seseorang tidak mudah terserang penyakit, maka ia rajin berolahraga.",
            "B. Jika seseorang rajin berolahraga, maka ia tidak mudah terserang penyakit.",
            "C. Seseorang rajin berolahraga dan ia mudah terserang penyakit.",
            "D. Seseorang tidak rajin berolahraga jika ia tidak terserang penyakit."
        ],
        "kunci": "B",
        "pembahasan": "Prinsip Silogisme Hipotetis: [(P -> Q) DAN (Q -> R)] menyimpulkan (P -> R). Jika seseorang rajin berolahraga, maka ia tidak mudah terserang penyakit."
    },
    {
        "id": 9,
        "judul": "Aturan Kelulusan Praktikum",
        "materi": "Logika Konjungsi & Biimplikasi",
        "stimulus": "Aturan Praktikum: 'Siswa dinyatakan lulus praktikum jika dan hanya jika hadir 100% dan menyerahkan laporan lengkap.'",
        "pertanyaan": "Jika Roni menyerahkan laporan lengkap tetapi tidak hadir 100%, kesimpulan yang tepat adalah...",
        "pilihan": [
            "A. Roni tetap dinyatakan lulus praktikum.",
            "B. Roni tidak dinyatakan lulus praktikum.",
            "C. Roni harus mengulang ujian teori.",
            "D. Kelulusan Roni tergantung keputusan guru."
        ],
        "kunci": "B",
        "pembahasan": "Biimplikasi (P <-> Q) bernilai Benar jika kedua syarat dipenuhi bersamaan. Karena syarat kehadiran 100% tidak dipenuhi, maka syarat kelulusan bernilai SALAH (Roni tidak lulus praktikum)."
    },
    {
        "id": 10,
        "judul": "Bantahan Klaim Juara",
        "materi": "Negasi Pernyataan Eksistensial",
        "stimulus": "Pernyataan: 'Ada siswa SMA 1 yang memenangkan medali emas sains.'",
        "pertanyaan": "Ingkaran (negasi) dari pernyataan di atas adalah...",
        "pilihan": [
            "A. Ada siswa SMA 1 yang tidak memenangkan medali emas sains.",
            "B. Semua siswa SMA 1 tidak memenangkan medali emas sains.",
            "C. Beberapa siswa SMA 1 tidak memenangkan medali emas sains.",
            "D. Semua siswa SMA 1 memenangkan medali emas sains."
        ],
        "kunci": "B",
        "pembahasan": "Negasi dari kuantor eksistensial 'Ada P yang Q' (∃x P(x)) adalah kuantor universal 'Semua P tidak Q' / 'Tidak ada P yang Q' (∀x ~P(x))."
    },
    {
        "id": 11,
        "judul": "Investigasi Kecepatan Lari",
        "materi": "Penalaran Analitis (Perbandingan)",
        "stimulus": "Lari 100 meter: Doni lebih cepat dari Ari. Fani lebih lambat dari Ari tetapi lebih cepat dari Gita. Ari lebih lambat dari Eko, dan Eko lebih lambat dari Doni.",
        "pertanyaan": "Siapakah pelari yang paling cepat?",
        "pilihan": [
            "A. Doni",
            "B. Eko",
            "C. Ari",
            "D. Fani"
        ],
        "kunci": "A",
        "pembahasan": "Urutan dari paling cepat ke paling lambat: Doni > Eko > Ari > Fani > Gita. Maka pelari paling cepat adalah Doni."
    },
    {
        "id": 12,
        "judul": "Modus Ponens Cuaca Ekstrem",
        "materi": "Penarikan Kesimpulan (Modus Ponens)",
        "stimulus": "Premis 1: Jika cuaca ekstrem terjadi, maka penerbangan ditunda.\nPremis 2: Hari ini terjadi cuaca ekstrem.",
        "pertanyaan": "Kesimpulan yang sah adalah...",
        "pilihan": [
            "A. Penerbangan tidak ditunda.",
            "B. Penerbangan ditunda.",
            "C. Tidak terjadi cuaca ekstrem.",
            "D. Maskapai mengalami kerugian."
        ],
        "kunci": "B",
        "pembahasan": "Mengikuti aturan Modus Ponens: [(P -> Q) DAN P] menyimpulkan Q (Penerbangan ditunda)."
    },
    {
        "id": 13,
        "judul": "Dua Kondisi Perpustakaan",
        "materi": "Logika Konjungsi (Negasi)",
        "stimulus": "Pernyataan: 'Ruang perpustakaan tenang dan sejuk.'",
        "pertanyaan": "Ingkaran (negasi) menggunakan Hukum De Morgan dari pernyataan di atas adalah...",
        "pilihan": [
            "A. Ruang perpustakaan tidak tenang dan tidak sejuk.",
            "B. Ruang perpustakaan tidak tenang atau tidak sejuk.",
            "C. Ruang perpustakaan tenang tetapi tidak sejuk.",
            "D. Ruang perpustakaan tidak tenang dan sejuk."
        ],
        "kunci": "B",
        "pembahasan": "Hukum De Morgan untuk konjungsi: ~(P AND Q) ≡ (~P OR ~Q). Maka negasinya adalah 'Ruang perpustakaan tidak tenang ATAU tidak sejuk'."
    },
    {
        "id": 14,
        "judul": "Sistem Proteksi Komputer",
        "materi": "Logika Implikasi",
        "stimulus": "Pernyataan: 'Jika komputer terinfeksi virus, maka sistem antivirus akan memberikan peringatan.'",
        "pertanyaan": "Manakah kondisi yang membuktikan bahwa pernyataan di atas SALAH?",
        "pilihan": [
            "A. Komputer terinfeksi virus dan antivirus memberikan peringatan.",
            "B. Komputer terinfeksi virus tetapi antivirus tidak memberikan peringatan.",
            "C. Komputer tidak terinfeksi virus dan antivirus tidak memberikan peringatan.",
            "D. Komputer tidak terinfeksi virus tetapi antivirus memberikan peringatan."
        ],
        "kunci": "B",
        "pembahasan": "Tabel kebenaran implikasi (P -> Q) bernilai SALAH (False) hanya jika sebabnya terjadi (P = True), namun akibatnya tidak terjadi (Q = False)."
    },
    {
        "id": 15,
        "judul": "Urutan Tinggi Badan Tim Basket",
        "materi": "Penalaran Analitis (Tinggi Badan)",
        "stimulus": "Tinggi badan lima pemain basket: Raka lebih tinggi dari Soni. Tono lebih pendek dari Soni tetapi lebih tinggi dari Yoga. Raka lebih pendek dari Viko.",
        "pertanyaan": "Urutan pemain dari yang paling pendek ke yang paling tinggi adalah...",
        "pilihan": [
            "A. Yoga - Tono - Soni - Raka - Viko",
            "B. Viko - Raka - Soni - Tono - Yoga",
            "C. Yoga - Soni - Tono - Raka - Viko",
            "D. Tono - Yoga - Soni - Raka - Viko"
        ],
        "kunci": "A",
        "pembahasan": "Urutan tinggi badan dari paling pendek ke paling tinggi: Yoga < Tono < Soni < Raka < Viko."
    }
]

# ==============================================================================
# INISIALISASI STATE & PROSEDUR TAMPILAN
# ==============================================================================
def inisialisasi_state():
    if "soal_index" not in st.session_state:
        st.session_state.soal_index = 0
    if "jawaban_user" not in st.session_state:
        st.session_state.jawaban_user = {}
    if "sudah_submit" not in st.session_state:
        st.session_state.sudah_submit = False

def render_header():
    st.markdown('<div class="detective-title">🕵️‍♂️ MATH DETECTIVE: KASUS LOGIKA TKA</div>', unsafe_allow_html=True)
    st.markdown('<div class="doc-code">KODE DOKUMEN: MATHDETECTIVE-LKPD-XJ4ZPQGGHFVZY4UNPYEAJJ</div>', unsafe_allow_html=True)

def render_sidebar():
    st.sidebar.markdown("### 🔍 NAVIGASI SOAL")
    st.sidebar.write(f"Soal Aktif: **{st.session_state.soal_index + 1} dari {len(BANK_SOAL)}**")
    
    # Pilih Soal Langsung
    pilihan_soal = [f"Kasus {i+1}" for i in range(len(BANK_SOAL))]
    pilihan_terpilih = st.sidebar.selectbox(
        "Lompat ke Kasus:",
        pilihan_soal,
        index=st.session_state.soal_index
    )
    st.session_state.soal_index = pilihan_soal.index(pilihan_terpilih)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 STATUS LEMBAR KERJA")
    dijawab = len(st.session_state.jawaban_user)
    st.sidebar.progress(dijawab / len(BANK_SOAL))
    st.sidebar.write(f"Terjawab: **{dijawab} / {len(BANK_SOAL)} Kasus**")

def render_soal_tunggal():
    item = BANK_SOAL[st.session_state.soal_index]
    soal_id = item["id"]
    
    st.markdown(f"""
    <div class="case-card">
        <div class="case-header">[KASUS {item['id']:02d}] {item['judul']}</div>
        <small style="color: #a0a0a0;">Fokus Materi: {item['materi']}</small>
        <div class="evidence-box">
            <b>Bukti / Stimulus:</b><br>{item['stimulus']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"**Pertanyaan:** {item['pertanyaan']}")
    
    # Radio Button untuk Pilihan Jawaban
    key_radio = f"radio_{soal_id}"
    jawaban_sebelumnya = st.session_state.jawaban_user.get(soal_id, None)
    
    # Mencari index jawaban sebelumnya
    index_default = 0
    if jawaban_sebelumnya:
        for idx, pil in enumerate(item["pilihan"]):
            if pil.startswith(jawaban_sebelumnya):
                index_default = idx
                break

    pilihan = st.radio(
        label=f"Pilih analisis kamu untuk Kasus {soal_id}:",
        options=item["pilihan"],
        index=index_default if jawaban_sebelumnya else 0,
        key=key_radio,
        disabled=st.session_state.sudah_submit
    )
    
    # Simpan jawaban huruf (A/B/C/D)
    st.session_state.jawaban_user[soal_id] = pilihan[0]
    
    # Tampilkan Pembahasan Khusus Halaman Ini
    if st.session_state.sudah_submit:
        kunci = item["kunci"]
        user_ans = st.session_state.jawaban_user.get(soal_id, "")
        
        if user_ans == kunci:
            st.success(f" BUKTI COCOK! Analisis kamu benar ({kunci}).")
        else:
            st.error(f" BUKTI MISMATCH. Jawaban kamu: {user_ans} | Kunci Jawaban: {kunci}")
            
        with st.expander("📜 Lihat Pembahasan Logika Formal", expanded=True):
            st.write(item["pembahasan"])

def render_navigasi_tombol():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ Kasus Sebelumnya", disabled=(st.session_state.soal_index == 0)):
            st.session_state.soal_index -= 1
            st.rerun()
            
    with col3:
        if st.button("Kasus Selanjutnya ➡️", disabled=(st.session_state.soal_index == len(BANK_SOAL) - 1)):
            st.session_state.soal_index += 1
            st.rerun()

def render_evaluasi_akhir():
    st.markdown("---")
    st.markdown("### 📊 HASIL EVALUASI SELURUH KASUS")
    
    total = len(BANK_SOAL)
    benar = 0
    
    for item in BANK_SOAL:
        if st.session_state.jawaban_user.get(item["id"]) == item["kunci"]:
            benar += 1
            
    skor = (benar / total) * 100
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Kasus", total)
    c2.metric("Kasus Terpecahkan", benar)
    c3.metric("Skor Akurasi", f"{skor:.0f}%")
    
    if skor == 100:
        st.balloons()
        st.success("🏆 GELAR: DETEKTIF UTAMA! Seluruh 15 kasus dipecahkan dengan sempurna.")
    elif skor >= 70:
        st.info(" DETEKTIF SENIOR! Analisis logika kamu sudah sangat baik.")
    else:
        st.warning("⚠️ DETEKTIF MAGANG. Tinjau kembali pembahasan di setiap soal.")

# ==============================================================================
# ALUR UTAMA PROGRAM
# ==============================================================================
def main():
    inisialisasi_state()
    render_header()
    render_sidebar()
    
    # Render Soal Sesuai Halaman Aktif (1 Halaman 1 Soal)
    render_soal_tunggal()
    st.markdown("---")
    render_navigasi_tombol()
    
    # Tombol Aksi Akhir
    st.markdown("<br>", unsafe_allow_html=True)
    if not st.session_state.sudah_submit:
        if st.button("🚨 Selesaikan & Kirim Seluruh Analisis Kasus", type="primary"):
            st.session_state.sudah_submit = True
            st.rerun()
    else:
        render_evaluasi_akhir()
        if st.button("🔄 Ulangi Seluruh Misi Kasus", type="secondary"):
            st.session_state.jawaban_user = {}
            st.session_state.sudah_submit = False
            st.session_state.soal_index = 0
            st.rerun()

if __name__ == "__main__":
    main()