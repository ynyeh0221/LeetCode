class Solution {  
public:  
    double myPow(double x, int n) {  
        double temp = 0;
        if(n < 0)  
            temp = 1.0 / power(x, -n);  
        else  
            temp = power(x, n);
        if (!isfinite(temp))
            return 0.0;
        return temp;
    }  
  
    double power(double x, int n) {  
        if(n == 0)  
            return 1.0;
        double temp=power(x, n/2);
        
        if(n % 2 == 0)  
            return temp * temp;  
        else  
            return temp* temp * x;  
    }  
}; 
