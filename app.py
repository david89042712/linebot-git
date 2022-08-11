from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from porsche import *
from EVALUE import *
from BMW import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========


app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('g8+w08P64649E/7EPxaAFlliyw6dBu/As7eV+rYZ/KV7bD3MDRsPd3R1LjSfQJVsg3kel5iuNc/ipQv1cHvaoBIJ5H1OK7kvOQ6We4LW8xGUFiy6T9HWKxmVgxKfCACf4GMmNwYZ+GzARlOchln4XgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3a2379aa832775fac84a8fac1124d2fb')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    msg = event.message.text
    uid=event.source.user_id
    profile=line_bot_api.get_profile(uid)
    name=profile.display_name
    pic_url=profile.picture_url
#=======================圖文選單功能===========================================
    if mtext == '@關於我們':
        try:
            message =[ 
            TextSendMessage(  
                text = "「Amidas 是世界唯一保固50年的儲能櫃供應商」\n\n隨時可以自由安裝的行動/快充電樁 180KWh/180 度電 AI ESS+EV charger，不需要等1~2年申請台電來安裝，讓 AI ESS 智能電池+快充電樁的偉大事業可以邁開新世紀開創電動車關鍵產業的腳步。 為何我們立志開發智能電池儲能封裝這個產業？我們有製造電池充電器數十年經驗，投注的無數年華及資金，不斷地專注於讓100度電、2000度電...以至千萬度電的儲能櫃能在世界各地的不斷電裝置——包含停車場、電動車、太陽能儲能、風力儲能、地熱儲能、無線基地台、飛機 、機器人、自動化搬運車、太空站等——安全無虞地運轉。儲能電池將深入生活的各個領域，但是儲能櫃越大就代表危險時時在我們周圍。沒有 AI ESS、沒有人工智慧運算，就沒有深度學習的雲運算，也無法提前知曉危險的存在，有了 AI 就能輕易導引維修電池的回春功能、恢復90%的電力，並可避免日後大量電池垃圾產生。未來我們將成為各大電池廠的品質驗證憑證，因為 AI 雲運算會明確地告訴我們的顧客和電池供應商各家電池品質的優劣。大量的雲端智慧雲會用大數據告訴眾人，何者擁有最佳的電池封裝技術，不容言語爭辯，一切看 AI 大數據，單單這個數據庫就有百億元價值。\n\n我們符合技術創新、整合技術綜合提高成高功效。有知覺的電池，AI 運算功能將電池組賦予身份認證，並能用 AI 運算出每個電池組、儲能櫃的年齡對應未來回收之價格定位。以充放電的電壓+電流+溫度的曲線，演算出趨勢曲線來判定電池組的健康曲線、定義電池組壽命/年齡、每個儲能電池的儲電能量（battery power capacity），讓我們可以在地區缺電時互相配電系統分派，實時掌握地區的儲能電量的體量以供政府及相互分配支援。每個電池儲能系統利用太陽能、風能、火力發電、核能電力充足時，將儲蓄多餘電力，並詳實記錄於我們的雲端，以便不時之需。我們的 AI 智能電池還有知覺系統，當電池組所在地淹水、遭外力破壞時、過充過放造成電池傷害時，都會即時提出警告，以利馬上斷絕部分受傷的電池，使其暫停運作，讓電力輸出不會中斷或產生危險，如起火火災或電池燒毀等。或者在 BMS 的 PCB 的設計線路申請 copyright 或著作財產權來保護我們的產業；或者儲存我們工程團隊的研發過程紀錄的 records ，在日後主張我們的技術或專利權利。\n\n以上供您參考及指點，感恩。\n\nEdge computer on HBMS 完成電池的 AI 初級演算數據趨勢再投入雲端Cloud computer在雲端深度演算、自我學習、自我進階，主動聯繫客人電池狀態及採取相應措施。AI 智能電池是全球未來的趨勢，1~5年內市場營業額或爆發式的成長，沒有 AI 的功能是無法在市場行銷的（但是整合充電、放電、溫度、時間的函數才有機會供給 AI 深度運算，這個能力非台灣的40~50年的功力莫屬，所以世界的AI電池，就是一塊台灣技術的開發地，加上我們委託的台積電的ASIC 晶片將如虎添翼）89萬筆專利，只有偵測的專利，還未有演算法的專利。\n\n王錦生 James Wang\n+886 932924084\n+886 227881838\nmail:jameswang120188@gmail.com\n地址:台北市南港區重陽路457號1樓"
            ),
             TextSendMessage(  
                text = "https://youtu.be/iyp09Ks2qYY"
            ) 
            ]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
   
  
    elif mtext == '@地圖查詢':
        try:
            message = TextSendMessage (  
            text="請選擇您的選項",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="本公司地址",text="公司地址")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="保時捷",text="保時捷")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="其他",text="其他")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="華城",text="華城")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="BMW",text="BMW")
                    ),
                   
                ]
            )   
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    

    elif mtext == '@網頁':
        try:
            message = TextSendMessage(  
                text = "https://www.midasgroup.com.tw/"
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    

#==================地圖查詢服務按鈕=======================================
    if '公司地址' in msg:
            message = buttons_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif '保時捷' in msg:
            message = buttons2_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif '其他' in msg:
            message = buttons3_message()
            line_bot_api.reply_message(event.reply_token, message) 
    elif '華城' in msg:
            message = buttons4_message()
            line_bot_api.reply_message(event.reply_token, message)   
    elif 'BMW' in msg:
            message = buttons6_message()
            line_bot_api.reply_message(event.reply_token, message)   
#==================保時捷分布============================================= 
    if 'PORSCHE北部' in msg:
            message = location_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif 'PORSCHE中部' in msg:
            message = location2_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif 'PORSCHE南部' in msg:
            message = location3_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif 'PORSCHE東部' in msg:
            message = location4_message()
            line_bot_api.reply_message(event.reply_token, message)
#==================華城分布============================================= 
    if 'EVALUE北部' in msg:
            message = buttons5_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif '北市EVALUE' in msg:
            message = location5_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif '桃園新竹EVALUE' in msg:
            message = location6_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif 'EVALUE中部' in msg:
            message = location7_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif 'EVALUE南部' in msg:
            message = location8_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif 'EVALUE東部' in msg:
            message = location9_message()
            line_bot_api.reply_message(event.reply_token, message)
#======================BMW============================================
    
    if '寶馬北部' in msg:
            message = buttons7_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif '寶馬北市' in msg:
            message = location10_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif '寶馬桃園新竹' in msg:
            message = location11_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif '寶馬中部' in msg:
            message = location12_message()
            line_bot_api.reply_message(event.reply_token, message)
    elif '寶馬南部' in msg:
            message = location13_message()
            line_bot_api.reply_message(event.reply_token, message)
#==================================================================

    print('name',name)
    print('picture',pic_url)
    print('uid',uid)
    print('msg',msg)
    

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
