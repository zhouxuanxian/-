#coding=gbk
#�����ļ�����
def jiami():
    yuanName = input('��������Ҫ���ܵ��ļ���:')
    yuanFile = open(yuanName,'r')
    while True:
        try:
            password = int(input('���������͵���Կ:'))
            if password<256:
                break
            else:
                print("������һ����0��256֮�������!")
        except:
            print("���������������������!")
    num = yuanName.rfind('.')
    jiamiFileName = yuanName[0:num]+'[����]'+yuanName[num:]
    content = yuanFile.read(1)
    jiamiFile = open(jiamiFileName, 'w')
    while len(content)>0:
        # ����ȡ������ĸת��Ϊascall��
        position = ord(content)
        # ����
        position = position+password
        # ��ascall��ת��Ϊ��ĸд��
        contents = chr(position)
        jiamiFile.write(contents)
        content = yuanFile.read(1)
    print('�������')
    jiamiFile.close()
    yuanFile.close()
def jiemi():
    yuanName = input('��������Ҫ���ܵ��ļ���:')
    yuanFile = open(yuanName, 'r')
    while True:
        try:
            password = int(input('��������ܵ���Կ:'))
            break
        except:
            print("���������������������!")
    num = yuanName.rfind('.')
    num1 = yuanName.rfind('[')
    jiamiFileName = yuanName[0:num1] + '[����]' + yuanName[num:]
    content = yuanFile.read(1)
    jiamiFile = open(jiamiFileName, 'w')
    while len(content) > 0:
        #����ȡ������ĸת��Ϊascall��
        position = ord(content)
        #����
        position = position - password
        #��ascall��ת��Ϊ��ĸд��
        contents = chr(position)
        jiamiFile.write(contents)
        content = yuanFile.read(1)
    print('�������')
    jiamiFile.close()
    yuanFile.close()
def main():
    while True:
        try:
            num = int(input("��ѡ����Ҫ���еĲ�����1--����  2--����  3--�˳�����"))
        except:
            print("������������������!!!")
            continue;
        if num ==1:
            jiami()
        elif num==2:
            jiemi()
        elif num==3:
            break
        else:
            pass
if __name__ == '__main__':
    main()
