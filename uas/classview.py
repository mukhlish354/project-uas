class StudentView:
    """Class untuk menampilkan data mahasiswa."""
    @staticmethod
    def display_students(students):
        print("\nDaftar Mahasiswa:")
        print(f"{'No':<5} {'Nama':<20} {'Usia':10} {'Jurusan':<15}")
        print("-" * 50)
        for index, student in enumerate(students, start=1):
            print(f"{index:<5} {student.name:<20} {student.age:<10} {student.major:<15}")