// importing required packages
#include <iostream>
using namespace std;

void minmaxArray (int values[], int size, int minmax[]){
    // let the first element of the array be assigned to min and max
    int min = values[0];
    int max = values[0];

    // iterate over the elements of the array
    for ( int i = 0; i < size; i++ ){
        // if a smaller value than min found, update it
        if (values[i]<min){
            min = values[i];
        }

        // if a greater value than max found, update it
        if (values[i]>max){
            max = values[i];
        }
    }
    minmax[0] = min;
    minmax[1] = max;
}

int main (){
    // user input for array
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;
    int values[ size ];
    for ( int i = 0; i < size; i++ ){
        cout << "Enter value " << i << ": ";
        cin >> values[ i ];
    }
    int minmax[2];

    // printing min and max of the array
    minmaxArray(values, size, minmax);
    cout << "Minimum: " << minmax[0] << endl;
    cout << "Maximum: " << minmax[1] << endl;
}