from translate import Translator
title_list =[
"kamala-harris", "pink",
"joe-biden", "rich-paul",
"geoffrey-hinton", "mark-millie",
"merrick-garland", "deion-sanders",
"volodymyr-zelenskyy", "denzel-washington"
]
def reformatText(text):
    newLineNeeded = False
    strbuilder = "";
    for i in range(len(text)):
        if i%100 == 0 and i != 0:
            newLineNeeded = True
        if newLineNeeded and text[i] == " ":
            strbuilder += '\n'
            newLineNeeded = False
        strbuilder += text[i];
    return strbuilder
translator= Translator(from_lang="english",to_lang="spanish")
for i in range(len(title_list)):
    file_= open("./whisper_text/" + title_list[i]+ ".txt")
    englishText = file_.read()
    reformatted = reformatText(englishText)
    translation = translator.translate(reformatted[1:])
    ## print(translation, end="\n\n\n\n\n\n")
    ## print("******NEW FILE INSERTED******\n\n\n\n\n\n")

    break;
