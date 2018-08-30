#Converts the qnap format to h264 from q264
#All credit to Yogesh: https://blog.catprosystems.com/2014/10/qnap-surveillance-station-recording-q264-to-h264/   

import os
import sys

# Get the total number of args passed to the demo.py
total = len(sys.argv)

# return the instructions if there are no arguments present
if (0 == total):
    print "No prarameters specificed, please use the following paramerters:-"
    print "    python q264toh264.py [path to process e.g. /Users/username/Documents/Videos/folder/] [extension to process e.g. .avi (optional) default is .avi] [Use -Y to proceed without any checks or messages]"
  
else:
	# Get the arguments list
	# print (str(sys.argv[1]))

	# The top argument for walk
	# topdir = '/path/to/files/'
	topdir= str(sys.argv[1])
	
	# If the 2nd parameter is not -Y, then use it as the extension
	if (total >2 ) and (('-Y' != str(sys.argv[2]).upper())):	
            exten = sys.argv[2]
            
	else:
            exten = '.avi'


        #Messages to the user
	print ("\nDir to process: %s " % topdir)
	print ("extensions to process: %s " % exten)
	print ("\n")


        #Count the number of files and let the user know how many files are going to be changed as a final check
        count = 0
        try: 
            for dirpath, dirnames, files in os.walk(topdir):
                for name in files:
                    if name.lower().endswith(exten):
                        #print what we find
                        print(os.path.join(dirpath, name))
                        count += 1
            print "There are %0.0f files that will be modified (listed above) are you sure you have set the right directory" % count
        except:
            print("Unexpected error: Please check directory names", sys.exc_info()[0])
            print str(count)



        ## do a check to see if the parameter -Y has been included to bypass checks        
        Yparamset = False
        for param in sys.argv:
            if ('-Y' == str(param).upper()):
                Yparamset  = True

        if Yparamset:
            finalcheck = 'Y'
        else:
            finalcheck = raw_input("Are you sure you want to process this directory? ")
        
	
	if ('Y' == finalcheck.upper()):
            try: 
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
            except:
                print("Unexpected error: Please check directory names", sys.exc_info()[0])
	    
print("Finished")
