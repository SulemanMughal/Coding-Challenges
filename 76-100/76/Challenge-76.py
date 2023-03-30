from re import*
dakiti=lambda s:' '.join(sub('\d','',y)for y in sorted(s.split(),key=lambda x:search('(\d)',x).group()))