def owofied(sentence):
    new_sentence = sentence.replace("e", "we").replace("i", "wi")
    return new_sentence + " owo"

#assert owofied("I'm gonna ride 'til I can't no more") == "I'm gonna rwidwe 'twil I can't no morwe owo"

#assert owofied("Do you ever feel like a plastic bag") == "Do you wevwer fwewel lwikwe a plastwic bag owo"

print(owofied("We've known each other for so long"))
#assert owofied("We've known each other for so long") == "Wwe'vwe known weach othwer for so long owo"

