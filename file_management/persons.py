from io import open

file = open('persons.txt', 'r', encoding="utf8")
lines = file.readlines()
file.close()

persons = []
for line in lines:
    data = line.replace("\n", "").split(";")
    person = {"id": data[0], "name": data[1], "surname": data[2], "birth": data[3]}
    persons.append(person)

for p in persons:
    print("(id={}) {} {} => {} ".format(p['id'], p['name'], p['surname'], p['birth']))
