#列表去掉重复元素(不要直接在原列表上操作)
def dedup (l):
    seen = set()#查找更快，性能高
    result = []
    for item in l:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return(result)
l = [2,7,4,8,2,4,9,3]
print(dedup(l))