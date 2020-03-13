if __name__ == '__main__':
    s = input()

    print(bool([x for x in s if x.isalnum()]))
    print(bool([x for x in s if x.isalpha()]))
    print(bool([x for x in s if x.isdigit()]))
    print(bool([x for x in s if x.islower()]))
    print(bool([x for x in s if x.isupper()]))
