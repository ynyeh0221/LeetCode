class NumArray {
private:
    vector<int> numlist;
public:
    NumArray(vector<int> &nums) {
        numlist = nums;
    }

    void update(int i, int val) {
        numlist[i] = val;
    }

    int sumRange(int i, int j) {
        int res = 0;
        for (int k = i; k <= j; k++)
            res += numlist[k];
        return res;
    }
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);
