class barbecue():
    def __init__(self,num,interval):
        self.customers = []
        self.num_customer =num
        self.interval_time = interval
        for num in range(0,self.num_customer):
            self.new_customer = {'begin_time':0,'bar_wait_time':0,'grill_wait_time':0}
            self.customers.append(self.new_customer)
    def barbacue_begin(self):
        for i in range(0,int(self.num_customer/20)):
            for j in range(0,20):
                if self.interval_time*60 > 10*5:
                    self.customers[i*20+j]['bar_wait_time'] = 0
                else:
                    if (i*20+j) < 20:
                        self.customers[i*20+j]['bar_wait_time'] = 0
                    else:
                        self.customers[i*20+j]['bar_wait_time'] = self.customers[(i-1)*20+j]['bar_wait_time']+5*10-self.interval_time*60
        for i in range(0,int(self.num_customer/8)):
            for j in range(0,8):
                if self.interval_time*60 > 3*60:
                    self.customers[i*8+j]['grill_wait_time'] = 0
                else:
                    if (i*8+j) < 8:
                        self.customers[i*8+j]['grill_wait_time'] = 0
                    else:
                        self.customers[i*8+j]['grill_wait_time'] = self.customers[(i-1)*8+j]['grill_wait_time']+3*60-self.interval_time*60
    def averagetime(self):
        total = 0
        barwaittime = 0
        grillwaittime = 0
        for number in range(0,len(self.customers)):
            total += self.customers[number]['bar_wait_time'] + self.customers[number]['grill_wait_time'] + 10*5 + 3*60
        print("全部顾客的平均时间是" + str(total/len(self.customers)))
        for number in range(0,len(self.customers)):
            barwaittime += self.customers[number]['bar_wait_time']
        print("顾客在吧台的平均等待时间是" + str(barwaittime/len(self.customers)))    
        for number in range(0,len(self.customers)):    
            grillwaittime += self.customers[number]['grill_wait_time']
        print("顾客在烧烤架的平均等待时间是" + str(grillwaittime/len(self.customers)))
        
a = barbecue(100,5)
a.barbacue_begin()
a.averagetime()
 
            
