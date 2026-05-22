class Solution:
#******* encode a list of strings into a string******************
# If the input list is empty, return an empty string.
# Create an empty list to store the sizes of each string.
# For each string, append its length to the sizes list.
# Build a single string by:
# Writing all sizes separated by commas.
# Adding a '#' to mark the end of the size section.
# Appending all the actual strings in order.
# Return the final encoded string.
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s)) # appends the size as an int
        for sz in sizes:
            res += str(sz)
            res += ',' # res list
        res += '#'
        for s in strs:
            res += s
        return res

# If the encoded string is empty, return an empty list.********************
# Read characters from the start until reaching '#' to extract all recorded sizes:
# Parse each size by reading until a comma.
# After the '#', extract substrings according to the sizes list:
# For each size, read that many characters and append the substring to the result.
# Return the list of decoded strings.
# sent over network, & decoded back into original list of strings
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1 # read until the commas
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
