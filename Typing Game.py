def correct_stream(user, correct):
    a = []
    for j in range(0, len(user)):
        for i in correct:
            if i == user[j]:
                a = a + [1]
                j = j + 1
            else:
                a = a + [-1]
                j = j + 1
        return a
        
print(correct_stream(
  ["april", "showrs", "bring", "may", "flowers"],
  ["april", "showers", "bring", "may", "flowers"]
)) # [1, -1, 1, 1, 1]