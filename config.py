import os# current dirtorybasedir = os.path.abspath(os.path.dirname(__file__))# debug modeDEBUG = True# folder maintains uploaded fileUPLOAD_FOLDER = basedir + '/files/upload/'# folder maintains out fileOUT_FOLDER = basedir + '/files/out/'# max size of uploaded fileMAX_CONTENT_LENGTH = 10 * 1024 * 1024