/* 
################################################################################
#                                                                              #
# This code was created by veilwr4ith                                          #
#                                                                              #
# BrainFuck Decoder                                                            #
#                                                                              #
################################################################################
*/

#include <stdio.h>
#include <stdlib.h>

#define MEMORY_SIZE 30000

void brainfuck_interpreter(char *code) {
    unsigned char tape[MEMORY_SIZE] = {0};
    int pointer = 0;
    char output[1000] = {0};

    int output_index = 0;
    for (int i = 0; code[i] != '\0'; i++) {
        switch (code[i]) {
            case '>':
                pointer++;
                break;
            case '<':
                pointer--;
                break;
            case '+':
                tape[pointer]++;
                break;
            case '-':
                tape[pointer]--;
                break;
            case '.':
                output[output_index++] = tape[pointer];
                break;
            case ',':
                break;
            case '[':
                if (tape[pointer] == 0) {
                    int loop_count = 1;
                    while (loop_count != 0) {
                        i++;
                        if (code[i] == '[') {
                            loop_count++;
                        } else if (code[i] == ']') {
                            loop_count--;
                        }
                    }
                }
                break;
            case ']':
                if (tape[pointer] != 0) {
                    int loop_count = 1;
                    while (loop_count != 0) {
                        i--;
                        if (code[i] == ']') {
                            loop_count++;
                        } else if (code[i] == '[') {
                            loop_count--;
                        }
                    }
                }
                break;
            default:
                break;
        }
    }
    printf("\nDecoded Brainfuck Code: %s\n", output);
}

int main() {
    char code[1000];

    printf("Enter Brainfuck code: ");
    fgets(code, sizeof(code), stdin);

    brainfuck_interpreter(code);

    return 0;
}
