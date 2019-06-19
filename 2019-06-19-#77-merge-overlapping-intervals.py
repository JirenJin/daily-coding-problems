"""
Given a list of possibly overlapping intervals,
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)],
you should return [(1, 3), (4, 10), (20, 25)].
"""


# time: O(nlogn) | space: O(n)
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    res = []
    pre_interval = intervals[0]
    for i in range(1, len(intervals)):
        curr_interval = intervals[i]
        if curr_interval[0] <= pre_interval[1]:
            pre_interval = (pre_interval[0],
                            max(pre_interval[1], curr_interval[1]))
        else:
            res.append(pre_interval)
            pre_interval = curr_interval
    res.append(pre_interval)
    return res


# track the last interval in the result list
def merge_intervals(intervals):
    res = []
    for interval in sorted(intervals):
        if res and res[-1][1] >= interval[0]:
            res[-1] = (res[-1][0], max(res[-1][1], interval[1]))
        else:
            res.append(interval)
    return res
