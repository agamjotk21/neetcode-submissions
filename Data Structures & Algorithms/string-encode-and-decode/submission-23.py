class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '' 
        for word in strs: 
            res += str(len(word)) + '#'
            res += word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while len(s) > 0: 
            delimInd = s.find('#')
            lenWord = s[:delimInd]

            startInd = len(lenWord) + 1
            lenWord = int(lenWord)
            endInd = startInd + lenWord

            curr = s[startInd:endInd]
            s = s[endInd:]
            res.append(curr)

        return res


