#include<stdio.h>
#include<string.h>
char str[110];
int main(){
    int c=1;
    scanf("%s",&str);
    for(int i = 0; i<strlen(str); i++){
        if(str[i] == 'A' && c == 1){
            c = 2;
        }
        else if(str[i] == 'A' && c == 2){
            c = 1;
        }
        else if(str[i] == 'B' && c == 2){
            c = 3;
        }
        else if(str[i] == 'B' && c == 3){
            c = 2;
        }
         else if(str[i] == 'C' && c == 1){
            c = 3;
        }
        else if(str[i] == 'C' && c == 3){
            c = 1;
        }   
    }
    printf("%d", c);
}
