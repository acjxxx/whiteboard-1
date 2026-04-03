def clean_string(s):
    result = ""
    for ch in s:
        if ch.isalnum():
            result += ch.lower()
    return result


def anagram_check(s1, s2):
    s1 = clean_string(s1)
    s2 = clean_string(s2)
    
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    
    for ch in s2:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    
    return True