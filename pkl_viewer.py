import pickle

pickle_path = r"th\th_head_down_parsed\face_kp_simple.pkl"

with open(pickle_path, 'rb') as f:
    my_list = pickle.load(f)

print(len(my_list))