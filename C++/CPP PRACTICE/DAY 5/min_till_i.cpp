#include <bits/stdc++.h>
using namespace std;
void solve(int arr[], int n)
{
    int mx = arr[0];
    for (int i = 0; i < n; i++)
    {
        mx = max(mx, arr[i]);
        cout << mx << " ";
    }
}
int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    solve(arr, n);

    return 0;
}