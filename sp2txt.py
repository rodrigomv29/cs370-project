import whisper
title_list =[
"kamala-harris", "pink",
"joe-biden", "rich-paul",
"geoffrey-hinton", "mark-millie",
"merrick-garland", "deion-sanders",
"volodymyr-zelenskyy", "denzel-washington"
]

def writeToFile(s, name):
    path ="./whisper_text/"
    filename = name +".txt"
    path+=filename
    f1 = open(path, "w")
    f1.write(s)
    f1.close()
if __name__ == '__main__':
    for i in range(len(title_list)):
        model = whisper.load_model("base")
        filepath = "./mp3/"
        filepath += title_list[i] + str(".mp3")
        result = model.transcribe(filepath)
        writeToFile(result["text"], title_list[i])
