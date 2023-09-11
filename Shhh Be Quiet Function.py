def shhh(txt):
    txt = txt.capitalize()
    return '"{}", whispered Edabit.'.format(txt)

print(shhh("HI THERE!")) # '"Hi there!", whispered Edabit.'