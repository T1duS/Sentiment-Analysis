from nltk.tokenize import word_tokenize,sent_tokenize
import sys

# Calculate probabilities of positive words
pos_file = open('pos.txt', 'r')
pos_text = pos_file.read()
pos_lines = sent_tokenize(pos_text)
pos_total = len(pos_lines)
pos_count = {}
total_count = {}
for sent in pos_lines:
	words = word_tokenize(sent)
	proper_words = set()
	for i in words:
		if len(i) > 1:
			proper_words.add(i)
	for i in proper_words:
		pos_count[i] = pos_count.get(i,0)+1	
		total_count[i] = total_count.get(i,0)+1		

# Calculate probabilities of negative words
neg_file = open('neg.txt', 'r')
neg_text = neg_file.read()
neg_lines = sent_tokenize(neg_text)
neg_total = len(neg_lines)
neg_count = {}
for sent in neg_lines:
	words = word_tokenize(sent)
	proper_words = set()
	for i in words:
		if len(i) > 1:
			proper_words.add(i)
	for i in proper_words:
		neg_count[i] = neg_count.get(i,0)+1		
		total_count[i] = total_count.get(i,0)+1

total_lines = pos_total+neg_total		

# Taking input file and giving result
if len(sys.argv) < 2:
	print("Missing file name")
	exit()
inpy = open(sys.argv[1],"r")
words = word_tokenize(inpy.read())
n = len(words)
# Using naive bayes calculate the probability
# P(pos | words) = (P(pos)*P(pos|word[0])*P(pos|word[1])....*P(pos|word[n-1]))/(P(word[0])*P(word[1])....*P(word[n-1]))
# Similarly for neg
probability_pos = pos_total/float(total_lines)
probability_neg = neg_total/float(total_lines)
for i in range(n):
	if(len(words[i]) <= 1): continue
	if(words[i] in pos_count):  
		probability_pos *= pos_count[words[i]]/float(pos_total)
		probability_pos *= total_lines/float(total_count[words[i]])
	if(words[i] in neg_count):  
		probability_neg *= neg_count[words[i]]/float(neg_total)
		probability_neg *= total_lines/float(total_count[words[i]])	

print(probability_pos,probability_neg)

if probability_pos > probability_neg:
	if (probability_pos - probability_neg)/probability_pos <= 0.05:
		print("Neutral")
	else:
		print("Positive")
else:
	if (probability_neg - probability_pos)/probability_neg <= 0.05:
		print("Neutral")
	else:
		print("Negative")				