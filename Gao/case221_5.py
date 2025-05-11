#字符串不含重复字符的最长子串长度
def lengsubstr(s: str) -> int:
    char_set = set()#使用集合来存储当前窗口中的字符
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)#right - left + 1表示当前不重复子串的长度
    return max_length
print(lengsubstr("abcabcdbbx"))#3