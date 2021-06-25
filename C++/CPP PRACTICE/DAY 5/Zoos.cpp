#include <bits/stdc++.h>
using namespace std;
int main()
{
    string str;
    cin >> str;
    int n = str.size();
    float z = 0.0, o = 0.0;
    for (int i = 0; i < n; i++)
    {
        if (str[i] == 122)
        {
            z++;
        }
        else if (str[i] == 111)
        {
            o++;
        }
    }
    if (z == (o / 2))
    {
        cout << "Yes";
    }
    else
    {
        cout << "No";
    }
    return 0;
}