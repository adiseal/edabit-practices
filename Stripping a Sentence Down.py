def strip_sentence(txt, chars):
    for x in txt:
        if x in chars:
            txt = txt.replace(x, "")
    return txt
    
print(strip_sentence("the quick brown fox jumps over the lazy dog", "aeiou")) #➞ "th qck brwn fx jmps vr th lzy dg"