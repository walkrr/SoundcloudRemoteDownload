from flask import Flask, render_template, request
import youtube_dl
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
import mutagen
import os
import shutil
app = Flask(__name__)
app._static_folder = ''

@app.route("/")
def index():
    return app.send_static_file('index.html')



@app.route("/download", methods = ['POST'])
def download():
    url = request.form.get("URL")
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

    try:
        with ydl:
            result = ydl.extract_info(
                url,
                download=True
            )
    except:
        return("An error was encountered when downloading the requested file")
    outFile = result['id'] + "." + result['ext']
    artist = result['uploader']
    title = result['title']
    art = result['thumbnail']
    return render_template('downloadTemplate.html', art = art, artist = artist, title = title, path = outFile)



@app.route("/update", methods =['POST'])
def setdData():
    path = request.form.get("path")
    try:
        meta = mutagen.File(path, easy=True)
        meta.add_tags()
        meta.save(path, v1=2)
    except:
        pass
    response = requests.get(request.form.get('art'), stream=True)
    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    audio = EasyID3(path)
    audio['artist'] = request.form.get('artist')
    audio['title'] = request.form.get('title')
    audio['album'] = request.form.get('title')
    audio.save()

    audio = ID3(path)
    with open('img.jpg', 'rb') as albumart:
        audio['APIC'] = APIC(
                          encoding=3,
                          mime='image/jpeg',
                          type=3, desc=u'Cover',
                          data=albumart.read()
                        )            
    os.remove('img.jpg')
    audio.save()
    os.popen("beet import -A " + path)
    return("added")

if __name__ == "__main__":
    app.run()