#include <stdio.h>
int main(){
  int number, num1, num2, result1, result2, result3, result4, result5;

  printf("if you wanna PLUS please input number 1\nif you wanna MINUS please input number 2\nif you wanna MULTIPLE please input number 3\nif you wanna DIVISION please input number 4\nif you wanna REST please input number 5\n");
  printf("Input your number: ");
  scanf("%d", &number);

  if(number == 1){
    printf("\nYOU WANNA PLUS!\n");
    printf("Input your first number: ");
    scanf("%d", &num1);
    printf("input your second number: ");
    scanf("%d", &num2);

    result1 = num1 + num2;

    printf("%d", result1);
  }

  else if(number == 2){
    printf("\nYOU WANNA MINUS!\n");
    printf("Input your first number: ");
    scanf("%d", &num1);
    printf("input your second number: ");
    scanf("%d", &num2);

    result2 = num1 - num2;

    printf("%d", result2);
  }

  else if(number == 3){
    printf("\nYOU WANNA MULTIPLE!\n");
    printf("Input your first number: ");
    scanf("%d", &num1);
    printf("input your second number: ");
    scanf("%d", &num2);

    result3 = num1 * num2;

    printf("%d", result3);
  }

  else if(number == 4){
    printf("\nYOU WANNA DIVISION!\n");
    printf("Input your first number: ");
    scanf("%d", &num1);
    printf("input your second number: ");
    scanf("%d", &num2);

    result4 = num1 / num2;

    printf("%d", result4);
  }

  else if(number == 5){
    printf("\nYOU WANNA REST!\n");
    printf("Input your first number: ");
    scanf("%d", &num1);
    printf("input your second number: ");
    scanf("%d", &num2);

    result5 = num1 % num2;

    printf("%d", result5);
  }

  else{
      printf("YOU INPUT WRONG NUMBER, PLEASE TRY AGAIN !!");
    }

  return 0; 
}