#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
    int q, n;
    cin >> n >> q;
    vector<vector<long>> arr(n);
    for (int i = 0; i < n; i++)
    {

        int r;
        cin >> r;
        arr[i].resize(r);
        for (int j = 0; j < r; j++)
        {
            cin >> arr[i][j];
        }
    }
    for (int k = 0; k < q; k++)
    {
        int x, y;
        cin >> x >> y;
        cout << arr[x][y] << endl;
    }
    return 0;
}
