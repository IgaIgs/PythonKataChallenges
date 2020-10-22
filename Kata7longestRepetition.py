# For a given string s find the character c (or C) with longest consecutive repetition and return:
#
# (c, l)
# where l (or L) is the length of the repetition.
# If there are two or more characters with the same l return the first in order of appearance.
#
# For empty string return:
#
# ('', 0)


def longest_repetition(chars):
    length = (len(chars) - 1)
    max_count = 0
    count = 1
    char_winner = ''
    for i in range(length):
        if i < length and chars[i] == chars[i + 1]:
            count += 1
        if i < length and chars[i] != chars[i + 1]:
            count = 1
        if count > max_count:
            max_count = count
            char_winner = chars[i]
        if i == length:
            break
    print((char_winner, max_count))
    return char_winner, max_count


longest_repetition('ba')
