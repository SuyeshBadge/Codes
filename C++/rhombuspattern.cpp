#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = n - i; j >= 1; j--)
        {
            cout << " ";
        }
        for (int j = 1; j <= n; j++)
        {
            cout << " * ";
        }
        cout << endl;
    }
    return 0;
}
