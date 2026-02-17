class SmartPhone:
    """
    Bu sınıf, Python'da Constructor (__init__) mantığını
    öğretmek amacıyla oluşturulmuştur.
    """

    def __init__(self, brand: str, model: str, price: int, storage: int):
        """
        CONSTRUCTOR (Yapıcı Metot):
        Nesne oluşturulduğu anda (örneğin: telefon fabrikadan çıktığında)
        otomatik olarak çalışan ilk metottur.

        'self' parametresi, o an oluşturulan spesifik nesneyi temsil eder.
        """
        # Özellikleri (Attributes) tanımlıyoruz
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage
        self.is_on = False  # Her yeni telefon kapalı başlar (Varsayılan değer)

        print(f"--- [SİSTEM]: {self.brand} {self.model} başarıyla üretildi. ---")

    def show_specs(self):
        """Telefonun teknik özelliklerini yazdırır."""
        status = "Açık" if self.is_on else "Kapalı"
        print(f"\n📱 Cihaz Bilgileri:")
        print(f"Marka/Model: {self.brand} {self.model}")
        print(f"Depolama: {self.storage} GB")
        print(f"Fiyat: {self.price} TL")
        print(f"Durum: {status}")

    def power_button(self):
        """Telefonu açar veya kapatır."""
        self.is_on = not self.is_on
        action = "açıldı" if self.is_on else "kapandı"
        print(f"\n[BİLGİ]: {self.brand} {self.model} {action}.")


# --- NESNE OLUŞTURMA (CONSTRUCTOR BURADA TETİKLENİR) ---

# 1. Örnek: iPhone nesnesi oluşturuyoruz
# Not: __init__ içindeki self'i biz göndermeyiz, Python onu otomatik halleder.
phone1 = SmartPhone(brand="Apple", model="iPhone 15", price=55000, storage=128)
phone1.show_specs()

# 2. Örnek: Samsung nesnesi oluşturuyoruz
phone2 = SmartPhone("Samsung", "S24 Ultra", 65000, 256)
phone2.power_button()  # Telefonu açtık
phone2.show_specs()

# 3. Örnek: POCO nesnesi (Senin kullandığın cihazlardan biri gibi)
phone3 = SmartPhone("POCO", "F6", 28000, 512)
phone3.show_specs()