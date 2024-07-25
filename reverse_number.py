def number(given_number):
    a = (given_number//10000)
    b = ((given_number//1000)%10)
    c = ((given_number//100)%10)
    d = ((given_number//10)%10)
    e = (given_number%10)
    new_number = e*10000 + d*1000 + c*100 + b*10 + a*1
    print(new_number)

number(12345)