import argparse
import vimage

def resizeCheck(widthxheight):
    try:
        width, height = re.split('[xX]', widthxheight)
        return (int(width), int(height))
    except Exception:
        raise argparse.ArgumentTypeError("{} is an invalid resize value".format(widthxheight))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', required=True, help='Video File')
    parser.add_argument('-d', '--delay', required=False, type=float, default=1.0, help='Delay seconds between each capture')
    parser.add_argument('-r', '--resize', required=False, type=resizeCheck, help='WIDTHxHEIGHT pixels to resize capture')

    args = parser.parse_args()
    print(args)

    data = vimage.retrieve_media_data(args.video)
    print(vimage.retrieve_captures(data))
    
