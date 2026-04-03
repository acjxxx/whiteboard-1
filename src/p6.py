def max_occur(s):
    count = {}

    for ch in s:
        if not ch.isalnum():
            continue
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    max_occur = None
    max_count = 0

    for ch in count:
        if count[ch] > max_count:
            max_occur = ch
            max_count = count [ch]

    return max_occur, max_count

         