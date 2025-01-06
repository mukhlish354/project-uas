from uas.classstudent import Student

class StudentProcess:
    """Class untuk memproses input dan validasi data mahasiswa."""
    def __init__(self):
        self.students = []

    def add_student(self, name, age, major):
        if not name or not major:
            raise ValueError("Nama dan jurusan tidak boleh kosong.")
        if age <= 0:
            raise ValueError("Usia harus lebih besar dari 0.")
        
        student = Student(name, age, major)
        self.students.append(student)

    def get_students(self):
        return self.students
