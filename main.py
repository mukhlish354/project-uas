from uas.classstudent import Student
from uas.classStudentproses import StudentProcess
from uas.classview import StudentView


def main():
    process = StudentProcess()

    while True:
        try:
            name = input("Masukkan nama mahasiswa (atau ketik 'exit' untuk keluar): ")
            if name.lower() == 'exit':
                break
            
            age = int(input("Masukkan usia mahasiswa: "))
            major = input("Masukkan jurusan mahasiswa: ")

            process.add_student(name, age, major)

        except ValueError as e:
            print(f"Error: {e}")

    # Menampilkan data mahasiswa
    view = StudentView()
    view.display_students(process.get_students())

if __name__ == "__main__":
    main()