"""Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true."""


class Solution(object):
    def fizzBuzz(self, n):
        output = ["" for i in range(n)]
        for i in range(n):
            j = i + 1
            if j % 3 == 0:
                output[i] += "Fizz"
            if j % 5 == 0:
                output[i] += "Buzz"
            if not output[i]:
                output[i] += str(j)
        return output


# Runtime: 39ms | Memory Usage: 14.2 MB
