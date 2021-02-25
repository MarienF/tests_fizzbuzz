class fizzbuzzchecker:

    @staticmethod
    def is_bob(num):
        if (num <= 0):
            raise NameError('Exeption')

        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
            return True

        if (num % 3 == 0):
            print("Fizz")
            return True

        if (num % 5 == 0):
            print("Buzz")
            return True

        print(num)
        return True