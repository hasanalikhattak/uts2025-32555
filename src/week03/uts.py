import testStudent
class UTS:
    def showAllStudents():
        print("All students are shown")
        print("UTS Students:")
        print("Name:", uts001.email)
        print("Name:", uts007.email)

    uts001 = testStudent.Student()
    uts001.enroll()
    uts001.makeEmail("uts001@std.uts.edu.au")

    uts007 = testStudent.Student()
    uts007.enroll()
    uts007.makeEmail("uts007@std.uts.edu.au")