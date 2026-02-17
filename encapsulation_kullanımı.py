import datetime


class BankAccount:
    """
    Kapsülleme (Encapsulation) prensibini gösteren Banka Hesabı Sınıfı.
    Veri güvenliği ve tutarlılığı için 'private' değişkenler kullanılmıştır.
    """

    def __init__(self, owner: str, initial_balance: float = 0.0):
        # Public (Herkes erişebilir)
        self.owner = owner

        # Private (Sadece sınıf içinden erişilebilir - Çift alt çizgi)
        self.__balance = initial_balance
        self.__account_logs = []  # İşlem geçmişini gizli tutuyoruz

        self.__add_log(f"Hesap açıldı. İlk Bakiye: {initial_balance} TL")

    # --- GETTER (Okuma) Metodu ---
    @property
    def balance(self):
        """
        Bakiyeyi dışarıya sadece 'okunabilir' olarak sunar.
        Dışarıdan 'hesap.balance = 500' denilerek değiştirilemez.
        """
        return self.__balance

    # --- Güvenli İşlem Metotları ---
    def deposit(self, amount: float):
        """Hesaba güvenli para yatırma işlemi."""
        if amount > 0:
            self.__balance += amount
            self.__add_log(f"Yatırılan: +{amount} TL")
            print(f" {amount} TL yatırıldı. Yeni Bakiye: {self.__balance} TL")
        else:
            print(" Hata: Yatırılacak tutar sıfırdan büyük olmalıdır!")

    def withdraw(self, amount: float):
        """Hesaptan güvenli para çekme işlemi."""
        if amount > self.__balance:
            print(" Hata: Yetersiz bakiye!")
        elif amount <= 0:
            print(" Hata: Geçersiz tutar!")
        else:
            self.__balance -= amount
            self.__add_log(f"Çekilen: -{amount} TL")
            print(f" {amount} TL çekildi. Kalan Bakiye: {self.__balance} TL")

    # --- Private Yardımcı Metot ---
    def __add_log(self, message: str):
        """
        Bu metot sadece sınıf içinde kullanılır. Dışarıdan log eklenemez.
        """
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__account_logs.append(f"[{time_stamp}] {message}")

    def get_account_history(self):
        """Gizli tutulan hesap geçmişini güvenli şekilde görüntüler."""
        print(f"\n--- {self.owner} İçin Hesap Dökümü ---")
        for log in self.__account_logs:
            print(log)
        print("---------------------------------------")


# --- TEST SENARYOSU ---
if __name__ == "__main__":
    # 1. Hesabı Oluşturma
    my_account = BankAccount("Ali Veli", 1000)

    # 2. Bakiyeyi Okuma (Getter çalışır)
    print(f"Mevcut Bakiye: {my_account.balance} TL")

    # 3. Hatalı Erişim Denemesi
    # my_account.balance = 5000  # HATA VERİR! (AttributeError: can't set attribute)
    # print(my_account.__balance) # HATA VERİR! (Veri gizlidir)

    # 4. İşlemler
    my_account.deposit(500)  # Para yatırma
    my_account.withdraw(2000)  # Yetersiz bakiye hatası
    my_account.withdraw(300)  # Başarılı çekim

    # 5. Geçmişi Görüntüleme
    my_account.get_account_history()