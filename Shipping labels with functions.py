def shipping_label(*args , **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if 'apt' in kwargs:
        print(f"{kwargs.get('street')},{kwargs.get('apt')}")
        print(f"{kwargs.get('city')},{kwargs.get('state')}")
        print(f"{kwargs.get('Pin')}")
    elif 'po_box' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('po_box')}")
        print(f"{kwargs.get('city')},{kwargs.get('state')}")
        print(f"{kwargs.get('Pin')}")
    else:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('city')},{kwargs.get('state')}")
        print(f"{kwargs.get('Pin')}")
        
shipping_label("Avatar","Aang","The Last Airbender",
                     street = "Air nomads",
                     po_box = "Air #100 PO",
                     city= "Appa's Domain",
                     state = "Air Nation",
                     Pin= "685506")