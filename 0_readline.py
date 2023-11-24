#Чтение из файла
#'r' -	открытие на чтение (является значением по умолчанию).

# open() – открывает файл
# сlose() – закрывает файл
# метод readlines() – позволяет считать все строки из файла и сохранить их в список.
inputfile="input.csv"
file=open(inputfile)
data=file.readlines()
print(file)
print(data)
file.close()
