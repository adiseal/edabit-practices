def apocalyptic(n):
    num = str(2 ** n)
    index = num.find('666')
    if index != -1:
        return "Repent! {} days until the Apocalypse!".format(index)
    else:
        return "Crisis averted. Resume sinning."
