#creating the classifier 
class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

#opening positive and negative files for training
short_pos = open("positive.txt", "r").read()
short_neg = open("negative.txt", "r").read()

#creating all words
all_words = []
documents = []

#  j is adject, r is adverb, and v is verb
# allowed_word_types = ["J","R","V"]
allowed_word_types = ["J"]

for p in short_pos.split('\n'):
    documents.append((p, "pos"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for p in short_neg.split('\n'):
    documents.append((p, "neg"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

#analyzing words with wordcloud
def word_cloud(wd_list):
    stopwords = set(STOPWORDS)
    all_words = ' '.join([text for text in wd_list])
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        width=1600,
        height=800,
        random_state=21,
        colormap='jet',
        max_words=50,
        max_font_size=200).generate(all_words)    plt.figure(figsize=(12, 10))
    plt.axis('off')
    plt.imshow(wordcloud, interpolation="bilinear")
word_cloud(all_words)
word_cloud(short_neg)
word_cloud(short_pos)

#saving the word_documents
save_all = open("all.pickle", "wb")
pickle.dump(all, save_all)
save_all.close()

#getting frequency distribution
all_words = nltk.FreqDist(all_words)

#getting features
word_features = list(all_words.keys())[:5000]

#saving features
save_features = open("save_features.pickle", "wb")
pickle.dump(save_features, save_features)
save_features.close()

#getting features
def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#creating and saving featureset
featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)
print(len(featuresets))

save_featuresets = open("featuresets.pickle", "wb")
pickle.dump(featuresets, save_featuresets)
save_featuresets.close()

#creating train and test set
testing_set = featuresets[10000:]
training_set = featuresets[:10000]

#creating and saving all algorithms for voted classiier
classifier = nltk.NaiveBayesClassifier()
classifier = classifier.train(training_set)
print("Original Naive Bayes Algorithm accuracy:", (nltk.classify.accuracy(classifier, testing_set)) * 100)
classifier.show_most_informative_features(20)

save_classifier = open("originalnaivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy:", (nltk.classify.accuracy(MNB_classifier, testing_set)) * 100)

save_classifier = open("MNB_classifier.pickle", "wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set)) * 100)

save_classifier = open("BernoulliNB_classifier.pickle", "wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy:",(nltk.classify.accuracy(LogisticRegression_classifier, testing_set)) * 100)

save_classifier = open("LogisticRegression_classifier.pickle", "wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) * 100)

save_classifier = open("LinearSVC_classifier.pickle", "wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(training_set)
print("SGDClassifier accuracy:", nltk.classify.accuracy(SGDC_classifier, testing_set) * 100)

save_classifier = open("SGDC_classifier.pickle", "wb")
pickle.dump(SGDC_classifier, save_classifier)
save_classifier.close()
