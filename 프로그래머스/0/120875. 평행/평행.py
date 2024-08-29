def solution(dots):
    # list unpacking
    [x1, y1], [x2, y2], [x3, y3], [x4, y4] = dots

    # check parallel lines with slope(slope = dy/dx)
    if (abs(y1 - y2) / abs(x1 - x2) == abs(y3 - y4) / abs(x3 - x4)
            or abs(y1 - y3) / abs(x1 - x3) == abs(y2 - y4) / abs(x2 - x4)
            or abs(y1 - y4) / abs(x1 - x4) == abs(y2 - y3) / abs(x2 - x3)):
        return 1
    # return 0 when there's no parallel lines
    else:
        return 0