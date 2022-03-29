import cv2
import os
import numpy
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
            save_frame(data, '{}.jpg'.format(f_readed), frame, with_ndd=True)
            f_saved += 1
        is_success, frame = data['capture'].read()

    data['saved'] = f_saved
    data['readed'] = f_readed

    return data

def save_frame(data, name, frame, with_ndd=False):
    f_dir = data.get('dir', data['path'] + '_vimage')
    if not os.path.exists(f_dir):
        os.makedirs(f_dir)
        data['dir'] = f_dir
    if with_ndd:
        hash_size = 8
        f_hash = ndd.dhash(frame, hash_size=hash_size)
        f_pack = numpy.packbits(f_hash.flatten())
        #print('hash: {}'.format(ndd.binary_array_to_hex(f_hash)))
        #print('pack: {}'.format(f_pack))
        last = data.get('last')
        if last is not None:
            hd = sum(numpy.bitwise_xor(numpy.unpackbits(last), 
                                       numpy.unpackbits(f_pack)))
            similarity = (hash_size**2 - hd) / hash_size**2
            if similarity < 0.8:
                print('{} - {} - '.format(name, similarity))
                data['last'] = f_pack
                cv2.imwrite(os.path.join(f_dir, name), frame)
        else:
            data['last'] = f_pack
            cv2.imwrite(os.path.join(f_dir, name), frame)
    
    else:
        cv2.imwrite(os.path.join(f_dir, name), frame)

