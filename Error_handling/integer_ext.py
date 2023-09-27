while True:
    try:
        intro = input()
        repeat = int(input())
        for x in range(repeat):
            print(intro, end="")
        break
    except ValueError:
        print("Variable error must be integers!")
