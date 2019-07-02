import os

currentpath = './'
outputdir = currentpath + 'batchresult'
if not os.path.exists(outputdir):
    os.mkdir(outputdir)
filenamelist = os.listdir(currentpath)
print(filenamelist)
for filename in filenamelist:
    inputpath = currentpath + filename
    if os.path.isfile(inputpath):
        if filename.lower().endswith('.mp4'):
            filename = filename.replace(' ', '\\ ') # safe spaces
            inputpath = currentpath + filename
            outputpath = "{}/{}".format(outputdir, filename)
            commad = "ffmpeg -i {} -crf 23 {}".format(inputpath, outputpath)
            print(commad)
            os.system(commad)
                
