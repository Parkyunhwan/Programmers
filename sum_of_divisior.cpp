/*
코딩테스트 연습
연습문제
약수의 합
*/
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int i=1;
    while(i<=n){
        if(n%i==0)
            answer+=i;
        i++;
    }
    return answer;
}