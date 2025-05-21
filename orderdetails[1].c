#include<stdio.h>
extern void user();
extern void ordering();
int main()
{
    char l[20];     
    user(l);        
    printf("Hello, %s!\n", l);  
    ordering();
}



