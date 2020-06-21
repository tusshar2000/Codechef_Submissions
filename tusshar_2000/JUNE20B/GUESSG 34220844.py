from sys import *
out1=stdout.flush
n=int(input())
def main():
    low=1
    high=n
    while True:
        if high-low<4:
            break
        # print(low,high)
        mid=(low+high)//2
        one_fourth=(low+mid)//2
        three_fourth=(mid+high)//2
        print(one_fourth)
        out1()
        one_fourth_inp=input()
        if one_fourth_inp=="E":
            return
        print(mid)
        out1()
        mid_inp=input()
        if mid_inp=="E":
            return
        print(three_fourth)
        out1()
        three_fourth_inp=input()
        if three_fourth_inp=="E":
            return
        total=one_fourth_inp+mid_inp+three_fourth_inp
        if total=="LLL":
            high=mid-1
        elif total=="LLG":
            high=three_fourth-1
        elif total=="LGL":
            low-=1
        elif total=="LGG":
            low=one_fourth+1
        elif total=="GLL":
            high=three_fourth-1
        elif total=="GLG":
            high+=1
        elif total=="GGL":
            low=one_fourth+1
        elif total=="GGG":
            low=mid+1

    for ii in range(low,high+1):
        print(ii)
        out1()
        inpp=input()
        if inpp=="E":
            return

if __name__== "__main__":
    main()
