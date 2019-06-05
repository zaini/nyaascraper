# horriblesubsscraper
An application to scrap and run magnet links for HorribleSubs torrents from nyaa.si where batches don't already exist.

This scraper will search for the entered show at the selected quality on HorribleSubs page on nyaa.si and open the magnet links.

Video walkthrough: https://youtu.be/IetQGifSNEs (This is before an installer was made, now you can just use that which is much simpler.)

# Features
* searches for shows using the same search engine as on nyaa.si
* allows user to select quality (480p, 720p or 1080p)
* select range of episodes to download, including episodes with decimals e.g. 13.5
* doesn't download premade batch files which are already available by HorribleSubs on nyaa.si
* loads magnets in chronological order of upload to nyaa.si

**Soon:**
* use horriblesubs.info instead of nyaa.si
* optimise how the number of pages and rows are found, should improve performance
* add validation to episode range input
* updated installer and demo video for latest features

# Requirements
* Python 3+
* Any BitTorrent client which allows for magnet links

# Installation
* Download HorribleSubsScraper.py and run it through Python IDLE, Python 3.7+ is what it was made with.

Or

(Installer is missing some features.)
1. Download HorribleSubsScraper-Installer
2. Run it and follow the instructions to install the program and run it.

# Usage
Enter the show's name as you would search for it on nyaa.si/user/HorribleSubs

Enter a number corresponding to the quality you want it to be downloaded in.

# Additional information
If the specified show at the specified quality is not available, it will not be installed and you'd have to check that manually.
To avoid having to change the file download location for each torrent, change it on one torret so it becomes the default then run the program. Your client may also allow you to check a box to not open up a dialog box.

I thought to make this when I used jtara1's version (found here: https://github.com/jtara1/horriblesubs_batch_downloader) but had it crash due to dialog Windows opening up and also that I couldn't change the quality. It was also a learning expierence for my first somewhat useful scraper.

This was another similar program, although I haven't used it: https://youtu.be/97Mfx11qjIs
