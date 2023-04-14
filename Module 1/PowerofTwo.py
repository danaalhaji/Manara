'''
*******Best Solution*********
    def isPowerOfTwo(n):
        if n==2 or n == 2 
        while n%2==0:
            n=n//2
        return True if n==1 else False
''' 
def isPoeeOfTwo(n):
    if n == 1 or n == 2:
        return 2
    elif (n/2)%2 == 0:
        for i in range(0,int(n/2)+1,1):
            if pow(2,i) == n :
                return True
                break
            else:
                continue
    else:
        return False