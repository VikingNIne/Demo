import random

print('------------------�Ұ���C������------------------')
secret = random.randint(1,10)
temp = input("������һ��С������������������ĸ����֣�")
guess = int(temp)

while guess != secret:
    temp = input("��ѽ���´��ˣ�����������ɣ�")
    guess = int(temp)
    if guess == secret:
        print("�Բۣ�����С��������Ļ׳��𣿣�")
        print("�ߣ�������Ҳû�н�����")
    else:
        if guess > secret:
            print("���ˣ�����~~~")
        else:
            print("С�ˣ�С��~~~")
            
print("��Ϸ������������^_^")