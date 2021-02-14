#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <bits/stdc++.h>

int solve(void)
{
    int amt;
    float bal;
    std::cin >> amt;
    std::cin >> bal;
    if (amt % 5 == 0 and amt < bal)
    {

        bal = (bal - (float)amt - 0.50);

        std::cout << std::fixed << std::setprecision(2) << bal;
    }
    else
    {
        std::cout << std::fixed << std::setprecision(2) << bal;
    }

    return 0;
}
int main()
{
    solve();
}