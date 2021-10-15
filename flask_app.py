#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############
    
from flask import Flask
from flask import render_template
from flaskext.markdown import Markdown

import markdown

import os  # used to serve specific port
from os import walk

## Specify the location of your folders
path_templates = '/Users/jonahbrown-joel/Library/Mobile Documents/com~apple~CloudDocs/Data_Science_Blog/Blog_App/templates/'
path_static = '/Users/jonahbrown-joel/Library/Mobile Documents/com~apple~CloudDocs/Data_Science_Blog/Blog_App/static/'
path_blog_content = '/Users/jonahbrown-joel/Library/Mobile Documents/com~apple~CloudDocs/Data_Science_Blog/Blog_Content/'
###############################################################################

# Grab a list of folders in the /Blog_Content/ folder
content_folders = os.listdir(path_blog_content)
content_folders.remove('.DS_Store')  # remove '.DS_Store' from the list, and watch this for other funny stuff being added
sorted_folders = sorted(content_folders)
    # TODO - Consider Dropping the prefix

# Create a dictionary with the name of each folder and a list of the files in that folder
folder_contents = {}
for folder in sorted_folders:
    path = path_blog_content + folder + '/'
    # path_filenames = glob.glob(path+"*.md")  # get all the markdown files from the folder
    # path_filenames.replace(path)
    # remove the path
    filenames = next(walk(path), (None, None, []))[2]  # get a list of the filenames in the folder 
    
    # Sometime '.DS_Store' shows up in the list. if so, then remove it
    try:
        filenames.remove('.DS_Store')
    except:
        None
    folder_contents[folder] = filenames  # add the folder name and its filenames to the dictionary

# 'content_list' will contain a dictionary within a dictionary 
# for each folder and dictionary for the folder containing the name of the file and it's contents   
# you can get the contents with 'content_list[folder][f]'    
content_list = {}
for folder, files in folder_contents.items():
    # create a dictionary of the contents with the filename and the file contents
    file_text = {}
    for f in files:
        file_path = path_blog_content + folder + '/' + f  # construct a path
        file = open(file_path, 'r')                       # get the .md content
        file_contents = file.read()
        mkd_string = markdown.markdown(file_contents, extensions=['fenced_code', 'codehilite'] )  # convert to markdown
        file_text[f] = mkd_string                                              # save the file name and contents in a dict

    content_list[folder] = file_text                                           # save the topic and it's filename/contents combo dict as a dict
    
# Get a list of the folders
ls_folders = list(content_list.keys())

# Get a list of the files contained in a particular folder 
folder_name = 'A_Home'                              # specify a folder
ls_files_in_a_folder = content_list[folder_name].keys()

# get the html contents from the a given folder name file name combo 
md_file_name = 'Thougts.md'
content_list[folder_name][md_file_name]  
 
# get the html contents for the first file for a topic

# returns a dict with info needed to display data if user clicks on homescreen:
# the sorted_folder_list, first_folder_name, files_in_first_folder, first_filename_first_folder, and  first_file_html_contents
def home_screen_filters(content_list):
 
    ls_folders = list(content_list.keys())  # get a list of all the folders
    first_folder_name = ls_folders[0]       # get the first folder name
    
    # Get a list of the files contained in the first folder 
    files_in_first_folder   = list(content_list[first_folder_name].keys() ) 
    first_filename_first_folder = files_in_first_folder[0]
    
    # get the HTML contents for the first first file in the first folder
    first_file_html_contents = content_list[first_folder_name][first_filename_first_folder] 
    
    return_dict = {  'sorted_folder_list'          : ls_folders                  # a sorted list of folders
                   , 'first_folder_name'           : first_folder_name           # the name of the first folder
                   , 'files_in_first_folder'       : files_in_first_folder       # a list of the files contained in the first folder
                   , 'first_filename_first_folder' : first_filename_first_folder # the filename for the first file in the first folder
                   , 'first_file_html_contents'    : first_file_html_contents    # the html contents for the first file in the first folder
        }
    
    # return the html contents for the first file in the first folder
    return(return_dict) 

