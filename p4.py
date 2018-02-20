def latinika(num):
    r=[]
    if num >= 1000 :
        r.append(num//1000*"M")
        num=num%1000
    if num >= 900 :
        r.append(num//900*"CM")
        num=num%900
    if num >= 500 :
        r.append(num//500*"D")
        num=num%500
    if num >= 400 :
        r.append(num//400*"CD")
        num=num%400
    if num >= 100 :
        r.append(num//100*"C")
        num=num%100
    if num >= 90 :
        r.append(num//90*"XC")
        num=num%90
    if num >= 50 :
        r.append(num//50*"L")
        num=num%50
    if num >= 40 :
        r.append(num//40*"XL")
        num=num%40
    if num >= 10 :
        r.append(num//10*"X")
        num=num%10
    if num >= 9 :
        r.append(num//9*"IX")
        num=num%9
    if num >= 5 :
        r.append(num//5*"V")
        num=num%5
    if num >= 4 :
        r.append(num//4*"IV")
        num=num%4
    else :
        r.append(num*"I")

    print r
                                                #den vrika tropo na ta tiponi stin idia grammi prospathisa na valo se lista
                                                #kai me to for pou ekana apla ta tiponi katheta
    for r in r: print r

x=input()
latinika(x)
