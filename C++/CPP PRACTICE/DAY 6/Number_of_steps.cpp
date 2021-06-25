#include <bits/stdc++.h>
using namespace std;
int minno(int arr[], int n)
{
    int ans = arr[0];
    for (int i = 0; i < n; i++)
    {
        ans = min(ans, arr[i]);
    }
    return ans;
}
int main()
{
    int n;
    cin >> n;
    int a[n], b[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin >> b[i];
    }

    int m = minno(a, n);
    int j = 0;
    int step = 0;

    while (j < n)
    {   if(a[j]<b[j]){
            step = -1;
            break;
    }
        if (a[j] == m)
        {
            j++;
            // cout << "j inc";
        }
        else
        {
            a[j] = a[j] - b[j];
            step++;
            // cout << j;
        }
    }
    cout << step;
    return 0;
}
