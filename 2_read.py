#Чтение из файла
#'r'	открытие на чтение (является значением по умолчанию).

# метод read() :
# - позволяет считать все содержимое файла и сохранить в строке
# - сохраняет исходное форматирование файла.
# - имеет необязательный аргумент: количество символов, которое необходимо считать.


inputfile="input.csv"
myfile=open(inputfile,'r')  #открытие файла на чтение
content = myfile.read()
print(content)
myfile.close()

with open(inputfile,'r') as myfile:#открытие файла на чтение
    content = myfile.read()
    print(content)
myfile.close()