/*
코딩테스트 연습
연습문제
나누어 떨어지는 숫자 배열
*/
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    for(auto& i : arr)
    {
        if(i%divisor==0)
            answer.push_back(i);
    }
    if(answer.empty())
        answer.push_back(-1);
    sort(answer.begin(),answer.end());
    return answer;
}