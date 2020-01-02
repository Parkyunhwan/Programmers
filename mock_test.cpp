#include <string>
#include <vector>
/*코딩테스트 연습
완전탐색
모의고사
*/
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> answers) {
    vector<vector<int>> supo;
    vector<int> supoza[3]={{1,2,3,4,5},{2,1,2,3,2,4,2,5},{3,3,1,1,2,2,4,4,5,5}};
    vector<int> answer;
    vector<int> v_max;
    int su_num=1;
    int k;
    int re = 0;
    int max = 0;
    for(int i=0; i < 3; i++){
        k = 0;
        for(int j=0;j < answers.size(); j++)
        {
            if(supoza[i][k]==answers[j]) //수포자의 정답과 답안이 같다면
                re++;                   // 정답 증가
            k++;                       // 수포자 답안 증가
            if(supoza[i].size()==k)
                k=0;                   // 수포자의 답안을 처음부터 반복함
        }
        v_max.push_back(re);            //정답갯수 저장
        max = max > re ? max : re;    //max 저장
        re=0;
    }
    for(int i=0; i < v_max.size(); i++){
        if(max == v_max[i])
            answer.push_back(i+1);  //max와 같은 수포자만 포함시킴
    }
    return answer;
}