#include <iostream>
#include <stdio.h>
using namespace std;
int c = 0;
int main()
{
    int t, k;
    std::cin >> t;
    std::cin >> k;
    while (t--)
    {
        int num;
        std::cin >> num;
        if (num % k == 0)
        {
            c++;
        }
    }
    std::cout << c;
}
