#include <bits/stdc++.h>
using namespace std;
bool solve(int n)
{
    int zc = 0, oc = 0;
    while (n > 0)
    {
        int ln = n % 10;
        if (ln == 0)
        {
            oc = 0;
            zc++;
            if (zc >= 7)
            {
                return true;
            }
        }
        else
        {
            zc = 0;
            oc++;
            if (oc >= 7)
            {
                return true;
            }
        }
        n = n / 10;
    }
    return false;
}
int main()
{
    int n;
    cin >> n;
    bool ans = solve(n);
    if (ans)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}