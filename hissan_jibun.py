ue = input("かけられる数: ")
ue_num = int(ue)
ue_keta = input("かけられる数は何桁？(1~4桁まで): ")
ue_keta_num = int(ue_keta)
shita = input("かける数: ")
shita_num = int(shita)
shita_keta = input("かける数は何桁？(1~4桁まで): ")
shita_keta_num = int(shita_keta)
kotae = ue_num * shita_num

if ue_keta_num == 2 and shita_keta_num == 2:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("× " + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 2 and shita_keta_num == 3:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×" + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 2 and shita_keta_num == 4:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×    " + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 3 and shita_keta_num == 3:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×    " + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 3 and shita_keta_num == 2:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×  " + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 3 and shita_keta_num == 4:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×    " + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 4 and shita_keta_num == 4:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×    " + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 4 and shita_keta_num == 3:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×    " + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 4 and shita_keta_num == 2:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×    " + str(shita_num))
    print("---------")
    print(youranswer_num)

elif ue_keta_num == 4 and shita_keta_num == 1:
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    print("  " + str(ue_num))
    print("×    " + str(shita_num))
    print("---------")
    print(youranswer_num)
