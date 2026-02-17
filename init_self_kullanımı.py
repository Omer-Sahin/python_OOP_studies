class Employees:
    def __init__(self, name: str, surname: str, salary: int, department: str):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department

    def get_employee_information(self):
        """
        Bu Fonksiyon Employees Bilgilerini Yazdırır
        """
        print(f"Name: {self.name}, Surname: {self.surname}, Salary: {self.salary}, Department: {self.department}")

# --- Sınıfın Dışında Nesne Oluşturma ---
employee_1 = Employees(
    name="Ali",
    surname="Cengiz",
    salary=6500,
    department="Bilgi Teknolojileri"
)

# Bilgileri Yazdır
employee_1.get_employee_information()

# Kapsülleme kullanılmış Hali -->

class Employees:
    def __init__(self, name: str, surname: str, salary: int, department: str):
        self.name = name
        self.surname = surname
        self.__salary = salary  # Maaş artık gizli (Private)
        self.department = department

    def get_employee_information(self):
        """Bilgileri ekrana yazdırır."""
        print(f"Name: {self.name}, Surname: {self.surname}, "
              f"Salary: {self.__salary}, Department: {self.department}")

    def set_salary(self, new_salary: int):
        """Maaşı güvenli bir şekilde günceller."""
        if new_salary > 0:
            self.__salary = new_salary
            print(f"Maaş güncellendi: {self.__salary}")
        else:
            print("Hata: Maaş negatif bir değer olamaz!")

    def get_salary(self):
        """Maaş bilgisini güvenli bir şekilde döndürür."""
        return self.__salary

# --- Kullanım ---
emp1 = Employees("Ali", "Cengiz", 6500, "Bilgi Teknolojileri")

# Doğrudan erişim denemesi:
# print(emp1.__salary)  # Bu satır hata verir, çünkü maaş gizli!

# Bilgileri görme:
emp1.get_employee_information()

# Maaşı güncelleme:
emp1.set_salary(7500)  # Doğru yöntem
emp1.set_salary(-100)  # Hatalı giriş denemesi (Bloklanır)