class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1 or (len(s) == 2 and s[0] != s[1]):
            return s[0]
        
        string = ''
        
        for i in range(len(s)):
            str_aux_left = ''
            str_aux_right = ''

            j = i
            k = len(s) -1

            last_index_j = j
            last_index_k = k

            while j < k:
                if s[j] == s[k]:

                    if (last_index_j == j or last_index_j == j -1 ) and (last_index_k==k or last_index_k== k + 1):
                        str_aux_left += s[j]
                        str_aux_right = s[k] + str_aux_right

                        if j + 2 == k:
                            str_aux_left += s[j+1]
                        last_index_j = j
                        last_index_k = k
                        #if j + 2 == k:
                            
                        j += 1
                        k -= 1

                    else:
                        str_aux_left = s[j]
                        str_aux_right = s[k]

                        if j + 2 == k:
                            str_aux_left += s[j+1]

                        last_index_j = j
                        last_index_k = k
                        j += 1
                        k -= 1

                else:
                    k -= 1

                
                if len(str_aux_right) + len(str_aux_left) > len(string):
                    string = str_aux_left + str_aux_right
                    
            
        return string
    

S = Solution()
print(S.longestPalindrome("aaabgaaccaa"))