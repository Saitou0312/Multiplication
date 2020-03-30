print("(必ず読むこと) ズレは調整用のためです。気にしないでください。")
print("(必ず読むこと) 数字以外(Int型だとできます)入れないでください。エラーが出ます。String型にも対応していません。")
ue = input("かけられる数: ")
ue_num = int(ue)
ue_keta = input("かけられる数は何桁？(2~4桁まで): ")
ue_keta_num = int(ue_keta)
shita = input("かける数: ")
shita_num = int(shita)
shita_keta = input("かける数は何桁？(2~4桁まで): ")
shita_keta_num = int(shita_keta)
ue_num_num = str(ue_num)
shita_num_num = str(shita_num)

if ue_keta_num == 2 and shita_keta_num == 2:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    if shita_ichinokurai == 0:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-----")
        print(ue_num * shita_num)
    else:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-----")
        print("  " + str(ichiretu))
        print(niretu)
        print("-----")
        print(ue_num * shita_num)

elif ue_keta_num == 1 and shita_keta_num == 2:
    ue_ichinokurai = str(ue_num_num[-1])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyuunokurai = str(shita_num_num[-2])
    print("  " + str(ue_num))
    print("×  " + str(shita_num))
    print("-----")
    print(" " + str(ue_num * shita_num))

elif ue_keta_num == 2 and shita_keta_num == 1:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    shita_ichinokurai = str(shita_num_num[-1])
    print("  " + str(ue_num))
    print("×  " + str(shita_num))
    print("-----")
    print(" " + str(ue_num * shita_num))

elif ue_keta_num == 3 and shita_keta_num == 2:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    if shita_ichinokurai == 0:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-----")
    else:
        print(" " + str(ue_num))
        print("× " + str(shita_num))
        print("-------")
        print(" " + str(ichiretu))
        print("" + str(niretu))
        print("-------")
        print(ue_num * shita_num)

elif ue_keta_num == 3 and shita_keta_num == 1:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    print(" " + str(ue_num))
    print("×  " + str(shita_num))
    print("-------")
    print(ue_num * shita_num)

elif ue_keta_num == 3 and shita_keta_num == 3:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_hyakunokurai = str(shita_num_num[-3])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    shita_hyakunokuraihaint = int(shita_hyakunokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    sanretu = ue_num * shita_hyakunokuraihaint * 100
    if shita_ichinokurai == 0:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-----")
    else:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-------")
        print("  " + str(ichiretu))
        print(" " + str(niretu))
        print(sanretu)
        print("-------")
        print(ue_num * shita_num)

elif ue_keta_num == 4 and shita_keta_num == 3:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    if shita_ichinokurai == 0:
        print(" " + str(ue_num))
        print("× " + str(shita_num))
        print("-----")
    else:
        print(" " + str(ue_num))
        print("× " + str(shita_num))
        print("-------")
        print(" " + str(ichiretu))
        print(niretu)
        print("-------")
        print(ue_num * shita_num)

elif ue_keta_num == 4 and shita_keta_num == 2:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    if shita_ichinokurai == 0:
        print("  " + str(ue_num))
        print("×  " + str(shita_num))
        print("-----")
    else:
        print(" " + str(ue_num))
        print("×  " + str(shita_num))
        print("-------")
        print(" " + str(ichiretu))
        print(niretu)
        print("-------")
        print(ue_num * shita_num)

elif ue_keta_num == 4 and shita_keta_num == 4:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    ue_sennokurai = str(ue_num_num[-4])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_hyakunokurai = str(shita_num_num[-3])
    shita_sennokurai = str(shita_num_num[-4])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    shita_hyakunokuraihaint = int(shita_hyakunokurai)
    shita_sennokuraihaint = int(shita_sennokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    sanretu = ue_num * shita_hyakunokuraihaint * 100
    yonretu = ue_num * shita_sennokuraihaint * 1000
    if shita_ichinokurai == 0:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-----")
    else:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("----------")
        print("   " + str(ichiretu))
        print("  " + str(niretu))
        print(" " + str(sanretu))
        print(yonretu)
        print("----------")
        print(ue_num * shita_num)
