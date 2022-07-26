import argparse
import colorlog
import logging
import logging.config
import os
import sys
import re
import vimage.video

def load_log():
    log_config = {
        'version': 1,
        'root': { 'handlers': ['console'], 'level': 'DEBUG' },
	'handlers': {'console': {'class': 'StreamHandler', 'formatter': 'color'}},
	'formatters': {'color': {'class': 'colorlog.ColoredFormatter', 'format': '%(asctime)s %(log_color)s%(levelname)-8s%(reset)s %(process)s %(name)s %(message)s'}}
    }
   
    logging.config.dictConfig(log_config)
    try:
        if isinstance(logging.getLogger().handlers[0].formatter, colorlog.ColoredFormatter):
            logging.getLogger().handlers[0].formatter.log_colors = {'DEBUG': 'cyan', 
                                                                    'INFO': 'green', 
                                                                    'WARNING': 'yellow', 
                                                                    'ERROR': 'red', 
                                                                    'CRITICAL': 'purple'}
    except:
        pass

def resizeCheck(widthxheight):
    try:
        width, height = re.split('[xX]', widthxheight)
        return (int(width), int(height))
    except Exception:
        raise argparse.ArgumentTypeError("{} is an invalid resize value".format(widthxheight))

def main():
    load_log()
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', required=True, help='Video File')
    parser.add_argument('-d', '--delay', required=False, type=float, default=15.0, help='Delay seconds between each capture')
    parser.add_argument('-r', '--resize', required=False, type=resizeCheck, help='WIDTHxHEIGHT pixels to resize capture')
    parser.add_argument('-H', '--lsh_hashsize', required=False, type=int, default=8, help='LSH hashsize')

    args = parser.parse_args()
    logging.info('params: {}'.format(args.__dict__))

    data = vimage.video.retrieve_media_data(args.video)
    logging.debug('{}'.format(vimage.video.retrieve_captures(data,
                                                       delta_skip=args.delay,
                                                       resize=args.resize,
                                                       ndd_hash_size=args.lsh_hashsize)))

if __name__ == '__main__':
    main()
