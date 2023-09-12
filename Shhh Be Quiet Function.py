def shhh(txt):
    txt = txt.capitalize()
    return '"{}", whispered Edabit.'.format(txt)

print(shhh("HI THERE!")) # '"Hi there!", whispered Edabit.'
print(shhh("tHaT'S Pretty awesOme")) # '"That's pretty awesome", whispered Edabit.'
print(shhh("")) # '"", whispered Edabit.'