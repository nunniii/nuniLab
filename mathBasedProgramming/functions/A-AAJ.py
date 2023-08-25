
l = [['P1', 2], ['P2', 4], ['P3', 7], ['P4', 5], ['P5', 1]]
def ordernar(item):
    return item[1]
l.sort(key=ordernar)
print(l)