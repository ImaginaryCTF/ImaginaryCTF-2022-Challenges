#include <stdlib.h>
#include <stdio.h>

char dead;
int init = 0;

int get_rand(){
    rand();
    if (init == 0) {
        init = 1;
        uint seed = 0;
        FILE* urandom = fopen("/dev/urandom", "r");
        for (int i = 0; i < 8; i++) {
            seed += fgetc(urandom);
            if (i!= 7){
                seed <<=8;
            }
        }
        fclose(urandom);
        srand(seed);
        for (int i = 0; i < rand()>>15; i++){
            rand();
        }
    }
    return (uint)(rand() >> 15);
}

int main() {
    setvbuf(stdout,NULL,2,0);
    setvbuf(stdin,NULL,2,0);

    printf("You start with $100. Get 1 billion dollars, and we'll give you the flag.\n");
    printf("Run out of money, and we kick you out of the casino.\n\n");
    printf("Are you feeling lucky?\n\n");

    uint money = 100;

    while(1) {
        int n1 = get_rand();
        printf("Current money: %u\n", money);
        if (money > 1000000000) {
            char flag_buf[50];
            FILE* file = fopen("./flag.txt", "r");
            fscanf(file, "%s", flag_buf);
            printf("How'd you beat the house? %s\n", flag_buf);
            exit(0);
        }
        printf("How much are you betting? (minimum bet $5)\n");
        printf(">>> ");
        uint gamble;
        scanf("%u%c", &gamble, &dead);
        if (gamble < 5 || gamble > money) {
            printf("You can't bet that!\n");
            printf("Get out of here, and come back with some real money!\n");
            exit(1);
        }
        money -= gamble;
        printf("The first number is %d.\n\n", n1);
        float low_odds = ((float)n1+1)/65536;
        float high_odds = 1 - low_odds;
        int low_payout = (.99 * gamble / low_odds);
        int high_payout = (.99 * gamble / high_odds);
        printf("Odds of higher: %.2f\tPayout of higher: %u\n", high_odds*100, high_payout);
        printf("Odds of lower:  %.2f\tPayout of lower:  %u\n\n", low_odds*100, low_payout);
        printf("Do you think the next number will be:\n");
        printf("1) Higher\n");
        printf("2) Lower\n\n");
        printf("Remember, the house wins ties!\n");
        printf(">>> ");
        char guess;
        scanf("%c%c", &guess, &dead);
        int n2 = get_rand();
        int win = 0;
        int payout = 0;
        printf("The second number is %d!\n", n2);
        if (guess == '1' && n1 < n2) {
            win = 1;
            payout = high_payout;
        } else if (guess == '2' && n1 > n2) {
            win = 1;
            payout = low_payout;
        }

        if (win) {
            printf("Congrats! You won %u dollars!\n\n", payout);
            money += payout;
        } else {
            printf("You lost... Better luck next time!\n\n");
        }
    }

    
}