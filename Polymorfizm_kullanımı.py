from abc import ABC, abstractmethod


# --- SOYUT ANA SINIF (ABSTRACT BASE CLASS) ---
# Bu sınıf tek başına kullanılamaz, sadece bir "şablon" veya "sözleşme" görevi görür.
class GameUnit(ABC):
    """
    Savaş alanındaki tüm birimler için ortak arayüz (interface).
    ABC (Abstract Base Class) sınıfından miras alır.
    """

    def __init__(self, name: str):
        self.name = name

    # @abstractmethod: Bu bir kuraldır!
    # Bu sınıftan türetilen HER sınıf, bu 'attack' metodunu
    # KENDİ İÇİNDE tanımlamak ZORUNDADIR. Yoksa hata verir.
    @abstractmethod
    def attack(self):
        pass


# --- SOMUT SINIFLAR (CONCRETE CLASSES) ---

class Knight(GameUnit):
    """Şövalye Sınıfı"""

    # Sözleşmeye uyuyoruz ve 'attack' metodunu kendimize göre yazıyoruz (Override).
    def attack(self):
        print(f" {self.name} (Şövalye), kılıcını savurdu! (Yakın Dövüş Hasarı)")


class Archer(GameUnit):
    """Okçu Sınıfı"""

    def attack(self):
        # Okçu saldırısı farklıdır.
        print(f" {self.name} (Okçu), yayını gerdi ve ok fırlattı! (Menzilli Hasar)")


class Wizard(GameUnit):
    """Büyücü Sınıfı"""

    def attack(self):
        # Büyücü saldırısı bambaşkadır.
        print(f" {self.name} (Büyücü), kadim sözler fısıldayarak ATEŞ TOPU attı! (Büyü Hasarı)")


# --- POLİMORFİZMİN GÜCÜ (SİHİRLİ FONKSİYON) ---
def battlefield_command(unit: GameUnit):
    """
    Bu fonksiyon, kendisine gelen nesnenin Şövalye mi, Okçu mu yoksa Büyücü mü
    olduğunu BİLMEZ ve UMURSAMAZ.

    Bildiği tek şey, gelen nesnenin bir 'GameUnit' olduğu ve
    mutlaka bir '.attack()' metoduna sahip olduğudur.
    """
    print(f"\n[KOMUTAN]: {unit.name}, saldırı emri verildi!")
    unit.attack()  # <-- İşte Polimorfizm tam olarak burada gerçekleşir.


# --- TEST SENARYOSU ---
if __name__ == "__main__":
    print("--- Savaş Hazırlığı ---")

    # Farklı türdeki nesneleri oluşturuyoruz
    k1 = Knight("Arthur")
    a1 = Archer("Legolas")
    w1 = Wizard("Gandalf")

    # Hepsini ortak bir listeye (Orduya) koyuyoruz
    my_army = [k1, a1, w1]

    print("\n--- SAVAŞ BAŞLADI! (Polimorfizm Gösterisi) ---")

    # Döngü içinde türüne bakmaksızın hepsine aynı komutu veriyoruz.
    for soldier in my_army:
        # soldier değişkeni her turda farklı bir sınıfa dönüşür (Çok biçimlilik)
        battlefield_command(soldier)

    print("\n--- Savaş Sona Erdi ---")

    # --- Ekstra Bilgi: Soyut Sınıf Denemesi ---
    # Aşağıdaki satırı açarsan hata alırsın. Çünkü soyut sınıflardan (GameUnit)
    # doğrudan nesne üretilemez.
    # test_unit = GameUnit("Test")