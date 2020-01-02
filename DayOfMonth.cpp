#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(int a, int b) {
    vector<int> month = {31,29,31,30,31,30,31,31,30,31,30,31};
    vector<string> dow = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
    string answer = "";
    int mtod=0;
    int day=0;
    for(int i = 0; i < a-1; i++)
        mtod+=month[i];
    day=mtod+b;
    cout << day << endl;
    answer=dow[(4+day)%7];
    return answer;
}