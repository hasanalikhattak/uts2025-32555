class Student:
    def enroll(self):
        print("You are enrolled")

    def makeEmail(self, em):
        self.email = em
        print("Email is set to:", self.email)