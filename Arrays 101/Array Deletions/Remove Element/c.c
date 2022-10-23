// Most Optimal C Solution
int removeElement(int* nums, int numsSize, int val){
    int c = 0;
    int y = 0;
    for(int i = 0; i< numsSize; i++){
        if(*(nums+i) == val){          
            c+=1;
        }else{
            *(nums+y) = *(nums+i);
            y+=1;       
        }
    }
    return numsSize-c;
}
