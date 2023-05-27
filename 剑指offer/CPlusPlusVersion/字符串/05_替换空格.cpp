/*
 * 05  �滻�ո�
 *
 *
 * requirement��ʵ��һ�����������ַ��� s �е�ÿ���ո��滻�� %20
 *
 * example�����룺s = "We are happy."
            �����"We%20are%20happy."

    ˼·�����������У����URL�����к��������ַ�����ո�# �ȣ�����ܵ��·��������޷������ȷ�Ĳ���ֵ
    ������Ҫ����Щ�����ַ�ת���ɷ���������ʶ����ַ���ת���Ĺ�����%�����ASCII�����λʮ�����Ƶı�ʾ��
    ����ո��ASCII����32����ʮ�����Ƶ�0x20����˿ո��滻��%20
    ����#��ASCII����35����ʮ�����Ƶ�0x23������URL�б��滻��%23

    ֮ǰ��pythonд�����úܼ򵥣��޷Ǿ����滻��һ��forѭ�����ɡ�
    ����python�У��ַ����Ǳ����Ϊ���ɱ�����ͣ����޷�ֱ���޸��ַ�����ĳ���ַ�����Ҫ�½�һ���ַ���ʵ��

    ������C++�ˣ���Ϊstring�ǿɱ����ͣ���˿����ڲ����µ��ַ����������ʵ��ԭ���޸�
    ���ַ����ĳ���= ԭ�ַ����ĳ��� + n���ո񳤶�

    �����������˼�����Ǿ��Ǵ�ͷ��βɨ���ַ�����ÿ�������ո��ַ���ʱ������滻�������ǰ�һ���ַ����滻��3���ַ���
    ���Ǳ���ѿո���������ַ���������2���ֽڣ�������������ַ����������ˡ�
    �����������ǻᷢ�֣�����������ո����⣬��ô������ַ�����Ҫ�ƶ����Ρ�
    ���Ժܶ��ַ������ƶ��˺ܶ�Σ���������ƶ��Ĵ�������ô�ͺ�nice��

    ������õ�˼·�Ǽ����ַ����ƶ��Ĵ��������ַ�����ǰ����滻 ===�� ��Ϊ�Ӻ���ǰ�滻��
    1�������ȱ���һ���ַ����������Ϳ���ͳ�Ƴ��ַ����пո�ĳ��ȵ�����
    2��ÿ���滻һ�οո񣬳�������2
    3�����Ǵ��ַ������濪ʼ���ƺ��滻��׼������ָ�� P1ָ��ԭʼ�ַ�����ĩβ��P2ָ���滻����ַ�����ĩβ
    4���ƶ�ָ��P1���������ָ���ַ����Ƶ�P2ָ���λ�ã�ֱ��������һ���ո�Ϊֹ��
    5�������˵�һ���ո�󣬰�P1��ǰ�ƶ�1��P2ǰ�����%20������%20�ĳ���Ϊ3�����԰�P2�ƶ�3�����ӡ�

    �������Ļ������е��ַ�����ֻ���ƣ��ƶ�һ�Σ���������㷨��ʱ��Ч����O(n)��

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
 * ������Ҳ�����ˣ���C++�У�std::string���Ѿ��ṩ���滻�ַ����ĺ���replace��Ҳ����ֱ��ʹ�øú�����ʵ����ͬ�Ĺ���
 */


class Solution2 {
public:
    std::string replaceSpace(std::string s) {
        size_t pos = 0;
        while ((pos = s.find(' ', pos)) != std::string::npos) {
            s.replace(pos, 1, "%20");
            pos += 3; // �����²�����ַ�������
        }
        return s;
    }
};
