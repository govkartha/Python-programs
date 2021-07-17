#Hotel Bookings Possible - interviewbit
#https://www.interviewbit.com/problems/hotel-bookings-possible/
'''A hotel manager has to process N advance bookings of rooms for the next season. 
His hotel has C rooms. Bookings contain an arrival date and a departure date. 
He wants to find out whether there are enough rooms in the hotel to satisfy the demand.'''

def roomavail(arr,dep,k):
    arr.sort()
    dep.sort()
    n = len(arr)
    i,j,c = 0,0,0
    while(i<n and j<n):
        if(arr[i]<dep[j]):
            i += 1
            c += 1
            if(c > k):
                return False
        else:
            j += 1
            c -= 1
    return True


arr = list(map(int,input().split()))
dep = list(map(int,input().split()))
k = int(input())
print(roomavail(arr,dep,k))

