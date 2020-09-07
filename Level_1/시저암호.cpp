#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string s, int n) {
    string answer = "";
    char start=' ';
    for(int i=0; i<s.length(); i++)
    {
        //char ch = s[i];
        if('A' <= s[i] && s[i] <= 'Z')
            start = 'A';
        else if('a' <= s[i] && s[i] <= 'z')
            start = 'a';
        if(s[i]!=' ')
            s[i] = (s[i]+n-start)%26 + start;
        cout << s[i] << "\n";
    }   
    return s;
}