def openr(fname):
    with open(fname, "r") as f:
        return f.read().splitlines()


def openw(fname, messagew):
    with open(fname, "w") as f:
        return f.write(messagew)
