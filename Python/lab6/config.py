# -------------------------------------------------------------------------
## THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_lab6.py "

_BATCH_ACCOUNT_NAME = 'lab6ayush'  # Your batch account name
_BATCH_ACCOUNT_KEY = 'GNClQJ4x9h4D/Om+SvGm7rXMeyaTE9yQRd6nxeizQzTJG1cXfOHzw+2pjtikjheIlQii3djN8Asm66ph+Smm2w=='  # Your batch account key
_BATCH_ACCOUNT_URL = 'https://lab6ayush.norwayeast.batch.azure.com'  # Your batch account URL
_STORAGE_ACCOUNT_NAME = 'lab6ayushstorage'
_STORAGE_ACCOUNT_KEY = '/g1sXVeXLK98SEMLT5R/yl3LnTAvJC9qClk3wdHsTi6pJOYYwCpLLmhXMAfndRQByVk0egRDpOem52VbOfZJ7A=='
_STORAGE_ACCOUNT_DOMAIN = 'blob.core.windows.net' # Your storage account blob service domain

_POOL_ID = 'lab6ayushpool'  # Your Pool ID
_POOL_NODE_COUNT = 4  # Pool node count
_POOL_VM_SIZE = 'STANDARD_DS1_V2'  # VM Type/Size
_JOB_ID = 'lab6ayushjob'  # Job ID
_STANDARD_OUT_FILE_NAME = 'stdout.txt'  # Standard Output file
