#!/usr/bin/env python
def add_fig(fig_list):
    '''Form a template file in reST format and add the codes with the resized figures
    return rst_file (str), fig_num (int)
    usage: form_rst(str_list fig_list)
    example: form_rst(['fig1.jpg','fig2.jpg',...])'''
    import os
    import time
    from fnmatch import fnmatch
    time_label = time.strftime('%Y%m%d %H:%M:%S',time.localtime())
    try:
        rst_temp_file_obj = open('/'+os.getcwd().split('/')[1]+'/'+os.getcwd().split('/')[2]+'/.vim/template/temp_rst.txt','r')
        rst_slug = os.getcwd().split('/')[-1]
        rst_file = rst_slug+'.rst'
        jpg2rst_temp_file_obj = open(rst_file,'w')
        line_info = rst_temp_file_obj.readline()
        while line_info != '.\n':
            line_info = rst_temp_file_obj.readline()
            if fnmatch(line_info,'*slug:*'):
                jpg2rst_temp_file_obj.write('.. slug: '+rst_slug+'\n')
            elif fnmatch(line_info,'*data:*'):
                jpg2rst_temp_file_obj.write('.. data: '+time_label+'\n')
            elif fnmatch(line_info,'*description:*'):
                jpg2rst_temp_file_obj.write('.. description: Created at '+time_label+'\n')
            elif fnmatch(line_info,'*<body>*'):
                #Insert codes of resized figure here       
                jpg2rst_temp_file_obj.write(line_info)
                fig_number = len(fig_list)
                for rst_figure in fig_list:
                    jpg2rst_temp_file_obj.write('\n.. figure:: '+rst_figure+'\n')
                    jpg2rst_temp_file_obj.write('   :target: '+rst_figure+'\n')
                    jpg2rst_temp_file_obj.write('   :align: center\n\n\n\n')
#                    jpg2rst_temp_file_obj.write('   :width: 640'+'\n\n')

            elif line_info == '.\n':
                print('\nMake '+rst_file+' complete\n')
            else:
                jpg2rst_temp_file_obj.write(line_info)


    finally:
        jpg2rst_temp_file_obj.close()
        rst_temp_file_obj.close()
        return rst_file


def main():
     add_fig()

if __name__ == "__main__":
    main()


