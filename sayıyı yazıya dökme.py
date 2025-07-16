
def ntob(number):
    sayı = ["","bir","iki","üç","dört","beş",
        "altı","yedi","sekiz","dokuz"]
    sayıs = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    if not (1000<= number <=9999):
        return "4 Basamaklı sayı giriniz"
    
    one = number % 10
    ten = (number // 10) % 10
    hundert = (number //100) % 10
    thousand = number // 1000
    result=""
    if(thousand>0):
        if(thousand>1):
            result+=f"{sayı[thousand]} bin "
        else:
            result+=" bin "
    if(hundert>0):
        if(hundert>1):
            result+=f"{sayı[hundert]} yüz "
        else:
            result+=" yüz "
    if(ten>0):
            result+=f"{sayıs[ten]} "
    if(one>0):
            result+=f"{sayı[ten]} "
    return result.strip()

number = int(input("4 basamaklı sayı gir"))
print(ntob(number))
