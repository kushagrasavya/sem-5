#include <stdio.h>
#include <string.h>
int main() {
    char binary[100];
    int i, count = 0;
    char parity_choice;
    printf("Enter a binary number: ");
    scanf("%s", binary);
    printf("Choose parity even(e) or odd(o): ");
    scanf(" %c", &parity_choice);  // Note the space before %c to ignore newline
    for (i = 0; i < strlen(binary); i++) {
        if (binary[i] == '1') {
            count++;
        }
    }
    if (parity_choice == 'e') {
        if (count % 2 == 0) {
            strcat(binary, "0");
        } else {
            strcat(binary, "1");
        }
    } else if (parity_choice == 'o') {
        if (count % 2 == 0) {
            strcat(binary, "1");
        } else {
            strcat(binary, "0");
        }
    } else {
        printf("Invalid parity choice!\n");
        return 1;
    }
    printf("Parity encoded data: %s\n", binary);
    return 0;
}