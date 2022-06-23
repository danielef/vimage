import cv2
import logging
import os
import vimage.ndd

def retrieve_media_data(path):
    cap = cv2.VideoCapture(path)
    fps = float(cap.get(cv2.CAP_PROP_FPS))
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if length < 0:
        logging.warn("Video length: {} frames!".format(length))
    return {'capture': cap, 'fps': fps, 'length': length, 'path': path}

def retrieve_captures(data, delta_skip=15, resize=(270,480), ndd_threshold=0.5, ndd_hash_size=8):
    is_success, frame = data['capture'].read()
    f_readed = 0
    f_saved  = 0
    f_skip   = int(delta_skip * data['fps']) + 1
    logging.debug('f_skip: {}'.format(f_skip))
    while is_success:
        f_readed += 1
        if f_readed % f_skip == 0:
            # print('Saving frame {}'.format(f_readed))
            f_saved += save_frame(data,
                                  '{}.jpg'.format(f_readed),
                                  frame, resize,
                                  ndd_threshold=ndd_threshold,
                                  ndd_hash_size=ndd_hash_size)
        is_success, frame = data['capture'].read()

    data['saved'] = f_saved
    data['readed'] = f_readed

    return data

def write_frame(data, frame, resize, f_hash, f_dir, f_name, similarity=0.0):
    try:
        data['last'] = f_hash
        file_name = os.path.join(f_dir, f_name)
        logging.info('Writing: {} - {}'.format(file_name, similarity))
        frame = frame if resize is None else cv2.resize(frame, resize, interpolation = cv2.INTER_AREA)
        status = cv2.imwrite(file_name, frame)
        if not status:
            raise Exception('Unable to write: {}'.format(file_name))
        return 1
    except Exception as e:
        logging.error(e)
        return 0

def save_frame(data, name, frame, resize, ndd_threshold=0.5, ndd_hash_size=8):
    try:
        f_dir = data.get('dir', data['path'] + '_vimage')
        if not os.path.exists(f_dir):
            os.makedirs(f_dir)
            data['dir'] = f_dir

        if ndd_threshold > 0:
            f_hash = vimage.ndd.dhash(frame, hash_size=ndd_hash_size)
            last = data.get('last')
            if last is not None:
                similarity = vimage.ndd.similarity(last, f_hash, ndd_hash_size)
                if similarity < ndd_threshold:
                    return write_frame(data, frame, resize, f_hash, f_dir, name, similarity)
            else:
                return write_frame(data, frame, resize, f_hash, f_dir, name)
            return 0
        else:
            return write_frame(data, frame, resize, None, f_dir, name)
    except Exception as e:
        logging.error(e)
        return 0
