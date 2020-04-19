import getopt
import sys

qualities = ["480", "720", "1080"]


# TODO validation
def download(show_name, quality, start_ep, end_ep):
    print(show_name, quality, start_ep, end_ep)
    pass


if __name__ == '__main__':
    show_name = None
    quality = None
    start_ep = None
    end_ep = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:q:a:z:",["help","show=","quality=","start=","end="])
    except getopt.GetoptError:
        print("horriblescraper.py -s <showname> -q <quality> -a <start_episode> -z <end_episode>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # TODO add more help information
            print("usage: horriblescraper.py -s <showname> -q <quality> -a <start_episode> -z <end_episode>")
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