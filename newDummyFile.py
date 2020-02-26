# cook your dish here
if __name__=="__main__":
    numOfTC = int(input())
    
    while(numOfTC>0):
        numOfTC-=1
        llen = int(input())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        A.sort()
        B.sort()
        sumOfDia=0
        for i in range(0,llen):
            sumOfDia  =sumOfDia + min(A[i],B[i])   
        print(sumOfDia)