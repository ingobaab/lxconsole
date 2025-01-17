from flask import Flask, Blueprint
from . import server
from . import servers
from . import certificates
from . import cluster_members
from . import images
from . import container
from . import containers
from . import networks
from . import network_acl
from . import network_acls
from . import profiles
from . import operations
from . import projects
from . import simplestreams
from . import storage_pools
from . import storage_volumes
from . import virtual_machine
from . import virtual_machines

from . import users
from . import groups
from . import roles
from . import access_controls
#from . import logs


api = Blueprint('api', __name__, url_prefix='/api')


# URLs are prefixed with /api...
api.add_url_rule('/container/<endpoint>', view_func=container.api_container_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/containers/<endpoint>', view_func=containers.api_containers_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/servers/<endpoint>', view_func=servers.api_servers_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/server/<endpoint>', view_func=server.api_server_endpoint)
api.add_url_rule('/certificates/<endpoint>', view_func=certificates.api_certificates_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/cluster-members/<endpoint>', view_func=cluster_members.api_cluster_members_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/images/<endpoint>', view_func=images.api_images_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/networks/<endpoint>', view_func=networks.api_networks_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/network-acl/<endpoint>', view_func=network_acl.api_network_acl_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/network-acls/<endpoint>', view_func=network_acls.api_network_acls_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/profiles/<endpoint>', view_func=profiles.api_profiles_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/operations/<endpoint>', view_func=operations.api_operations_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/projects/<endpoint>', view_func=projects.api_projects_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/simplestreams/<endpoint>', view_func=simplestreams.api_simplestreams_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/storage-pools/<endpoint>', view_func=storage_pools.api_storage_pools_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/storage-volumes/<endpoint>', view_func=storage_volumes.api_storage_volumes_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/virtual-machine/<endpoint>', view_func=virtual_machine.api_virtual_machine_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/virtual-machines/<endpoint>', view_func=virtual_machines.api_virtual_machines_endpoint, methods=['GET', 'POST'])

api.add_url_rule('/users/<endpoint>', view_func=users.api_users_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/groups/<endpoint>', view_func=groups.api_groups_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/roles/<endpoint>', view_func=roles.api_roles_endpoint, methods=['GET', 'POST'])
api.add_url_rule('/access-controls/<endpoint>', view_func=access_controls.api_access_controls_endpoint, methods=['GET', 'POST'])
#api.add_url_rule('/logs/<endpoint>', view_func=logs.api_logs_endpoint, methods=['GET', 'POST'])