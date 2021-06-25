#include <bits/stdc++.h>
using namespace std;
bool allCharactersSame(string s)
{
    set<char> s1;

    // Insert characters in the set
    for (int i = 0; i < s.length(); i++)
        s1.insert(s[i]);
    if (s1.size() == 1)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{
    int n;
    cin >> n;
    string str;
    cin >> str;
    for (int i = 0; i < n; i++)
    {
        if (str[i] == '.')
        {
            str[i] = 'B';
        }
    }
    if (allCharactersSame(str))
    {
        cout << "NO";
    }
    else
    {
        cout << "YES" << endl
             << str;
    }

    return 0;
}
