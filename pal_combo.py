import random
palindrome = ["NE", "VER", "ODD", "OR", "EV", "EN"]
syllable_dict = dict(enumerate(palindrome)) 

voices_num = int(raw_input("How many voices will speak each syllable? ")) # user input

iter_num = int(raw_input("How many times would you like the palindrome spoken?  ")) # user input

syllable_num = len(palindrome)

voices = range(1, voices_num + 1)

def shuffleACopy(x):
        b = x[:] # make a copy of the keys
        random.shuffle(b) # shuffle the copy
        return b # return the copy

voices_list = [shuffleACopy(voices) for x in range(syllable_num)]
print(voices_list)
voice_dict = dict(enumerate(voices_list)) 
#voice_dict is made using a shortcut, but should use keys from
#syllable_dict rather than enumerate

voice_dict #dictionary of one iteration

#experimenting with desired output
for key, value in voice_dict.items():
    print key, value[0]

#create outer dictionary for each iteration
for i in range(iter_num):

