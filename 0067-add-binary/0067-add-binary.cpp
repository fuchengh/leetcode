#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        int pa = a.length()-1, pb = b.length()-1;
        if(pa < pb) return addBinary(b, a);
        
        string sum = "";
        int carry = 0;
        
        while(pb >= 0) {
            int s = a[pa] - '0' + b[pb] - '0' + carry;
            carry = (s >= 2) ? 1 : 0;
            s %= 2;
            sum += to_string(s);
            pa--;
            pb--;
        }
        while(pa >= 0) {
            int s = a[pa] - '0' + carry;
            carry = (s >= 2) ? 1: 0;
            s %= 2;
            sum += to_string(s);
            pa--;
        }
        if(carry) sum += '1';
        
        
        reverse(sum.begin(), sum.end());
        return sum;
    }
};