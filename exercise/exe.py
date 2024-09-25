f = open("./titanic.csv")

lines = f.readlines()

datas = []

for line in lines:
    data = line.split(",")
    datas.append(data)


print(datas)
