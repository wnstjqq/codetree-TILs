#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    cout << A + B << "\n";

    double avg = (A + B) / 2;

    cout << fixed;
    cout.precision(1);

    cout << avg;
     
    return 0;
}