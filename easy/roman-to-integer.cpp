#include<bits/stdc++.h>
using namespace std;

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

class Solution {
public:
    int romanToInt(string s) {
        int conv = 0;
        for(int i=0; i<s.length(); i++){
            if (i+1 < s.length() && (value(s[i]) < value(s[i+1]))){
                conv += value(s[i+1]) - value(s[i]);
                i++;
            }else{
                conv += value(s[i]);
            }
            // cout<<conv<<endl;
        }
        return conv;
    }
    
    int value(char r){
        if (r == 'I')
            return 1;
        if (r == 'V')
            return 5;
        if (r == 'X')
            return 10;
        if (r == 'L')
            return 50;
        if (r == 'C')
            return 100;
        if (r == 'D')
            return 500;
        return 1000;
    }
};


int main(){
    cout<<Solution().romanToInt("III")<<endl;
    cout<<Solution().romanToInt("IX")<<endl;
    cout<<Solution().romanToInt("LVIII")<<endl;
    cout<<Solution().romanToInt("MCMXCIV")<<endl;
    return 0;
}