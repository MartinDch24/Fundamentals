list_of_integers = input().split()
n = int(input())
sorted_list = list_of_integers.copy()
sorted_list.sort(key=int)
removed_numbers = []

for i in range(n):
    removed_numbers.append(sorted_list[i])
for element in removed_numbers:
    list_of_integers.remove(element)

print(", ".join(list_of_integers))
