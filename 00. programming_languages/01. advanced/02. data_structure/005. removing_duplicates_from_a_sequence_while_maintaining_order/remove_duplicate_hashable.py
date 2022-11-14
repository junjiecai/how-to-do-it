
# 加个性能比较 list
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__ == '__main__':
    a = [1, 1, 2, 3, 9, 2, 2, 111]
    print(a)
    print(list(dedupe(a)))
