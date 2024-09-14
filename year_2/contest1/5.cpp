#include <iostream>


int main(){

    int n, input_number, res = 0;

    std::cin >> n;

    for (int i = 0; i < n; i++){
        std::cin >> input_number;
        if (abs(input_number) > abs(res))
            res = input_number;
    }

    std::cout << res << "\n";
    
    return 0;
}