#include <iostream>
using namespace std;
int main(){
    // typecasting & type conversion
    // implicit conversion (automatic -- done by compiler itself)
    // conversion is implicit and typecasting is explicit
    int a = 10;
    double b = a; // int to double
    cout << "Implicit Conversion: " << b << endl;
    // explicit conversion (manual -- done by programmer)
    double c = 9.78;
    int d = (int)c; // double to int
    cout << "Explicit Conversion: " << d << endl;
    return 0;
}