electrons = int(input())
shells = []
for shell in range(1, electrons + 1):
    max_electrons_in_current_shell = 2 * shell ** 2
    if electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
        electrons -= max_electrons_in_current_shell
        if electrons == 0:
            break
    else:
        shells.append(electrons)
        break
print(shells)