# selected_folder_name = 'A_Home'      
def selected_folder_filters(content_list, selected_folder_name):
 
    # get a list of all the folders (for header)
    ls_folders = list(content_list.keys())  
    #first_folder_name = ls_folders[0]       # get the first folder name
    
    # Get a list of the files contained in the selected folder (for sidebar)                      
    files_in_selected_folder = list(content_list[selected_folder_name].keys())
    
    # get the first filename in the selected folder     
    first_filename_selected_folder = files_in_selected_folder[0]
    
    # get the HTML contents for the first first file in the selected folder
    first_file_html_contents = content_list[selected_folder_name][first_filename_selected_folder] 
    
    return_dict = {  'sorted_folder_list'          : ls_folders                  # a sorted list of folders
                   , 'selected_folder_name'        : selected_folder_name        # the name of the selected folder
                   , 'files_in_selected_folder'    : files_in_selected_folder    # a list of the files contained in the selected folder
                   , 'first_filename_selected_folder' : first_filename_selected_folder  # the filename for the first file in the selected folder
                   , 'first_file_html_contents'    : first_file_html_contents    # the html contents for the first file in the selected folder
        }
    
    # return the html contents for the first file in the first folder
    return(return_dict) 



app = Flask(__name__
          , template_folder = path_templates)
Markdown(app)  # construct a 'Markdown' so that you can use markdown


@app.route('/test')  # This is the home page
def test_page():
    return render_template('zz_Test_page.html'
                         , mkd_text = mkd_string)

    
@app.route('/')  # This is the home page
def home_page():
    
    # run the filters
    home_screen_dict = home_screen_filters(content_list)
    
    # grab the data elements out of the filter
    sorted_folder_list          = home_screen_dict['sorted_folder_list']
    first_folder_name           = home_screen_dict['first_folder_name']
    files_in_first_folder       = home_screen_dict['files_in_first_folder']
    first_filename_first_folder = home_screen_dict['first_filename_first_folder']
    first_file_html_contents    = home_screen_dict['first_file_html_contents']
    
    
    return render_template('C_main_content.html'
                         , Header_Topics = sorted_folder_list
                         , Sidebar_Files = files_in_first_folder  # used to display sidebar files
                         , topic         = first_folder_name
                         , mkd_text      = first_file_html_contents)

@app.route('/<url_topic>.html')  # This is the home page
def topic_selected(url_topic):
    topic = url_topic

    # run the filters to create a dict
    folder_selected_dict = selected_folder_filters(content_list = content_list, selected_folder_name = topic)
    
    # grab the data elements out of the filter dict
    sorted_folder_list             = folder_selected_dict['sorted_folder_list']
    selected_folder_name           = folder_selected_dict['selected_folder_name']
    files_in_selected_folder       = folder_selected_dict['files_in_selected_folder']
    first_filename_selected_folder = folder_selected_dict['first_filename_selected_folder']
    first_file_html_contents       = folder_selected_dict['first_file_html_contents']

    # use the data elements to render the page

#    if topic == 'A - Home':     # if the home url is entered...
#        topic = ''              # null it out and send 
    # filter the 'folder_contents' dictionary using the url that the user entered
    # and save the list of files in that folder
#    files_in_topic = folder_contents[topic]  # filter the folders to the specific one in the url
    
    return render_template('C_main_content.html'     
                         , Header_Topics = sorted_folder_list  # uaws to disply hEADER
                         , Sidebar_Files = files_in_selected_folder  # used to display sidebar files
                         , topic         = topic
                         , mkd_text      = first_file_html_contents)          # used to 


@app.route('/<url_topic>/<url_page>.html')  # This is the home page
def page_selected(url_topic, url_page):
    topic = url_topic
    page = url_page
    #url_topic = 'B_Import%20Export/B_Import%20Export/'
#    if topic.count('/') == 2:  # if the url appears twice... cut out the first half
#        index = topic.find('/')
#        topic = url_topic[index + 1:]
    

    
 #   if topic == 'A_Home':     # if the home url is entered...
 #       topic = ''              # null it out and send 
    
    # filter the 'folder_contents' dictionary using the url that the user entered
    # and save the list of files in that folder
    files_in_topic = folder_contents[topic]  # filter the folders to the specific one in the url
    
    # get the page content - filter a list of pages within the topic to the one they searched for in the url
    mkd_string =  content_list[topic][page]   
    
    
    return render_template('C_main_content.html'     
                         , Header_Topics = sorted_folders  # uaws to disply hEADER
                         , Sidebar_Files = files_in_topic  # used to display sidebar files
                         , topic         = topic
                         , mkd_text      = mkd_string)          # used to 


if __name__ == "__main__":
    # app.run(debug=True)  # change to this when you deploy
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))





