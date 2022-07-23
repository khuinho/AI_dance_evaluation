# input shape: {frame: mediapipe.framework.formats.landmark_pb2.NormalizedLandmarkList}
# output shape: {frame:{join_num:[x,y,z]}}

def pick_xyz_from_mediapipe_landmark(landmarks):
    result = {}
    for frame in landmarks:
        joint = 0
        value = {}
        value_list = []
        for cnt, i in enumerate(str(landmarks[frame])):
            try:
                if i == 'x':
                    value_list.append((str(landmarks[frame])[cnt+3: cnt+10]))
                elif i == 'y':
                    value_list.append((str(landmarks[frame])[cnt+3: cnt+10]))
                elif i == 'z':
                    value_list.append((str(landmarks[frame])[cnt+3: cnt+10]))
                    
                    if len(value_list) == 4:
                        del value_list[0]
                    value[joint] = value_list

                    value_list = []

                    joint +=1

            except:
                print('error')

        result[frame] = value
    
    return result

