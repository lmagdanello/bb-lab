vagrant_config = {
    'vm_box': 'generic/rocky9',
    'bluebanquise_version': '3.0.1',
    
    'vms': {
        'mgt1': {
            'ip': '192.168.56.10',
            'group': 'management',
            'hostnames': {
                'primary': 'mgt1',
                'others': ['mgt1.bluebanquise.example.com'],
            },
            'port_forwarding': [
                (80, 8081),
                (8080, 8082),
            ],
            'networks': [
                {'type': 'private_network', 'ip': '10.0.0.11'},
            ],
            'disks': [
                {'size': '1024', 'controller': 'sata'},
                {'size': '1024', 'controller': 'sata'},
            ],
        },
        
        'mgt2': {
            'ip': '192.168.56.11',
            'group': 'management',
            'hostnames': {
                'primary': 'mgt2',
                'others': ['mgt2.bluebanquise.example.com'],
            },
            'port_forwarding': [
                (80, 8083),
                (8080, 8084),
            ],
            'networks': [
                {'type': 'private_network', 'ip': '10.0.0.12'},
            ],
            'disks': [
                {'size': '1024', 'controller': 'sata'},
                {'size': '1024', 'controller': 'sata'},
            ],
        },
        
        'login1': {
            'ip': '192.168.56.12',
            'group': 'login',
            'hostnames': {
                'primary': 'login1',
                'others': ['login1.bluebanquise.example.com'],
            },
            'port_forwarding': [
                (80, 8085),
            ],
            'networks': [
                {'type': 'private_network', 'ip': '10.0.0.13'},
            ],
        },
        
        'c001': {
            'ip': '192.168.56.13',
            'group': 'compute',
            'hostnames': {
                'primary': 'c001',
                'others': ['c001.bluebanquise.example.com'],
            },
            'port_forwarding': [
                (80, 8086),
            ],
            'networks': [
                {'type': 'private_network', 'ip': '10.0.0.14'},
            ],
        },
    },
}