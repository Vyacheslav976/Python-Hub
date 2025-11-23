def is_yesr_leap(year):
    if (year % 4 == 0):
        print(f"Год {year}: - True")
    else:
        print(f"Год {year}: - False")


is_yesr_leap(int(input("Введите год: ")))
