##함수 선언부
def add_func(n1,n2) :
    return n1+n2

def sub_func(n1,n2) :
    return n1-n2

def multi_func(n1,n2) :
    return n1*n2

def div_func(n1,n2) :
    return n1/n2

def sq_func(n1) :
    return n1**2

##전역 변수부
num1, num2, res = 100, 200, 0

##메인 코드부
res = add_func(num1, num2)
print(num1,'+',num2,'=',res)

res = sub_func(num1, num2)
print(num1,'-',num2,'=',res)

res = multi_func(num1, num2)
print(num1,'x',num2,'=',res)

res = div_func(num1, num2)
print(num1,'/',num2,'=',res)

res = sq_func(num1, num2)
print(num1,'x',num2,'=',res)