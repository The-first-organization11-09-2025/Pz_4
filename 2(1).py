def sum_list(list_glav):
    summa = 0
    for i in (list_glav):
        if (type(i) == float) or (type(i) == int):
            summa += i
        elif type(i) == list:
            summa += sum_list(i)
    return summa

listik = [1, [2,3], [4, [5,6]], [-1, -5], 0]
print (sum_list(listik))