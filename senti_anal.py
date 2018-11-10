import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import sys
nltk.download('punkt')
nltk.download('vader_lexicon')

def main():

	if len(sys.argv) < 2:
		print("Missing file name")
		exit()

	inpy = open(sys.argv[1],"r")
	sentences = tokenize.sent_tokenize(inpy.read())
	for sent in sentences:
		print("\n-------------")
		print(sent)
		ss = SentimentIntensityAnalyzer().polarity_scores(sent)
		print("Positivity : "+str(ss['pos']))
		print("Neutrality : "+str(ss['neu']))
		print("Negativity : "+str(ss['neg']))
		if ss['pos']>ss['neu'] and ss['pos']>ss['neg']:
			print("Sentence is Positive")
		if ss['neg']>ss['neu'] and ss['neg']>ss['pos']:
			print("Sentence is Negative")
		if ss['neu']>ss['pos'] and ss['neu']>ss['neg']:
			print("Sentence is Neutral")
		print("")	

if __name__ == '__main__':
	main()	  		