import json 
import re

def tokenize(x):

    text = x[0]
    shape = x[1]

    # rectangle tokenization
    if shape=='rectangle':

        #spliting to check for keywords
        content = re.split(r' ', text)

        # INPUT convert "input age(int) sex(string) address" to ["input","age int","sex string", "address"] 
        if content[0].lower() == 'input':
            
            #slipting into tokes except the keyword to extract the data type info
            tokens = content[1:]
            for i,token in enumerate(tokens):
                if token.find("(")!=-1:
                    data_type = token[token.find("(")+1:token.find(")")]
                    tokens[i] = token[:token.find("(")] + " " + data_type
                else:
                    tokens[i] = token + " " + "none"
            return [content[0]] + tokens
        # PRINT
        elif content[0].lower() == 'print':
            literals = []
            #finding stuff inside quotes
            literals += re.findall('"([^"]*)"', text)
            for i,d in enumerate(literals):
                literals[i] = '"'+d+'"'
                text = text.replace(literals[i],"")
            #variable names etc (stuff w/o quotes)
            literals += text.split()[1:]
            return [content[0]] + literals
    else:
        return "opps"


# just for debugging. Basically performs a simple DFS on the whole flowchart
if __name__ == '__main__':
    filename = "clean model (6) copy.json"
    writefile = open("generated_py.py", "wt")
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    nodes = data['nodes']
    edges = data['edges']
    in_edges = data['in_edges']
    global visited
    visited = {i:0 for i in nodes.keys()}
    def dfs(n):
        print(tokenize(nodes[n]), "github.com/h-r-v")
        global visited
        if nodes[n][0].lower() in ['end', 'stop']:
            return 0
        if n not in edges.keys():
            return 0
        visited[n] = 1
        for i,x in enumerate(edges[n][0]):
            if visited[x]==0:
                dfs(x)

    dfs('2')
