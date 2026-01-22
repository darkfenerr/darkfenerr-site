from flask import Flask

app = Flask(__name__)

@app.route("/darkfenerr")
def darkfenerr():
    return """
    <html>
        <head>
            <title>İlk Sayfam</title>
        </head>
        <body>
            <h1>Hoş geldin</h1>
            <p>
                Merhaba benim adım Darkfenerr. Instagramda edit sayfam var, orada editlerimi paylaşıyorum.
                Telegramda ise Premium kanalım var, orada kendi yaptığımız compları paylaşıyoruz.
                <br><br>
                <a href="https://t.me/wdpremiumteaser" target="_blank">Telegram kanalım</a><br>
                <a href="https://www.instagram.com/darkfenerr.ae7/" target="_blank">Instagram edit sayfam</a>
                <br><br>
                İletişim:<br>
                Instagram: darkfenerr.ae7<br>
                Telegram: Darkfenerrr 🙂
            </p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
