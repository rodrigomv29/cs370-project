from youtube_transcript_api import YouTubeTranscriptApi

## l = YouTubeTranscriptApi.get_transcript("rPvBPodP7Ds")
def bracketIsMusic(bracket):
    return bracket == "[Music]"
def bracketIsApplause(bracket):
    return bracket == "[Applause]"
def bracketIsLaughter(bracket):
    return bracket == "[Laughter]"
def writeToFile(s, name):
    path ="./transcripts/"
    filename = name +".txt"
    path+=filename
    f1 = open(path, "w")
    f1.write(s)
    f1.close()
id_list=[
"G3Eup4mfJdA","480OGItLZNo",
"OA2Tj75T3fI", "qrvK_KuIeJk",
"oFVuQ0RP_As", "4aPp8KX6EiU",
"h8PSWeRLGXs", "Z8qC2tVkGeU",
"Y9nM_9oBj2k", "ervLwxz7xPo"
]
title_list =[
"kamala-harris", "pink",
"joe-biden", "rich-paul",
"geoffrey-hinton", "mark-millie",
"merrick-garland", "deion-sanders",
"volodymyr-zelenskyy", "denzel-washington"
]

def getTranscriptStr(video_id):
    trans_str = "";
    l = YouTubeTranscriptApi.get_transcript(video_id)
    for i in l:
        if bracketIsMusic(i["text"]) or bracketIsApplause(i["text"]) or bracketIsLaughter(i["text"]):
            continue
        trans_str += i["text"]
        trans_str += ", "
    isInsideBracket = False
    final_trans_str=""
    for i in trans_str:
        if i=="[":
            isInsideBracket = True
            continue
        if isInsideBracket:
            if i=="]":
                isInsideBracket = False
                final_trans_str += " EXPLETIVE "
        else:
            final_trans_str += i
    return final_trans_str;

if __name__ == '__main__':
    for i in range(len(id_list)):
        v_id = id_list[i]
        solution = getTranscriptStr(v_id)
        writeToFile(solution, title_list[i])
