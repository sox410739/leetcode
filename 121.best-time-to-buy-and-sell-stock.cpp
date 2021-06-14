/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        #include <algorithm>
        
        int length = prices.size();
        vector<int> regist(length, 0);
        int min_price = INT_MAX;
        int max_profit = INT_MIN;

        for(int i=0;i<length;i++){
            min_price = min(min_price, prices[i]);
            regist[i] = prices[i] - min_price;
            max_profit = max(max_profit, regist[i]);
        }
        
        if(max_profit < 0){
            return 0;
        }
        return max_profit;
    }
};
// @lc code=end

