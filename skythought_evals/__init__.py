import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../")))
cache_dir = '/scratch/pbsjobs/wxy320/huggingface'
project_dir = '/home/wxy320/ondemand/program/o1-reproduce'
hug_token = None

os.environ["HF_HOME"] = cache_dir

