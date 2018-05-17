class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        ones = num % 10
        tens = num % 100 // 10
        hundreds = num % 1000 // 100
        thousands = num % 10000 // 1000

        return '{}{}{}{}'.format(
            self.convert(thousands, ['M', '', '']),
            self.convert(hundreds, ['C', 'D', 'M']),
            self.convert(tens, ['X', 'L', 'C']),
            self.convert(ones, ['I', 'V', 'X'])
        )

    def convert(self, num, mapping):
        if num == 0:
            return ''
        elif num < 4:
            return mapping[0] * num
        elif num == 4:
            return mapping[0] + mapping[1]
        elif num == 5:
            return mapping[1]
        elif 5 < num < 9:
            return mapping[1] + mapping[0] * (num - 5)
        else:
            return mapping[0] + mapping[2]
