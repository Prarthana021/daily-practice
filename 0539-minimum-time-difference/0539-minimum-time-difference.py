class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = []
        for t in timePoints:
            h, m = t.split(":")
            minutes.append(int(h) * 60 + int(m))

        # sort so adjacent values are closest
        minutes.sort()

        min_diff = float('inf')

        # check difference between each adjacent pair
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)

        # handle circular wraparound (last to first across midnight)
        circular = minutes[0] + 1440 - minutes[-1]
        min_diff = min(min_diff, circular)

        return min_diff