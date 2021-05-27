#include <bits/stdc++.h>
#include <cmath>
using namespace std;
int main()
{
    int test;
    cin >> test;

    while (test--)
    {
        long long int n, x;
        cin >> n >> x;
        long long int z;
        long long int a[1000000];

        for (long long int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        long long int i = 0;
        long long int kk = x;
        while (kk > 0 and i < n - 1)
        {

            int flag = 0;
            long long int p = log(a[i]) / log(2);
            long long int r = 1 << p;
            a[i] = a[i] ^ r;

            long long int j = i + 1;

            while (j < n)
            {
                if ((a[j] ^ r) < a[j])
                {
                    a[j] = a[j] ^ r;
                    flag = 1;
                    break;
                }
                j++;
            }

            if (flag == 0)
            {
                a[n - 1] = a[n - 1] ^ r;
            }

            while (a[i] <= 0)
            {
                i++;
            }

            z = kk + 1;

            kk--;
        }
        if (z > 0)
        {
            if ((n < 3) and z % 2 > 0)
            {
                a[n - 1] = a[n - 1] ^ 1;
                a[n - 2] = a[n - 2] ^ 1;
            }
        }

        for (int i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }
        cout << endl;
    }
}