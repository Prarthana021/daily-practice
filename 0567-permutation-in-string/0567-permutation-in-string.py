class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1arr = [0] * 26
        s2arr = [0] * 26

        # build frequency arrays for s1 and first window in s2
        for i in range(len(s1)):
            index_s1 = ord(s1[i]) - ord('a')  # character index in s1
            index_s2 = ord(s2[i]) - ord('a')  # character index in s2

            s1arr[index_s1] += 1
            s2arr[index_s2] += 1

        # sliding window
        for i in range(len(s2) - len(s1)):
            if s1arr == s2arr:
                return True

            # calculate indices for clarity
            index_right = ord(s2[i + len(s1)]) - ord('a')  # new char entering window
            index_left = ord(s2[i]) - ord('a')             # old char leaving window

            # update s2arr
            s2arr[index_right] += 1
            s2arr[index_left] -= 1

        # final window check
        return s1arr == s2arr
