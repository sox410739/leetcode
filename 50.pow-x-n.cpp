/*
 * @lc app=leetcode id=50 lang=cpp
 *
 * [50] Pow(x, n)
 */

// @lc code=start
class Solution {
public:
    double myPow(double x, int n) {
        if(n < 0){
            if(n == -2147483648){
                return 1/(pow(x, 2147483647)*x);
            }
            return 1/pow(x, -n);
        }

        return pow(x, n);
    }

    double pow(double x, int n){
        if(n == 1){
            return x;
        }
        if(n == 0){
            return 1;
        }
        double half = pow(x, n/2);
        if(half == 0){
            return 0;
        }

        if(n & 1 == 1){ //奇數
            return half*half*x;
        }
        else{
            return half*half;
        }
    }
};
// @lc code=end

