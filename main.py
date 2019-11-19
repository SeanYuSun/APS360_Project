KT_PATH_BASE = r"E:\DropBoxNew\Dropbox\DropBox大四\APS360\Project\data_videos\from_drive\kt_labelled\kt_labelled"
TH_PATH_BASE = r"E:\DropBoxNew\Dropbox\DropBox大四\APS360\Project\data_videos\from_drive\th"

HU_TOKEN = 'head_up'
HN_TOKEN = 'head_normal'
HD_TOKEN = 'head_down'

THRESHOLD = 0.5

FACE_KP_FORMAT = [(8,8),(7,9),(6,10),(5,11),(4,12),
    (3,13),(2,14),(1,15),(0,16),(17,26),
    (18,25),(19,24),(20,23),(21,22),(50,52),
    (48,54),(58,56),(33,33),(31,35),(27,27),
    (28,28),(29,29),(30,30),(36,36),(37,37),
    (38,38),(39,39),(40,40),(68,68),(42,42),
    (43,43),(44,44),(45,45),(46,46),(47,47),
    (69,69) 
]

FACE_KP_FORMAT_SIMPLE = [
    (8,8),(6,10),(4,12),(2,14),(0,16),
    (18,25),(20,23),(50,52),(58,56),(33,33),
    (31,35),(28,28),(29,29),(30,30),(37,44),
    (41,46),(36,45),(39,42)
]

POSE_KP_FORMAT = [
    (0,0),(1,1),(2,2),(5,5),(15,15),
    (16,16),(17,17),(18,18)
]

import os
import json
import pickle

my_path_base = TH_PATH_BASE
my_path_hu = ''
my_path_hn = ''
my_path_hd = ''

def parse(my_kp, format):
    result = []
    index_set = set()
        
    for pair in format:
        index_set.add(pair[0])
        index_set.add(pair[1])
        x1,y1,c1 = my_kp[pair[0]*3:pair[0]*3+3]
        x2,y2,c2 = my_kp[pair[1]*3:pair[1]*3+3]
        
        if c1>THRESHOLD and c2>THRESHOLD:
            result.append((y1+y2)/2)
        elif c1>=c2:
            result.append(y1)
        else:
            result.append(y2)
    
    min_y = 99999
    min_y_c = 0
    max_y = -99999
    max_y_c = 0
    for i in range(len(my_kp)//3):
        if i not in index_set: continue
        if my_kp[i+1] > max_y:
            max_y = my_kp[i+1]
            max_y_c = my_kp[i+2]
        if my_kp[i+1] < min_y:
            min_y = my_kp[i+1]
            min_y_c = my_kp[i+2]
    
    if min_y_c < THRESHOLD or max_y_c < THRESHOLD:
        return None
    
    min_y = min(result)
    scale_max = max(result) - min(result)
    result = [(y-min_y)/scale_max for y in result]
    return result

for folder in os.listdir(my_path_base):
    if HU_TOKEN in folder:
        my_path_hu = os.path.join(my_path_base, folder)
    elif HN_TOKEN in folder:
        my_path_hn = os.path.join(my_path_base, folder)
    elif HD_TOKEN in folder:
        my_path_hd = os.path.join(my_path_base, folder)
        
if len(my_path_hu)+len(my_path_hd)+len(my_path_hn) == 0:
    print("Folder load error!!!")
    
'''
print(my_path_hu)
print(my_path_hn)
print(my_path_hd)
'''

total_json = 0
success = 0

for path in [my_path_hu, my_path_hn, my_path_hd]:
    parsed_path = path + '_parsed'
    os.mkdir(parsed_path)
    
    face_kp_result_list = list()
    face_kp_simple_result_list = list()
    pose_kp_result_list = list()
    
    for my_json in os.listdir(path):
        if not my_json.endswith('.json'):
            continue
        my_json_path = os.path.join(path, my_json)
        #total_json += 1
        with open(my_json_path) as json_file:
            data = json.load(json_file)
            face_kp = data['people'][0]['face_keypoints_2d']
            face_kp_result = parse(face_kp, FACE_KP_FORMAT)
            #if face_kp_result:
                #success += 1
            if face_kp_result:
                face_kp_result_list.append(face_kp_result)
                
            face_kp_simple_result = parse(face_kp, FACE_KP_FORMAT_SIMPLE)
            if face_kp_simple_result:
                face_kp_simple_result_list.append(face_kp_simple_result)
                
            pose_kp = data['people'][0]['pose_keypoints_2d']
            pose_kp_result = parse(pose_kp, POSE_KP_FORMAT)   
            if pose_kp_result:
                pose_kp_result_list.append(pose_kp_result)            
    
    f = open(os.path.join(parsed_path, 'face_kp.pkl'), 'wb')
    pickle.dump(face_kp_result_list, f, 0)
    
    f = open(os.path.join(parsed_path, 'face_kp_simple.pkl'), 'wb')
    pickle.dump(face_kp_simple_result_list, f, 0)
    
    f = open(os.path.join(parsed_path, 'pose_kp.pkl'), 'wb')
    pickle.dump(pose_kp_result_list, f)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        