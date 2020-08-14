#include<bits/stdc++.h>
using namespace std;

// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> s;
        int r;
        vector<int> ans;
        for(int i = 0; i < nums.size(); i++){
            r = target - nums[i];
            if (s.find(r) != s.end()){
               if (s[r] != i){
                   ans.push_back(s[r]);
                   ans.push_back(i);
                   break;
               } 
            }
            s[nums[i]] = i;
        }
        
        return ans;
    }
};


int main(){
    return 0;
}