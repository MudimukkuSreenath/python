def result(n):
    for num in range(n):
        if num % 3 == 0:
            print("hello",end="")
        elif num % 5== 0:
            print("world",end="")
        elif num % 3 == 0 and num % 5 == 0:
            print("hello world",end="")
        else:
            pass
            
if __name__=="__main__":
    n=500
    result(n)
