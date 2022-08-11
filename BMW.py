from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#------------------------------BMW--------------------------------------------------------
def buttons6_message():
    message = TemplateSendMessage(
                alt_text="您所使用的裝置無法適用此功能",
                template=ButtonsTemplate(
                    thumbnail_image_url="https://teamqualityservices.com/wp-content/uploads/2021/03/BMW-600x599.jpg",
                    title='請選擇地區',
                    text='請選擇',
                    actions=[
                        MessageTemplateAction(
                            label='北部',
                            text='寶馬北部'

                        ),
                        MessageTemplateAction(
                            label='中部',
                            text='寶馬中部'

                        ),
                        MessageTemplateAction(
                            label='南部',
                            text='寶馬南部'

                        ),

                    ]
                )
    )
    return message
def buttons7_message():
    message = TextSendMessage (  
            text="請選擇您的選項",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="北市BMW",text="寶馬北市")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="桃園新竹BMW",text="寶馬桃園新竹")
                    ),       
                ]
                )   
            )
    return message

def location10_message():
    message =[ 
       LocationSendMessage(
        title='BMW-鎔德服務中心',
        address='台北市內湖區行善路48巷9號',
        latitude=25.05724234124739,
        longitude=121.57552226906776
    ),
       LocationSendMessage(
        title='BMW-i台北101充電站',
        address='台北市信義區市府路45號',
        latitude=25.034151346749667,
        longitude=121.56401046906744
    ),
       LocationSendMessage(
        title='BMW-汎德台北濱江展示中心',
        address='台北市中山區濱江街337號',
        latitude=25.07266590182821, 
        longitude=121.54826399790369
    ),
        LocationSendMessage(
        title='BMW-依德展示中心',
        address='新北市中和區建一路68號',
        latitude=25.00312005413642,
        longitude=121.48734296906709
    )
    ]
    return message
def location11_message():
    message =[ 
       LocationSendMessage(
        title='BMW-大桐桃園展示中心',
        address='桃園市桃園區文中路746號',
        latitude=24.99320125649574,
        longitude=121.27484042673844
    ),
       LocationSendMessage(
        title='BMW-中鎂展示中心',
        address='新竹市東區中華路一段239號',
        latitude=24.8131967607998,
        longitude=120.99038459790043
    )
    ]
    return message

def location12_message():
    message =[ 
       LocationSendMessage(
        title='BMW-汎德台中崇德展示中心',
        address='台中市北屯區崇德路三段489號',
        latitude=24.19186177099031,
        longitude=120.68627382672861
    ),
       LocationSendMessage(
        title='BMW-長慶展示中心',
        address='南投縣南投市南崗三路288號',
        latitude=23.939424890388956,
        longitude=120.66484426905399
    ),
       LocationSendMessage(
        title='BMW-彰化昌一展示中心',
        address='彰化縣花壇鄉中山路二段498-1號',
        latitude=24.039786480947054,
        longitude=120.53531599789095
    )
    ]
    return message
def location13_message():
    message =[ 
       LocationSendMessage(
        title='BMW-汎德台南永康展示中心',
        address='台南市永康區小北路15號',
        latitude=23.021083033764388,
        longitude=120.21461982671468
    ),
       LocationSendMessage(
        title='BMW-汎德高雄新生展示中心',
        address='高雄市前鎮區新生路206號',
        latitude=22.581686604050585,
        longitude=120.31230279787388
    )
    ]
    return message