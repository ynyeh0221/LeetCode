class Solution {
public:
    int gcd(int a,int b)
    {
        return b==0? a: gcd(b,a%b);
    }
    bool canMeasureWater(int x, int y, int z) {
        if (z == 0) return true;
        if (z > x+y) return false;
        return z % gcd(x,y) == 0 ? true: false;
    }
};
