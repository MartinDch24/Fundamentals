deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_of_deck = len(deck) // 2
    left_part = deck[0:middle_of_deck]
    right_part = deck[middle_of_deck:]
    deck_after_shuffling = []

    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append((right_part[card_index]))
    deck = deck_after_shuffling

print(deck)