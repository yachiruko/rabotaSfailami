#Записать в файл т случайных чисел
import random
outputfile="result.txt"
result_file=open(outputfile,'a')
c=int(input("Введите число:"))
numbers =[]
for sum in range(c):
    numbers.append(random.randint(0,100))
    result_file.write(str(random.randint(0,100))+"\n")
result_file.write(str(numbers))
result_file.close()

outputfile='result.txt'
result_file=open(outputfile,'a')
result_file.write(str(sum(numbers)))
result_file.close()

