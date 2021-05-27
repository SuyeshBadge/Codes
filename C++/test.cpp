
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int count_prime[1000000 + 1];

int SieveOfEratosthenes()
{
    ll n = 1000000;
    bool prime[n + 1];
    memset(prime, true, sizeof(prime));

    for (int p = 2; p * p <= n; p++)
    {

        if (prime[p] == true)
        {

            for (int i = p * p; i <= n; i += p)
                if (prime[i])
                {
                    prime[i] = false;
                }
        }
    }
    int count = 0;
    for (int p = 2; p <= n; p++)
    {
        if (prime[p])
        {
            count++;
        }
        count_prime[p] = count;
    }

    return 0;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    SieveOfEratosthenes();
    int t;
    cin >> t;
    while (t--)
    {
        int x, y;
        cin >> x >> y;

        if (count_prime[x] <= y)
        {
            cout << "Chef\n";
        }
        else
        {
            cout << "Divyam\n";
        }
    }
    return 0;
}
