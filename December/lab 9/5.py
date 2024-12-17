numbers = [1,2,3,4,5,6,8]
n = len(numbers) + 1
maybesum = n * (n + 1) // 2 #use formula to find theoretical sum
sum = sum(numbers)
print("The missing number is:", maybesum - sum) #subtract theoretical from actual sum to find missing number
