bool validMountainArray(int* arr, int arrSize){
    bool i = true;
    bool p = true;
    for(int j = 0; j<arrSize-1; j++){
        if(*(arr+j) == arr[j+1] || ((p || *(arr+j) < *(arr+j+1)) && !i)){
            return false;
        }
        else if( i && *(arr+j) > *(arr+j+1)){
            i = false;  
            p = true;
        }
        if(j == 0 || (i && j == arrSize-2)){
            p = true;
        }else{
            p = false;
        }
    }
    return !p; 
}
