from read_data import READ_DATA
from dotenv import load_dotenv
import os
load_dotenv()
file_path1=os.getenv('file_path1')
file_path2=os.getenv('file_path2')
obj=READ_DATA(file_path1,file_path2)
visa_df=obj.csvloader()
hr_df=obj.xcelloader()
print(hr_df.head)