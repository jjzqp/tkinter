import json
'''
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
data2 = json.dumps(data,sort_keys=True, indent=4, separators=(',', ': '))
print(data2)
'''
path = "./ui_designer/ui_240x240_watch/UI/project/prj_2020-12-10.json"

def open_json_file(path):
    with open(path, 'r', encoding='utf-8') as f:

        data = f.read() # 读出json字符串
        data = eval(data)#转成字典
        #字典转成json对象
        data = json.dumps(data,sort_keys=True, indent=4, separators=(',', ': '))
        
        #json对象转成字典
        data = json.loads(data)

        return data

def dump_json_data(data):
    data = json.dumps(data,sort_keys=True, indent=4, separators=(',', ': '))
    print(data)

def parse_layer(data):
    _property = data['property']
    ename = _property[0]['ename']
    rect = _property[1]['struct'][0][3]['rect']
    
    #dump_json_data(rect)
    return rect

def parse_layout(data):
    layout_property = data['property']
    ename = layout_property[0]['ename']
    dump_json_data(layout_property)
    

if __name__ == "__main__":
    json_data = open_json_file(path)
    #print(json_data['-name'])
    pages_json = json_data['pages'][0]
    layer_json = pages_json['layer'][0]
    layout_json = layer_json['layout'][0]
  
    layer_rect = parse_layer(layer_json)

    #dump_json_data(layer_rect)
    parse_layout(layout_json)
    

    


    

    
