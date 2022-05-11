from flask import Flask, render_template
from lyricShit import *
import json
import youtube_dl
app = Flask(__name__)
app._static_folder = ''

@app.route("/")
def index():
    return app.send_static_file('index.html')



@app.route("/downloaded")
def download():
    url = 'https://soundcloud.com/not_ac/biscotti-in-the-air-juice-1?utm_source=clipboard'
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            url,
            download=True
        )
    outFile = result['id'] + result['ext']
    artist = result['uploader']
    title = result['title']
    art = result['thumbnail']
    # TODO finish download template html and link it here
    return render_template('downloadTemplate.html', art = art, artist = artist, title = title, path = outFile)



@app.route("/update", methods =['POST'])
def update():
    # TODO updates specified metadata fields for a given path
    return False



@app.route("/import", methods =['POST'])
def beet():
    path = None
    try: 
        runner = pyexpect.spawn("beet import "+path)
        runner.expect("files")
        runner.sendline("y")
    except:
        return False
    # do i need to kill the runner? do it if so
    return True



@app.route("/embedArt", methods =['POST'])
def art():
    # TODO embeds art to a given url
    return False



@app.route("/fetchGenuis", methods = ['POST'])
def genuis():
    # TODO fetch genuis lyrics for setting up metadata sync
    return False



@app.route("/path", methods = ["POST"])
def path():
    # TODO return relative path for use with lrc data generator
    return False



@app.route("/getData", methods = ["POST"])
def data(file):
    # TODO get metadata for specified file
    return False



if __name__ == "__main__":
    app.run()