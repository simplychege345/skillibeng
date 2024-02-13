class fruits:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def onyesha(self):
        print(f"i like eating {self.name} and it costs {self.price}")
myjob=fruits("bananas","10/=")
myjob.onyesha()
myjob=fruits("mangoes","15/=")
myjob.onyesha()
myjob=fruits("apples","20/=")
myjob.onyesha()
myjob=fruits("watermelon","5/=")
myjob.onyesha()
myjob=fruits("oranges","25/=")
myjob.onyesha()