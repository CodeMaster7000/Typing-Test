from wonderwords import RandomSentence
import random
import time

sent_list = []
sent_para = ""
for i in range(5):
    sent = RandomSentence()
    random_sent = sent.sentence()
    sent_list.append(random_sent)
    sent_para += random_sent +  " "
    
def errorrate(sent_para, typed_para):
    errorcount = 0
    length = len(sent_para)
    for character in range(length):
        try: 
            if sent_para[character] != typed_para[character]:
            errorcount += 1
        except:
            errorcount += 1
    errorpercent = errorcount/length * 100
    return errorpercent

print("Your typing test paragraph: \n")
print(sent_para)
print("\n")
start_time = time.time()
typed_para = input()
end_time = time.time()
time_taken = end_time - start_time
errorpercent = errorrate(sent_para, typed_para)
print("\n")

if errorpercent > 35:
    print(f"Your error rate {error_percent} was fairly high, hence your accurate speed could not be computed.")

else:
    speed = len(typed_para)/time_taken
    print("Score Report: ")
    print(f"Your typing speed was {speed} words/second.")
    print(f"Your error rate was {errorpercent}.")
