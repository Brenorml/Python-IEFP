fich = open("hours.txt")
print("read(): \n", fich.read())

input = open("hours.txt")
print("readline(): \n", input.readline())

outro = open("hours.txt")
print("readlines(): \n", outro.readlines())

novo = open("hours.txt")
for line in novo:
    print("---------------------------------")
    print(line.strip())

#-------------------------------------------------------------------------------------------------------------
def input_stats(filename):
    input = open(filename)
    count = 0
    longest = ''
    for line in input:
        if len(line) > len(longest):
            longest = line
            count += 1
    print('longest line = ', len(longest))
    print("A linha mais longa é a ", count , " = ", longest)

input_stats("carroll.txt")

name = "Brave Sir Robin"
for word in name.split():
    print(word)

"LL".join(name.split("r"))
"LL".join(name.split("R"))

input = open("hours.txt")
for line in input:
    id, name, mon, tue, wed, thu, fri = line.split()

    hours = float(mon) + float(tue) + float(wed) + float(thu) + float(fri)

    print(name, "ID", id, "worked", hours, "hours: {0:.2f} / day".format(hours/5))

# -------------------------------------------------------------------------------------------------------------

import os
cwd = os.getcwd()
print("**********************\n", cwd, "\n*************************")

fich = open("hours.txt")
ficheiro = fich.read()
print(ficheiro)
print("****************************************")
for i in ficheiro:
    print(i, sep = " ", end = " ")
print("****************************************")

fich = open("hours.txt")
print("read():\n", fich.read())
print("ficheiro:\n", ficheiro)

fich = open("hours.txt")
print("readline():\n", fich.readline())
print("readlines():\n", fich.readlines())

fich = open("hours.txt")
fichLista = fich.readlines()
print(fichLista)

for i in fichLista:
    print(i)

fich = open("hours.txt")
for line in fich:
    print(line.strip())