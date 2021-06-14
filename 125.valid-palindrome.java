/*
 * @lc app=leetcode id=125 lang=java
 *
 * [125] Valid Palindrome
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        String answer = "";
        boolean palindromeFlag = true;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) >= 'A' && s.charAt(i) <= 'Z'){
                answer += s.charAt(i);
            }
            else if(s.charAt(i) >= 'a' && s.charAt(i) <= 'z'){
                answer += s.charAt(i);
            }
            else if(s.charAt(i) >= '0' && s.charAt(i) <= '9'){
                answer += s.charAt(i);
            }
        }

        answer = answer.toLowerCase();
        System.out.println(answer);
        int length = answer.length();
        for(int i=0;i<length/2;i++){
            if(answer.charAt(i) != answer.charAt(length-i-1)){
                palindromeFlag = false;
                break;
            }
        }

        return palindromeFlag;
    }
}
// @lc code=end

