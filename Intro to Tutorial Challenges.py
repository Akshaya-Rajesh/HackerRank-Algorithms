#!/binimport sys

def introTutorial(V, arr):
    for i in range(0,n):
        if(arr[i]==V):
            return(i)
    return(-1)

if __name__ == "__main__":
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = introTutorial(V, arr)
    print(result)
