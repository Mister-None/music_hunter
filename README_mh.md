<<<<<<< HEAD
# OpusDB Manager
OpusDB Manager is a powerful Python utility for managing, identifying, and organizing large collections of `.opus` audio files. It integrates a SQLite backend with audio recognition technology to keep your music library clean, tagged, and easily playable.

## Features
The script provides a multi-functional CLI interface:
- **Automatic Recognition:** Uses `SongRec` (Shazam API) to identify tracks and fetch metadata (Artist, Title, Genre, Album, etc.).
- **Database Management:** Maintains a SQLite database for fast searching and filtering.
- **Smart Cleanup:** Removes metadata from files to maintain a "clean" local state and deletes duplicate tracks based on Artist/Title matching.
- **Interactive Playback:** Search and play music by Artist, Genre, Title, or Year using `mpv`.
- **Playlist Generation:** Automatically creates `.m3u8` playlists based on genres.
- **Batch Processing:** Normalize database strings or update existing metadata for specific tracks.
- **Excel Integration:** Import track lists from external Excel spreadsheets.

## Prerequisites

### System Dependencies
This script is designed for Linux-based systems. You must have the following tools installed:
- [FFmpeg](https://ffmpeg.org/): For audio processing and metadata stripping.
- [SongRec](https://github.com/marin-m/SongRec): CLI Shazam client for track recognition.
- [mpv](https://mpv.io/): For audio playback.

### Python Libraries
1. Install the required Python packages:
```bash
pip install requests pandas moviepy python-dotenv colorama tqdm openpyxl
```
2. Use `ms_data_template.db` for storing data about track

## Usage
For listing options run:
```bash
python mh_bot.py
#output
1 ==> add to base
2 ==> clean metadata
3 ==> play by arist/title/genre/year
4 ==> normalize
5 ==> remove duplicactes
6 ==> update base
7 ==> remove from base
8 ==> create playlists
9 ==> add specific base
```
=======
# yplayer
Search and play youtube videos using terminal and mpv player

## TODO
1. Create youtube-data-api key using cloud.google;
2. Create `.env` file and put there your key,  should be `YPLAYER_KEY=your_key`;
3. Add in your `.env` three path:
    ```.env
    BL_PATH=blacklist videos
    FV_PATH=favourite videos
    WT_PATH=watched videos
    ```
4. For help use:
    ```bash
    python yplayer.py h
    ```
5. By default yplayer in audio mode, if you want to watch video:
    ```bash
    python yplayer.py v
    ```
6. For selecting duration use options in "Query" prompt; 
    * `jazz night --l` (shows only videos that are more than 20 minutes)
    * `phonk music --m` (shows only videos that are more or equal than 4 minutes but less or equal than 20 minutes)
    * `funny videos --s` (shows only videos that are less than 4 minutes)
7. For quiting enter `q` in "Query" prompt;
8. For showing next list of results enter `next` in "Query" prompt;
9. For selecting previous list of results enter `prev` in "Query" prompt;
10. For selecting video:
    ```bash
    1. video1
    2. video2
    3. video3
    4. video4
    ...
    50. video50
    >>> 1 # play video1
    >>> 3<= # play from 3 to the end of list
    >>> 2,3,45 # play video2, video3, video45
    >>> 30>= # play from video30 to the first item of list
    >>> 3bl # add video to blacklist
    >>> 3fv # add video to favourite list
    >>> 3d # download audio track
    # enter 'q' for exiting playing
    # enter 'r' for  returning to main query
    ```
11. Listened/watched videos automatically add to watched list, so you wont see them again in a search results, if you wanna see list use option `b, f, w` (blacklist, favourite, watched respectfully)**
    ```bash
    python yplayer.py b
    python yplayer.py f
    python yplayer.py w
    ```
**Enjoy minimalistic represantion of youtube**   
>>>>>>> yplayer/main
