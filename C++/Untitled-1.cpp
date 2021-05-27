#include <bits/stdc++.h>
#define ll long long int

using namespace std;

ll Ifpossible(ll x, ll a[], ll n)
{
    int psum[x + 1] = {'\0'};

    psum[0] = 1;

    for (int i = 0; i < n; i++)
    {
        for (int j = x; j >= a[i]; j--)
        {
            if (psum[j - a[i]] == 1)
                psum[j] = 1;
        }
    }
    return psum[x];
}

void solve()
{
    ll n, k;
    cin >> n >> k;
    ll sum1 = 0, ans1 = 0;
    ll a[n] = {'\0'};
    for (ll i = 0; i < n; i++)
    {
        cin >> a[i];
        sum1 += a[i];
    }

    sort(a, a + n, greater<>());

    if (n == 1 || sum1 < 2 * k)
    {
        cout << "-1\n";
        return;
    }

    else if (sum1 == 2 * k)
    {
        if (sum1 % 2 == 1 || a[0] > k)
        {
            cout << "-1\n";
            return;
        }

        //exat posiible case
        else if (a[0] == k)
        {
            cout << n << "\n";
        }

        else
        {

            if (Ifpossible(k, a, n))
            {
                cout << n << "\n";
                return;
            }
            else
            {
                cout << "-1\n";
                return;
            }
        }
    }

    else if (a[0] >= k)
    {
        ans1 = 1;
        ll tempsum = 0;
        for (ll i = 1; i < n; i++)
        {
            tempsum += a[i];
            ans1++;
            if (tempsum >= k)
            {
                cout << ans1 << "\n";
                return;
            }
        }
    }

    else
    {

        ll tsum = 0;
        for (ll i = 0; i < n; i++)
        {
            tsum += a[i];
            if (tsum >= 2 * k)
            {
                cout << i + 1 << "\n";
                return;
            }
        }
        cout << "-1\n";
    }
}

int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}