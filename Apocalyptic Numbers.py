def apocalyptic(n):
    num = str(2 ** n)
    index = num.find('666')
    if index != -1:
        return "Repent! {} days until the Apocalypse!".format(index)
    else:
        return "Crisis averted. Resume sinning."

print(apocalyptic(109)) # "Crisis averted. Resume sinning."
print(apocalyptic(157)) # "Repent! 9 days until the Apocalypse!"
print(apocalyptic(175)) # "Crisis averted. Resume sinning."  
print(apocalyptic(220)) # "Repent! 6 days until the Apocalypse!"
print(apocalyptic(157)) # "Repent! 9 days until the Apocalypse!"
print(apocalyptic(175)) # "Crisis averted. Resume sinning."
print(apocalyptic(220)) # "Repent! 6 days until the Apocalypse!"
print(apocalyptic(333)) # "Crisis averted. Resume sinning."
print(apocalyptic(499)) # "Repent! 138 days until the Apocalypse!"