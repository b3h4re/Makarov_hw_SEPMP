#include <iostream>


int main(){

    char c = '0';
    int res = 0;

    while (c == '0' || c == '1'){
        std::cin >> c;
        if (c == '1') res++;
    }

    std::cout << res << "\n";
    
    return 0;
}