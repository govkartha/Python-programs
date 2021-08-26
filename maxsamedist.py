#Maximum distance between two occurrences of same element in array
#Given an array with repeated elements, the task is to find the maximum distance two occurrences of an element.

st = "".join(input().split())
m = -1
for i in st:
    n = st.rfind(i) - st.find(i)
    m = max(m,n)
print(m)