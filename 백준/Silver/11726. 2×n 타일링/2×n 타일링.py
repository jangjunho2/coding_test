nums = [0] * (1000+1)
nums[1] = 1  # 2*1 인 경우  #1가지
nums[2] = 2  # 2*2 인 경우  #2가지

n = int(input())

for i in range(3, n+1):
    nums[i] = nums[i-1]+nums[i-2]


print(nums[n] % 10007)
