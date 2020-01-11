#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int sub=arr[0];
    for(auto& i : arr)
    {
        if(sub==i) continue;
        answer.push_back(sub);
        sub=i;
    }
    answer.push_back(sub);

    return answer;
}