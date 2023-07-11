def is_anagrams(fst_word, snd_word):

    fst_word.lower()
    snd_word.lower()

    is_sorted_fst_word = sorted(fst_word)
    is_sorted_snd_word = sorted(snd_word)

    if is_sorted_fst_word == is_sorted_snd_word:
        return True
    else:
        return False

print (is_anagrams("TOP_CODER", "COTO_PRODE"))

