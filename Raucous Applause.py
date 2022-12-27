def count_claps(txt):
	return txt.count("C")
    


assert count_claps("ClaClaClaClap!") == 4

assert count_claps("ClClClaClaClaClap!") == 6

assert count_claps("CCClaClClap!Clap!ClClClap!") == 9