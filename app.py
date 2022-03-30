import argparse
import colorlog
import logging
import logging.config
import os
import vimage

def load_log(config='.'):
    config_dir = os.path.dirname(config)
    file_log = os.path.join(config_dir, 'log.conf')
    print("Loading logging configuration from: {}".format(file_log))
    if os.path.isfile(file_log):
        logging.config.fileConfig(file_log)
        try:
            import colorlog
            if isinstance(logging.getLogger().handlers[0].formatter, colorlog.ColoredFormatter):
                logging.getLogger().handlers[0].formatter.log_colors = {'DEBUG': 'cyan', 
                                                                        'INFO': 'green', 
                                                                        'WARNING': 'yellow', 
                                                                        'ERROR': 'red', 
                                                                        'CRITICAL': 'purple'}
        except:
            pass
    else:
        logging.error('Log config file: \'{}\' does not exists'.format(file_log))
        exit(2)

def resizeCheck(widthxheight):
    try:
        width, height = re.split('[xX]', widthxheight)
        return (int(width), int(height))
    except Exception:
        raise argparse.ArgumentTypeError("{} is an invalid resize value".format(widthxheight))

if __name__ == '__main__':
    load_log()
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', required=True, help='Video File')
    parser.add_argument('-d', '--delay', required=False, type=float, default=1.0, help='Delay seconds between each capture')
    parser.add_argument('-r', '--resize', required=False, type=resizeCheck, help='WIDTHxHEIGHT pixels to resize capture')

    args = parser.parse_args()
    logging.info('params: {}'.format(args.__dict__))

    data = vimage.retrieve_media_data(args.video)
    logging.debug(vimage.retrieve_captures(data))
    
