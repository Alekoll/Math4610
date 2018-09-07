//
//  main.cpp
//  DmacEp
//
//  Created by Alex Collantes on 9/5/18.
//  Copyright © 2018 Alex Collantes. All rights reserved.
//

#include <iostream>
#include <cmath>


using namespace std;

//Calculates Double Precision
void DmacEp(double Dep, int iPow){
    //Set values close to 1
    double one = 1.0;
    Dep = 1.0;
    double appOne = one + Dep;
    
    iPow = 0;
    for( int i = 1; i < 1000; i++){
        iPow += 1;
        Dep = Dep/2;
        appOne = one + Dep;
        if(abs(appOne - one) == 0.0){
            break;
        }
        
    }
    std::cout << "Digits: " << iPow << " Machine Ep: " << Dep << endl;
}



int main(int argc, const char * argv[]) {
    DmacEp(1.0, 0);
    return 0;
}
