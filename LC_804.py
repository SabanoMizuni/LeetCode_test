class Solution1: # https://leetcode.com/problems/unique-morse-code-words/discuss/362150/Solution-in-Python-3-(beats-~100)-(two-lines)
    def uniqueMorseRepresentations(self, words):
        M = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---','.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
        return len(set([''.join(map(lambda x: M[ord(x) - 97], w)) for w in words]))
        """
        ord(): Given a string of length one, return an integer representing the Unicode code point of the character
         when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. 
         For example, ord(‘a’) returns the integer 97.
        lambda: https://stackoverflow.com/questions/1583617/what-does-lambda-mean-in-python-and-whats-the-simplest-way-to-use-it
        map(fun, iter): Returns a list of the results after applying the given function 
         to each item of a given iterable (list, tuple etc.)
        """

s1 = Solution1()
words = ["gin", "zen", "gig", "msg"]
print(s1.uniqueMorseRepresentations(words))

import string
class Solution2: # https://leetcode.com/problems/unique-morse-code-words/discuss/348948/Python-3-using-dict-and-set
    def uniqueMorseRepresentations(self, words):
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", ".." \
            , ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-" \
            , ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        D = dict(zip( string.ascii_lowercase, code ))  # string.ascii_lowercase returns "abc...xyz"
        s = set()
        for word in words:
            # add the joint of letter (in code format) to a set
            s.add("".join([D[letter] for letter in word]))
        return len(s)

s2 = Solution2()
words = ["gin", "zen", "gig", "msg"]
print(s2.uniqueMorseRepresentations(words))


class Solution3: # https://leetcode.com/problems/unique-morse-code-words/discuss/275680/beats-97.85-simple-python-code
    def uniqueMorseRepresentations(self, words):
        result_letter = ""
        result_word = []
        morse_arr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        for word in words:
            for letter in word:
                result_letter = result_letter + morse_arr[ord(letter) - 97]
            result_word.append(result_letter)
            result_letter = ""
        return (len(set(result_word)))

s3 = Solution3()
words = ["gin", "zen", "gig", "msg"]
print(s3.uniqueMorseRepresentations(words))