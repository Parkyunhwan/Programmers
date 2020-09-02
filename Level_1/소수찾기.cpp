/*
    https://programmers.co.kr/learn/courses/30/lessons/12921

    생각
        * 소수는 1과 자기자신 사이의 모든 숫자로 나눠질 수 없다. 즉, 사잇숫자로 나눴을 때 나머지가 나올 수 없다.
        * 이 방법은 가장 먼저 생각할 수 있으나 모든 수에 대한 이중 for문으로 인해 효율성에서 실패한다.
        * 
        * 2번째 방법은 '에라토스체네스의 체'라는 소수를 구하는 최적의 알고리즘 이다.
        * 현재 i의 배수에 해당하는 숫자를 n보다 작은 범위까지 표시해둔다. 해당 숫자는 소수가 아니다.
        * 해당 내용을 반복하면서 남아있는 숫자가 소수이므로 이 숫자들을 세도록 한다.
*/
#include <string>
#include <vector>
bool arr[1000001];
using namespace std;

int solution(int n) {
    int answer = 0;
    for(int i=2; i<=n; i++){
        if(arr[i]==false)
            answer++;
        for(int j=2; i*j<=n; j++){
            arr[i*j]=true;
        }
    }
    return answer;
}