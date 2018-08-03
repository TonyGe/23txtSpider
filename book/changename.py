# -*- coding: utf-8 -*-
import os
path = './data/'

total_file = open('all.md','w')
result = [(i, os.stat(path+i).st_mtime) for i in os.listdir(path)]
i = 1
for file_info in sorted(result, key=lambda x: x[1]):
    file = file_info[0]
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.')<0:
            newname=file+'.txt'            
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file,'ok'
        if file.find('正文_')>=0:
            newname=file.replace('正文_','')
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file,'ok'
        if file.find('-')<0:
            newname=str(i)+'-'+file           
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print newname,'ok'
            i+=1
    with open(os.path.join(path,file)) as inputfile:
    	title=file.split('-')[1].replace('.txt','')
    	txt=inputfile.read().replace('\n','\n\n')
    	total_file.write('##'+title+'\n\n')
    	total_file.write(txt)
