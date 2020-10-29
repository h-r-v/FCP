import json

#convert XML to graph
def create_graph(data):
    #root only contains nodes and edges now
    root = data['mxGraphModel'][0]['root'][0]['mxCell'][2:]

    nodes = {}
    edges = {}
    in_edges = {}

    for x in root:
        #is node
        if 'edge' not in x['_attr'].keys():
            id = str(x['_attr']['id']['_value'])
            text = str(x['_attr']['value']['_value'])
            shape = str(x['_attr']['style']['_value'][6:])
            nodes[id] = [text,shape]
        #is edge
        else:
            source = str(x['_attr']['source']['_value'])
            target = str(x['_attr']['target']['_value'])
            
            if "value" in x['_attr']:
                label = str(x['_attr']['value']['_value'])
            else:
                label = ""

            #edges
            # append more nodes
            if source in edges.keys():
                edges[source][0] += [target]
                edges[source][1] += [label]

            # source not in edge list
            else:
                edges[source] = [[],[]]
                edges[source][0] = [target]
                edges[source][1] = [label]

            #in_edges
            # append more nodes
            if target in in_edges.keys():
                in_edges[target][0] += [source]
                in_edges[target][1] += [label]

            # source not in edge list
            else:
                in_edges[target] = [[],[]]
                in_edges[target][0] = [source]
                in_edges[target][1] = [label]

    #rearanging all outgoing edges of a if/elif/else to make sure that unlabeled edges always come last
    for n in nodes:
        if nodes[n][1] == "rhombus":
            if n in edges:
                delindex = []

                #copying all the "else" to the last of the list
                for i in range(len(edges[n][0])):
                    # selecting edges inside a if statements that are else
                    if len(in_edges[n][0])==1 and edges[n][1][i].lower()=="else":
                        edges[n][0] += [str(edges[n][0][i])]
                        edges[n][1] += [str(edges[n][1][i])]
                        delindex+=[i]
                        break
                
                #copying all the "" to the last of the list
                for i in range(len(edges[n][0])):
                    # selecting edges inside a if statements that are either unlabeled or is pointing at a parent node
                    if len(in_edges[n][0])==1 and ( edges[n][0][i] in in_edges[n][0] or not edges[n][1][i] ):
                        edges[n][0] += [str(edges[n][0][i])]
                        edges[n][1] += [str(edges[n][1][i])]
                        delindex+=[i]
                
                #deleting the index that have been copied to the end of the lists.
                for index in sorted(delindex, reverse=True):
                    del edges[n][0][index]
                    del edges[n][1][index]
                        

    flowdata = {"nodes":nodes,"edges":edges,"in_edges":in_edges}

    return flowdata