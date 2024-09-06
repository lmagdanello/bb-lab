# bb-lab

`bb-lab` is a project designed to automate the setup and configuration of virtual environments using Vagrant and Ansible. The primary goal is to create a laboratory environment for utilizing the [Bluebanquise](https://github.com/bluebanquise/bluebanquise) project, facilitating the management and testing of virtual machines.

## project Structure

- **config/**
  - **config.py**: Contains the configuration for virtual machines, including IP addresses, groups, hostnames, and other settings.
- **main.py**: Python script that generates configuration files from Jinja2 templates based on the settings in `config.py`.
- **playbooks/**
  - **bluebanquise/**
    - **defaults/main.yml**: Default variables for the Bluebanquise role.
    - **files/groups.yml**: Generated Ansible inventory file for groups.
    - **files/nodes.yml**: Generated Ansible inventory file for nodes.
    - **tasks/main.yml**: Ansible tasks for configuring the Bluebanquise role.
    - **vars/main.yml**: Variables for the Bluebanquise role.
  - **playbook.yml**: Ansible playbook that applies the Bluebanquise role to the virtual machines.
- **templates/** (_these templates are used to create inventories dynamically through config.py_)
  - **groups.yml.j2**: Jinja2 template for generating the groups inventory file.
  - **nodes.yml.j2**: Jinja2 template for generating the nodes inventory file.
  - **Vagrantfile.j2**: Jinja2 template for generating the Vagrantfile.

## requirements

- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)
- [Ansible](https://www.ansible.com/)
- [Python](https://www.python.org/)

## installation and setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/bb-lab.git
   cd bb-lab
   ```

2. **Configuration:**

Edit the `config/config.py` file to define the configuration for your virtual machines. This includes IP addresses, groups, hostnames, networks, and disks.

- **Example --** (minimal config) ->
```python
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
            'port_forwarding': [(80, 8081), (8080, 8082)],
            'disks': [{'size': '1024', 'controller': 'sata'}, {'size': '1024', 'controller': 'sata'}],
        },
        'login1': {
            'ip': '10.0.0.12',
            'group': 'login',
            'hostnames': {
                'primary': 'login1',
                'others': ['login1.bluebanquise.example.com'],
            },
            'port_forwarding': [(80, 8085)],
        },
        'c001': {
            'ip': '10.0.0.13',
            'group': 'compute',
            'hostnames': {
                'primary': 'c001',
                'others': ['c001.bluebanquise.example.com'],
            },
            'port_forwarding': [(80, 8086)],
        },
    },
}
```

> **If you need to use HTTP Proxy, uncomment the section: `'http_proxy': 'http://'` or `'https_proxy': 'http://'` and add your proxy URL**

> **At least one node must be assigned to the `management` group for the Ansible playbook to be applied correctly.**

- **Ideal Test Scenario**

An ideal test setup consists of the following nodes:

```lua
+---------------------+
|       Vagrant       |
|      Environment    |
+---------------------+
|     +---------+     |
|     |  mgt1   |     |
|     | (management)| |
|     +---------+     |
|     +---------+     |
|     |  mgt2   |     |
|     | (management)| |
|     +---------+     |
|     +---------+     |
|     | login1  |     |
|     |  (login) |    |
|     +---------+     |
|     +---------+     |
|     |  c001   |     |
|     | (compute) |   |
|     +---------+     |
+---------------------+
```

3. **Generate Configuration Files**

Run the Python script to generate the necessary configuration files:

```bash
python main.py
```

4. **Generate RSA keys**

Run the commando below to generate your RSA keys.

```bash
ssh-keygen -t ed25519 -f playbooks/bluebanquise/files/id_ed25519
```

5. **Initialize the Environment**

Use Vagrant to create and configure the virtual machines:

```bash
cd vagrant/
vagrant up
```

---

## contributing

If you would like to contribute to this project, please open a pull request.