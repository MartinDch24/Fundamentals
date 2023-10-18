factor = int(input())
count = int(input())
multiples_of_the_factor = []

for number in range(1, count + 1):
    multiples_of_the_factor.append(number*factor)
print(multiples_of_the_factor)
