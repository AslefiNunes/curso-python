print(20 * "-")
print("BANGU X MADUREIRA")
print(20 * "-")
bag = int(input("Quantos gol fez BANGU: "))
mad = int(input("Quantos gol fez MADUREIRA: "))

difer = bag - mad

print(20 * "-")
if difer < 0:
    difer = difer * -1
    print(f"O BANGU perdeu por {difer} gol(s) de diferença")
elif difer == 0:
    print("")
else:
    print(f"O BANGU ganhou por {difer} gol(s) de diferença")


match difer:
    case 0:
        print("Empate")
    case 1:
        print("Partida Normal")
    case 2:
        print("Partida Normal")
    case 3:
        print("Partida Normal")
    case _:
        print("Goleada")
print(20 * "-")