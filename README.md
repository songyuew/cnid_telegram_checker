# cnid_telegram_checker
Conduct real-name verification of Chinese National ID(中国身份证) with a Telegram bot
Use an real-name verification API on Aliyun Marketplace

  - Whether an ID # exists in MPS(Ministry of Public Security) system
  - Whether the name provided matches the record in MPS system
  - Shows the household register(户口) area of the holder

![demo](/img/demo.png)

## Getting Started
  1. Install `requests` and `python-telegram-bot`
  
     ```
     pip install requests
     ```
     ```
     pip install python-telegram-bot
     ```
  3. Buy real-name verification service at Aliyun Marketplace [here](https://market.aliyun.com/products/57000002/cmapi022049.html?spm=5176.730005.result.18.59353524AT5PSu&innerSource=search_%E8%BA%AB%E4%BB%BD%E8%AF%81#sku=yuncode1604900000)
  4. Replace `APP_CODE` in `cnid_checker.py` with your own Aliyun appcode
     You can find your appcode in [Aliyun Console](account.aliyun.com)
  5. Replace `API_TOKEN` in `guard_id_checker.py` with your Telegram bot API key
  6. Fill the Telegram ID(s) of Telegram client account(s) that is going to use this bot in `authorized` in `guard_id_checker.py`
     This avoids unauthorized people using your bot and Aliyun Marketplace API(API calls are charged by the provider)
     If you don't know your Telegram ID, search ```Get My ID``` in Telegram, this bot will send you the user ID
     
     ![userid](/img/useridpng.png)
     
## Usage

Run the `guard_id_checker.py` script to start the bot

```
python guard_id_checker.py
```

### Input
Check an ID card number by sending this message to the bot:
```
[CNID]-CNID_NUMBER-CHN_NAME
```
Replace `CNID_NUMBER` and `CHN_NAME` with ID number and name in simplified Chinese(简体中文)

### Authorization
If you are sending message to the bot with an unauthorized client account, the request will not be processed and you will get `Not authorized` message. 

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<!-- CONTACT -->

## Contact

Songyue Wang Aaron - me@songyue.wang

Project Link: [https://github.com/songyuew/cnid_telegram_checker](https://github.com/songyuew/cnid_telegram_checker)

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Aliyun API Marketplace](https://market.aliyun.com/products/57000002/cmapi022049.html?spm=5176.730005.result.18.59353524AT5PSu&innerSource=search_%E8%BA%AB%E4%BB%BD%E8%AF%81#sku=yuncode1604900000)
- [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)
