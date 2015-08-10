import os
from secrets import *

secrets_list = [
    'CHAIN_API_ID', 'CHAIN_API_SECRET', 'PRIVATE_KEY', 'PRIVATE_KEY_2',
    'RPC_USERNAME', 'RPC_PASSWORD', 'NAMECOIN_PRIVATE_KEY',
    'BLOCKCHAIN_API_KEY', 'BLOCKCYPHER_API_KEY'
]

for env_variable in os.environ:
    if env_variable in secrets_list:
        env_value = os.environ[env_variable]
        exec(env_variable + " = \"\"\"" + env_value + "\"\"\"")