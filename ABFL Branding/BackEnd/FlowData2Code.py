#this file needs a little house keeping
from tokenizer import *

def create_code(data):
    start = ['start', 'begin']
    stop = ['stop', 'end']

    #output file
    writefile = open("generated_py.txt", "wt")  

    #nodes: {node_index=[ [inside_text], [shape]]}
    nodes = data['nodes']
    #edges: {node_index=[ [adjecency_list], [relation_to_each_node_on_the_adjecency_list]]}
    edges = data['edges']
    #in_edges: {node_index=[ [list_of_all_incoming_edges], [relation_for_every_incoming_edge]]}
    in_edges = data['in_edges']

    #output to file and print with indentation
    def to_file(ip_str):
        global tab_counter

        op_str = tab_counter*'\t'+ip_str
            
        writefile.write(op_str)
        writefile.write('\n')
        #print(op_str)

    #ellipse
    def ellipse( n, label):

        x = nodes[n]

        #START keyword for main 
        if x[0].lower() in start:
            op_str = "#main\nif __name__==\"__main__\":"
            to_file(op_str)
        
        #SUB keyword for sub_routines
        elif x[0].split()[0].lower() == 'sub':
            op_str = f"def {x[0].split()[1]}("
            for arg in x[0].split()[2:]:
                op_str+=f"{arg},"
            op_str+="):"
            to_file(op_str)

        #STOP keyword
        elif x[0].lower() in stop:
            op_str = "#STOP\n"
            to_file(op_str)

        #FUTURE expansion
        else:
            #print(f"description for {x[0]} with shape {x[1]} not found. Node number: {n}")
            pass

    #rectangle  
    def rectangle( n, label):

        x = nodes[n]

        #INPUT keyword
        if "input" in x[0].lower().split(' '):
            for i in tokenize(nodes[n])[1:]:
                if i.split()[1] != "none":
                    op_str = f"{i.split()[0]} = {i.split()[1]}(input())"
                else:
                    op_str = f"{i.split()[0]} = input()"

                to_file(op_str)
        
        #print keyword
        elif "print" in x[0].lower().split(' '):
            op_str = f"print("
            for i in tokenize(nodes[n])[1:]:
                op_str += f'{i},'
            op_str+=')'
            to_file(op_str)

        #RECTANGLE without any keyword
        else:
            op_str = f"{x[0]}"
            to_file(op_str)
        
    #rhombus
    def rhombus( n, label, curr_index):

        x = nodes[n]
        
        label = True if label.lower()=="yes" else False if label.lower()=="no" else label

        #RHOMBUS if/elif/else case
        if len(in_edges[n][0])==1:
            if curr_index==0 and label!="else" and label!="":
                op_str = f"if ({x[0]})==({label}):"
                to_file(op_str)
            elif curr_index>=1 and label!="else" and label!="":
                op_str = f"elif ({x[0]})==({label}):"
                to_file(op_str)
            elif label=="else":
                op_str = f"else:"
                to_file(op_str)
            else:
                pass

        #For loops
        elif len(x[0].split(','))==4 and len(in_edges[n][0])>1:
            for_params = x[0].split(',')
            op_str = f"for {for_params[0]} in range({for_params[1]},{for_params[2]},{for_params[3]}):"
            to_file(op_str)

        #custom For loops
        elif 'for' == x[0].split(' ')[0] and len(in_edges[n][0])>1:
            op_str = f"{x[0]}:"
            to_file(op_str)

        #Whileloops
        elif len(in_edges[n][0])>1:
            op_str = f"while {x[0]}:"
            to_file(op_str)
        
        #FUTURE expansion
        else:
            #print(f"description for {x[0]} with shape {x[1]} not found. Node number: {n}")
            pass

    #swimlane
    def swimlane( n, label):
        global importlib
        x = nodes[n]

        #GSHEET keyword
        if x[0].split(" ")[0] == 'GSHEET':
            data_ = x[0].split(' ')
            op_str = f"{data_[3]} = gsheet({data_[1]},{data_[2]})"
            importlib += 'from gsuitutil.gsheet import gsheet' + '\n'
            to_file(op_str)
        #GDOC keyword
        elif x[0].split(" ")[0] == 'GDOCS':
            data_ = x[0].split(' ')
            if len(data_)==4:
                op_str = f"{data_[3]} = gdocs({data_[1]},{data_[2]})"
            elif len(data_)==3:
                op_str = f"{data_[2]} = gdocs({data_[1]})"
            else:
                op_str = "ERROR DEFINING GDOC"
            importlib += 'from gsuitutil.gdocs import gdocs' + '\n'
            to_file(op_str)
        #MAIL keyword
        elif x[0].split(" ")[0] == 'MAIL':
            data_ = x[0].split(' ')
            op_str = f"sendmail({data_[1]},{data_[2]},{data_[3]})"
            importlib += 'from mailutil.sendmail import sendmail' + '\n'
            to_file(op_str)
        else:
            to_file(x[0])

    #cloud
    def cloud( n, label):
        x = nodes[n]
        op_str = f"\"\"\"{x[0]}\"\"\""
        to_file(op_str)

    #node data to python3 code conversion
    def code( n, label, curr_index):
        
        global tab_counter

        #x = [text], [shape]
        x = nodes[n]

        #ellipse
        if x[1] == "ellipse":
            ellipse(n,label)
        
        #rectangle
        elif x[1] == "rectangle":
            rectangle(n,label)

        #rhombus
        elif x[1] == "rhombus":
            rhombus( n, label, curr_index)

        #swimline
        elif x[1] == "swimlane":
            swimlane( n, label)

        #cloud
        elif x[1] == "cloud":
            cloud( n, label)
        
        #FUTURE expansion
        else:
            #print(f"description for {x[0]} with shape {x[1]} not found. Node number: {n}")
            pass


    #traversing
    def dfs_root(n):

        global tab_counter

        #return if it's the "STOP" node
        if n in stop_nodes:
            return 0

        #mark current node as visited
        visited[n] = 1

        for i,x in enumerate(edges[n][0]):

            #anything except LOOPS and IFs
            #checking if x has been visited. If not do dfs on it.
            if visited[x]==0 and nodes[x][1] != "rhombus":
                code( x, edges[n][1][i], i)
                dfs_root(x)
            
            #only loops and ifs
            elif visited[x]==0 and nodes[x][1] == "rhombus":
                dfs_rhombus(x)



    def dfs_rhombus(n):

        global tab_counter

        #return if it's the "STOP" node
        if n in stop_nodes:
            code(n,"", -1)
            return 0

        #for "leaf" nodes which are not "STOP" nodes
        if edges[n]==[[],[]]:
            code(n,"", -1)
            return 0

        #mark current node as visited
        visited[n] = 1
        
        for i,x in enumerate(edges[n][0]):
            
            #doing tab reduction when a loop back if found (done for all kind of loops)
            if visited[x]==1 and nodes[x][1] == 'rhombus':
                code(n,"", i)
            
            #checking for loops that have been executed ones and getting out of the loop
            elif nodes[n][1] == 'rhombus' and visited[x]==0 and len(in_edges[n][0])>1 and i>0:
                dfs_rhombus(x)

            #Making sure that that "no lebel" is not in scope of if
            elif nodes[n][1] == 'rhombus' and visited[x]==0 and len(in_edges[n][0])==1 and not edges[n][1][i]:
                dfs_rhombus(x)

            #seperated rhombus and rhombus for tab_counter
            #checking if x has been visited before if not then dfs on it
            elif nodes[n][1] == 'rhombus' and visited[x]==0:
                code( n, edges[n][1][i], i)
                tab_counter+=1
                dfs_rhombus(x)
                tab_counter-=1

            #anything that's not a rhombus
            elif visited[x]==0:
                code( n, edges[n][1][i], i)
                dfs_rhombus(x)

    #index of ellipse node containing "START" keyword
    start_node = -1

    #index of ellipse nodes containing "SUB" keyword
    sub_routine_start_nodes = []

    #storing all stop nodes' index
    global stop_nodes
    stop_nodes = []

    #visited nodes during DFS
    global visited
    visited = {i:0 for i in nodes.keys()}

    #tab count for indentation
    global tab_counter
    tab_counter = 0

    #list storing all required packages for the program to execute
    global importlib
    importlib = ''

    #search for root node
    for key, value in nodes.items():

        if value[1] == "ellipse":
            #looking for __main__ start node
            if value[0].lower() in start:
                start_node = key
            #looking for all stop nodes
            elif value[0].lower() in stop:
                stop_nodes += [key]
            #looking for all sub start nodes
            elif value[0].split(' ')[0] == "sub":
                sub_routine_start_nodes += [key]
        #looking for all leaf nodes
        if key not in edges.keys():
            edges[key] = [[],[]]

    # DEBUGING SWITCH
    #start_node = -1

    #DFS for sub routines
    for sub_routine_start_node in sub_routine_start_nodes:
        code( sub_routine_start_node, "", 0)
        tab_counter+=1
        dfs_root(sub_routine_start_node)
        tab_counter-=1

    #DFS for __main__
    if start_node != -1:
        code(start_node,"", 0)
        tab_counter+=1
        dfs_root(start_node)
        tab_counter-=1
    else:
        op_str = "#start_node not found"
        writefile.write(op_str) 
        #print(op_str)

    #close generated_py.py
    writefile.close()

    #writing all the imported libraries at the begining of the file
    if not importlib=='':
        with open('generated_py.txt', 'r+') as f:
            lines = f.readlines()    
            lines.insert(0, importlib+'\n')  
            f.seek(0)                
            f.writelines(lines)