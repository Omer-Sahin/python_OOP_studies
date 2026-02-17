class Calc:
    """
    Temel Matematik İşlemleri Yapan Hesap Makinesi Sınıfı.
    """

    def __init__(self, sayi1: float = 0, sayi2: float = 0):
        # Tip belirleme (float) profesyonel bir yaklaşımdır
        self.value1 = sayi1
        self.value2 = sayi2

    def add(self):
        """Toplama işlemi sonucunu döndürür."""
        return self.value1 + self.value2

    def multiply(self):
        """Çarpma işlemi sonucunu döndürür."""
        return self.value1 * self.value2


def hesapla():
    """Kullanıcıdan girdi alarak hesaplamayı yöneten ana fonksiyon."""
    print("\n--- Hesap Makinesi ---")
    print("1: Toplama")
    print("2: Çarpma")
    print("Çıkış için başka bir tuşa basınız.")

    secim = input("Seçiminiz: ")

    if secim in ["1", "2"]:
        try:
            # Kullanıcıdan sayıları alıyoruz
            v1 = float(input("Sayı 1: "))
            v2 = float(input("Sayı 2: "))

            # Nesneyi oluşturuyoruz (Constructor burada tetiklenir)
            calculator = Calc(v1, v2)

            if secim == "1":
                # :.0f tam sayı gibi gösterir
                print(f"Sonuç: {calculator.add():.0f}")
            elif secim == "2":
                # :.2f virgülden sonra iki basamak gösterir
                print(f"Sonuç: {calculator.multiply():.2f}")

        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz!")
    else:
        print("Programdan çıkılıyor...")


# Programın çalışması için fonksiyonu çağırıyoruz
if __name__ == "__main__":
    hesapla()