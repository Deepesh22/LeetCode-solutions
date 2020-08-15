#include<bits/stdc++.h>
using namespace std;

// Example 1:
// Input: 121
// Output: true

// Example 2:
// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0){
            return false;
        }
        return x == reverse(x);

    }

    int reverse(int x) {
        long rev = 0;
        while(abs(x)>0){
            rev = 10*rev + (x%10);
            x = x / 10;
            if (rev>INT_MAX || rev<INT_MIN){
                return 0;
            }
            cout<<rev<<x<<endl;
        }
        
        return rev;
    }
};



int main(){
    return 0;
}