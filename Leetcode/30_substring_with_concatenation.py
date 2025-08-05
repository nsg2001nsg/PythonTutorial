from collections import Counter

strings = ["bar","foo","the"]
s = "barfoofoobarthefoobarman"


def findSubstring(s, words):
    need = Counter(words)
    have = {k: 0 for k in need.keys()}
    formed = 0
    res = []
    win = len(words[0])
    right = 0
    count = 0
    print(need)
    print(have)
    while right < len(s) and count < 100:
        count += 1
        print(right, "right")
        word = s[right:right + win]
        if word in need:
            curr = right
            while word in need:
                print(word)
                if have[word] < need[word]:
                    have[word] += 1
                    if have[word] == need[word]:
                        formed += 1

                    if formed == len(need):
                        print("in")
                        res.append(curr)
                        have = {k: 0 for k in need.keys()}
                        formed = 0
                        right += win
                        break
                elif have[word] == need[word]:
                    right -= win
                    have = {k: 0 for k in need.keys()}
                    formed = 0
                    break
                right += win
                word = s[right:right + win]
            if word not in need:
                have = {k: 0 for k in need.keys()}
                formed = 0

    return res


print("result:", findSubstring(s, strings))
