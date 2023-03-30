def longest_time(h, m, s):
        return max((h*3600, h), (m*60, m), (s, s))[1]