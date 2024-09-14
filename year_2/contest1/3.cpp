#include <iostream>


int main() {
    int a;
    std::cin >> a;

    if (a % 2 == 0){
        std::cout << "Yes\n";
    } else{
        std::cout << "No\n";
    }
    return 0;
}