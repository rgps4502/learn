def openr(fname):
    with open(fname, "r", encoding='utf-8') as f:
        return f.read().splitlines()


def openw(fname, messagew):
    with open(fname, "w", encoding='utf-8') as f:
        return f.write(messagew)
