import requests
import datetime as dt
import smtplib

try:
    STOCK = "EAF"
    COMPANY_NAME = "GrafTech"

    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



    API_key="GVPUR03AIR45JIZP"

    response=requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=EAF&interval=30min&apikey=GVPUR03AIR45JIZP")
    response.raise_for_status()
    data=response.json()["Time Series (30min)"]
    # print(data)

    change=False
    today=dt.datetime.now()
    day=today.day
    month=today.month
    if month<10:
        month=f"0{month}"
    year=today.year

    temp1=data[f"{year}-{month}-{day-1} 19:00:00"]["1. open"].split(".")
    yes_open=int(temp1[1])


    temp2=data[f"{year}-{month}-{day-2} 19:00:00"]["4. close"].split(".")
    pr_yes_open=int(temp2[1])


    per_in_de=(yes_open - pr_yes_open)/pr_yes_open*100


    if(per_in_de>=5 or per_in_de<=-5):
        change=True
        if(per_in_de>=5):
            perme=f"🔺{round(per_in_de,2)}"
        else:
            perme=f"🔻{round(-per_in_de,2)}"




    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    News_API_key="8e31ecbeab174b4a92f9885488f688e6"
    if change:
        URL=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={year}-{month}-{day-2}&sortBy=publishedAt&apiKey={News_API_key}"

        response1=requests.get(url=URL)
        response1.raise_for_status()
        data1=response1.json()

        news_title=[]
        news_content=[]

        for i in data1["articles"]:
            news_title.append(i["title"])
            news_content.append(i["content"])


    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 

    MSG=""

    for i in range(len(news_title)):
        MSG=MSG + f"{STOCK}: {perme}%\nHEADLINES: {news_title[i]}.\nBRIEF: {news_content[i]}\n\n"

    MSG=MSG.encode("ASCII")
    my_id="ansh.formal@gmail.com"
    Password="uhdsjfftgspyqsxg"
    to_id="rrdesai123@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
                        connection.starttls()
                        connection.login(user=my_id,password=Password)
                        connection.sendmail(from_addr=my_id,to_addrs=to_id,msg=f"Subject: ANSH TRIAL PROJECT\n{MSG}")


    #Optional: Format the SMS message like this: 
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
except:
      pass

