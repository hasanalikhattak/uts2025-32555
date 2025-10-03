import csv
import random
from typing import Dict
class Student:
    def __init__(self, name: str, mark: int):
        self.name = name
        self.mark = mark
        self.grade = self.determine_grade()

    def determine_grade(self) -> str:
        if self.mark >= 85:
            return 'HD'
        elif self.mark >= 75:
            return 'D'
        elif self.mark >= 65:
            return 'C'
        elif self.mark >= 50:
            return 'P'
        else:
            return 'Z'

    def __str__(self) -> str:
        return f"{self.name} → {self.grade}"

class Faculty:
    def __init__(self):
        self.students: Dict[str, Student] = {}

    def enroll_students(self):
        for i in range(100, 110):
            name = f"Student_{i}"
            mark = random.randint(1, 100)
            student = Student(name, mark)
            self.students[name] = student
        print("10 students enrolled.")

    def save(self):
        with open("grades.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Mark", "Grade"])
            for student in self.students.values():
                writer.writerow([student.name, student.mark, student.grade])
        print("Student records saved to grades.csv.")

    def show(self):
        try:
            with open("grades.csv", mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(', '.join(row))
        except FileNotFoundError:
            print("grades.csv not found. Please save the records first.")

    def help(self):
        print("Choices:")
        print("(e) enrol – adds 10 students with IDs ranging from 100 to 109 with randomly generated marks")
        print("(s) save – save the student records to the grades.csv file")
        print("(v) show – read and show csv content")
        print("(x) exit")

    def menu(self):
        while True:
            self.help()
            choice = input("Enter your choice: ").strip().lower()
            if choice == 'e':
                self.enroll_students()
            elif choice == 's':
                self.save()
            elif choice == 'v':
                self.show()
            elif choice == 'x':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def main(self):
        self.menu()

if __name__ == "__main__":
    faculty = Faculty()
    faculty.main()