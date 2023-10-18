def loading_bar(number)-> str:
    if number == 100:
        return f"{number}% Complete!\n[%%%%%%%%%%]"
    loaded_percentage = number // 10
    return f"{number}% [{'%' * loaded_percentage}{'.' * (10 - loaded_percentage)}]\nStill loading..."


percentage = int(input())
print(loading_bar(percentage))
