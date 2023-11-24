#Чтение из файла
#'r' -	открытие на чтение (является значением по умолчанию).

# open() – открывает файл
# сlose() – закрывает файл


inputfile="input.csv"
with open(inputfile,'r') as myfile:    #открытие файла на чтение
    summ=0
    for line in myfile:
        summ += int(line)
       #print(line, end="")
myfile.close()
print(summ)
