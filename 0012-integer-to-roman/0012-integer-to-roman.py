class Solution:
    def intToRoman(self, num: int) -> str:
        i=1
        dic={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        s=""
        while num!=0:
            y=num%pow(10,i)//pow(10,i-1)
            if y==5:
                s=dic[y*pow(10,i-1)]+s
            elif y==1:
                s=dic[y*pow(10,i-1)]+s
            elif y==4:
                s=dic[1*pow(10,i-1)]+dic[5*pow(10,i-1)]+s
            elif y==9:
                s=dic[1*pow(10,i-1)]+dic[1*pow(10,i)]+s
            elif y<4:
                s=dic[pow(10,i-1)]*y+s
            elif y>5 and y<9:
                y-=5
                s=dic[5*pow(10,i-1)]+dic[pow(10,i-1)]*y+s
            num=num//pow(10,i)
            num*=pow(10,i)
            i+=1
        return s