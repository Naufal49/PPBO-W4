# Latihan 1
class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_ID = nomer_ID

# Latihan 2
class Mahasiswa(Orang):
    SARJANA, MASTER, DOKTOR = range(3)

    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

# Latihan 3
class Karyawan(Orang):
    TETAP, TDK_TETAP = range(2)

    def __init__(self, status_karyawan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status_karyawan = status_karyawan

# Latihan 4
class Dosen(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_diajar = []

    def mengajar(self, matkul_diajar):
        self.matkul_diajar.append(matkul_diajar)

# Latihan 5
bowo = Mahasiswa(Mahasiswa.SARJANA, "Bowo", "Nugroho", "987654")
bowo.enrol("Basis Data")

# Latihan 6
rizki = Dosen("Rizki", "Setiabudi", "456789", Karyawan.TETAP)
rizki.mengajar("Statistik")

