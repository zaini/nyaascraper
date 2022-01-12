# nyaascraper

An application to scrape and open magnet links for HorribleSubs/subsplease/Erai-raws torrents from nyaa.si. Useful for when batches don't exist or you don't have some particular episodes.

This scraper will search for the provided show at the specified quality on the corresponding groups page on nyaa.si and open the magnet links in your default BitTorrent client.

This is a modified version of my old HorribleSubs scraper, but made to work with a couple more groups: https://github.com/zaini/horriblesubsscraper

Video walkthrough (of horriblescraper, which is very similar): https://youtu.be/YAVOioo6PPM

# Features

- searches for shows using the same search engine as on nyaa.si
- allows user to select quality (480p, 720p or 1080p)
- select range of episodes to download, including episodes with decimals e.g. 13.5
- doesn't download premade batch files which are already available by the groups on nyaa.si
- loads magnets in chronological order of upload to nyaa.si
- tells you how many episodes weren't found/loaded
- option to download the .torrent files instead of opening the magnets directly (although not recommended)

**Soon:**

- updated demo video
- output which files were not found
- add more videos
- deal with more errors
- update this README

# Requirements

- Python 3.0+
- Any BitTorrent client which allows for magnet links

# Installation

1. Download nyaascraper.py
2. Make sure you have [pip](https://pip.pypa.io/en/stable/installation/) installed
3. Run `pip install -r requirements.txt`

# Usage

Find the list of group names [below.]

```
python nyaascraper.py -g <group_name> -s <show_name> -q <quality> -a <start_epsiode> -z <end_epsiode>
```

e.g.

```
python nyaascraper.py -s "shingeki no kyojin" -q 720 -a 10 -z 15 -g hs
```

```
python nyaascraper.py -s Gleipnir -q 1080 -a 0 -z 999 -g sp
```

If the group doesn't exist (or you don't specify a group) then Erai-raws will be used as a default.

```
python nyaascraper.py -s "shingeki no kyojin" -q 720 -a 10 -z 15 -g fakegroup
```

Enter the show's name as you would search for it on nyaa.si/user/INSERT_GROUP_NAME

Enter the quality you want. Usually just 480p, 720p or 1080p

Then enter the first episode and last episode you want to download. This is an inclusive range. e.g. Entering 10 and 15 will also download episodes 10 and 15.

You can add `-f` or `--file` at the end of the command to download the .torrent files instead of opening the magnets, although this is not suggested.

(in case it's not clear, you'll need to run all these commands from a terminal)

# Groups

## NOTE: I HAVEN'T USED ALL OF THESE GROUPS SO IDK IF THEY SUCK OR EVEN WORK. I personally suggest one of the first 3.

| Group                                                             | Code         |
| ----------------------------------------------------------------- | ------------ |
| [HorribleSubs](https://nyaa.si/user/HorribleSubs)                 | hs           |
| [subsplease](https://nyaa.si/user/subsplease)                     | sp           |
| [Erai-raws](https://nyaa.si/user/Erai-raws)                       | er           |
| [kiyoshiisubs](https://nyaa.si/user/kiyoshiisubs)                 | kiyoshiisubs |
| [Mayansito](https://nyaa.si/user/Mayansito)                       | mayansito    |
| [SmallSizedAnimations](https://nyaa.si/user/SmallSizedAnimations) | ssa          |
| [Ember_Encodes](https://nyaa.si/user/)                            | ember        |

# Additional information

If the specified show at the specified quality is not available, it will not be loaded and you'd have to check that manually.
To avoid having to change the file download location for each torrent, change it on one torrent so it becomes the default then run the program. Your client may also allow you to check a box to not open up a dialog box.

This is a modified version of my old HorribleSubs scraper: https://github.com/zaini/horriblesubsscraper
