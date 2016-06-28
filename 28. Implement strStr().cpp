class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.size() == 0 && needle.size() == 0)
            return 0;
        for (int i = 0; i < haystack.size(); i++)
        {
            string temp = haystack.substr(i, needle.size());
            if (i + needle.size() <= haystack.size() && temp == needle)
                return i;
        }
        return -1;
    }
};
