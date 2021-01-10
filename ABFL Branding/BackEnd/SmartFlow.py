#this file needs a little house keeping
from tokenizer import *
import sys
sys.path.append('../')
from gsuitutil.gdocs import gdocs
from gsuitutil.gsheet import gsheet
from mailutil.sendmail import sendmail
from AIUtil import find_fn
import os
from pickle import load as pload
import re

#global variables to share data between smart_exec and it's helper funstions
global doc_content, nodes, edges, writefile, clf

#loading the ML model(s)
model_name = 'finalized_model.sav'
model_path = os.path.join('AI Models', model_name)
clf = pload(open(model_path, 'rb'))

#used to generate preview for smart previw option
def smart_preview(data):
    #output file
    writefile = open("generated_smart_preview.txt", "wt")  

    #nodes: {node_index=[ [inside_text], [shape]]}
    nodes = data['nodes']
    #edges: {node_index=[ [adjecency_list], [relation_to_each_node_on_the_adjecency_list]]}
    edges = data['edges']

    #output to file and print with indentation
    def to_file(ip_str):
        writefile.write(ip_str)
        writefile.write('\n')

    #list of docs/spreadsheet links 
    swimlanes = []

    #search for swimalane shapes that contain links inside them
    for key, value in nodes.items():
        if value[1] == "swimlane":
            link = nodes[key][0]
            if link.find('/') < 0:
                to_file('ERROR: \''+link+'\' is not a link')
                to_file('')
                continue

            swimlanes+=[key]
    
    #check if we found any suitable swimalane shape
    if len(swimlanes) == 0:
        to_file('No swimlane shapes found')
        return
    
    #generating options for each link that is in a swimlane shape
    count_links=0
    for node in swimlanes:
        link = nodes[node][0]
        #extract document type and id
        doc_type = link.split('/')[3]
        doc_id = link.split('/')[5]

        if doc_type=='spreadsheets':
            count_links+=1
            to_file(str(count_links)+'.')
            to_file(doc_id+' is a spreadsheet.')
            to_file('Available columns:')
            #making an API call to get the data in the spreadsheet
            doc_content = gsheet(doc_id,'Sheet1')
            for column_name in doc_content[0]:
                to_file('  '+column_name)


        elif doc_type=='document':
            count_links+=1
            to_file(str(count_links)+'.')
            to_file(doc_id+' is a document.')
            #making an API call to get the data in the documnet
            doc_content = gdocs(doc_id)
            to_file( str(len(doc_content[0].split())) + ' word title.')
            to_file( str(len(doc_content[1].split())) + ' word body.')
        
        to_file('')    

    #closing generated_smart_preview.txt
    writefile.close()

def smart_exec(data):
    #for sharing variables w helper functions
    global doc_content, nodes, edges, writefile

    #output file
    writefile = open("generated_smart_output.txt", "wt")  

    #nodes: {node_index=[ [inside_text], [shape]]}
    nodes = data['nodes']
    #edges: {node_index=[ [adjecency_list], [relation_to_each_node_on_the_adjecency_list]]}
    edges = data['edges']

    #output to file and print with indentation
    def to_file(ip_str):
        writefile.write(ip_str)
        writefile.write('\n')

    #list of docs/spreadsheet links 
    swimlanes = []

    #search for swimalane shapes that contain links inside them
    for key, value in nodes.items():
        if value[1] == "swimlane":
            link = nodes[key][0]
            if link.find('/') < 0:
                to_file('ERROR: \''+link+'\' is not a link')
                continue

            swimlanes+=[key]
    
    #check if we found any suitable swimalane shape
    if len(swimlanes) == 0:
        to_file('No swimlane shapes found')
        return
    
    for node in swimlanes:
        link = nodes[node][0]
        #extract document type and id
        doc_type = link.split('/')[3]
        doc_id = link.split('/')[5]

        if doc_type=='spreadsheets':
            doc_content = gsheet(doc_id,'Sheet1')
            doc_content[0] = list(map(str.lower, doc_content[0]))
            #traversing all adjecent nodes to the swimlane
            adjacent_nodes_spredsheet(node)


        elif doc_type=='document':
            doc_content = gdocs(doc_id)
            #traversing all adjecent nodes to the swimlane
            adjacent_nodes_document(node)

    #closing generated_smart_output.txt
    writefile.close()

def adjacent_nodes_spredsheet(node):

    global doc_content, nodes, edges, writefile, clf    

    if not node in edges.keys():
        return

    for n in edges[node][0]:
        instruction = nodes[n][0]
        writefile.write(instruction+': ')
        #finding the column the user is refering to
        target_column = list(set(instruction.lower().split()).intersection(set(doc_content[0])))

        #if no target column is found
        if len(target_column)==0:
            writefile.write('No target columns found'+'\n')
            continue
        else:
            target_column = target_column[0]

        #using the ML model to find out which function is the user refering to
        y = find_fn(clf, instruction)
        
        #executing the function according to the ML model
        target_column = doc_content[0].index(target_column)
        if y==0: #SUM
            ans = 0
            for i in range(len(doc_content)-1):
                ans+=int(doc_content[i+1][target_column])
            writefile.write(str(ans)+'\n')
        elif y==1: #AVERAGE
            ans = 0
            for i in range(len(doc_content)-1):
                ans+=int(doc_content[i+1][target_column])
            ans = float(ans/int(len(doc_content)-1))
            writefile.write(str(ans)+'\n')
        elif y==2: #SORT
            ans = []
            for i in range(len(doc_content)-1):
                ans+=[int(doc_content[i+1][target_column])]

            if 'descending' in instruction.lower() or 'reverse' in instruction.lower():
                ans = sorted(ans, reverse=True)
            else:
                ans = sorted(ans)

            writefile.write(str(ans)+'\n')
                    
        

def adjacent_nodes_document(node):

    global doc_content, nodes, edges, writefile, clf

    if not node in edges.keys():
        return

    for n in edges[node][0]:
        instruction = nodes[n][0]
        writefile.write(instruction+': ')
        if 'mail' in instruction.lower() or 'send' in instruction.lower():
            mail_ids = re.findall('\S+@\S+',instruction)
            
        if len(mail_ids) == 0:
            writefile.write('no mail ids found' + '\n')
            return
        
        for _id in mail_ids:
            sendmail(_id, doc_content[0], doc_content[1])
        
        writefile.write('mailed document as mail to ' + str(mail_ids) + '\n')