#include <sstream>
#include <unordered_map>
class Solution {
public:
    vector<string> split(string str, char delimiter)
    {
        vector<string> internal;
        stringstream ss(str);
        string tok;
        while(getline(ss, tok, delimiter))
            internal.push_back(tok);
        return internal;
    }
    bool wordPattern(string pattern, string str) {
        vector<string> str_split = split(str, ' ');
        if (pattern.length() != str_split.size())
            return false;
        unordered_map <string, char> words_to_patterns;
        unordered_map <char, string> patterns_to_words;
        for (int i = 0; i < pattern.size(); i++)
        {
            if (words_to_patterns.count(str_split[i]) == 0 && patterns_to_words.count(pattern[i]) == 0)
            {
                words_to_patterns[str_split[i]] = pattern[i];
                patterns_to_words[pattern[i]] = str_split[i];
            }
            else
            {
                if (words_to_patterns.count(str_split[i]) > 0 && patterns_to_words.count(pattern[i]) > 0 && words_to_patterns[str_split[i]] == pattern[i] && patterns_to_words[pattern[i]] == str_split[i])
                    continue;
                else
                    return false;
            }
        }
        return true;
    }
};
