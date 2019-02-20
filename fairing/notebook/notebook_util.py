import json
import os
import ipykernel
import requests
import re
import pprint

from notebook.notebookapp import list_running_servers
from requests.compat import urljoin


def get_notebook_name():
    """
    Return the full path of the jupyter notebook.
    """
    home = os.path.expanduser('~')
    # runtime_dir = os.path.join(home, '.local/share/jupyter/runtime')
    # runtime_files = [f for f in os.listdir(runtime_dir) if os.path.splitext(f)[1] == '.json']
    # runtime_files.sort(key=lambda f: os.path.getmtime(os.path.join(runtime_dir, f)), reverse=True)
    # current_runtime_file = os.path.join(runtime_dir, runtime_files[0])

    # with open(current_runtime_file, 'r') as fp_:
    #     token = json.load(fp_).get('token')
    token = os.getenv('KERNEL_JHUB_API_TOKEN')

    url = urljoin('http://{}/user/{}/'.format(os.getenv('PROXY_PUBLIC_SERVICE_HOST'), os.getenv('KERNEL_USERNAME')), 'api/sessions')
    response = requests.get(url, params={'token': token}, verify=False)

    kernel_id = os.getenv('KERNEL_ID')

    for nn in json.loads(response.text):
        if nn['kernel']['id'] == kernel_id:
            full_path = nn['notebook']['path']
            # return os.path.basename(full_path)
            # return full_path
            return os.path.join(home, full_path)
    return None


def get_notebook_name1():
    """
    Return the full path of the jupyter notebook.
    """
    kernel_id = re.search('kernel-(.*).json',
                          ipykernel.connect.get_connection_file()).group(1)
    servers = list_running_servers()
    for ss in servers:
        response = requests.get(urljoin(ss['url'], 'api/sessions'),
                                params={'token': ss.get('token', '')})
        for nn in json.loads(response.text):
            if nn['kernel']['id'] == kernel_id:
                full_path = nn['notebook']['path']
                return os.path.basename(full_path)


def is_in_notebook():
    try:
        ipykernel.get_connection_info()
    except RuntimeError:
        return False
    return True
