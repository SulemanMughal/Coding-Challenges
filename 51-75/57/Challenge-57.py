import re
negative_sum=lambda s:sum(map(int,re.findall('-\d+',s)))