# horriblesubsscraper
An application to scrap and open magnet links for HorribleSubs torrents from nyaa.si. Useful for when batches don't exist or you don't have some particular episodes.

This scraper will search for the provided show at the specified quality on HorribleSubs' page on nyaa.si and open the magnet links in your default BitTorrent client.

Video walkthrough: https://youtu.be/IetQGifSNEs [OUTDATED, check usage below]

# Features
* searches for shows using the same search engine as on nyaa.si
* allows user to select quality (480p, 720p or 1080p)
* select range of episodes to download, including episodes with decimals e.g. 13.5
* doesn't download premade batch files which are already available by HorribleSubs on nyaa.si
* loads magnets in chronological order of upload to nyaa.si
* tells you how many episodes weren't found/loaded

**Soon:**
* use horriblesubs.info instead of nyaa.si
* validation for user input. for now just don't be an idiot.
* updated demo video
* output which files were not found

# Requirements
* Python 3+
* Any BitTorrent client which allows for magnet links

# Installation
* Download horriblescraper.py and run it

# Usage

```
python horriblescraper.py -s <show_name>> -q <quality> -a <start_epsiode> -z <end_epsiode>
```

e.g.

```
python horriblescraper.py -s "shingeki no kyojin" -q 720 -a 10 -z 15
```

```
python horriblescraper.py -s Gleipnir -q 1080 -a 0 -z 999
```

Enter the show's name as you would search for it on nyaa.si/user/HorribleSubs

Enter the quality you want. HorribleSubs is usually just 480p, 720p or 1080p

Then enter the first episode and last episode you want to download. This is an inclusive range. e.g. Entering 10 and 15 will also download episodes 10 and 15.

# Additional information
If the specified show at the specified quality is not available, it will not be loaded and you'd have to check that manually.
To avoid having to change the file download location for each torrent, change it on one torrent so it becomes the default then run the program. Your client may also allow you to check a box to not open up a dialog box.

I thought to make this when I used jtara1's version (found here: https://github.com/jtara1/horriblesubs_batch_downloader) but had it crash due to dialog Windows opening up and also that I couldn't change the quality. It was also a learning expierence for my first somewhat useful scraper.

This was another similar program, although I haven't used it: https://youtu.be/97Mfx11qjIs

You can watch a demo of the old version here: https://youtu.be/IetQGifSNEs