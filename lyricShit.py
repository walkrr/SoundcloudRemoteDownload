import requests
from bs4 import BeautifulSoup
import youtube_dl

# Function to clean up lyrics from genius 
def cleanGenuis(lyrics):
    olyrics = []

    # iterate over each line checkign if valid
    for i in range(len(lyrics)):

        # Skip lines that are empty
        if (lyrics[i] == "" or lyrics[i] == '\n'):
            continue

        # Skip lines that start with brackets
        elif (lyrics[i][0] == "[" or lyrics[i][0] == "("):
            continue

        # Add valid lines to output, removing the newline char at the end
        olyrics.append(lyrics[i][:-1])

    # TODO remove embed code at the end of each lyric set
    # Skip first line, genius has it as the title
    return olyrics[1:]

# Function to clean RC lyrics
def cleanRC(lrc):
    # TODO implement
    return False

# function to compare downloaded LRC against genius lyrics to ensure lrc is for correct song and formatted correctly
def validateLyrics(genius, lrc):
    # TODO implement
    return False


# function to combine a timestamp array with lyrics from genius and return lrc
def mergeTimestamps(genius, timestamps):
    # TODO implement
    return False


# function to seperate timestamps from lyrics in a given lrc file
def extractTimestamps(lrc):
    # TODO implement
    return False


# function to get lyrics from genius, code taken from beets lyric plugin
def getGenius(url):
    # TODO implement
    return False

# function to search genius for a specified song and artist, then retrun a url to the specified song
def genuisSearch(song,artist):
    # TODO implement
    return False

# Function to try to retrive LRC file from site given song and artist
def retrieveLrc(song,artist):
    # Generate url for request
    baseURL = 'https://rclyricsband.com/?s='
    qurl = baseURL + song + "+" + artist
    qurl = qurl.replace(" ","+")


    r = requests.get(qurl)
    soup = BeautifulSoup(r.content, 'html.parser')
    # get results
    result = soup.find('div',class_='content-area clr')


    # Iterate over results, each result has a few lines of info and then says Continue reading, if artist and song are in the info line, it sets found to true and 
    # breaks the loop, if the line is continue reading it incriments the index, if neither of these happen it just continues looping, index is later used to select the right link from list of links
    index = 0
    found = False
    splat = result.text.split("\n")
    for line in splat:
        if (line.lower() == 'continue reading'):
            index += 1
        if (song.lower() in line.lower() and artist.lower() in line.lower()):
            found = True
            break


    # If a song with the right artist and title isn't found, return false
    if (found == False):
        return False

    # Each link is duplicated, this takes the each link destination and removes duplicates
    links = []
    add = True
    for link in result.find_all('a'):
        if (add):
            links.append(link.get('href'))
        add = not add
    
    # Sets the next page to navigate to where the download link for the lrc file is
    nextPage = links[index]
    return(nextPage)

    # TODO 
    # Get downlaod link from selected page


print(retrieveLrc('lucid Dreams', 'juice wrld'))
