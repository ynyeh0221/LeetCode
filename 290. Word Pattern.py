class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(str) != len(pattern):
            return False
        words_to_patterns = {}
        patterns_to_words = {}
        for i,j in zip(str, pattern):
            if i not in words_to_patterns and j not in patterns_to_words:
                words_to_patterns[i] = j
                patterns_to_words[j] = i
            else:
                if i in words_to_patterns and j in patterns_to_words and words_to_patterns[i] == j and patterns_to_words[j] == i:
                    continue
                else:
                    return False
        return True
