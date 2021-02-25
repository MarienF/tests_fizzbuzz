from fizzbuzz_checker import fizzbuzzchecker

def main():
    print("Alice donne le nombre :")
    numAlice = input()
    print(fizzbuzzchecker.is_bob(int(numAlice)))



if __name__ == '__main__':
    main()