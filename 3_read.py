# метод readline():
# – позволяет считать одну строку из файла и сохранить в строке;
# - имеет необязательный аргумент: количество символов, которое необходимо считать.

inputfile="input.csv"
myfile=open(inputfile,'r')#открытие файла на чтение
data = myfile.readline()
print(data)
data = myfile.readline()
print(data)
myfile.close()
