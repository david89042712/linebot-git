from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#-----------------------華城----------------------------  
def buttons4_message():
    message = TemplateSendMessage(
                alt_text="您所使用的裝置無法適用此功能",
                template=ButtonsTemplate(
                    thumbnail_image_url="https://www.evalue.com.tw/images/logo.png",
                    title='請選擇地區',
                    text='請選擇',
                    actions=[
                        MessageTemplateAction(
                            label='北部',
                            text='EVALUE北部'

                        ),
                        MessageTemplateAction(
                            label='中部',
                            text='EVALUE中部'

                        ),
                        MessageTemplateAction(
                            label='南部',
                            text='EVALUE南部'

                        ),
                        MessageTemplateAction(
                            label='東部',
                            text='EVALUE東部'

                        ),
                    ]
                )
    )
    return message
def buttons5_message():
    message = TextSendMessage (  
            text="請選擇您的選項",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="北市EVALUE",text="北市EVALUE")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="桃園新竹EVALUE",text="桃園新竹EVALUE")
                    ),       
                ]
                )   
            )
    return message
def location5_message():
    message =[ 
        LocationSendMessage(
        title='華城-新北萬里沐舍酒店',
        address='新北市萬里區大鵬里萬里加投166-1號',
        latitude=25.21532569041132,
        longitude=121.64338872674112
    ),
        LocationSendMessage(
        title='華城-台北新光南港軟體園區',
        address='台北市南港區經貿二路196號B2',
        latitude=25.059864640622223,
        longitude=121.61480456906773
    ),
        LocationSendMessage(
        title='華城-台北內湖旗艦店',
        address='台北市內湖區民權東路六段186-8號',
        latitude=25.06874750214101,
        longitude=121.59352842673934
    ),
        LocationSendMessage(
        title='華城內部站點',
        address='台北市松山區復興北路191號(限內部員工用)',
        latitude=25.055300022461747,
        longitude=121.54434319790342
    ),
        LocationSendMessage(
        title='華城-新北土城日月光廣場',
        address='新北市土城區學府路二段210號B3',
        latitude=24.978972734586,
        longitude=121.44498596906676
    )


    ]
    return message
def location6_message():
    message =[ 
        LocationSendMessage(
        title='華城-桃園南崁特力家居',
        address='桃園市蘆竹區中正路1號',
        latitude=25.040201724862815,
        longitude=121.29472196906754
    ),

        LocationSendMessage(
        title='華城-7-11_桃園江園門市',
        address='桃園市大園區中正東路三段620號一樓',
        latitude=25.00442660726841,
        longitude=121.22853826906709
    ),

        LocationSendMessage(
        title='華城-金弘笙_新竹竹北店',
        address='新竹縣竹北市莊敬南路88號',
        latitude=24.817987022061182,
        longitude=121.02035524022894
    ),
        LocationSendMessage(
        title='華城-新竹和選旅',
        address='新竹市東區大學路16號',
        latitude=24.789344924324745,
        longitude=121.00255329790009
    )
    ]
    return message
def location7_message():
    message =[ 
       LocationSendMessage(
        title='華城-燦坤_台中超越店',
        address='台中市南屯區大墩路888號',
        latitude=24.15642845238487,
        longitude=120.65040969789231
    ),
       LocationSendMessage(
        title='華城-燦坤_台中五權店',
        address='台中市南屯區五權西路二段777號',
        latitude=24.142778665152292,
        longitude=120.63621019789208
    ),
       LocationSendMessage(
        title='華城-7-11_南投中潭門市',
        address='南投縣魚池鄉通文巷6-28號',
        latitude=23.905160909988385,
        longitude=120.92722814021782
    ),
        LocationSendMessage(
        title='華城-7-11_南投竹秀門市',
        address='南投縣竹山鎮集山路二段58號',
        latitude=23.800122417456702,
        longitude=120.71336909788798
    )
    ]
    return message
def location8_message():
    message =[ 
       LocationSendMessage(
        title='華城-嘉義翁聚德觀光工廠',
        address='嘉義縣中埔鄉司公廍4-1號',
        latitude=23.450783406647897,
        longitude=120.48246661343063
    ),
       LocationSendMessage(
        title='華城-金弘笙_台南永康店',
        address='台南市永康區中正北路199號',
        latitude=23.041877330707116,
        longitude=120.2441922978792
    ),
       LocationSendMessage(
        title='華城-燦坤_高雄華榮店',
        address='高雄市鼓山區華榮路345號',
        latitude=22.66790358521628, 
        longitude=120.29556056903917
    ),
        LocationSendMessage(
        title='華城-金弘笙_高雄九如店',
        address='高雄市三民區九如一路501號',
        latitude=22.638884691667865,
        longitude=120.32828194020313
    )
    ]
    return message
def location9_message():
    message =[ 
       LocationSendMessage(
        title='華城-宜蘭九號溫泉旅店',
        address='宜蘭縣礁溪鄉溫泉路85號',
        latitude=24.82983312112436,
        longitude=121.7722929979005
    ),
       LocationSendMessage(
        title='華城-宜蘭安永心食館',
        address='宜蘭縣蘇澳鎮中山路二段415號1F',
        latitude=24.61489959194278,
        longitude=121.81795272673368
    )
    ]
    return message