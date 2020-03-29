ue = input("かけられる数: ")
ue_num = int(ue)
ue_keta = input("かけられる数は何桁？(2~4桁まで): ")
ue_keta_num = int(ue_keta)
shita = input("かける数: ")
shita_num = int(shita)
shita_keta = input("かける数は何桁？(2~4桁まで): ")
shita_keta_num = int(shita_keta)

if ue_keta_num == 2 and shita_keta_num == 2:
    print(" " + str(ue_num))
    print("×" + str(shita_num))
    print("----")
    print(ue_num * shita_num)

elif ue_keta_num == 2 and shita_keta_num == 3:
    print("  " + str(ue_num))
    print("×" + str(shita_num))
    print("----")
    print(ue_num * shita_num)

elif ue_keta_num == 2 and shita_keta_num == 4:
    print("    " + str(ue_num))
    print("× " + str(shita_num))
    print("---------")
    print(ue_num * shita_num)

elif ue_keta_num == 3 and shita_keta_num == 3:
    print(" " + str(ue_num))
    print("×" + str(shita_num))
    print("-------")
    print(ue_num * shita_num)

elif ue_keta_num == 3 and shita_keta_num == 2:
    print(" " + str(ue_num))
    print("× " + str(shita_num))
    print("------")
    print(ue_num * shita_num)

elif ue_keta_num == 3 and shita_keta_num == 4:
    print("   " + str(ue_num))
    print("× " + str(shita_num))
    print("---------")
    print(ue_num * shita_num)

elif ue_keta_num == 4 and shita_keta_num == 4:
    print("  " + str(ue_num))
    print("× " + str(shita_num))
    print("---------")
    print(ue_num * shita_num)

elif ue_keta_num == 4 and shita_keta_num == 3:
    print("  " + str(ue_num))
    print("×  " + str(shita_num))
    print("---------")
    print(ue_num * shita_num)

elif ue_keta_num == 4 and shita_keta_num == 2:
    print("  " + str(ue_num))
    print("×   " + str(shita_num))
    print("---------")
    print(ue_num * shita_num)
