#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string s) {
    string answer = "";
    if(s.length()%2==0){
        answer+=(s[s.length()/2 - 1]);
        answer+= s[s.length()/2];
    }
    else{
        answer+=(s[s.length()/2]);
    }
    return answer;
}

// #include <string>

// using namespace std;

// string solution(string s) {
//     return s.length()&1 ? s.substr(s.length()*0.5,1) : s.substr(s.length()*0.5-1,2);  한 줄로 문제를 마무리 함.
// }