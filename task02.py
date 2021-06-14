# O(N**2)
def array_min(myarr):
    for i in myarr:
        r = True
        for j in (myarr):
            if i > j:
                r = False

        if r == True:
            return i


def n_min(myarr):
    min = myarr[0]
    for i in myarr[1:]:
        if i < min:
            min = i
    return min


def my_min(myarr):  # O(N Log N)
    return sorted(myarr)[0]


my_arr = [7, 9, 4, 6, 25, 8, 3, 78, 99, 23]

r1 = array_min(my_arr)
print(r1)

r2 = n_min(my_arr)
print(r2)

r3 = my_min(my_arr)
print(r3)
