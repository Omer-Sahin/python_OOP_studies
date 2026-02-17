class UniversityMember:
    """
    Ana Sınıf (Parent Class):
    Tüm üniversite üyelerinin ortak özelliklerini tutar.
    Kod tekrarını önlemek için 'name' ve 'id_no' burada tanımlanır.
    """

    def __init__(self, name: str, id_no: str):
        self.name = name
        self.id_no = id_no

    def get_details(self):
        """Bu metot alt sınıflar tarafından ezilecek (Override)."""
        print(f"\nKimlik: {self.id_no} | İsim: {self.name}")

    def enter_campus(self):
        """Herkesin yapabildiği ortak eylem."""
        print(f" {self.name}, kampüs kartını okuttu ve giriş yaptı.")


class Student(UniversityMember):
    """
    Çocuk Sınıf (Child Class) - Öğrenci:
    UniversityMember sınıfından miras alır.
    Ekstra olarak 'gpa' (not ortalaması) özelliğine sahiptir.
    """

    def __init__(self, name: str, id_no: str, gpa: float):
        # super() fonksiyonu, miras alınan üst sınıfın __init__ metodunu çağırır.
        # Böylece name ve id_no'yu tekrar elle atamak zorunda kalmayız.
        super().__init__(name, id_no)
        self.gpa = gpa

    # Method Overriding (Metot Ezme)
    def get_details(self):
        # Önce ana sınıftaki metodu çağırıp ismini yazdıralım
        super().get_details()
        # Sonra öğrenciye özel bilgiyi ekleyelim
        print(f"   └── Statü: Öğrenci | Not Ortalaması: {self.gpa}")

    def study(self):
        print(f" {self.name} kütüphanede ders çalışıyor...")


class Academician(UniversityMember):
    """
    Çocuk Sınıf (Child Class) - Akademisyen:
    UniversityMember sınıfından miras alır.
    Ekstra olarak 'department' ve 'title' özelliklerine sahiptir.
    """

    def __init__(self, name: str, id_no: str, department: str, title: str):
        super().__init__(name, id_no)
        self.department = department
        self.title = title

    # Method Overriding
    def get_details(self):
        super().get_details()
        print(f"   └── Statü: {self.title} | Bölüm: {self.department}")

    def give_lecture(self):
        print(f"🎓 {self.title} {self.name}, {self.department} dersini anlatıyor.")


# --- SİSTEM TESTİ ---

if __name__ == "__main__":
    # 1. Öğrenci Nesnesi Oluşturma
    student1 = Student("Ahmet Yılmaz", "2024001", 3.45)

    # 2. Akademisyen Nesnesi Oluşturma
    prof1 = Academician("Dr. Zeynep Kaya", "TR-552", "Bilgisayar Müh.", "Prof. Dr.")

    # 3. Ortak Metotları Test Etme (Miras alınan özellik)
    student1.enter_campus()
    prof1.enter_campus()

    # 4. Özelleştirilmiş (Overridden) Metotları Test Etme
    # İkisi de get_details() çağırır ama farklı çıktı verirler (Polimorfizm)
    members = [student1, prof1]

    print("\n--- Sistemdeki Kişiler ---")
    for member in members:
        member.get_details()

    # 5. Sınıfa Özgü Metotlar
    print("\n--- Günlük Aktiviteler ---")
    student1.study()  # Sadece öğrenci yapabilir
    prof1.give_lecture()  # Sadece hoca yapabilir