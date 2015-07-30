__author__ = 'philip_j'

from python_integration import Satellite, Station, lol


# import importlib
# import inspect
# from docutils.core import publish_doctree

def show():
    s = Satellite()
    station = Station()
    l = lol()

    l.speak()
    s.speak()
    station.speak()

# def readNode(node, size):
#     print('\t'*size + node.nodeName, end="")
#     if node.nodeValue != None:
#         print(' : ' + node.nodeValue, end="")
#
#     try :
#         if node.hasAttributes():
#             print(', attributes : ', end="")
#             for key in node.attributes.keys():
#                 print(str(node.attributes[key]) + ', ', end="")
#     except Exception as e:
#         pass
#
#     print()
#
#
#
#     if node.hasChildNodes():
#         size+=1
#         for element in node.childNodes:
#             readNode(element, size)
#
# if __name__ == '__main__':
#     #main()
#     name = "source.ground"
#     a =  importlib.import_module(name, package=None)
#
#
#     tet = None
#
#     for b in vars(a):
#         if b.startswith('__'):
#             continue
#
#         #print(str(vars(a)[b]) + ' : ' +vars(a)[b].__name__)
#         if(vars(a)[b].__name__ == "Antenna"):
#             tet = vars(a)[b]
#
#     print(tet)
#     li = inspect.getmembers(tet, predicate=inspect.isfunction)
#
#
#     func = li[1][1]
#
#     print()
#
#     #name
#     print('name : ')
#     print(li[1][0])
#     print()
#     #file
#     print(inspect.getsourcefile(func))
#     #line
#     print(inspect.getsourcelines(func)[1])
#     #length
#     print(inspect.getsourcelines(func)[0])
#     #signature
#     print(inspect.signature(func))
#     #doc
#     print(inspect.getdoc(func))
#
#
#     doctree = publish_doctree(inspect.getdoc(func)).asdom()
#
#
#
#     readNode(doctree.firstChild , 0)
#
#     print(doctree.toprettyxml())
#
#
#     from docutils.core import publish_doctree
#     import docutils.nodes
#
#     def walk_docstring(prop):
#         doc = prop.__doc__
#         doctree = publish_doctree(doc)
#         class Walker:
#             def __init__(self, doc):
#                 self.document = doc
#                 self.fields = {}
#             def dispatch_visit(self,x):
#                 if isinstance(x, docutils.nodes.field):
#                     field_name = x.children[0].rawsource
#                     field_value = x.children[1].rawsource
#                     self.fields[field_name]=field_value
#         w = Walker(doctree)
#         doctree.walk(w)
#         # the collected fields I wanted
#         print(w.fields)
#
#     walk_docstring(func)
