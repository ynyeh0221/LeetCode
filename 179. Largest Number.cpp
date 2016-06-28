class Solution {
public:
    struct
    {  
        bool operator()(string a, string b)  
        {  
            string c1 = a + b;  
            string c2 = b + a;  
            return c1 > c2;  
        }  
    } compare;
    
    string largestNumber(vector<int>& nums) {
        vector <string> snums;
        for (int i = 0; i < nums.size(); i++)
            snums.push_back(to_string(nums[i]));
        sort(snums.begin(), snums.end(), compare);
        string res = "";
        for (int i = 0; i < snums.size(); i++)
            res += snums[i];
        return res[0] == '0' ? "0" : res;
    }
};
