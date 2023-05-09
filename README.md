# 毕业设计-多模态情绪分析
doing  gui界面


# 数据集简介

## MOSI:
**2 classes**: Positive/Negative <br>
Raw Features: (Pickle files) <br>
Audio: dataset/mosi/raw/audio_2way.pickle <br>
Text: dataset/mosi/raw/text_2way.pickle <br>
Video: dataset/mosi/raw/video_2way.pickle <br>

**Each file contains: <br>**
train_data, train_label, test_data, test_label, maxlen, train_length, test_length

train_data - np.array of dim (62, 63, feature_dim) <br>
train_label - np.array of dim (62, 63, 2) <br>
test_data - np.array of dim (31, 63, feature_dim) <br>
test_label - np.array of dim (31, 63, 2) <br>
maxlen - max utterance length  int of value 63 <br>
train_length - utterance length of each video in train data. <br>
test_length - utterance length of each video in test data. <br>

Train/Test split: 62/31 videos. Each video has utterances. The videos are padded to 63 utterances.

## IEMOCAP:
**6 classes**: happy/sad/neutral/angry/excited/frustrated<br>
Raw Features: dataset/iemocap/raw/IEMOCAP_features_raw.pkl (Pickle files) <br>
The file contains:  
videoIDs[vid] = List of utterance IDs in this video in the order of occurance <br>
videoSpeakers[vid] = List of speaker turns. e.g. [M, M, F, M, F]. here M = Male, F = Female <br>
videoText[vid] = List of textual features for each utterance in video vid. <br>
videoAudio[vid] = List of audio features for each utterance in video vid. <br>
videoVisual[vid] = List of visual features for each utterance in video vid. <br>
videoLabels[vid] = List of label indices for each utterance in video vid. <br>
videoSentence[vid] = List of sentences for each utterance in video vid. <br>
trainVid =  List of videos (videos IDs) in train set. <br>
testVid =  List of videos (videos IDs) in test set. <br>

Refer to the file dataset/iemocap/raw/loadIEMOCAP.py for more information.
We use this data to create a speaker independent train and test splits in the format. (videos x utterances x features)

Train/Test split: 120/31 videos. Each video has utterances. The videos are padded to 110 utterances.

## MOSEI:
**3 classes**: positive/negative/neutral <br>
Raw Features: (Pickle files) <br>
Audio: dataset/mosei/raw/audio_3way.pickle <br>
Text: dataset/mosei/raw/text_3way.pickle <br>
Video: dataset/mosei/raw/video_3way.pickle <br>

The file contains:
train_data, train_label, test_data, test_label, maxlen, train_length, test_length

train_data - np.array of dim (2250, 98, feature_dim) <br>
train_label - np.array of dim (62, 63, 2) <br>
test_data - np.array of dim (31, 63, feature_dim) <br>
test_label - np.array of dim (31, 63, 2) <br>
maxlen - max utterance length  int of value 98 <br>
train_length - utterance length of each video in train data. <br>
test_length - utterance length of each video in test data. <br>

Train/Test split: 2250/678 videos. Each video has utterances. The videos are padded to 98 utterances.