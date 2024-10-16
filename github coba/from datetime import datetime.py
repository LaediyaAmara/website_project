from datetime import datetime

# Fungsi untuk memberikan informasi tentang Maulid Nabi
def info_maulid_nabi():
    print("==== Peringatan Maulid Nabi ====")
    print("Maulid Nabi Muhammad SAW diperingati setiap tanggal 12 Rabiul Awal,")
    print("hari kelahiran Nabi Muhammad SAW.")
    print("Maulid Nabi biasanya dirayakan dengan doa, sholawat, serta kajian tentang kehidupan Rasulullah.")
    print()

# Fungsi untuk mengecek apakah hari ini adalah Maulid Nabi
def cek_maulid_nabi():
    # Mengambil tanggal saat ini
    hari_ini = datetime.now()

    # Tanggal peringatan Maulid Nabi di kalender Hijriah
    # Biasanya sekitar 12 Rabiul Awal, ini tergantung pada tahun Hijriah, jadi perlu konversi
    tanggal_maulid = datetime(2024, 9, 15)  # Sebagai contoh untuk tahun 2024

    if hari_ini.date() == tanggal_maulid.date():
        print("Hari ini adalah Maulid Nabi Muhammad SAW!")
    else:
        print("Hari ini bukan Maulid Nabi. Tetap bershalawat dan ingat ajaran Rasulullah setiap hari.")

# Menjalankan fungsi
info_maulid_nabi()
cek_maulid_nabi()
