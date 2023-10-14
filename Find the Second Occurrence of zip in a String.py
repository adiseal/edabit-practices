def find_zip(s):
    return s.find("zip", s.find("zip")+1) if s.count("zip") > 1 else -1
