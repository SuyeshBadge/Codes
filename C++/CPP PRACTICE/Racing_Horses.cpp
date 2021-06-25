#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        sort(arr, arr + n);
        int dif = INT_MAX;
        for (int i = 1; i < n; i++)
        {
            if (arr[i] - arr[i - 1] < dif)
            {
                dif = arr[i] - arr[i - 1];
            }
        }
        cout << dif << endl;
    }
    return 0;
}
