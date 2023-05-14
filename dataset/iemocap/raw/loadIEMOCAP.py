import pandas as pd
import numpy as np
import pickle


videoIDs, videoSpeakers, videoLabels, videoText, videoAudio, videoVisual, videoSentence, trainVid, testVid = pickle.load(open("IEMOCAP_features_raw.pkl", "rb"), encoding='latin1')

'''
情绪编码 ： {'hap':0, 'sad':1, 'neu':2, 'ang':3, 'exc':4, 'fru':5}
'''

# print(trainVid)
print(len(trainVid))
# print(testVid)
print(len(testVid))
i = 0
for vid in trainVid:
    # print(np.array(videoText[vid]).shape) 文本特征：100
	# print(np.array(videoAudio[vid]).shape) 声音特征：100
	# print(np.array(videoVisual[vid]).shape) 图像特征：512
	print(len(videoIDs[vid]))
	i += 1
	if i == 3:
		break
# for vid in trainVid:
	# videoIDs[vid] = List of utterance IDs in this video in the order of occurance
	# videoSpeakers[vid] = List of speaker turns. e.g. [M, M, F, M, F]. here M = Male, F = Female
	# videoText[vid] = List of textual features for each utterance in video vid
	# videoAudio[vid] = List of audio features for each utterance in video vid
	# videoVisual[vid] = List of visual features for each utterance in video vid
	# videoLabels[vid] = List of label indices for each utterance in video vid
	# videoSentence[vid] = List of sentences for each utterance in video vid


# for vid in testVid:
# 	# videoIDs[vid] = List of utterance IDs in this video in the order of occurance
# 	# videoSpeakers[vid] = List of speaker turns. e.g. [M, M, F, M, F]. here M = Male, F = Female
# 	# videoText[vid] = List of textual features for each utterance in video vid
# 	# videoAudio[vid] = List of audio features for each utterance in video vid
# 	# videoVisual[vid] - List of visual features for each utterance in video vid
# 	# videoLabels[vid] = List of label indices for each utterance in video vid
# 	# videoSentence[vid] = List of sentences for each utterance in video vid