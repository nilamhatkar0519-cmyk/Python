class Student:

    # Private variable
    __name = "Nilam"

    # Protected variable
    _roll_no = 25

    # Private function
    def __private_function(self):
        print("Private function: Student details")

    # Protected function
    def _protected_function(self):
        print("Protected function: Roll No =", self._roll_no)


class Marks(Student):

    def display_marks(self):
        print("Maths: 85")
        print("Physics: 80")
        print("Computer: 90")

        # Protected function can be accessed
        self._protected_function()


class Result(Marks):

    def display_result(self):
        print("Result: PASS")

        # Protected variable can be accessed
        print("Roll No:", self._roll_no)


r = Result()

r.display_marks()
r.display_result()