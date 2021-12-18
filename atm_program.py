import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    pin = int(input("Masukkan pin anda: "))
    tries = 0
    while pin != int(atm.GetCustID()) and tries < 3:
        id = int(input("Pin anda salah. Silahkan Masukkan lagi: "))
        tries += 1

        if tries == 3:
            print("Error. Silahkan ambil kartu dan coba lagi..")
            exit()

