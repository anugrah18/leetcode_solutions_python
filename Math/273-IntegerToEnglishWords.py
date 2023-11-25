class Solution:
    def numberToWords(self,num):
        under_twenty = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
                        'Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen',
                        'Eighteen','Nineteen']
        tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        chunks = ['Thousand','Million','Billion']

        def to_words(num):
            if num==0:
                return []
            if num < 20: return [under_twenty[num]]
            if num < 100: return [tens[num//10]]+ to_words(num%10)
            if num < 1000:
                quotient, remainder = divmod(num,100)
                return [under_twenty[quotient], 'Hundred']+ to_words(remainder)
            for power,chunk in enumerate(chunks,1):
                if num < 1000 ** (power+1):
                    quotient, remainder = divmod(num,1000**power)
                    return to_words(quotient)+[chunk]+to_words(remainder)
        return ' '.join(to_words(num)) or 'Zero'

X = Solution()
print(X.numberToWords(123456789))