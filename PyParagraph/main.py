import os
import csv

txtpath1 = open('paragraph_1.txt', 'r')

words = 0
sentences = 0
letters = 0
avg_letter = 0
sent_length = 0

# find the number of words, sentences, letters, and sentence length
for wordcount in txtpath1.read().split(" "):
		#find number of words
		words +=1
		#find number of sentences
		sentences += wordcount.count(".")
		#find Total letter count in order to find average letter count
		letters += sum(len(words) for words in wordcount)
		#find average letter count (divide total letter count by number of words)
		avg_letter = letters/words
		# find average sentence length (divide total words by number of sentences)
		# giving me ZeroDivisionError
sent_length = words/sentences


#print results
print("Paragraph Analysis")
print("---------------------")
print("Approximate Word Count: " + str(words))
print("Approximate Sentence Count: " + str(sentences))
print("Average Letter Count: " + str(avg_letter))
print("Average Sentence Length: " + str(sent_length))

#print("Total Letter Count: " + str(letters)) #use as test

text_file = open("Output.txt", "w")
text_file.write("Paragraph Analysis")
text_file.write("\n---------------------")
text_file.write("\nApproximate Word Count: " + str(words))
text_file.write("\nApproximate Sentence Count: " + str(sentences))
text_file.write("\nAverage Letter Count: " + str(avg_letter))
text_file.write("\nAverage Sentence Length: " + str(sent_length))

text_file.close()



