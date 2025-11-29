# Merge Overlapping Meetings
# You are given n meeting time intervals as an array intervals, where intervals[i] = [start_i, end_i] and start_i < end_i.
# Merge all overlapping intervals and return the result in any order.
# Examples


# [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]


# [[1,4],[4,5]] → [[1,5]]


def merge_overlapping_mettings(intervals):
    merged = []
    intervals.sort(key=lambda x:x[0])
    current = intervals[0]
    for i in range(1, len(intervals)):
        next = intervals[i]
        if  next[0] <= current[1]:
            current[1] = max(current[1],next[1])
        else :
            merged.append(current)
            current = next
    merged.append(current)
    return merged


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_overlapping_mettings(intervals))
