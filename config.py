import os# current dirtorybasedir = os.path.abspath(os.path.dirname(__file__))# debug modeDEBUG = True# folder maintains uploaded fileUPLOAD_FOLDER = basedir + '/upload/'# max size of uploaded fileMAX_CONTENT_LENGTH = 10 * 1024 * 1024