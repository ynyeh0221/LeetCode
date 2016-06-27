class Solution {
public:
    vector<int> countBits(int num) {
        vector <int> res {0,1,1,2,1,2,2,3};
        int ind = 4;
        while (res.size() <= num)
        {
            vector <int> temp (res.begin() + ind, res.end());
            ind = res.size();
            res.insert(res.end(), temp.begin(), temp.end());
            for (int i = 0; i < temp.size(); i++)
                temp[i]++;
            res.insert(res.end(), temp.begin(), temp.end());
        }
        vector <int> rres (res.begin(), res.begin() + num + 1);
        return rres;
    }
};
