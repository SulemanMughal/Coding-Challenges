import re
    
def remove_virus(files):
    safe = [f for f in files[10:].split(", ") if f and not re.fullmatch(r"(?!not|anti).*(virus|malware)\.exe", f)]
    return "PC Files: %s" % (", ".join(safe) if safe else "Empty")