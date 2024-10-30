# kun = input("Bugun qaysi kun:  ")
# harorat = float(input("Bugun kunning harorati nechiga teng: "))

# if(kun.lower == 'Shanba' or 'Yakshanba') and (harorat >= 30 ):
#     print("Cho'milishga ketdik")
# elif (kun.lower == 'Shanba' or 'Yakshanba') and (harorat < 30):
#     print ("Cho'milishga bormaymiz!")



# osh = 20000
# salat = True
# choy = False

# if choy and salat :
#     print(f"{osh + 10000 } bo'ldi")
# elif choy or salat :
#     print (f"{osh + 5000 } bo'ldi")



# kalbasa = 25000
# choy = True
# non = True
# salat = False
# cola= 0
# assorti = True

# if kalbasa:
#     print("Kalbasa oldingiz")
#     narx = kalbasa
# if choy:
#     print("Choy oldingiz" )
#     narx= narx + 5000
# if non:
#     print("Non oldingiz")
#     narx = narx + 15000
# if salat:
#     print("Salat oldingiz")
#     narx = narx + 5000
# if cola:
#     print("Siz cola oldingiz")
#     narx = narx + 15000
# if assorti :
#     print("Siz assorti oldingiz")
#     narx = narx +50000

# print(f"Jami summa: {narx}")

menu = ['osh','sho\'rva','shashlik', 'somsa','chuchvara','baliq']
buyurtmalar = ['baliq','shashlik', 'manti','lavash']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Bizda  {taom} bor")
        else :
            print(f"Bizda  {taom} yo'q")
else :
    print('Savatchangiz bo\'sh')



    
    

