filepath = "valaszok.txt"
fileobject = open(filepath, "r")
read_file = fileobject.read()
print("1. feladat: Az adatok beolvasva.")
fileobject.close()

fileobject = open(filepath, "r")
lines = fileobject.readlines()
print("2. feladat: A versenyen ", len(lines)-1, " versenyző indult.")

only_answers = "valaszok_csak.txt"
search = open(only_answers, "r")
search_lines = search.readline()


answer = input("3. feladat: Kérem adja meg a versenyző azonosítóját: ")
if answer in search:

else:

