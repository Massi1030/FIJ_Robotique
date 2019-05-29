alphabet = ["a", "b", "c"]
morse = [".-", "-...", "-.-."]

print("quel lettre voulez vous ?")
reponse = input()


for element in alphabet :
    if reponse == element :
        print(element)
        index = alphabet.index(element)
        print(morse[index])


print("tapez un code morse")
reponse =input()

for element in alphabet
    if reponse == element :
       print(element)
       index = morse.index(element)
       print(alphabet)[index])