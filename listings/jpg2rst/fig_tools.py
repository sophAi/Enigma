#!/usr/bin/env python
def resize(resolution,jpg_list):
    ''' Input the resolution referring to the maximal height and width of the resizing jpg files
    Return: resize_jpg_list (str list)
    Usage: resize_jpg(str/int/str_list resolution, str_list jpg_list)
    Example: resize_jpg(resolution=['640','800'],jpg_list=[])
    Resolution can be either integer, string, or a list of strings'''
    import subprocess, string, sys, os, shutil
    resize_jpg_list=list()
    if type(resolution).__name__ == 'int':
        resize_res_list=[str(resolution)]
    elif type(resolution).__name__ == 'str':
        resize_res_list=[resolution]
    elif type(resolution).__name__ == 'list':
        resize_res_list=resolution
       
    for resize_res in resize_res_list:
        if os.path.isdir(resize_res):
            print (resize_res+'/'+" directory exist! Cleaning it\n")
            shutil.rmtree(resize_res)
          
        print ("Making new directory: "+resize_res+'/ \n')
        os.mkdir(resize_res)
        for file_name in jpg_list:
            if file_name.find(resolution+'_') == -1:  #Detect existing resized jpg file
                resize_file_name=file_name.split('/')[0:-1]
                resize_file_name.append(resize_res+'/'+resize_res+'_'+file_name.split('/')[-1])
                resize_file_name = string.join(resize_file_name,'/')
                convert_command=['convert',file_name,'-colorspace','RGB','-filter','LanczosSharp','-distort','Resize',resize_res+'x'+resize_res,'-unsharp','1x0.55+1.5+0.002','-colorspace','sRGB','-border','10','-quality','95',resize_file_name]
                print(" ".join(convert_command)+"\n")
                cmd_status = subprocess.call(convert_command)
                if cmd_status != 0:                 
                    print('Subprocess.call failure! Exit now!\n')
                    sys.exit(1)

                resize_jpg_list.append(resize_file_name)


    resize_jpg_list.sort()
    return resize_jpg_list


def log(log_file,jpg_list):
    ''' Write a list of jpg file names to a log file
    Return: none
    Usage: fig_log(str log_file, str_list/str jpg_list)
    Example: fig_log(log_file='fig_list.log',jpg_list)'''
    import os
    log_file_obj = open(log_file,'w')
    if type(jpg_list).__name__ == 'str':
        file_list = [jpg_list]
    elif type(jpg_list).__name__ == 'list':
        file_list = jpg_list

    for file_name in file_list:
        log_file_obj.write(file_name+'\n')
     
    log_file_obj.close()
    print('Write log file to '+log_file+'\n')

def main():
    resize()

if __name__ == "__main__":
    main()

