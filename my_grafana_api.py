import time
import requests

def my_grafana_api (ip,content):
        seconds_since_epoch = time.time()
        seconds_since_epoch = seconds_since_epoch * 1000000000
        seconds_since_epoch  = format(seconds_since_epoch , '.0f')
        data =  content+"  %s" % (seconds_since_epoch)
        url = 'http://'+ip+':8086/write?consistency=any&db=telegraf' 
        requests.post(url, data,headers={'Connection':'close'},timeout = 1)