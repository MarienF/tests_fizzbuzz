class fizzbuzzchecker:

    @staticmethod
    def is_bob(num):
        if (num <= 0):
            #raise NameError('Exeption')
            return False

        if (num % 3 == 0):
            print("Fizz")
            return True

        return False