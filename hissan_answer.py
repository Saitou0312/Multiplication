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
    print(" " + str(ue_num))
    print("×" + str(shita_num))
    print("----")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    elif not youranswer == kotae:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 2 and shita_keta_num == 3:
    print("  " + str(ue_num))
    print("×" + str(shita_num))
    print("----")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 2 and shita_keta_num == 4:
    print("    " + str(ue_num))
    print("× " + str(shita_num))
    print("---------")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 3 and shita_keta_num == 3:
    print(" " + str(ue_num))
    print("×" + str(shita_num))
    print("-------")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 3 and shita_keta_num == 2:
    print(" " + str(ue_num))
    print("× " + str(shita_num))
    print("------")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 3 and shita_keta_num == 4:
    print("   " + str(ue_num))
    print("× " + str(shita_num))
    print("---------")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 4 and shita_keta_num == 4:
    print("  " + str(ue_num))
    print("× " + str(shita_num))
    print("---------")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 4 and shita_keta_num == 3:
    print("  " + str(ue_num))
    print("×  " + str(shita_num))
    print("---------")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 4 and shita_keta_num == 2:
    print("  " + str(ue_num))
    print("×   " + str(shita_num))
    print("---------")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)

elif ue_keta_num == 4 and shita_keta_num == 1:
    print("  " + str(ue_num))
    print("×    " + str(shita_num))
    print("---------")
    youranswer = input("答えを入れてください: ")
    youranswer_num = int(youranswer)
    if kotae == youranswer_num:
        print("正解！")
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
    else:
        print("答えは" + str(kotae) + "です")
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(kotae)
