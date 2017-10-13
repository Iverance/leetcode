import os
for filename in os.listdir("."):
    if filename[0] in '0123456789':
        if '.' in filename[:2]:
            #print('00'+filename)
            os.rename(filename, '00'+filename)
        elif '.' in filename[:3]:
            #print('0'+filename)
            os.rename(filename, '0'+filename)
