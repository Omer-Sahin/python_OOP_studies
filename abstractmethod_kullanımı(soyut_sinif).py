from abc import ABC, abstractmethod

# --- SOYUT SINIF (ABSTRACT CLASS) ---
class OdemeYontemi(ABC):
    """
    Bu sınıf bir şablondur. Tek başına kullanılamaz.
    Bunu miras alan herkes 'ode' metodunu yazmak ZORUNDADIR.
    """
    @abstractmethod
    def ode(self, miktar: float):
        pass  # İçeriği boştur, kural koyucudur.

# --- SOMUT SINIFLAR (CONCRETE CLASSES) ---
class KrediKarti(OdemeYontemi):
    def ode(self, miktar: float):
        print(f" Kredi Kartı ile {miktar} TL çekildi. İşlem başarılı.")

class KriptoPara(OdemeYontemi):
    def ode(self, miktar: float):
        print(f" Blockchain üzerinden {miktar} TL değerinde coin transfer edildi.")

# --- TEST ---
if __name__ == "__main__":
    # odeme = OdemeYontemi() # BU SATIR HATA VERİR! (Soyut sınıf üretilemez)

    kart = KrediKarti()
    kart.ode(250.50)

    kripto = KriptoPara()
    kripto.ode(10000)