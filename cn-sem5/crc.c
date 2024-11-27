#include <stdio.h>

// Function to perform XOR division for CRC calculation
void perform_crc(int data[], int data_len, int divisor[], int divisor_len, int remainder[]) {
    int temp[50], i, j;

    // Copy data into temp for CRC calculation (data + appended zeros)
    for (i = 0; i < data_len + divisor_len - 1; i++) {
        temp[i] = data[i];
    }

    // Perform XOR division
    for (i = 0; i < data_len; i++) {
        if (temp[i] == 1) { // Only perform division if the leading bit is 1
            for (j = 0; j < divisor_len; j++) {
                temp[i + j] = temp[i + j] ^ divisor[j];
            }
        }
    }

    // Copy the remainder from temp to remainder array
    for (i = 0; i < divisor_len - 1; i++) {
        remainder[i] = temp[data_len + i];
    }
}

// Function to validate received data
int validate_crc(int data[], int data_len, int divisor[], int divisor_len) {
    int remainder[20] = {0};

    // Perform CRC check
    perform_crc(data, data_len, divisor, divisor_len, remainder);

    // Check if the remainder is all zeros
    for (int i = 0; i < divisor_len - 1; i++) {
        if (remainder[i] != 0) {
            return 0; // Error detected
        }
    }
    return 1; // No error
}

int main() {
    int data[50], transmitted_data[50], divisor[20], remainder[20], received_data[50];
    int data_len, divisor_len, i;

    // Input divisor
    printf("Enter the length of the divisor: ");
    scanf("%d", &divisor_len);
    printf("Enter the divisor (%d bits):\n", divisor_len);
    for (i = 0; i < divisor_len; i++) {
        scanf("%d", &divisor[i]);
    }

    // Input data
    printf("Enter the length of the data: ");
    scanf("%d", &data_len);
    printf("Enter the data (%d bits):\n", data_len);
    for (i = 0; i < data_len; i++) {
        scanf("%d", &data[i]);
        transmitted_data[i] = data[i]; // Copy data for transmission
    }

    // Append zeros to transmitted data
    for (i = data_len; i < data_len + divisor_len - 1; i++) {
        transmitted_data[i] = 0;
    }

    // Display data after appending zeros
    printf("Data after appending zeros: ");
    for (i = 0; i < data_len + divisor_len - 1; i++) {
        printf("%d", transmitted_data[i]);
    }

    // Calculate CRC and store remainder
    perform_crc(transmitted_data, data_len, divisor, divisor_len, remainder);

    // Display the calculated CRC (remainder)
    printf("\nCRC (Remainder): ");
    for (i = 0; i < divisor_len - 1; i++) {
        printf("%d", remainder[i]);
    }

    // Combine data and CRC for transmission
    for (i = 0; i < divisor_len - 1; i++) {
        transmitted_data[data_len + i] = remainder[i];
    }

    // Display the transmitted data
    printf("\nTransmitted data (Data + CRC): ");
    for (i = 0; i < data_len + divisor_len - 1; i++) {
        printf("%d", transmitted_data[i]);
    }

    // Receiver end
    printf("\n\n--- Receiver End ---\n");
    printf("Enter the received data (Data + CRC, %d bits):\n", data_len + divisor_len - 1);
    for (i = 0; i < data_len + divisor_len - 1; i++) {
        scanf("%d", &received_data[i]);
    }

    // Validate received data
    if (validate_crc(received_data, data_len, divisor, divisor_len)) {
        printf("No error detected. Data is valid.\n");
    } else {
        printf("Error detected in the received data!\n");
    }

    return 0;
}
