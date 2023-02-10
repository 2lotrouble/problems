class Solution(object):
    def twoSum(self, numbers, target):
        dic = {}
        for i in range(len(numbers)):
            sec = target - numbers[i]  # разница если 2 то запись 7
            if (numbers[i] in dic.keys()):
                return sorted([i + 1, dic[numbers[i]] + 1])

            dic.update({sec: i})
