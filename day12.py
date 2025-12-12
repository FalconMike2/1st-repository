def groupAnagrams(words):
    groups = {}

    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)

    
    for key in groups:
        groups[key].sort()

    
    final = sorted(groups.values(), key=len, reverse=True)

    return final
