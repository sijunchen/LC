class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1): 
            return self.addStrings(num2, num1)

        assert(len(num1) >= len(num2))
              
        sum_str = ""
        sum_next = 0

       
        for index in range(1, (len(num2) +1)):
            sum_current = ord(num1[-index]) + ord(num2[-index]) - ord('0') - ord('0') 
             
            if sum_current + sum_next < 10:
                sum_str = str(sum_current + sum_next) + sum_str 
                sum_next = 0
            else:
                sum_str = str(sum_current + sum_next - 10) + sum_str 
                sum_next = 1
                sum_current = sum_str[0]

        if len(num1) == len(num2):
            if sum_next == 0:
                return sum_str
            return str(sum_next) + sum_str
                
        length_short = len(num2)

        while length_short != len(num1):
            for num in num1[-(length_short + 1)]:
                if sum_next == 1:
                    if (ord(num) - ord('0') == 9):
                        sum_current = 0
                        sum_next = 1
                        sum_str = str(sum_current) + sum_str
                    else:
                        sum_current = 1 + ord(num) - ord('0')
                        sum_next = 0
                        sum_str = str(sum_current) + sum_str
                        length_short += 1
                        continue
                if sum_next != 1:
                    sum_str = num + sum_str
                length_short += 1
        if sum_next == 1 and (ord(num) - ord('0') == 9):
            sum_str = str(sum_next) + sum_str
        return sum_str

def main():
    solution1 = Solution()
    num1 = '567'
    num2 = '1234'
    print(solution1.addStrings(num1, num2))

    solution1 = Solution()
    num1 = '5'
    num2 = '5'
    print(solution1.addStrings(num1, num2))

    solution1 = Solution()
    num1 = '0'
    num2 = '0'
    print(solution1.addStrings(num1, num2))

    solution1 = Solution()
    num1 = '9'
    num2 = '99'
    print(solution1.addStrings(num1, num2))

    solution1 = Solution()
    num1 = '9'
    num2 = '999'
    print(solution1.addStrings(num1, num2))

    solution1 = Solution()
    num1 = '408'
    num2 = '5'
    print(solution1.addStrings(num1, num2))

    solution1 = Solution()
    num1 = '19'
    num2 = '4'
    print(solution1.addStrings(num1, num2))



if __name__ == "__main__":
    main()


        
    