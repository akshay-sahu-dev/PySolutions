if __name__ == '__main__':

    n,m = map(int,input().split())

    for i in range(n):
        if i <= (n-3)/2:
            print("-"*int(((m-3)/2)-3*i)+".|."*(2*i+1)+"-"*int(((m-3)/2)-3*i))
        elif i == int(n-(n+1)/2):
            print("-"*int((m-7)/2)+"WELCOME"+"-"*int((m-7)/2))
        else:
            print("-"*int((m-3*(2*(n-i)-1))/2)+".|."*(2*(n-i)-1)+"-"*int((m-3*(2*(n-i)-1))/2))


## Input - 11 33            
##---------------.|.---------------
##------------.|..|..|.------------
##---------.|..|..|..|..|.---------
##------.|..|..|..|..|..|..|.------
##---.|..|..|..|..|..|..|..|..|.---
##-------------WELCOME-------------
##---.|..|..|..|..|..|..|..|..|.--- 
##------.|..|..|..|..|..|..|.------
##---------.|..|..|..|..|.---------
##------------.|..|..|.------------
##---------------.|.---------------
