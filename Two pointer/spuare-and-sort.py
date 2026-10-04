nums=[-7,-3,2,3,11]
left=0
right=len(nums)-1
i=len(nums)-1
result=[0]*len(nums)
while left<=right:
    if nums[left]**2<nums[right]**2:
        result[i]=nums[right]**2
        right-=1
    elif nums[right]**2<nums[left]**2:
        result[i]=nums[left]**2
        left+=1
    else:
        result[i]=nums[right]**2
        right-=1
    i-=1
    
print(result)