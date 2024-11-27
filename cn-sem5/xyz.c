#include <stdio.h>
#include <string.h>

// Function to perform XOR operation
void performXOR(char *dividend, char *divisor, int divisor_length) {
    for (int i = 0; i < divisor_length; i++) {
        dividend[i] = (dividend[i] == divisor[i]) ? '0' : '1';
    }
}

// Function to calculate CRC
void calculateCRC(char data[], char divisor[], char crc[]) {
    int data_length = strlen(data);
    int divisor_length = strlen(divisor);
    char temp[data_length + 1];
    
    // Append zero bits to data
    strcpy(temp, data);
    for (int i = 0; i < divisor_length - 1; i++) {
        strcat(temp, "0");
    }
    
    int temp_length = strlen(temp);
    char remainder[temp_length];
    strcpy(remainder, temp);
    
    // Perform division using XOR
    for (int i = 0; i <= temp_length - divisor_length; i++) {
        if (remainder[i] == '1') {
            performXOR(&remainder[i], divisor, divisor_length);
        }
    }

    // Extract remainder
    strncpy(crc, &remainder[temp_length - divisor_length + 1], divisor_length - 1);
    crc[divisor_length - 1] = '\0';
}

// Main function
int main() {
    char data[] = "100100";      // Input data
    char divisor[] = "1101";      // Divisor
    char crc[4];                  // CRC storage

    // Calculate CRC
    calculateCRC(data, divisor, crc);

    // Append CRC to original data
    char encodedData[strlen(data) + strlen(crc) + 1];
    strcpy(encodedData, data);
    strcat(encodedData, crc);

    // Display results
    printf("Data: %s\n", data);
    printf("Divisor: %s\n", divisor);
    printf("CRC: %s\n", crc);
    printf("Encoded Data: %s\n", encodedData);

    return 0;
}
