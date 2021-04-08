while True:

    n = input()

    if n == "0":
        break

    n_list1 = list(n)
    n_list2 = list(n)

    n_list2.reverse()

    if n_list1 == n_list2:
        print("yes")
    else:
        print("no")
