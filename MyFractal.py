import math
class MyFractal:
    def __init__(self,numerator,denumerator):
        self.numerator=numerator
        self.denumerator=denumerator
    def __str__(self):
        return f"{self.numerator}/{self.denumerator}"
    def __add__(self,other):
        if isinstance(other,MyFractal):
            commom_den=self.denumerator*other.denumerator
            second_num=other.numerator*self.denumerator
            first_num=self.numerator*other.denumerator
            result = MyFractal(first_num+second_num,commom_den)
            result.simplify()

            return result
        elif isinstance(other,int):
            second=MyFractal(other,1)
            commom_den=self.denumerator*second.denumerator
            second_num=second.numerator*self.denumerator
            first_num=self.numerator*second.denumerator
            result = MyFractal(first_num+second_num,commom_den)
            result.simplify()

            return result
    #def __sub__(self,other):
        #commom_den=self.denumerator*other.denumerator
        #second_num=other.numerator*self.denumerator
        #first_num=self.numerator*other.denumerator
        #return  MyFractal(first_num-second_num,commom_den) 
    def simplify(self):
        commom_den=math.gcd(self.numerator,self.denumerator)
        self.numerator //=commom_den
        self.denumerator //=commom_den
    def __mul__(self,other):
        if isinstance(other,MyFractal):
            result=MyFractal(self.numerator*other.numerator,self.denumerator*other.denumerator)
            result.simplify()

            return result
        elif isinstance(other,int):
            result=MyFractal(self.numerator*other,self.denumerator )
            result.simplify()

            return result
    
    def __truediv__(self,other):
        if isinstance(other,MyFractal):
            result=MyFractal(self.denumerator*other.denumerator,other.numerator*self.numerator)
            result.simplify()

            return result
        elif isinstance(other,int):
            result=MyFractal(self.numerator,self.denumerator*other)
            result.simplify()

            return result



        
       
