"""
Using a read7() method that returns 7 characters from a file,
implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”,
three read7() returns “Hello w”, “orld” and then “”.
"""


class CharacterReader:
    def __init__(self, n):
        self.pre = ''
        self.n = n

    def read(self, string):
        if self.n <= len(self.pre):
            res = self.pre[:self.n]
            self.pre = self.pre[self.n:]
            return res

        target = self.n - len(self.pre)
        res = [self.pre]
        while target > 7:
            res += read7()
            target -= 7
        last = read7()
        res += last[:target]
        self.pre = last[target:]
        return ''.join(res)
