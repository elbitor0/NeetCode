from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        clist = []
        for cs in strs:
            str_len = str(len(cs))
            for n in str_len:
                clist.append(n)
            clist.append('#')
            for c in cs:
                clist.append(c)
        return ''.join(clist)

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        str_len = 0
        bool_len =  True
        res = []
        w = []
        index = 0
        while index < len(s):
            c = s[index]
            
            if bool_len and c == '#':
                bool_len=False
                index+=1
            elif bool_len:
                str_len*=10
                str_len+=ord(c)-48  
                index+=1
            elif str_len == 0:
                print('zebo')
                res.append(''.join(w))
                w = []
                bool_len = True
            else:
                w.append(c)
                str_len-=1
                index+=1
        res.append(''.join(w))
        return res
