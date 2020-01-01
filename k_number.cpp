#include <string>
#include <vector>
#include <iostream>
using namespace std;
vector<int> div_arr(vector<int> arr, vector<int> range)
{
    vector<int> div;
    for(int i = range.front() ; i <= range.back(); i++)
    {
        div.push_back(arr[i]);
        cout << i <<" : "<<arr[i] << endl;
    }
    cout << "FF" <<endl;
    return div;
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> range;
    vector<int> arr_ran;
    for(int i=0; i<commands.size(); i++)
    {
        range.push_back(--commands[i][0]);
        range.push_back(--commands[i][1]);
        arr_ran = div_arr(array, range);
        range.clear();
    }
    

    return answer;
}

int main()
{
    vector<int> akr={1,5,2,6,3,7,4};
    vector<int> a={2,5,3};
    vector<int> b={4,4,1};
    vector<int> c={1,7,3};
    vector<vector<int>> bb;
    bb.push_back(a);
    bb.push_back(b);
    bb.push_back(c);
    solution(akr,bb);
}