# #======================
# #======= SOAL 1 =======
# #======================
# # print("\n======= SOAL 1 =======")

# # cara1:

# list_angka = input("Masukkan list angka yang dipisahkan dengan koma: ").split(sep=',')

# print(list_angka)

# for i in range(len(list_angka)):
#     list_angka[i] = int(list_angka[i])

# print(list_angka)

# print(list(map(lambda x: "Genap" if x%2 == 0 else "Ganjil", list_angka)))


# # cara2:

# list_angka = input("Masukkan list angka yang dipisahkan dengan koma: ").split(sep=',') # ["1", "2", "3"]

# print(list(map(lambda x: "Genap" if int(x)%2 == 0 else "Ganjil", list_angka)))


# #======================
# #======= SOAL 2 =======
# #======================
# print("\n======= SOAL 2 =======")

# list_gaji = [9.1, 9.8, 9.5, 10.3, 9.3]

# list_gaji_juta = list(map(lambda x: int(x*10**6), list_gaji))
# print(list_gaji_juta)

# print(list(filter(lambda x : x-x*(5/100) > 9e6, list_gaji_juta)))

# #======================
# #======= SOAL 3 =======
# #======================
# print("\n======= SOAL 3 =======")
# # No. 3
# # code:

def fungsi1(nama, iterasi):
    for i in range(iterasi):
        print(f'Hi {nama}!')

list1 = [0, fungsi1]
list2 = [0,1,list1]
dict1 = {'world': list2}

def fungsi2(bebas):
    return dict1

def fungsi3():
    return fungsi2

test = (0, fungsi3)

# # input: --> tidak bleh diubah
test[1]()('hello')['world'][2][1]('Garda', 5)

#output
# Hi Garda!
# Hi Garda!
# Hi Garda!
# Hi Garda!
# Hi Garda!

def fungsi1(nama, iterasi):
    for i in range(iterasi):
        print(f'Hi {nama}!')

dictonary = {'world': 
                    {2 : 
                        {1: fungsi1}}}

def fungsi2(apapun):
    if apapun == "hello":
        return dictonary

def fungsi3():
    return fungsi2

test = (0, fungsi3)

test[1]()('hello')['world'][2][1]('Garda', 5)