class NumArray {
private:
    vector<int> totalnums;
public:
    NumArray(vector<int> &nums) {
        totalnums = nums;
        for (int i = 1; i < totalnums.size(); i++)
            totalnums[i] += totalnums[i-1];
    }

    int sumRange(int i, int j) {
        return i == 0 ? totalnums[j] : totalnums[j] - totalnums[i-1];
    }
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
