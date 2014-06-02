#!/usr/bin/env python
def search(keyword='.jpg',recursive='n'):
    ''' Search for the files (default=.jpg) in the current or the subdirectories and return a list of the full paths.
    return: file_list (str list)
    usage: search_file(str keyword,str recursive)
    example: search_file(keyword='*.jpg',recursive='y')
    recursive: 'y'   # turn on the recursive searching in the subdirectories'''
    import os
    from fnmatch import fnmatch
    file_list = list()
    if recursive == 'y': 
        for root, dirs, files in os.walk('.'):
            for file_name in files:
                if fnmatch(os.path.join(root,
                    file_name).lower().lstrip('./'),keyword.lower()):
                    file_list.append(os.path.join(root,file_name).lstrip('./'))  #Using walk, the file name would start with './dir/file.dat'. Use lstrip('./') to remove the string. 



    else:
        for file_name in os.listdir('.'):
            if fnmatch(file_name.lower().lstrip('./'),keyword.lower()):
                file_list.append(file_name)


    file_list.sort()
    return file_list

def clear(file_list):
    ''' Delete the files by the file_list. Use search() first to determine the file_list'''
    import os
    if type(file_list).__name__ == 'str':
        print('Delete '+file_list)
        os.remove(file_list)
    elif tpye(file_list).__name__ == 'list':
        for file_name in file_list:
            print('Delete '+file_name)
            os.remove(file_name)
   

def copy(file_list,destinate_list='.'):
    ''' Copy the files listed in the file_list to the destinate_list. Use search() first to
    determine the file_list. 
    destinate_list may be a string(dir_path) or a list of full paths
    To copy the file to the current directory, specify '.' as the destinate_list'''
    import shutil, os, sys
    file_type = type(file_list).__name__
    file_len = len(file_list)
    destinate_type = type(destinate_list).__name__
    destinate_len = len(destinate_list)
    if file_list != destinate_list:
        if file_type == 'list' and destinate_type == 'list' and file_len == destinate_len:
            I0=0
            for file_name in file_list:
                print('Copy '+file_name+' to '+destinate_list[I0])
                shutil.copy(file_name,destinate_list[I0])  
                I0=I0+1
      
        elif file_type == 'list' and destinate_type == 'str' and os.path.isdir(destinate_list):
# A list of files copied to a directory
           for file_name in file_list:
                print('Copy '+file_name+' to '+destinate_list)
                shutil.copy(file_name,destinate_list)

        elif file_type == 'str' and destinate_type == 'str':
# Copy one file
            shutil.copy(file_list,destinate_list)  
        elif file_type == 'str' and destinate_type == 'list':
            multi_target_opt = raw_input("Copy one file to multiple targets. Are you sure? (y/n)\n")
            if multi_target_opt == 'y':
                for target_file_name in destinate_list:
                    print ('Copy '+ file_list+' to '+target_file_name)
                    shutil.copy(file_list,target_file_name)

        else:
            print ("Error occurs!Exit!")
            sys.exit(1)


def move(file_list,destinate_list='.'):
    ''' Move the files listed in the file_list to the destinate_list. Use searh() to determine
    the file_list'''
    print ('Copying files...')
    copy(file_list,destinate_list)
    remove_opt = raw_input('Delete the source files?(y/n)\n')
    if remove_opt == 'y':
        print('Deleting files...')
        clear(file_list)

    print('Moving files complete!')


def main():
     search()

if __name__ == "__main__":
    main()

