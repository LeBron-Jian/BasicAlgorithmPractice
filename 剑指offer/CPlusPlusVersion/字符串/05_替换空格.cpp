/*
 * 05  替换空格
 *
 *
 * requirement：实现一个函数，把字符串 s 中的每个空格替换成 %20
 *
 * example：输入：s = "We are happy."
            输出："We%20are%20happy."

    思路：在网络编程中，如果URL参数中含有特殊字符，如空格，# 等，则可能导致服务器端无法获得正确的参数值
    我们需要将这些特殊字符转换成服务器可以识别的字符。转换的规则是%后跟上ASCII码的两位十六进制的表示。
    比如空格的ASCII码是32，即十六进制的0x20，因此空格被替换成%20
    比如#的ASCII码是35，即十六进制的0x23，它在URL中被替换成%23

    之前是python写，觉得很简单，无非就是替换，一个for循环即可。
    但是python中，字符串是被设计为不可变的类型，即无法直接修改字符串的某个字符，需要新建一个字符串实现

    现在是C++了，因为string是可变类型，因此可以在不建新的字符串的情况下实现原地修改
    新字符串的长度= 原字符串的长度 + n个空格长度

    先是最基本的思考，那就是从头到尾扫描字符串，每次碰到空格字符的时候进行替换，由于是把一个字符串替换成3个字符串
    我们必须把空格后面所有字符串都后移2个字节，否则就有两个字符串被覆盖了。
    这种做法我们会发现，如果有两个空格，如题，那么后面的字符串都要移动两次。
    所以很多字符串都移动了很多次，如果减少移动的次数，那么就很nice。

    所以最好的思路是减少字符串移动的次数，把字符串从前向后替换 ===》 改为从后向前替换。
    1，我们先遍历一次字符串，这样就可以统计出字符串中空格的长度的总数
    2，每次替换一次空格，长度增加2
    3，我们从字符串后面开始复制和替换，准备两个指针 P1指向原始字符串的末尾，P2指向替换后的字符串的末尾
    4，移动指针P1，逐个将其指向字符复制到P2指向的位置，直到碰到第一个空格为止。
    5，碰到了第一个空格后，把P1向前移动1格，P2前面插入%20，由于%20的长度为3，所以把P2移动3个格子。

    这样做的话，所有的字符串都只复制，移动一次，所以这个算法的时间效率是O(n)。

 */


class Solution {
public:
    string replaceSpace(string s) {
        int length = s.size();
        if(length==0){
            return s;
        }
        int originalLength = 0;
        int numberOfBlank = 0;

        for(int i=0;i<length;++i){
            if (s[i] == ' '){
                numberOfBlank += 1;
            }
            originalLength += 1;
        }
        int newLength = originalLength + numberOfBlank*2;
        s.resize(newLength);

        int indexOfOrigin = originalLength-1;
        int indexOfNew = newLength-1;

        while(indexOfOrigin >=0 && indexOfNew > indexOfOrigin){
            if (s[indexOfOrigin] == ' '){
                s[indexOfNew--] = '0';
                s[indexOfNew--] = '2';
                s[indexOfNew--] = '%';

            } else{
                s[indexOfNew--] = s[indexOfOrigin];
            }
            indexOfOrigin--;
        }
        return s;

    }
};


/*
 * 后面我也发现了，在C++中，std::string类已经提供了替换字符串的函数replace，也可以直接使用该函数来实现相同的功能
 */


class Solution2 {
public:
    std::string replaceSpace(std::string s) {
        size_t pos = 0;
        while ((pos = s.find(' ', pos)) != std::string::npos) {
            s.replace(pos, 1, "%20");
            pos += 3; // 考虑新插入的字符串长度
        }
        return s;
    }
};
