if __name__ == '__main__':
    n = int(input())
    nummap=map(int,input().split())
    numlist=[k for k in nummap]
    numlist.sort(reverse=True)
    print(numlist)