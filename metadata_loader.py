import os, sqlite3
from mutagen.oggopus import OggOpus
from dotenv import load_dotenv
from tqdm import tqdm


load_dotenv(dotenv_path=os.getenv('DOTENV_FILE_PATH'))
MS_DATA = os.getenv('ms_data')
MS_DATA = os.getenv('ms_data')
con = sqlite3.connect(MS_DATA)
cur = con.cursor()
meta_data = [i for i in cur.execute('SELECT artist, title, album, label, genre, date, bpm, path FROM items')]

for i in tqdm(meta_data):
    audio = OggOpus(i[-1])
    if 'BPM' not in audio or str(audio['GENRE'][0]) != i[4]:
        artist = [j.title() for j in i[0].split('_')]
        title = [j.title() for j in i[1].split('_')]
        album = [j.title() for j in i[2].split('_')] 
        label = [j.title() for j in i[3].split('_')]
        audio['ARTIST'] = ' '.join(artist)
        audio['TITLE'] =  ' '.join(title)
        audio['ALBUM'] = ' '.join(album)
        audio['LABEL'] = ' '.join(label)
        audio['GENRE'] = i[4]
        audio['DATE'] = str(i[5])
        audio['BPM'] = str(i[6])
        audio.save()


con.commit()
cur.close()
con.close()
