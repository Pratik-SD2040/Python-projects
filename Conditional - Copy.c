#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    int rand_int,guess;
    //random integer generation

    srand((unsigned)time(NULL));                 // seed once so runs differ
    rand_int = 1 + rand() % 1000;                // val in [1,1000]

        printf("Try guessing the number\n");

    //Looping and logic
    while (guess!=rand_int) {
        scanf("%d", &guess);

            if (guess>rand_int) {
                printf("Try going lower\n");
            }else if (guess<rand_int) {
                printf("Try going higher\n");
            }else {
                printf("You guessed it!!!");
            }
    }
    return 0;
}
