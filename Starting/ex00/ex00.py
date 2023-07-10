ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"} 

ft_list[1] = "World!"               # Normal arraydir.
ft_tuple = ft_tuple[0], "Turkey!"   # Demetler değiştirilemez (immutable) olduğundan, yeni bir değerle yeni bir demet oluşturmalıyız.
ft_set = {"Hello", "Kocaeli!"}      # Kümeler değiştirilemez, bu yüzden eski kümemizi yeni bir küme ile değiştirdik.
ft_dict["Hello"] = "42Kocaeli!"     # Sözlükler, anahtar değer çiftlerini depolar ve bu çiftlerin değerleri değiştirilebilir.

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)