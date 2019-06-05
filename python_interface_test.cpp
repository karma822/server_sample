//
//  python_interface_test.cpp
//  python_interface_test
//
//  Created by Yousun Lee on 05/06/2019.
//  Copyright © 2019 Yousun Lee. All rights reserved.
//

#include "python_interface_test.hpp"
#include <iostream>

using namespace std;
extern "C" int* test_api()
{
    int *ret = new int[6];
    for( int i = 0 ; i < 6; ++i ) {
        ret[i] = i;
    }
    cout<<"test_api"<<endl;
    return ret;
}

extern "C" int test()
{
    cout<<"test"<<endl;
    return 0;
}
