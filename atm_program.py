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

    while True:
        print("Selamat datang di ATM Progate..\n")
        print("1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar\n")
        choice = int(input("Silahkan pilih menu: "))
        if choice == 1:
            print("\nSaldo anda sekarang: Rp. " + str(atm.GetCustBalance()) + "\n")
        elif choice == 2:
            nominal = float(input("Masukkan nominal yang ingin ditarik: "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet sebesar " + str(nominal) + " ? y/n")
            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.GetCustBalance()))
            else:
                break

            if nominal < int(atm.GetCustBalance()):
                atm.Withdraw(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo anda tersisa " + str(atm.GetCustBalance()) + "\n")
            else:
                print("Maaf. Saldo anda tidak mencukupi")
                print("Silahkan lakukan penambahan saldo")
        elif choice == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan sebesar " + str(nominal) + " ? y/n")

            if verify_withdraw == "y":
                atm.Deposit(nominal)
                print("Saldo anda sekarang adalah: " + atm.GetCustBalance() + "\n")
            else:
                break
        elif choice == 4:
            checkPin = int(input("Masukkan pin anda: "))
            while checkPin != int(atm.GetCustPin()):
                checkPin = int("Pin anda salah, silahkan masukkan pin: ")
            newPin = int(input("Silahkan masukkan pin baru: "))
            print("Pin anda berhasil diganti!")

            checkNewPin = int(input("Coba masukkan pin baru: "))

            if checkNewPin == newPin:
                print("Pin baru anda sukses!")
            else:
                print("Maaf, pin anda salah!")
        elif choice == 5:
            print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.GetCustBalance())
            print("Terima kasih telah menggunakan ATM Progate!")
            exit()
        else:
            print("Error. Maaf, menu tidak tersedia")
        
