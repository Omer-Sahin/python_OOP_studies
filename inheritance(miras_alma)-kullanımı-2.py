class GameCharacter:
    """
    Parent Class (Ana Sınıf):
    Oyundaki tüm karakterlerin sahip olduğu ortak özellikleri taşır.
    """

    def __init__(self, name: str, health: int, level: int = 1):
        self.name = name
        self.health = health
        self.level = level
        self.is_alive = True

    def attack(self, target):
        """Temel saldırı metodu."""
        if not self.is_alive:
            print(f" {self.name} ölü olduğu için saldıramaz!")
            return

        damage = 10 * self.level
        print(f"\n⚔️ {self.name}, {target.name} adlı düşmana saldırdı!")
        target.take_damage(damage)

    def take_damage(self, amount: int):
        """Hasar alma metodu."""
        self.health -= amount
        print(f" {self.name} {amount} hasar aldı. Kalan Can: {self.health}")

        if self.health <= 0:
            self.die()

    def die(self):
        """Karakter ölür."""
        self.is_alive = False
        self.health = 0
        print(f"XXXX {self.name} savaş alanında düştü! XXXX")

    def __str__(self):
        """Nesneyi print(character) yaptığımızda bu çalışır."""
        status = "Yaşıyor" if self.is_alive else "Ölü"
        return f"[{self.name} | Lvl: {self.level} | HP: {self.health} | {status}]"


# --- CHILD CLASS 1: WARRIOR (SAVAŞÇI) ---
class Warrior(GameCharacter):
    """
    GameCharacter sınıfından miras alır.
    Ekstra özellik: Kalkan (Shield)
    """

    def __init__(self, name: str, health: int, shield: int):
        # super() ile ana sınıfın özelliklerini alıyoruz
        super().__init__(name, health)
        self.shield = shield

    # METHOD OVERRIDING (Metot Ezme)
    # Savaşçı hasar alırken önce kalkanını kullanır!
    def take_damage(self, amount: int):
        if amount > self.shield:
            real_damage = amount - self.shield
            self.shield = 0
            print(f"🛡 {self.name}'in kalkanı kırıldı!")
            super().take_damage(real_damage)  # Kalan hasarı ana sınıfa gönder
        else:
            self.shield -= amount
            print(f"🛡 {self.name} hasarı kalkanıyla karşıladı! Kalkan Gücü: {self.shield}")


# --- CHILD CLASS 2: MAGE (BÜYÜCÜ) ---
class Mage(GameCharacter):
    """
    GameCharacter sınıfından miras alır.
    Ekstra özellik: Mana
    """

    def __init__(self, name: str, health: int, mana: int):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self, target):
        """Büyücüye özel yetenek."""
        if self.mana >= 30:
            spell_damage = 40 * self.level
            self.mana -= 30
            print(f"\n {self.name} ATEŞ TOPU fırlattı! (Mana: {self.mana})")
            target.take_damage(spell_damage)
        else:
            print(f"\n {self.name}'in manası bitti, büyü yapamıyor!")


# --- OYUN SENARYOSU (TEST) ---
if __name__ == "__main__":
    # Karakterleri Oluşturuyoruz
    arthas = Warrior("Arthas", health=100, shield=50)
    jaina = Mage("Jaina", health=80, mana=100)

    print("--- OYUN BAŞLADI ---")
    print(arthas)
    print(jaina)

    # 1. Round: Savaşçı saldırıyor (Normal Saldırı)
    arthas.attack(jaina)

    # 2. Round: Büyücü yetenek kullanıyor (Özel Yetenek)
    jaina.cast_spell(arthas)

    # 3. Round: Savaşçı tekrar saldırıyor
    arthas.attack(jaina)

    # 4. Round: Büyücü son vuruşu yapıyor
    jaina.cast_spell(arthas)  # Kalkan kırılacak ve can gidecek

    print("\n--- SON DURUM ---")
    print(arthas)
    print(jaina)