# pal_combo
1. Unit of observation is a syllable in the palindrome, NE-VER-ODD-OR-EV-EN
2. For each syllable in the palindrome, we want x different voices to pronounce it
3. We will loop through the sets of syllables, always starting with the first (NE) and ending with the last (EN), and randomly choose a voice from the set of x voices, without repeating a voice until all options have been exhausted
4. We will repeat this process y times
