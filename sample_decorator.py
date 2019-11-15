def multiply_decorator(func):
    def mul(*num):
        ans=func(*num)
        return ans
    return mul

@multiply_decorator
def get_result(num):
    return num*num
print(get_result(2))
