import sys

def check_odd_even(number: int):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

def main():
    args = sys.argv[1:]  # İlk argüman, betiğin kendisidir. Bu yüzden onu atlıyoruz.
    
    if len(args) != 1:  # Eğer bir argümandan fazla veya hiç argüman verilmişse,
        raise AssertionError("more than one argument is provided or no argument is provided")
    
    try:
        number = int(args[0])  # Argümanı tam sayıya dönüştürmeye çalışıyoruz.
    except ValueError:  # Eğer dönüştürme başarısız olursa, bir AssertionError oluşturuyoruz.
        raise AssertionError("argument is not an integer")
    
    check_odd_even(number)  # Tam sayıyı kontrol etmek için check_odd_even fonksiyonunu çağırıyoruz.

""" yukarı yazdığım kod kendi kendine çalışan bir script bu dosyayı import alanlarda otomatik hemen çalışmasın diye böyle birşey. """
if __name__ == "__main__":
    main()
