vagrant_config = {
    'vm_box': 'generic/rocky9',
    'ssh_host': '127.0.0.1',
    'ssh.insert_key': 'false',
    'ssh.private_key_path': '~/.vagrant.d/insecure_private_key',
    'bluebanquise_version': '3.0.1',
    'vms_network': 'net-1',
    'vms_subnet': '10.0.0.0',
    'vms_prefix': '16',
#    'http_proxy': 'http://',
#    'https_proxy': 'http://',
    'vms': {
        'mgt1': {
            'ip': '10.0.0.11',
            'group': 'management',
            'hostnames': {
                'primary': 'mgt1',
                'others': ['mgt1.bluebanquise.example.com'],
            },
            'port_forwarding': [
                (80, 8080),
            ],
            'disks': [
                {'size': '1024', 'controller': 'sata'},
                {'size': '1024', 'controller': 'sata'},
            ],
        },
        
        'mgt2': {
            'ip': '10.0.0.12',
            'group': 'management',
            'hostnames': {
                'primary': 'mgt2',
                'others': ['mgt2.bluebanquise.example.com'],
            },
            'disks': [
                {'size': '1024', 'controller': 'sata'},
                {'size': '1024', 'controller': 'sata'},
            ],
        },
        
        'login1': {
            'ip': '10.0.0.13',
            'group': 'login',
            'hostnames': {
                'primary': 'login1',
                'others': ['login1.bluebanquise.example.com'],
            },
        },
        
        'c001': {
            'ip': '10.0.0.14',
            'group': 'compute',
            'hostnames': {
                'primary': 'c001',
                'others': ['c001.bluebanquise.example.com'],
            },
        },
    },
}
