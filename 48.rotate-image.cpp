/*
 * @lc app=leetcode id=48 lang=cpp
 *
 * [48] Rotate Image
 */

// @lc code=start
#include <vector>
#include <iostream>

using namespace std;


class Solution {
#include <iostream>
public:
    void rotate(vector<vector<int>>& matrix) {
        int length = matrix.size();

        for(int i=0;i<length;i++){
            for(int j=i+1;j<matrix[i].size();j++){        
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        for(int i=0;i<length;i++){
            for(int j=0;j<length/2;j++){
                swap(matrix[i][j], matrix[i][length-j-1]);
            }
        }
    }
};

// int main(){
//     Solution temp;
//     vector<vector<int>> test;
//     vector<int> emp;
//     int length = 3;
//     for(int i=0;i<length;i++){
//         test.push_back(emp);
//         for(int j=0;j<length;j++){
//             test[i].push_back(i*length+j);
//         }
//     }

//     temp.rotate(test);

//     return 0;
// }
// @lc code=end

