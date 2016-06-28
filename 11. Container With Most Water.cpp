class Solution {
public:
    int max(int a, int b)
    {
        return a > b ? a : b;
    }
    int min(int a, int b)
    {
        return a < b ? a : b;
    }
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int res = 0;
        while (l < r)
        {
            res = max(res, min(height[l], height[r]) * (r-l));
            if (height[l] < height[r])
                l++;
            else if (height[l] > height[r])
                r--;
            else
            {
                l++; r--;
            }
        }
        return res;
    }
};
