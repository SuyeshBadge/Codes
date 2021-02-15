#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        int n, k, i = 1, a, b;
        cin >> n >> k;
        a = n;
        b = 1;
        k = k % n;
        while (i < k)
        {
            if (a == b)
            {
                if (b < n)
                {
                    b += 1;
                }
                else
                {
                    b = 1;
                }
            }
            if (a == 1)
            {
                a = n;
            }
            else
            {
                a -= 1;
            }
            if (b == n)
            {
                b = 1;
            }
            else
            {
                b += 1;
            }
            i++;
            if (a == b)
            {
                if (b < n)
                {
                    b += 1;
                }
                else
                {
                    b = 1;
                }
            }
        }
        cout << b << "\n";
    }

    return 0;
}