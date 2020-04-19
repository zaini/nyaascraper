#!/usr/bin/python

import getopt
import sys
import requests
from bs4 import BeautifulSoup as bs

url = 'https://nyaa.si/user/HorribleSubs?f=0&c=0_0&q={}&o=desc&p={}'

qualities = ["480", "720", "1080"]

# python horriblescraper.py -s "one piece" -q 720 -a 800 -z 1000

# TODO validation
def download(show_name, quality, start_ep, end_ep):
    search_url = url.format(show_name, "{}")
    start_ep = int(start_ep)
    end_ep = int(end_ep)

    for page_number in range(1, 5 + 1):
        page_url = search_url.format(page_number)
        page_html = requests.get(page_url)
        soup = bs(page_html.text, 'html.parser')

        rows = soup.find_all('tr', class_='success')
        print(type(rows), len(rows))
        for row in rows:
            row_contents = row.findAll('a')
            for content in row_contents:
                # Checking that content being looked at is the 'a' element with the episode name
                if content.has_attr('title') and show_name.upper() in content['title'].upper():
                    row_title = content['title'].split(" ")
                    # Checking that row is an episode to be downloaded
                    if start_ep <= int(row_title[-2]) <= end_ep and quality in row_title[-1]:
                        print("Opening: " + content['title'])


if __name__ == '__main__':
    show_name = None
    quality = None
    start_ep = None
    end_ep = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:q:a:z:", ["help", "show=", "quality=", "start=", "end="])
    except getopt.GetoptError:
        print("horriblescraper.py -s <show_name> -q <quality> -a <start_episode> -z <end_episode>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # TODO add more help information
            print("usage: horriblescraper.py -s <show_name> -q <quality> -a <start_episode> -z <end_episode>")
            sys.exit(2)
        elif opt in ("-s", "--show"):
            show_name = arg
        elif opt in ("-q", "--quality"):
            quality = arg
        elif opt in ("-a", "--start"):
            start_ep = arg
        elif opt in ("-z", "--end"):
            end_ep = arg

    download(show_name, quality, start_ep, end_ep)
