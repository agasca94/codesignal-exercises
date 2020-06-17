def regularExpressionMatching(s, p):
    return helper(s + '$', p + '$', 0, 0)
    
def helper(s, p, si, pi):
    # If both the string and the pattern are finished the matching is successful
    if s[si] == p[pi] == '$':
        return True
    # If only the pattern is finished the matching is unsuccessful
    if p[pi] == '$':
        return False
    # If only the string is finished or the characters don't match
    # we must check the next character in the pattern if any
    if s[si] == '$' or (s[si] != p[pi] and p[pi] != '.'):
        # If the next character isn't a star the matching is unsuccessful
        if p[pi + 1] != '*':
            return False
        # If the next character is a star we must consume two positions of the pattern
        # (the current character and the star)
        return helper(s, p, si, pi + 2)
    # If the characters match and the next character isn't a star
    # we must consume one position of the pattern and the string
    if p[pi + 1] != '*':
        return helper(s, p, si + 1, pi + 1)
    # If the two charcters match and the next character is a star we can consume
    # a) one position of the string and leave the pattern alone
    sol = helper(s, p, si + 1, pi)
    if sol:
        return sol
    # b) two positions of the pattern (the current character and the star) and leave the string alone
    return helper(s, p, si, pi + 2)