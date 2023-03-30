import re
from datetime import datetime, timedelta
    
def sync_subs(subtitles, i):
    timestamps = re.compile(r'(2[0-3]|[01]\d):([5]\d|[0-4]\d):([5]\d|[0-4]\d),(\d{3})') 
    
    if not re.match(timestamps, i):
        return 'There is a problem with the second argument'
    i = timedelta(hours=int(i[:2]), minutes=int(i[3:5]), 
                    seconds=int(i[6:8]), milliseconds=int(i[9:]))
    def convert(s):
        s = datetime.strptime(s, '%H:%M:%S,%f')
        return str((s + i).time())[:-3].replace('.', ',')
    
    return re.sub(timestamps, lambda x: convert(x.group()), subtitles)