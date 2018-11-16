customers = []
def initial(num_customer,interval_time):
    for num in range(0,num_customer):
        new_customer = {'begin_time':0,'bar_wait_time':0,'grill_wait_time':0}
        customers.append(new_customer)

def bar_begin(num_customer,interval_time):
    for i in range(0,int(num_customer/20)):
        for j in range(0,20):
            if interval_time*60 > 10*5:
                customers[i*20+j]['bar_wait_time'] = 0
            else:
                if (i*20+j) < 20:
                    customers[i*20+j]['bar_wait_time'] = 0
                else:
                    customers[i*20+j]['bar_wait_time'] = customers[(i-1)*20+j]['bar_wait_time']+5*10-interval_time*60
def grill_begin(num_customer,interval_time):
    for i in range(0,int(num_customer/8)):
        for j in range(0,8):
            if interval_time*60 > 3*60:
                customers[i*8+j]['grill_wait_time'] = 0
            else:
                if (i*8+j) < 8:
                    customers[i*8+j]['grill_wait_time'] = 0
                else:
                    customers[i*8+j]['grill_wait_time'] = customers[(i-1)*8+j]['grill_wait_time']+3*60-interval_time*60
def averagetime():
    total = 0
    barwaittime = 0
    grillwaittime = 0
    for number in range(0,len(customers)):
        total += customers[number]['bar_wait_time'] + customers[number]['grill_wait_time'] + 10*5 + 3*60
    print("全部顾客的平均时间是" + str(total/len(customers)))
    for number in range(0,len(customers)):
        barwaittime += customers[number]['bar_wait_time']
    print("顾客在吧台的平均等待时间是" + str(barwaittime/len(customers)))    
    for number in range(0,len(customers)):    
        grillwaittime += customers[number]['grill_wait_time']
    print("顾客在烧烤架的平均等待时间是" + str(grillwaittime/len(customers)))
    return ' '
        
def start(num_customer,interval_time):
        initial(num_customer,interval_time)
        bar_begin(num_customer,interval_time)
        grill_begin(num_customer,interval_time)
        return averagetime()

print(start(100,5))
    
 
            
