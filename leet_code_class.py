#136
#var1
class Solution:
    def __init__(self, total: int):
        self.list_of_numbers = []
        self.total = total

    def add_numbers(self) -> list:
        for i in range(1, self.total+1):
            n = int(input('Введите число от 1 до 50: '))
            self.list_of_numbers.append(n)
        return self.list_of_numbers

    def simpleNumber(self) -> int:
        result = 0
        for num in self.list_of_numbers:
            result ^= num
        return result

result = Solution(5)
print(result.add_numbers())
print(result.simpleNumber())

#var2
class Soss:

    def __init__(self):
        self.result = 0
    def unique_one(self, numbers):
        for i in numbers:
            self.result ^= i
        return self.result

#numbers = [1, 2, 7, 2, 1]
#fe = Soss(numbers)
#print(fe.unique_one())

#var3
def unique_one(numbers) -> int:
    result = 0
    for i in numbers:
        result ^= i
    return result

#numbers = [1, 2, 4, 2, 1]
#ff = unique_one(numbers)
#print(ff)