#include <iostream>
using namespace std;
int main() {
    // unary operators in c++
    int a = 5;
    cout << "Original a: " << a << endl;
    // unary plus
    cout << "Unary plus: " << +a << endl; // remains 5
    // unary minus
    cout << "Unary minus: " << -a << endl; // becomes -5
    // increment operator
    cout << "Pre-increment: " << ++a << endl; // a becomes 6
    cout << "Post-increment: " << a++ << endl; // prints 6, then a becomes 7
    cout << "After Post-increment a: " << a << endl; // prints 7
    // decrement operator   
    cout << "Pre-decrement: " << --a << endl; // a becomes 6
    cout << "Post-decrement: " << a-- << endl; // prints 6, then a becomes 5
    cout << "After Post-decrement a: " << a << endl; // prints 5
}