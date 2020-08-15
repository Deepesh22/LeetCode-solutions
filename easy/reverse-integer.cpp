#include<bits/stdc++.h>
using namespace std;

// Input: 123
// Output: 321

class Solution {
public:
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
    cout<<Solution().reverse(-123);
    return 0;
}