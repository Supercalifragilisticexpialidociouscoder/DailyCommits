"""#arr=[2,3,4,5,6,7]
def prefix_sum(arr):
    n=len(arr)
    prefix=[0]*n
    prefix=[0]=arr[0]
    #prefix[1]=prefix[0]+arr[1]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+arr[i]
        #prefix[1]=prefix[0]=arr[1]
        #prefix[1]=2+3 -->5
        return prefix
    #example
    arr[2,3,4,5,6,7,8]
    print(prefix_sum(arr))"""


#create an array
n=int(input("Enter number of elements: "))#arr=[2,3,4,5,6,7]
#read the input #prefix=[2,5,9,14,20]
arr=list(map(int,input("Enter the elements: ").split()))
prefix=[0]*n
prefix[0]=arr[0] #2
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
        #print("Prefix sum is",prefix)
        #sum query
    start=int(input("Enter starting index: "))
    end=int(input("Enter ending index: "))
    if start == 0:
        res = prefix[end]
    else:
        res = prefix[end] - prefix[start-1]
    print(f"the sum value of {start} and {end} is {res}")

    