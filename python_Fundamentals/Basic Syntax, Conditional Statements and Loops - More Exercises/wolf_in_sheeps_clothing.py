sheep_wolves = input().split(", ")
if sheep_wolves[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    if 0 <= sheep_wolves.index('wolf')-1 < len(sheep_wolves):
        print(f"Oi! Sheep number {len(sheep_wolves) - sheep_wolves.index('wolf')-1}! You are about to be eaten by a wolf!")
