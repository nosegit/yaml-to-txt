import yaml
import sys
import time

filepath = "C:/Users/nose/Desktop/New folder/reality/test/annotations.yaml"
savepath = "C:/Users/nose/Desktop/New folder/reality/test/test/"

def load_data():

    with open(filepath, "r") as stream:
        try:
            print("[STATUS] Loading data...")
            data = yaml.safe_load(stream)
            print("[STATUS] data loaded")
        except yaml.YAMLError as exc:
            print(exc)

    #print(f"[DEBUG] data size : {len(data)}")
    data = data['images']
    #print(f"[DEBUG] redata size: {len(data)}")

    data_list = []
    for key,value in data.items() :
          data_list.append([key ,value])
    #print(f"[DEBUG] data_list [0] : \n {data_list[0]}")
    return data_list        

def split_detect(data_in):
    ball = []
    robot = []
    goalpost = []
    img_width = data_in[1]['width']
    img_height = data_in[1]['height']
    print("[STATUS] spliting data...")
    img_name = data_in[0]
    #print(f"[DEBUG] image name : {img_name}")
    data_in = data_in[1]['annotations']
    #print(f"[DEBUG] detection list : {len(data_in)}")
    for detect_dict in data_in:
        if(detect_dict['in_image'] == True):
            if(detect_dict['type']=='robot'):
                robot.append(detect_dict['vector'])
            elif(detect_dict['type']=='goalpost'):
                goalpost.append(detect_dict['vector'])
            elif(detect_dict['type']=='ball'):
                ball.append(detect_dict['vector'])
    #print(f"[DEBUG] ball vector : {ball}")
    #print(f"[DEBUG] robot vector : {robot}")
    #print(f"[DEBUG] goalpost vector : {goalpost}")

    return [img_name,img_width,img_height],ball,robot,goalpost

def detect_to_string(img_prop,ind,detect_arr): # ind 0:ball 1:robot 2:goalpost
    #print(f"[DEBUG] Split detect pos to string...")
    string = ''
    for rect in detect_arr:
        if(ind != 2) :
            x_start = rect[0][0]
            y_start = rect[0][1]
            x_stop = rect[1][0]
            y_stop = rect[1][1]
        else :
            x_start = 9999
            x_stop = 0
            y_start = 9999
            y_stop = 0
            for x,y in rect :
                x_start = min(x_start,x)
                x_stop = max(x_stop,x)
                y_start = min(y_start,y)
                y_stop = max(y_stop,y)
        center_x = (x_stop+x_start)/2
        center_y = (y_stop+y_start)/2
        box_width = abs(x_stop-x_start)
        box_height = abs(y_stop-y_start)
        string += (f"{ind} {center_x/img_prop[1]} {center_y/img_prop[2]} {box_width/img_prop[1]} {box_height/img_prop[2]}\n")
    return string

def detect_pos_to_file(img_prop,ball,robot,goalpost):
    print(f"[STATUS] Writing file...")
    with open(savepath+img_prop[0][:-4]+".txt", 'w') as f:
        f.write(detect_to_string(img_prop,0,ball))
        f.write(detect_to_string(img_prop,1,robot))
        f.write(detect_to_string(img_prop,2,goalpost))
    print(f"[STATUS] Saved file...")
        
def run():
    data_list = load_data()
    for ind in range(len(data_list)):
        print(f"[STATUS] -------Converting {ind}/{len(data_list)}-------")
        img_prop,ball,robot,goalpost = split_detect(data_list[ind])
        detect_pos_to_file(img_prop,ball,robot,goalpost)

if __name__ == "__main__" :
    start_time = time.time()
    run()
    print(f"Time : {time.time()-start_time} Sec")
    print("==========done==========")
