#!/usr/bin/env python
# =======================================================================
# File Name     : jpg2rst.py
# Creation Time : 20130629 23:45:54
# Last Modified : 20130717 09:57:01
# =======================================================================
# Copyright (c),2012-, Po-Jen Hsu. Contact: clusterga@gmail.com
# This software is distributed under the GNU General Public License.
# See the README file in the top-level directory.
# =======================================================================

def main():
    ''' Resize and sharpen jpg files. Then, generate the codes with figures to an rst file'''
    import file_tools as file_mod
    import rst_tools as rst_mod
    import fig_tools as fig_mod
    import os, subprocess

#   Determine the fig_path for figures within the inner sub-directories

    root_dir = 'arch_2013'

    file_dir = 'files'

    sub_dir_path = os.getcwd()[os.getcwd().find(file_dir)+len(file_dir.strip('/'))+1:]

    sub_dir_num = len(sub_dir_path.split('/'))

    fig_path = sub_dir_num*'../'+root_dir.strip('/')+'/'+sub_dir_path

    resolution_opt=raw_input("Please input the maximal resolution of height and width (ex: 640, or none to skip resize procedure):\n")

    recursive_opt = 'n'
    for file_name in os.listdir('.'):
        if os.path.isdir(file_name) and file_name != resolution_opt: # Avoid duplicating resized figures
            recursive_opt=raw_input("Would you like to apply to all the subdirectories (y/n)?\n")
            break


    fig_path_opt=raw_input("Use the default path: "+fig_path+" (y/n)?\n")

    if fig_path_opt == 'n':
        fig_path=raw_input("Please input the path of figures (ex: ../gallaries/):\n")


    if fig_path[-1] != '/':
      fig_path = "".join([fig_path,'/'])

    file_list=file_mod.search(keyword='*.jpg',recursive=recursive_opt)

#    fig_mod.log(log_file='fig_list.log',jpg_list=file_list)

    rst_jpg_list = list()
    if resolution_opt == 'none':
        for jpg_file_name in file_list:
            rst_jpg_list.append(fig_path+jpg_file_name)

    else:
        resize_jpg_list=fig_mod.resize(resolution=resolution_opt,jpg_list=file_list)
        for jpg_file_name in resize_jpg_list:
            rst_jpg_list.append(fig_path+jpg_file_name)


    rst_file=rst_mod.add_fig(fig_list=rst_jpg_list)

if __name__ == '__main__':
    main()

