# Debug Print out
# 使用法
# 使用したいスクリプト内にて
# import luna_GlobalScript.misc.debug_tool as debug_tool
#
# def example(str):
#   if Example == True:
#       debug_tool.dprint(str)
#
# example("DebugMode Only Printout!")

def dprint(str): 
    print(f"Debug: {str}")
    return str