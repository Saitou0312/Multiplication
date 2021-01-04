def hissan(ue, ue_keta, shita, shita_keta):
    print(" " + str(ue))
    print("×  " + str(shita))
    print("-" * (ue_keta + shita_keta))
    print(ue * shita)

ue = int(input("かけられる数: "))
ue_keta = len(str(ue))
shita = int(input("かける数: "))
shita_keta = len(str(shita))

hissan(ue, ue_keta, shita, shita_keta)
