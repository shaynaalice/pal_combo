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

#create iteration list of voice_dicts
iter_list = []

for i in range(iter_num):
    voices_list = [shuffleACopy(voices) for x in range(syllable_num)]
    #voice_dict is made using a shortcut, but should use keys from
    #syllable_dict rather than enumerate
    voice_dict = dict(enumerate(voices_list)) #dictionary of one iteration
    #depending on what you want the keys to be
#    iter_dict = {value : voice_dict.get(key, None) for key, value in syllable_dict.items()}
#    iter_list.append(iter_dict)
    iter_list.append(voice_dict)


#experimenting with desired output
for key, value in voice_dict.items():
    print key, value[0]

pal_iter = list(map(lambda x: x -1, voices))

for i in iter_list:
    #prints dictionaries within list
    #print i
    for key, value in i.iteritems():
        #prints keys and values in each dictionary (first position in
        #list)
        #want position to use pal_iter
        print key, value[0]
        


