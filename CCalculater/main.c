#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool isOperater(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '\0';
    // 要有c == '\0',原因暂时不明
}

float strToNum(const char* str, int startPosition, int endPosition) 
{
    // 找出小数点位置
    int dotPosition = endPosition + 1;
    for (int i = startPosition; i <= endPosition; ++i) {
        if (str[i] == '.') {
            dotPosition = i;
        }
    }

    // 解析整数部分
    int integerPart = 0;
    int weight = 1;
    for (int i = dotPosition - 1; i >= startPosition; --i) 
    {
        int num = str[i] - '0';
        integerPart += num * weight;
        weight *= 10;
    }

    // 解析小数部分
    float floatPart = 0;
    float weight2 = 0.1f;
    for (int i = dotPosition + 1; i <= endPosition; ++i) 
    {
        int num = str[i] - '0';
        floatPart += num * weight2;
        weight2 *= 0.1;
    }

    return integerPart + floatPart;
}

// 从左到右,无优先级解析
float evalLeftRight(const char* str, int overallStartPosition, int overallEndPosition)
{
    float result=0.0f;

    int startPosition = overallStartPosition, endPosition;
    char lastOperater = '*';

    char c=str[overallStartPosition];

    // 最后还要多检测到一个运算符,才能触发最后一个运算
    for (int i = overallStartPosition; i<=overallEndPosition + 1; ++i) 
    {
        c = str[i];

        if (isOperater(c)) 
        {
            endPosition = i - 1;
            float lastNumber = strToNum(str,startPosition,endPosition); // lastNumber是指当前解析到的运算符前面的数字

            switch (lastOperater) 
            {
                case '+': 
                {
                    result  += lastNumber;
                    break;
                }
                case '-': 
                {
                    result  -= lastNumber;
                    break;
                }
                case '*': 
                {
                    result  *= lastNumber;
                    break;
                }
                case '/': 
                {
                    result  /= lastNumber;
                    break;
                }
            }

            // --------- 为下一次做准备

            startPosition = i + 1;
            lastOperater = c;
        }
    }

    return result;
}

float eval(const char* str) {
    // "+ 234.56 + 3 - 2.1 * 2 * 3 - 5 - 3.2 * 2 * 3 - 1.1 + 5"
    int strLength = strlen(str);

    float result=0.0f;

    int startPostion = 0,endPosition,lastOperaterPosition = strLength;

    for (int i=0; i < strLength; ++i)
    {
        char c = str[i];

        // 如果这个运算符号是加和减,并且上一个运算符号不是加和减
        if(
            (c=='+' || c=='-')
            && (str[lastOperaterPosition] == '*' || str[lastOperaterPosition] == '/')
        )
        {
            endPosition = i - 1;
            result += evalLeftRight(str,startPostion - 1,endPosition);
            startPostion = i + 1;
        }

        // 如果这个运算符号是乘和除,并且上一个运算符号不是乘和除
        if(
            (c=='*' || c=='/')
            && (str[lastOperaterPosition] == '+' || str[lastOperaterPosition] == '-')
        )
        {
            endPosition = lastOperaterPosition - 1;
            result += evalLeftRight(str,startPostion - 1,endPosition); //包含第一个符号,以区别正负
            startPostion = lastOperaterPosition + 1;
        }

        lastOperaterPosition = isOperater(c)?i:lastOperaterPosition;
    }

    // 补充一次解析
    result += evalLeftRight(str,startPostion - 1,strLength-1);

    return result;
}

// 检查是否含有不能解析的字符
bool check(char* str)
{
    for(int i=0;str[i]!='\0';++i)
    {
        char c = str[i];
        if(
            c != '+' &&
            c != '-' &&
            c != '*' &&
            c != '/' &&
            c != '.' &&
            (c < '0' || c > '9')
        )
        {
            printf("含有无法处理的字符");
            return false;
        }
    }

    return true;
}

int main()
{
    char str[128] = "\0";

    puts("请输入要运算的字符串,不能含有空格:");
    scanf("%s",str);

    if(check(str))
    {
        float result = eval(str);
        printf("最终结果 = %F\n",result);
    }

    return 0;
}
