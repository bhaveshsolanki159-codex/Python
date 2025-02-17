def is_prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)):
        if (n%i==1):
            return False
    return True
    
def reverse_str(s):
    return s[::-1]
    

def is_palindrone(n):
    n=str(n)
    return n==n[::-1]

def sqr(n,m=2):
    return n**m

def circle(r):
    area = 3.14*(r**2)
    circum = 2*3.14*r
    return area, circum
# a,c = circle(2)
# print("area :",a,"circumfrence :",c)

# using lambda functions, Q. find cube of number

cube = lambda x : x**3 # here x is parameter and one time use only

def sum_all(*args):
    print(args) #*args convert multiple values into tuples
    return sum(args)

def is_armstrong(num):
    num_str = str(num)
    pow = len(num_str)
    n =0
    for i in num_str:
        n = int(i)**pow + n
    return n==num
      
def find_max(a,b,c):
    if(a>b & b>c):
        return a
    elif(b>a & a>c):
        return b
    else:
        return c

def sum_list(list):
    sum=0
    l=len(list)
    for i in range(0,l):
        sum=sum+list[i]
    return sum
    
def multiply_list(l1,l2):
    result =[a*b for a,b in zip(l1,l2)]
    return result

# movies =[]
# mov1 = input("enter mov1: ")
# mov2 = input("enter mov2: ")
# mov3 = input("enter mov3: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)
movies=[1,2,3,2,3]

l = len(movies)
for i in range(1,l):
    if(movies[i-1]==movies[l-i]):
        continue
    else:
        print("not a palindrone list")
        break
    print("palindrone") 











 










        




    


    


    