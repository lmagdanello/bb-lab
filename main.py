import os
import jinja2
from config.config import vagrant_config

def generate_file(template_name, output_path, config):
    output_dir = os.path.dirname(output_path)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(output_path, 'w+') as file:
        file.write(load_template(template_name).render(config))

def load_template(template_name):
    return (jinja2.Environment(autoescape=True,
                               loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
            .get_template(f'templates/{template_name}'))

if __name__ == '__main__':
    generate_file('Vagrantfile.j2', 'vagrant/Vagrantfile', vagrant_config)
    generate_file('nodes.yml.j2', 'playbooks/bluebanquise/files/nodes.yml', vagrant_config)
    generate_file('groups.yml.j2', 'playbooks/bluebanquise/files/groups.yml', vagrant_config)