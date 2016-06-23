class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int total = (C-A)*(D-B)+(G-E)*(H-F);
        if (A > G || B > H || C < E || D < F)
            return total;
        int x1 = A > E ? A : E;
        int x2 = C < G ? C : G;
        int y1 = B > F ? B : F;
        int y2 = D < H ? D : H;
        return total-(x2-x1)*(y2-y1);
    }
};
