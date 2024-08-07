class Solution:
    def numberToWords(self, num: int) -> str:
        def helper(a):
            digit_str = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            teen_str = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            ten_str = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

            result = ""
            
            if a > 99:
                result += digit_str[a // 100] + " Hundred "
            
            a = a % 100
            if 9 < a < 20:
                result += teen_str[a - 10] + " "
                a = a % 10
            else:
                if a >= 20:
                    result += ten_str[a // 10] + " "
                a = a % 10
                if a > 0:
                    result += digit_str[a] + " "
            
            return result
        

        if num == 0:
            return "Zero"

        big_str = ["Thousand", "Million", "Billion"]
        result = helper(num % 1000)
        num //= 1000

        for i in range(len(big_str)):
            if num > 0 and num % 1000 > 0:
                result = helper(num % 1000) + big_str[i] + " " + result
            num //= 1000
        
        return result.strip()
