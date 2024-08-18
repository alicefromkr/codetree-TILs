from decimal import Decimal, getcontext

def divide_and_truncate(a, b):

    # 소수점 21자리 precision 설정 
    getcontext().prec = 21

    # 나누기 
    result = a/b
    
    # 문자열로 변환 
    result_str = str(result).split(".")

    # 정수 
    number = result_str[0]
    # 소수점
    decimal_part = result_str[1]
    
    if len(decimal_part) < 21:
        n = len(decimal_part)
        decimal_part = decimal_part.ljust(20, '0')
    else:
        decimal_part = decimal_part[:20]

    return number + '.' + decimal_part

nlist = input("").split(" ")
a = Decimal(nlist[0])
b = Decimal(nlist[1])
print(divide_and_truncate(a,b))