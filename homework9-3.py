first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

res_first = [len(x) for x in first]
res_second = [len(y) for y in second]
first_result = ((len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
second_result = ((len(first[i]) == len(second[i])) for i in range(len(first)))

print(res_first)
print(res_second)
print(list(first_result))
print(list(second_result))
