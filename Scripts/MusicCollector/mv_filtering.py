import luna_GlobalScript.misc.compact_input as c
def main():
    mv3d = input("3DMVありのみダウンロード(0 or 1): ")
    mv2d = input("2DMVありのみダウンロード(0 or 1): ")
    mv_original = input("Original MVありのみダウンロード(0 or 1): ")
    mv_static = input("Static Imageのみダウンロード(0 or 1): ")

    a = c.tfgen_boolean(mv3d)
    b = c.tfgen_boolean(mv2d)
    c = c.tfgen_boolean(mv_original)
    d = c.tfgen_boolean(mv_static)
    
    return a, b, c, d