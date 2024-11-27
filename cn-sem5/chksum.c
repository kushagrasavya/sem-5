#include <stdio.h>
#include <stdlib.h>

// Function to validate binary input
int validate_binary_input(int n, int arr[]) {
    for (int i = n - 1; i >= 0; i--) {
        if (arr[i] != 0 && arr[i] != 1) {
            printf("Invalid input! Only binary digits (0 or 1) are allowed.\n");
            return 0;
        }
    }
    return 1;
}

int main() {
    int a[10], b[10], c[10], temp, sum[10], carry = 0, n, i;

    printf("------------- Checksum Program for Two Segments -------------\n");

    // Input number of bits
    printf("\nEnter the number of bits for each segment: ");
    scanf("%d", &n);

    if (n > 10 || n <= 0) {
        printf("Invalid bit size! Please enter a value between 1 and 10.\n");
        return 1;
    }

    // Input segments at sender's end
    printf("\n--- Sender's End ---\n");
    printf("Enter the first segment (%d bits, space-separated): ", n);
    for (i = n - 1; i >= 0; i--) scanf("%d", &a[i]);

    if (!validate_binary_input(n, a)) return 1;

    printf("Enter the second segment (%d bits, space-separated): ", n);
    for (i = n - 1; i >= 0; i--) scanf("%d", &b[i]);

    if (!validate_binary_input(n, b)) return 1;

    // Compute sum with carry
    for (i = 0; i < n; i++) {
        sum[i] = (a[i] + b[i] + carry) % 2;
        carry = (a[i] + b[i] + carry) / 2;
    }

    // Wrap-around carry
    if (carry) {
        for (i = 0; i < n; i++) {
            temp = sum[i];
            sum[i] = (temp + carry) % 2;
            carry = (temp + carry) / 2;
        }
    }

    // Compute checksum (one's complement of sum)
    printf("\nChecksum (Sender): ");
    for (i = n - 1; i >= 0; i--) {
        sum[i] = 1 - sum[i];
        printf("%d", sum[i]);
    }

    // Receiver's end
    printf("\n\n--- Receiver's End ---\n");
    printf("Enter the first received segment (%d bits, space-separated): ", n);
    for (i = n - 1; i >= 0; i--) scanf("%d", &a[i]);

    if (!validate_binary_input(n, a)) return 1;

    printf("Enter the second received segment (%d bits, space-separated): ", n);
    for (i = n - 1; i >= 0; i--) scanf("%d", &b[i]);

    if (!validate_binary_input(n, b)) return 1;

    printf("Enter the received checksum (%d bits, space-separated): ", n);
    for (i = n - 1; i >= 0; i--) scanf("%d", &c[i]);

    if (!validate_binary_input(n, c)) return 1;

    // Compute sum with checksum
    carry = 0;
    for (i = 0; i < n; i++) {
        temp = (a[i] + b[i] + c[i] + carry) % 2;
        carry = (a[i] + b[i] + c[i] + carry) / 2;
        sum[i] = temp;
    }

    // Wrap-around carry
    if (carry) {
        for (i = 0; i < n; i++) {
            temp = sum[i];
            sum[i] = (temp + carry) % 2;
            carry = (temp + carry) / 2;
        }
    }

    // Validate checksum
    int error_flag = 0;
    printf("\nReceiver's Checksum: ");
    for (i = n - 1; i >= 0; i--) {
        sum[i] = 1 - sum[i];
        printf("%d", sum[i]);
        error_flag += sum[i];
    }

    if (error_flag == 0)
        printf("\nChecksum PASSED. Data is valid.\n");
    else
        printf("\nChecksum FAILED. Data is corrupted.\n");

    return 0;
}
