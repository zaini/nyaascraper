#!/usr/bin/python

import getopt
import sys
import webbrowser

import requests
from bs4 import BeautifulSoup

url = 'https://nyaa.si/user/HorribleSubs?f=0&c=0_0&q={}&o=desc&p={}'


# TODO validation
def download(show_name, quality, start_ep, end_ep):
    search_url = url.format(show_name, "{}")
    start_ep = int(start_ep)
    end_ep = int(end_ep)
    episodes_to_download = end_ep - start_ep + 1

    for page_number in range(1, 100):  # maximum page is 15 anyways
        page_url = search_url.format(page_number)
        page_html = requests.get(page_url)
        soup = BeautifulSoup(page_html.text, 'html.parser')
        rows = soup.find_all('tr', class_='success')

        # Break if the actual page is not the same as page_number, meaning there are no more pages
        if page_number != int(soup.find('li', class_='active').text):
            break

        for row in rows:
            row_contents = row.findAll('a')

            links = row.find_all('td', class_='text-center')[0].find_all('a')
            magnet = links[1]['href']

            for content in row_contents:
                # Checking that content being looked at is the 'a' element with the episode name
                if content.has_attr('title') and show_name.upper() in content['title'].upper():
                    row_title = content['title'].split(" ")
                    # Checking that row is an episode to be downloaded
                    try:
                        if start_ep <= int(row_title[-2]) <= end_ep and quality in row_title[-1]:
                            print("Opening: " + content['title'])
                            webbrowser.open(magnet)
                            episodes_to_download -= 1
                    except:
                        # Title format is unexpected
                        pass

        # Break if episodes have been downloaded
        if episodes_to_download == 0:
            break

    print("Complete.")
    if episodes_to_download > 0:
        print("{} episode(s) could not be loaded.".format(episodes_to_download))


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
