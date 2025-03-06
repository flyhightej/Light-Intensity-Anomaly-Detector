import conf
from boltiot import Sms, Bolt
import json, time, math, statistics

def compute_bounds(history_data,frame_size,factor):
    if len(history_data)<frame_size :
        return None

    if len(history_data)>frame_size :
        del history_data[0:len(history_data)-frame_size]
    Mn=statistics.mean(history_data)
    Variance=0
    for data in history_data :
        Variance += math.pow((data-Mn),2)
    Zn = factor * math.sqrt(Variance / frame_size)
    High_bound = history_data[frame_size-1]+Zn
    Low_bound = history_data[frame_size-1]-Zn
    return [High_bound,Low_bound]

minimum_limit = 240 #the minimum threshold of light intensity value 
maximum_limit = 250 #the maximum threshold of light intensity value 


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

history_data=[]

while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    if data['success'] != 1:
        print("There was an error while retriving the data.")
        print("This is the error:"+data['value'])
        time.sleep(10)
        continue

    print ("This is the sensor value "+data['value'])
    sensor_value=0
    try:
        sensor_value = int(data['value'])
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            response2 = mybolt.analogWrite('1', '50')
            print (response2)
       
    except e:
        print("There was an error while parsing the response: ",e)
        time.sleep(10)
        continue

    bound = compute_bounds(history_data,conf.FRAME_SIZE,conf.MUL_FACTOR)
    if not bound:
        required_data_count=conf.FRAME_SIZE-len(history_data)
        print("Not enough data to compute Z-score. Need ",required_data_count," more data points")
        history_data.append(int(data['value']))
        time.sleep(10)
        continue

    try:
        if sensor_value > bound[0] :
            print ("Emergency!! Light Intensity has INCREASED drastically")
            response3 = mybolt.analogWrite('1', '255')
            print (response3)
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("Emergency!!\nThe Current Light Intensity sensor value is " +str(sensor_value))
            
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))

        if sensor_value < bound[1] :
            print ("Emergency!! Light Intensity has DECREASED drastically") 
            response3 = mybolt.analogWrite('1', '255')
            print (response3) 
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("Emergency!!\nThe Current Light Intensity sensor value is " +str(sensor_value))
            
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))  
            
        history_data.append(sensor_value);
    except Exception as e:
        print ("Error",e)
    time.sleep(10)
