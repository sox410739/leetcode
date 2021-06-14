/*
 * @lc app=leetcode id=119 lang=cpp
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
// #include <vector>
// #include <iostream>

// using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row;
        row.push_back(1);

        while(rowIndex > 0){
            vector<int> temp = row;
            row.insert(row.begin(), 0);
            for(int i=0;i<temp.size();i++){
                row[i] = row[i] + temp[i];
            }
            rowIndex--;
        }

        return row;
    }
};

// int main(){
//     cout << "hello world" << endl;
//     Solution temp;
//     vector<int> test = temp.getRow(4);
//     for(int i=0;i<test.size();i++){
//         cout << test[i] << " ";
//     }
//     cout << endl;

//     return 0;
// }
// @lc code=end

