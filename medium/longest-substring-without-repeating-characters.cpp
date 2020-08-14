#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 1200ms
    int lengthOfLongestSubstring(string s) {
        int maxlen = 0;
        unordered_set<char> lookup;
        int p1=0;
        int p2=0;

        while(p1<s.length() && p2<s.length()){
            if (lookup.find(s[p2]) != lookup.end()){
                lookup.clear();
                int len = p2 - p1;
                if (len > maxlen){
                    maxlen = len;
                }
                cout<<p1<<" "<<p2<<" "<<s[p2]<<endl;
                p1 = p1+1;
                lookup.insert(s[p1]);
                p2 = p1+1;
            }else{
                lookup.insert(s[p2]);
                p2 ++;
            }
        }
        int len = p2 - p1;
        if (len > maxlen){
            maxlen = len;
        }

        return maxlen;
    }

    // 8ms
    int lengthOfLongestSubstringFaster(string s) {
        int maxlen = 0;
        int a[256] = {0};
        int p1=0;
        int p2=0;

        while(p1<s.length()){
            if (a[s[p2]] == 0){
                a[s[p2]]++;
                maxlen = max(maxlen, p2-p1+1);
                p2 ++;
            }else{
                a[s[p1]]--;
                p1 ++;
            }
        }

        return maxlen;
    }
};

int main() {
    cout<<Solution().lengthOfLongestSubstring("abcabcbba")<<endl;
    cout<<Solution().lengthOfLongestSubstring("abacdefgahijk")<<endl;
    cout<<Solution().lengthOfLongestSubstring("a")<<endl;
    return 0;
}