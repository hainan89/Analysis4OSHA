'''
Created on 2015年8月12日

@author: hainan
'''

import sys

class NicePrint(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    # print the dict-variable in a easy and readable way
    def print_dict(self, obj, nested_level=0):
        
        spacing = '    '
        if isinstance(obj, dict):
            print(" %s { " % ((nested_level) * spacing))
            for k, v in obj.items():
                if isinstance(k, str):
                    k = '"' + k + '"'
                    
                if isinstance(v, dict):
                    print(" %s %s : " % ((nested_level + 1) * spacing, k))
                    self.print_dict(v, nested_level + 1)
                else:
                    if isinstance(v, str):
                        v = '"' + v + '"'
                    print(" %s %s : %s ," % ((nested_level + 1) * spacing, k, v))
                    
            print(" %s } " % (nested_level * spacing))
        elif isinstance(obj, list):
            print(" %s [ } " % ((nested_level) * spacing))
            for v in obj:
                if isinstance(k, str):
                    k = '"' + k + '"'
                    
                if isinstance(v, list) or isinstance(v, dict):
                    self.print_dict(v, nested_level + 1)
                else:
                    if isinstance(v, str):
                        v = '"' + v + '"'
                    print(" %s %s "% ((nested_level + 1) * spacing, v))
            print(" %s ] " % ((nested_level) * spacing))
        else:
            print(" %s %s " % (nested_level * spacing, obj))
            
        