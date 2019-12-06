data=[]
while (True):
    Nama = input("Nama               : ")
    NIM = input("NIM                : ")
    Tugas = int(input("Nilai Tugas        : "))
    UTS = int(input("Nilai UTS          : "))
    UAS = int(input("Nilai UAS          : "))
    Akhir = (30 * Tugas / 100) + (35 * UTS / 100) + (35 * UAS / 100)
    data.append([Nama, NIM, Tugas, UTS, UAS, Akhir])
    ulangi = input("Tambah data (Y/T)? ")
    if ulangi.lower() == "t":
        break;

print("\nDaftar Nilai Akhir\n")
print("=================================================================================")
print("|     Nama      |      NIM      |   Tugas   |    UTS    |    UAS    |   Akhir   |")
print("=================================================================================")
for x in data:
    print("|    {0:10} |    {1:10} | {2:5}     | {3:5}     | {4:5}     | {5:7}   |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
print("=================================================================================")