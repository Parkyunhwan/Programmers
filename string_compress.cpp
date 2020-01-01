/*코딩테스트 연습
2020 KAKAO BLIND RECRUITMENT
문자열 압축
도움말
*/
#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<string> convert(string s, int n){
    string sub;
    vector<string> ret;
    for(int i=0; i < s.length(); i+=n){
            sub=s.substr(i,n);
            ret.push_back(sub);
    }
    return ret;
}
int solution(string s) {
    int answer = 0;
    string front;
    int cnt;
    int min=s.length();

    vector<string> tok;
    for(int i=1; i < s.length()/2; i++)
    {
        string str="";
        tok=convert(s,i);
        front = tok[0];
        cnt=1;
        for(int j=1; j<tok.size();j++)
        {
            if(front==tok[j])cnt++;
            else 
            {
                if(cnt!=1)
                    str += to_string(cnt);
                str += front;
                cnt = 1;
                front=tok[j];
            }
        }
        if(cnt!=1)
            str += to_string(cnt);
        str += front;        
        cout << str << endl;
        min = min > str.length() ? str.length() : min;
    }
    return min;
}

int main(){
    string str1("ababcdcdababcdcd");
    int num;
    num=solution(str1);
    cout << "min" << num << endl;
}