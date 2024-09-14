#include <iostream>

int nod2(int a, int b) {
    if (a == b)
        return a;
    if (a > b)
        return nod2(a - b, b);
    return nod2(a, b - a);
}

int nok2(int a, int b) {
    return a / nod2(a, b) * b;
}

int main() {
    int a, b, c;

    std::cin >> a >> b >> c;

    std::cout << nok2(a, nok2(b, c)) << '\n';

    return 0;
}