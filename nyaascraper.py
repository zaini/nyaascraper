#!/usr/bin/python

import getopt
import sys
import time
import webbrowser

import requests
from bs4 import BeautifulSoup

class URL:
    def __init__(self, url, ep_index, quality_index, alt_ep_index = None, alt_quality_index = None, condition = lambda x: False):
        self.url = url

        self.ep_index = ep_index
        self.quality_index = quality_index

        self.alt_ep_index = ep_index if alt_ep_index == None else alt_ep_index
        self.alt_quality_index = quality_index if alt_quality_index == None else alt_quality_index

        self.condition = condition


subsplease_url = URL('https://nyaa.si/user/subsplease?f=0&c=0_0&q={}&o=desc&p={}', -3, -2)
erairaws_url = URL('https://nyaa.si/user/Erai-raws?f=0&c=0_0&q={}&o=desc&p={}', -2, -1, -3, -2, lambda x: "[Multiple Subtitle]" in x) # condition returns True if the given row_title or content['title'] should use the alt indices
horriblesubs_url = URL('https://nyaa.si/user/HorribleSubs?f=0&c=0_0&q={}&o=desc&p={}', -2, -1)

groups = {'hs' : horriblesubs_url, 'er' : erairaws_url, 'sp' : subsplease_url}

base_url = 'https://nyaa.si/'


def download(group, show_name, quality, start_ep, end_ep, req_file, sleep_time=0.5):
    search_url = group.url.format(show_name, "{}")
    start_ep = int(start_ep)
    end_ep = int(end_ep)
    episodes_to_download = end_ep - start_ep + 1

    for page_number in range(1, 100):  # maximum page is 15 anyways
        page_url = search_url.format(page_number)
        page_html = requests.get(page_url)
        soup = BeautifulSoup(page_html.text, 'html.parser')
        rows = soup.find_all('tr', class_='success')

        for row in rows:
            row_contents = row.findAll('a')

            links = row.find_all('td', class_='text-center')[0].find_all('a')
            magnet = base_url + links[0]['href'] if req_file else links[1]['href']
            
            for content in row_contents:
                # Checking that content being looked at is the 'a' element with the episode name
                if content.has_attr('title') and show_name.upper() in content['title'].upper():
                    row_title = content['title'].split(" ")

                    if group.condition(content['title']):
                        ep_index = group.alt_ep_index
                        quality_index = group.alt_quality_index
                    else:
                        ep_index = group.ep_index
                        quality_index = group.quality_index

                    # Checking that row is an episode to be downloaded
                    try:
                        if start_ep <= float(row_title[ep_index]) <= end_ep and quality in row_title[quality_index]:
                            print("Opening: " + content['title'])
                            webbrowser.open(magnet)
                            episodes_to_download -= 1
                            time.sleep(sleep_time)
                    except Exception as e:
                        # Title format is unexpected
                        print(f"Did not download: {content['title']}\nError: {e}\n")
                        pass

        # Break if the actual page is not the same as page_number, meaning there are no more pages
        # Break if episodes have been downloaded
        if soup.find('li', class_='active') is None or page_number != int(soup.find('li', class_='active').text) or episodes_to_download == 0:
            break

    print("Complete.")
    if episodes_to_download > 0:
        print("{} episode(s) could not be loaded.".format(episodes_to_download))


def usage_error():
    print("usage: nyaascraper.py -g <group_name> -s <show_name> -q <quality> -a <start_episode> -z <end_episode>\nAdd -f or "
          "--file at the end to download the .torrent files instead of open magnets\n"
          "If you don't give a group name, Erai-raws is used by default.\n"
          "er = Erai-raws, hs = horriblesubs, sp = subsplease")
    sys.exit(2)


if __name__ == '__main__':
    group_name = 'er'
    show_name = None
    quality = None
    start_ep = None
    end_ep = None
    req_file = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hfg:s:q:a:z:", ["help", "file", "group=", "show=", "quality=", "start=", "end="])
    except getopt.GetoptError:
        usage_error()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # TODO add more help information
            usage_error()
        elif opt in ("-g", "--group"):
            group_name = arg
        elif opt in ("-s", "--show"):
            show_name = arg
        elif opt in ("-q", "--quality"):
            quality = arg
        elif opt in ("-a", "--start"):
            start_ep = arg
        elif opt in ("-z", "--end"):
            end_ep = arg
        elif opt in ("-f", "--file"):
            req_file = True

    tags = [group_name, show_name, quality, start_ep, end_ep, req_file]

    if None in tags:
        usage_error()
    else:
        download(groups.get(group_name, groups['er']), show_name, quality, start_ep, end_ep, req_file)
