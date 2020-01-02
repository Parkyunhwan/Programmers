/*코딩테스트 연습
정렬
K번째수
*/
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
vector<int> div_arr(vector<int> arr, vector<int> range)
{
    vector<int> div;
    for(int i = range.front() ; i <= range.back(); i++)
    {
        div.push_back(arr[i]);
        //cout << i <<" : "<<arr[i] << endl;
    }
    //cout << "FF" <<endl;
    return div;
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> range;
    vector<int> arr_ran;
    vector<int>::iterator it;
    for(int i=0; i<commands.size(); i++)
    {
        range.push_back(--commands[i][0]);
        range.push_back(--commands[i][1]);
        arr_ran = div_arr(array, range);
        range.clear();
        sort(arr_ran.begin(),arr_ran.end());
        sort(--commands[i][0],--)
        answer.push_back(arr_ran[--commands[i][2]]);
    }

    return answer;
}

    // 다른 간결한 풀이
    // for(int i = 0; i < commands.size(); i++) {
    //     temp = array;
    //     sort(temp.begin() + commands[i][0] - 1, temp.begin() + commands[i][1]); //sorting을 위해 iterator사용, 필요한 위치를 찾아 바로 정렬함
    //     answer.push_back(temp[commands[i][0] + commands[i][2]-2]); //시작 + 선택번호 (원하는 순서) 값을 넣어줌
    // }


int main()
{
    vector<int> akr={1,5,2,6,3,7,4};
    vector<int> a={2,5,3};
    vector<int> b={4,4,1};
    vector<int> c={1,7,3};
    vector<vector<int>> bb;
    vector<int>::iterator it;
    vector<int> an;
    bb.push_back(a);
    bb.push_back(b);
    bb.push_back(c);
    an=solution(akr,bb);
    for(it=an.begin(); it!=an.end(); it++)
    {
        cout << *it << endl;
    }
}