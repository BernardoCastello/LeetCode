class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre = strs[0]
        
        for i in range(1, len(strs)):
            while pre not in strs[i][:len(pre)]:
                #print(pre, strs[i][:len(pre)])
                pre = pre[:-1]
                if pre == "":
                    return pre
        return pre
