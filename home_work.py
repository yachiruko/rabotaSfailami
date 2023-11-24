# Есть файл «input.txt», который содержит текст
# (включая буквы, цифры и другие видимые символы.
# Пробельных символов в тексте нет).
# Напишите программу, которая подсчитывает количество каждого из символов,
# а далее записывает эти данные в файл «answer.txt»
# Формат записи:  «буква: количество».
file=open("input.txt", 'r', encoding='utf-8')
data=file.read()
arr=[]
for line in data.readline():
    if line not in arr:
        arr.append(line)
    print(arr)
for item in arr:
    print(f"{item}:{data.count(item)}")
    file.close()