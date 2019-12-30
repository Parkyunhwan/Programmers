#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    cout << "aa" << endl;
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code!"};
    for (const string& word : msg)
    {
        cout << word << " ";
    }
    for(int i = 0; i < 5; i++){
        cout << i << endl;
    }
    cout << endl;
}