#include <iostream>
#include <stdio.h>

int solve(void)
{
    int a, b;
    std::cin >> a >> b;
    std::cout << a + b << "\n";
    return 0;
}
int main()
{
    int t;
    std::cin >> t;
    while (t--)
    {
        solve();
    }
}
