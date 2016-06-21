class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector <int> res;
        for (int i = 0; i < nums1.size(); i++)
        {
            if (nums2.size() > 0)
            {
                vector <int> :: const_iterator pos;
                pos = find (nums2.begin(), nums2.end(), nums1[i]);
                if (pos != nums2.end())
                {
                    res.push_back(nums1[i]);
                    nums2.erase(pos);
                }
            }
        }
        return res;
    }
};
