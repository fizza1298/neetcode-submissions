class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #order doesnt matter 
        # letter and times letter is used matter
        seen = {}
        if len(s) != len(t): 
            return False 
        for letter in s: 
            if letter not in seen: 
                seen[letter] = 1
            else: 
                seen[letter] += 1

        for letter in t: 
            if letter in seen: 
                seen[letter] -= 1
                if seen[letter] == 0:
                    del seen[letter]
            else: 
                return False
        if len(seen) != 0: 
            return False 
        return True