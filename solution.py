# Score of String

def scoreOfString(self, s):
    return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))
