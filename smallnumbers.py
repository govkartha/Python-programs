# How Many Numbers Are Smaller Than the Current Number
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]

nums = list(map(int, input().split()))
a = []
for i in nums:
    a.append(sorted(nums).index(i))
print(a)

