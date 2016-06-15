class Solution {
public:
    int hIndex(vector<int>& citations) {
        int end = citations.size();
        int start = 0;
        while (start < end)
        {
            int mid = (end + start) >> 1;
            if (citations[mid] >= citations.size() - mid)
                end = mid;
            else
                start = mid + 1;
        }
        return citations.size() - start;
    }
};
