#coding:utf-8

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#账号的key和secret
access_id='xxxxxx'
access_key_secret='xxxxxxxxx'
#ECS_ID 服务器ID
ecs_vpc_id=''
#带宽大小，200 就是 200M带宽
eip_bandwidth=200
#区域：cn-hongkong(香港),ap-southeast-1(新加坡)
ecs_regionid=''
#流量计费方式：PayByTraffic(按流量收费),PayByBandwidth(按带宽收费)
ecs_chargetype='PayByTraffic'
