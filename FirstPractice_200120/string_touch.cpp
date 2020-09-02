#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool solution(string s) {
    bool answer = true;
    int len = s.length();
    int num=0;
    int str=0;
    cout << int(s[0]);
    if( len != 4 && len != 6)
        answer = false;
    else
    {
        for(int i = 0; i < len; i++)
        {
            if(s[i]<97)
                num++;
            else
                str++;
        }
        if(num!=0 && str!=0)
            answer = false;
    }
    return answer;
}

// 다른 모범 풀이
#include <string>
#include <vector>
using namespace std;

bool solution(string s) {
    bool answer = true;

    for (int i = 0; i < s.size(); i++)
    {
        if (!isdigit(s[i])) // isdigit의 사용,,
//int isdigit( int c )
//c : 검사할 문자 또는 아스키 값
//반환값 : 문자가 0~9 사이에 속하면 true, 아니면 false
            answer = false;
    }

    return s.size() == 4 || s.size() == 6 ? answer : false;
}
