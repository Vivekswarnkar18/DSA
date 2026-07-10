class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        result = []

        # Store the last occurrence of each character
        mp = [-1] * 26

        for i in range(n):
            idx = ord(s[i]) - ord('a')
            mp[idx] = i

        i = 0

        while i < n:
            end = mp[ord(s[i]) - ord('a')]

            j = i

            while j < end:
                end = max(end, mp[ord(s[j]) - ord('a')])
                j += 1

            result.append(j - i + 1)

            i = j + 1

        return result