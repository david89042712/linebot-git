from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#-----------------------保時捷分布----------------------------  
def buttons2_message():
    message = TemplateSendMessage(
                alt_text="您所使用的裝置無法使用此功能",
                template=ButtonsTemplate(
                    thumbnail_image_url="https://www.wyborkierowcow.pl/wp-content/uploads/2022/05/Porsche-Logo-1963-present-scaled.jpg",
                    title='請選擇地區',
                    text='請選擇',
                    actions=[
                        MessageTemplateAction(
                            label='北部',
                            text='PORSCHE北部'

                        ),
                        MessageTemplateAction(
                            label='中部',
                            text='PORSCHE中部'

                        ),
                        MessageTemplateAction(
                            label='南部',
                            text='PORSCHE南部'

                        ),
                        MessageTemplateAction(
                            label='東部',
                            text='PORSCHE東部'

                        ),
                    ]
                )
    )
    return message
def location_message():
    message =[ 
        LocationSendMessage(
        title='保時捷-台北保時捷中心',
        address='台北市內湖區石潭路88號',
        latitude=25.062445873708718,
        longitude=121.58881572150328
    ),
        LocationSendMessage(
        title='保時捷-台北敦南保時捷展示中心Turbo Charging',
        address='台北市大安區基隆路二段238號',
        latitude=25.022988063661607,
        longitude=121.55069511072737
    ),
        LocationSendMessage(
        title='保時捷-新北保時捷中心Turbo Charging',
        address='新北市新莊區中正路50號',
        latitude= 25.041004704354005,
        longitude=121.46342253341996
    ),
        LocationSendMessage(
        title='保時捷-桃園保時捷中心Turbo Charging',
        address='桃園市中壢區中華路二段88號',
        latitude= 24.966425984345552,
        longitude=121.24194153605337
    ),
        LocationSendMessage(
        title='保時捷-新竹保時捷中心Turbo Charging',
        address='新竹縣竹北市中華路718號',
        latitude=24.848574755270942,
        longitude=121.00515261484745
    )
        
       
    ]
    return message

def location2_message():
    message =[ 
       LocationSendMessage(
        title='保時捷-麗寶Outlet Mall Turbo Charging',
        address='台中市后里區福容路201號',
        latitude=24.324390099698757,
        longitude=120.6992538577204
    ),
       LocationSendMessage(
        title='保時捷-台中保時捷中心Turbo Charging',
        address='台中市南屯區文心路一段447號1樓',
        latitude=24.15110086114168,
        longitude=120.64649079245295
    )
    ]
    return message
def location3_message():
    message =[ 
       LocationSendMessage(
        title='保時捷-嘉義水牛公園Turbo Charging',
        address='嘉義縣泰北市中山路一段64號',
        latitude=23.496403263590572,
        longitude=120.38653563823112
    ),  
       LocationSendMessage(
        title='保時捷-高雄保時捷中心Turbo Charging',
        address='高雄市楠梓區家加昌路639號',
        latitude=22.715019799438128, 
        longitude=120.29850267384869
    ),
       LocationSendMessage(
        title='保時捷-北基楓港站Turbo Charging',
        address='屏東縣枋山鄉舊庄路165號',
        latitude=22.194618083123448,
        longitude=120.6920228338156
    )
    ]
    return message
def location4_message():
    message =[ 
       LocationSendMessage(
        title='保時捷-台東娜路彎大酒店Turbo Charging',
        address='台東縣台東市連航路66號',
        latitude=22.77014147868762,
        longitude=121.12201343854225
    ),
       LocationSendMessage(
        title='保時捷-花蓮新天堂樂園Turbo Charging',
        address='花蓮縣吉安鄉南濱路一段503號',
        latitude=23.93883035213251,
        longitude=121.59470577271063
    ),
       LocationSendMessage(
        title='保時捷-宜蘭廣進萊爾富Turbo Charging',
        address='宜蘭縣宜蘭市中山路一段116號',
        latitude=24.723874311379348,
        longitude=121.76891969783361
    )
    ]
    return message