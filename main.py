import os
import sys

from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

file_path = sys.argv[1]
if os.path.exists(file_path):
    #print os.path.basename(file_path)
    print ("File exist")