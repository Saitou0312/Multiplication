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
    niretu = list(str(ue_num * shita_jyunokuraihaint * 10))
    niretu[-1] = ' '
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
        niretu_answer = ''
        for i in range(len(niretu) - 1):
            niretu_answer += niretu[i]
        print(" " + str(niretu_answer))
        print("-----")
        print(" " + str(ue_num * shita_num))

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
    niretu = list(str(ue_num * shita_jyunokuraihaint * 10))
    sanretu = list(str(ue_num * shita_hyakunokuraihaint * 100))
    niretu[-1] = ''
    sanretu[-1] = ''
    sanretu[-2] = ''
    niretu_answer = ''
    sanretu_answer = ''
    if shita_ichinokurai == 0:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-----")
    else:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-------")
        print("  " + str(ichiretu))
        for i in range(len(niretu) - 1):
            niretu_answer += niretu[i]
        print(" " + str(niretu_answer))
        for i in range(len(sanretu) - 1):
            sanretu_answer += sanretu[i]
        print(sanretu_answer)
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
    niretu = list(str(ue_num * shita_jyunokuraihaint * 10))
    sanretu = list(str(ue_num * shita_hyakunokuraihaint * 100))
    yonretu = list(str(ue_num * shita_sennokuraihaint * 1000))
    niretu[-1] = ''
    sanretu[-1] = ''
    sanretu[-2] = ''
    yonretu[-1] = ''
    yonretu[-2] = ''
    yonretu[-3] = ''
    niretu_answer = ''
    sanretu_answer = ''
    yonretu_answer = ''
    if shita_ichinokurai == 0:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("-----")
    else:
        print("   " + str(ue_num))
        print("×  " + str(shita_num))
        print("----------")
        print("   " + str(ichiretu))
        for i in range(len(niretu) - 1):
            niretu_answer += niretu[i]
        print("  " + str(niretu_answer))
        for i in range(len(sanretu) - 1):
            sanretu_answer += sanretu[i]
        print(" " + str(sanretu_answer))
        for i in range(len(yonretu) - 1):
            yonretu_answer += yonretu[i]
        print(yonretu_answer)
        print("----------")
        print(ue_num * shita_num)

elif ue_keta_num == 5 and shita_keta_num == 5:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    ue_sennokurai = str(ue_num_num[-4])
    ue_ichimannnokurai = str(ue_num_num[-5])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_hyakunokurai = str(shita_num_num[-3])
    shita_sennokurai = str(shita_num_num[-4])
    shita_ichimannnokurai = str(shita_num_num[-5])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    shita_hyakunokuraihaint = int(shita_hyakunokurai)
    shita_sennokuraihaint = int(shita_sennokurai)
    shita_ichimannnokuraihaint = int(shita_ichimannnokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    sanretu = ue_num * shita_hyakunokuraihaint * 100
    yonretu = ue_num * shita_sennokuraihaint * 1000
    goretu = ue_num * shita_ichimannnokuraihaint * 10000
    if shita_ichinokuraihaint == 0:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("---------")
        print(ue_num * shita_num)
    else:
        print("  " + str(ue_num))
        print("× " + str(shita_num))
        print("----------")
        print("    " + str(ichiretu))
        print("   " + str(niretu))
        print("  " + str(sanretu))
        print(" " + str(yonretu))
        print(goretu)
        print("----------")
        print(ue_num * shita_num)

elif ue_keta_num == 5 and shita_keta_num == 2:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    ue_sennokurai = str(ue_num_num[-4])
    ue_ichimannnokurai = str(ue_num_num[-5])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    if shita_ichinokuraihaint == 0:
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(ue_num * shita_num)
    else:
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("----------")
        print(" " + str(ichiretu))
        print(niretu)
        print("----------")
        print(ue_num * shita_num)

elif ue_keta_num == 5 and shita_keta_num == 3:
    ue_ichinokurai = str(ue_num_num[-1])
    ue_jyunokurai = str(ue_num_num[-2])
    ue_hyakunokurai = str(ue_num_num[-3])
    ue_sennokurai = str(ue_num_num[-4])
    ue_ichimannnokurai = str(ue_num_num[-5])
    shita_ichinokurai = str(shita_num_num[-1])
    shita_jyunokurai = str(shita_num_num[-2])
    shita_ichinokuraihaint = int(shita_ichinokurai)
    shita_jyunokuraihaint = int(shita_jyunokurai)
    ichiretu = ue_num * shita_ichinokuraihaint
    niretu = ue_num * shita_jyunokuraihaint * 10
    if shita_ichinokuraihaint == 0:
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("---------")
        print(ue_num * shita_num)
    else:
        print("  " + str(ue_num))
        print("×    " + str(shita_num))
        print("----------")
        print(" " + str(ichiretu))
        print(niretu)
        print("----------")
        print(ue_num * shita_num)
