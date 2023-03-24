# 12. Integer to Roman (Numeral)

# Given an integer, convert it to a roman numeral.

# Works, runtime 53.42nd percentile, 68.48th for memory
class Solution:
    def intToRoman(self, num: int) -> str:
        thous = num - (num % 1000)
        huns = num - thous - (num % 100)
        tens = num - thous - huns - (num % 10)
        units = num % 10
        roman = ""
        for m in range(thous // 1000):
            roman = roman + "M"
        if huns > 0:
            if huns == 900:
                roman = roman + "CM"
            elif huns >= 500:
                roman = roman + "D"
                huns -= 500
                for c in range(huns // 100):
                    roman = roman + "C"
            elif huns == 400:
                roman = roman + "CD"
            elif huns < 400:    # else?
                for c in range(huns // 100):
                    roman = roman + "C"
        if tens > 0:
            if tens == 90:
                roman = roman + "XC"
                tens -= 90
            elif tens >= 50:
                roman = roman + "L"
                tens -= 50
            elif tens == 40:
                roman = roman + "XL"
                tens -= 40
            for x in range(tens // 10):
                roman = roman + "X"
        if units > 0:
            if units == 9:
                return roman + "IX"
            elif units == 4:
                return roman + "IV"
            elif units >= 5:
                roman = roman + "V"
                units -= 5
            for i in range(units):
                roman = roman + "I"
        return roman