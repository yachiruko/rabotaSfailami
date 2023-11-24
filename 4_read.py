#Чтение данных  из файла в массив
inputfile="input.csv"
a=[]
with open(inputfile,'r') as myfile:#открытие файла на чтение
       for line in myfile:
              print(line.strip())# строка без пробельных символов
              a.append(line.rstrip()) #добавление в массив без переноса строки \n
print(a)
count=len(a)
summ=0
for item in a:
       summ +=int(item)
sr=str(round(summ/len(a),2))
print('{:.2f}'.format(sum/count))
outputfile="result.txt"
result_file=open(outputfile,'a')
result_file.write(str(sr))
result_file.close()

