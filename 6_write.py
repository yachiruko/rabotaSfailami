# запись в файл(2 способ - запись построчно)
#'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
#'x'	открытие на запись, если файла не существует, иначе исключение.
#'a'	открытие на дозапись, информация добавляется в конец файла.

# write - оператор записи информации в файл

inputfile="input.csv"
outputfile="result.txt"
myfile=open(inputfile,'r')#открытие файла на чтение
result_file=open(outputfile,'w')#открытие файла на запись
for line in myfile:
   	result_file.write(line)
myfile.close()
result_file.close()
