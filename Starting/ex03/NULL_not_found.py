import math

def NULL_not_found(object: any) -> int:
    """ 
        Bu fonksiyon, girdi olarak verilen nesnenin "Null" bir değer olup olmadığını kontrol eder.
        Eğer nesne None, NaN, 0, boş bir string ya da False ise, bu nesnenin türünü ve adını ekrana yazdırır.
        Eğer nesne bu "Null" türlerinden biri değilse, "Type not found" mesajını ekrana basar ve 1 değerini döndürür.
        Eğer nesne "Null" türlerinden biri ise, 0 değerini döndürür.
    """
    if object is None:
        print("Nothing: {} {}".format(object, type(object)))
    elif math.isnan(object):
        print("Cheese: {} {}".format(object, type(object)))
    elif object == 0:
        print("Zero: {} {}".format(object, type(object)))
    elif object == '':
        print("Empty: {} {}".format(object, type(object)))
    elif object == False:
        print("Fake: {} {}".format(object, type(object)))
    else:
        print("Type not Found")
        return 1
    return 0
