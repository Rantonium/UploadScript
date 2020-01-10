import os
import shutil
import logging
import sys
from pathlib import Path

fileName=sys.argv[1]
AnPublicare=sys.argv[2]
IdAutor=sys.argv[3]

root=os.getcwd()
uploadPath=root+"/uploads"
path=root+"/"+"storage"+"/"+AnPublicare+"/"+IdAutor
access_rights= 0o777
try:
    Path(path).mkdir(parents=True,exist_ok=True)
except OSError as err:
    logging.basicConfig(filename='/var/log/messages/FileUpload.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger=logging.getLogger(__name__)
    logger.error(err)
try:
    if os.path.isfile(fileName):
        os.path.remove(fileName)
    shutil.move(uploadPath+"/"+fileName,path)
except OSError as err:
    logging.basicConfig(filename='/var/log/messages/FileUpload.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger=logging.getLogger(__name__)
    logger.error(err)



