if __name__ == "__main__":
    print("you tried to run this as main")


def listAllImportedModules():
    import sys
    print(sys.modules.keys())
    print(list(imports()))
        
def imports():
    import types
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            try:
                yield val
            except:
                yield ''
