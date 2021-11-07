import os
from notice import get_notice
from db import save_to_db
from dotenv import load_dotenv

load_dotenv(verbose=True)

URL = os.getenv('URL')

def handler(event, context):
    notices = get_notice(URL)
    save_to_db(notices)
    
    print('success')
    
    return