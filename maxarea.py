#Container With Most Water - Leetcode
#https://leetcode.com/problems/container-with-most-water/
#Given n non-negative integers a1, a2, ..., an, 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

height = list(map(int,input().split()))
left,right,mx = 0,len(height)-1,-1
while(left<right):
    mx = max(mx,(right-left)*min(height[left],height[right]))
    if(height[left]<height[right]):
        left += 1
    else:
        right -= 1
print(mx)