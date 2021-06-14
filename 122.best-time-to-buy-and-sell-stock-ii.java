/*
 * @lc app=leetcode id=122 lang=java
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int length = prices.length;

        for(int i=1;i<length;i++){
            if(prices[i] - prices[i-1] > 0){
                profit += prices[i] - prices[i-1];
            }
        }

        if(profit < 0){
            return 0;
        }
        return profit;
    }

    public static void main(String[] args){
        System.out.println("Hello world");
        Solution temp = new Solution();
        int[] test = {7, 1, 5, 3, 6, 4};
        System.out.println(temp.maxProfit(test));
    }
}

// @lc code=end

