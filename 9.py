class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomer_ID):
        Orang.__init__(self, nama_depan, nama_belakang, nomer_ID)
        Pelajar.__init__(self)
        Pengajar.__init__(self)
