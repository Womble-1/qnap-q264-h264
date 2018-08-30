#Converts the qnap format to h264 from q264
#All credit to Yogesh: https://blog.catprosystems.com/2014/10/qnap-surveillance-station-recording-q264-to-h264/   

import os

# The top argument for walk
topdir = '/path/to/files/'
# The extension to search for
exten = '.avi'
 
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            #print what we find
            print(os.path.join(dirpath, name))
            # Save to results string instead of printing
            f=open(os.path.join(dirpath, name),"r+")
            f.seek(0x70)
            f.write('h264')
            f.seek(0xBC)
            f.write('h264')
            f.close()
print("Finished")
