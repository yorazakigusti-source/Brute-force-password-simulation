import itertools
import time

class PeretasSandi:
    def __init__(self, himpunan_karakter):
        self.karakter = himpunan_karakter

    def serang_langsung(self, sandi_target, panjang_min, panjang_max):
        waktu_mulai = time.time()
        total_percobaan = 0
        
        # Loop Eksternal: Bergerak dari panjang minimal ke maksimal
        for panjang in range(panjang_min, panjang_max + 1):
            
            # Loop Internal: Membangkitkan kombinasi secara iteratif
            for kombinasi in itertools.product(self.karakter, repeat=panjang):
                total_percobaan += 1
                tebakan = ''.join(kombinasi)
                
                # Operasi Dasar: Pencocokan string langsung (Plain text matching)
                if tebakan == sandi_target:
                    waktu_selesai = time.time()
                    durasi = waktu_selesai - waktu_mulai
                    return tebakan, total_percobaan, durasi
        
        waktu_selesai = time.time()
        durasi = waktu_selesai - waktu_mulai
        return None, total_percobaan, durasi