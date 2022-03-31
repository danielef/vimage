import cv2
import logging
import os
import ndd

def retrieve_media_data(path):
    cap = cv2.VideoCapture(path)
    fps = float(cap.get(cv2.CAP_PROP_FPS))
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return {'capture': cap, 'fps': fps, 'length': length, 'path': path}

def retrieve_captures(data, delta_skip=15):
    is_success, frame = data['capture'].read()
    f_readed = 0
    f_saved  = 0
    f_skip   = int(delta_skip * data['fps']) + 1
    print('f_skip: {}'.format(f_skip))
    while is_success:
        f_readed += 1
        if f_readed % f_skip == 0:
            # print('Saving frame {}'.format(f_readed))
            f_saved += save_frame(data, '{}.jpg'.format(f_readed), frame)
        is_success, frame = data['capture'].read()

    data['saved'] = f_saved
    data['readed'] = f_readed

    return data

def save_frame(data, name, frame, ndd_threshold=0.5, ndd_hash_size=8):
    f_dir = data.get('dir', data['path'] + '_vimage')
    if not os.path.exists(f_dir):
        os.makedirs(f_dir)
        data['dir'] = f_dir
    if ndd_threshold > 0:
        f_hash = ndd.dhash(frame, hash_size=ndd_hash_size)
        last = data.get('last')
        if last is not None:
            similarity = ndd.similarity(last, f_hash, ndd_hash_size)
            if similarity < ndd_threshold:
                data['last'] = f_hash
                file_name = os.path.join(f_dir, name)
                logging.info('Writing: {} - {}'.format(file_name, similarity))
                cv2.imwrite(file_name, frame)
                return 1
        else:
            data['last'] = f_hash
            file_name = os.path.join(f_dir, name)
            logging.info('Writing: {} - {}'.format(file_name, similarity))
            cv2.imwrite(file_name, frame)
            return 1
        return 0
    else:
        file_name = os.path.join(f_dir, name)
        logging.info('Writing: {}'.format(file_name))
        cv2.imwrite(file_name, frame)
        return 1
