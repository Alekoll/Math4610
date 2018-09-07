//
//  main.cpp
//  SmacEp
//
//  Created by Alex Collantes on 9/5/18.
//  Copyright © 2018 Alex Collantes. All rights reserved.
//

#include <iostream>
#include <cfloat>
#include <cmath>


using namespace std;

//Calculates Single Precision
void SmacEp(float Sep, int iPow){
    //Set values close to 1
    float one = 1.0;
    Sep = 1.0;
    float appOne = one + Sep;
    
    iPow = 0;
    for( int i = 1; i < 1000; i++){
        iPow += 1;
        Sep = Sep/2;
        appOne = one + Sep;
        if(abs(appOne - one) == 0.0){
            break;
        }
        
    }
    std::cout << "Digits: " << iPow << " Machine Ep: " << Sep << endl;
}



int main(int argc, const char * argv[]) {
    // insert code here...
    
    SmacEp(1.0, 0);
    return 0;
}
