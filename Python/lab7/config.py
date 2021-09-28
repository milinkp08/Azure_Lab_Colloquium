# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "batch_python_tutorial_ffmpeg.py"

# Update the Batch and Storage account credential strings below with the values
# unique to your accounts. These are used when constructing connection strings
# for the Batch and Storage client objects.

_BATCH_ACCOUNT_NAME = ''
_BATCH_ACCOUNT_KEY = ''
_BATCH_ACCOUNT_URL = ''
_STORAGE_ACCOUNT_NAME = ''
_STORAGE_ACCOUNT_KEY = ''
_POOL_ID = 'LinuxFfmpegPool'
_DEDICATED_POOL_NODE_COUNT = 0
_LOW_PRIORITY_POOL_NODE_COUNT = 5
_POOL_VM_SIZE = 'STANDARD_A1_v2'
_JOB_ID = 'LinuxFfmpegJob'
