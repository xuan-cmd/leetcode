#两个链表的第一个公共节点
num= input("请输入阿拉伯数字：")
han = "零一二三四五六七八九"

for i in range(len(num)):
    numsplit = int(num[i])
    print(han[numsplit], end='')