
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#-----------------------傑錦有限公司----------------------------  
def buttons_message():
    message = LocationSendMessage(
        title='傑錦有限公司',
        address='115台北市南港區重陽路457號一樓',
        latitude=25.05955398396485,  
        longitude=121.61031409783777
    )
    return message

 #-----------------------其他----------------------------   
def buttons3_message():
    message =[ 
        LocationSendMessage(
        title='汐止區',
        address='新北市汐止區秀山路104巷',
        latitude=25.056407422763716,
        longitude=121.66735371090795
    ),
        LocationSendMessage(
        title='內湖區',
        address='11494台北市內湖區民權東路六段21巷33號',
        latitude=25.069271067541557,
        longitude=121.58109818650598
    ),
        LocationSendMessage(
        title='松山區',
        address='105台北市松山區撫遠街403巷23號',
        latitude=25.066328559186072, 
        longitude=121.56646475767063
    ),
        LocationSendMessage(
        title='雲林好時光休息站',
        address='雲林縣西螺鎮76-10 號',
        latitude=23.77750298401776,
        longitude=120.47731581088294
    ),
        LocationSendMessage(
        title='大安區',
        address='106台北市大安區和平東路三段632巷2號',
        latitude=25.012973919156355,
        longitude=121.56337911779023
    )
    ]
    return message

