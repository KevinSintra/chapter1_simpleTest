class SimpleParser:
    def parseAndSum(self, numbers):
        if not numbers: # 判斷是否為 null or empty
            return 0
        elif ',' not in numbers :
            return int(numbers)
        
        return sum((int(number) for number in numbers.split(',')))
