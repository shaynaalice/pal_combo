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


#output of syllable id and voice id pairs until voice exhaustion and
#then moves to next iteration
for i in iter_list:
     for x in range(voices_num):
         for key, value in i.iteritems():
             print key, value[x]


#if we want it as a list:
[[k, d[k][i]] for d in iter_list for i in range(voices_num) for k in sorted(d)]
