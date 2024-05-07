* Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. You can install and use collections through a distribution server, such as Ansible Galaxy, or a Pulp 3 Galaxy server.

### Installing collections
> [source](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html)

#### Installing collections with `ansible-galaxy`
* By default, `ansible-galaxy collection install` uses [https://galaxy.ansible.com](https://galaxy.ansible.com/) as the Galaxy server (as listed in the `ansible.cfg` file under [GALAXY_SERVER](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#galaxy-server)). You do not need any further configuration.
* See [Configuring the ansible-galaxy client](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html#galaxy-server-config) if you are using any other Galaxy server, such as Red Hat Automation Hub.
* See [Collection structure](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_structure.html#collection-structure) for details on the collection directory structure.

#### Install multiple collections with a requirements file
* You can set up a `requirements.yml` file to install multiple collections in one command. This file is a YAML file in the format:
	```yaml
	---
	collections:
	# With just the collection name
	- my_namespace.my_collection
	
	# With the collection name, version, and source options
	- name: my_namespace.my_other_collection
	  version: ">=1.2.0" # Version range identifiers (default: ``*``)
	  source: ... # The Galaxy URL to pull the collection from (default: ``--api-server`` from cmdline)
	```
* You can specify the following keys for each collection entry:
	* name
	* version: The `version` key uses the same range identifier format documented in [Installing an older version of a collection](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html#collections-older-version).
	* signatures: The `signatures` key accepts a list of signature sources that are used to supplement those found on the Galaxy server during collection installation and `ansible-galaxy collection verify`. Signature sources should be URIs that contain the detached signature. The `--keyring` CLI option must be provided if signatures are specified.
	* source:
	* type: The `type` key can be set to `file`, `galaxy`, `git`, `url`, `dir`, or `subdirs`. If `type` is omitted, the `name` key is used to implicitly determine the source of the collection.
* You can also add roles to a `requirements.yml` file, under the `roles` key. The values follow the same format as a requirements file used in older Ansible releases.
	```yaml
	---
	roles:
	  # Install a role from Ansible Galaxy.
	  - name: geerlingguy.java
	    version: "1.9.6" # note that ranges are not supported for roles
	
	collections:
	  # Install a collection from Ansible Galaxy.
	  - name: geerlingguy.php_roles
	    version: ">=0.9.3"
	    source: https://galaxy.ansible.com
	```
* To install both roles and connections at the same time: `ansible-galaxy install -r requirements.yml`
* Running `ansible-galaxy collection install -r` or `ansible-galaxy role install -r` will only install collections, or roles respectively.

### Downloading collections
> [source](https://docs.ansible.com/ansible/latest/collections_guide/collections_downloading.html)
* To download a collection and its dependencies for an offline install, run `ansible-galaxy collection download`. This downloads the collections specified and their dependencies to the specified folder and creates a `requirements.yml` file which can be used to install those collections on a host without access to a Galaxy server. All the collections are downloaded by default to the `./collections` folder.
* Once you have downloaded the collections, the folder contains the collections specified, their dependencies, and a `requirements.yml` file. You can use this folder as is with `ansible-galaxy collection install` to install the collections on a host without access to a Galaxy server.
```bash
# This must be run from the folder that contains the offline collections and requirements.yml file downloaded
# by the internet-connected host
cd ~/offline-collections
ansible-galaxy collection install -r requirements.yml
```

### Listing collections
> [source](https://docs.ansible.com/ansible/latest/collections_guide/collections_listing.html)
* To list installed collections, run `ansible-galaxy collection list`. This shows all of the installed collections found in the configured collections search paths. It will also show collections under development which contain a galaxy.yml file instead of a MANIFEST.json. The path where the collections are located are displayed as well as version information. If no version information is available, a `*` is displayed for the version number.
```
# /home/astark/.ansible/collections/ansible_collections
Collection                 Version
-------------------------- -------
cisco.aci                  0.0.5
cisco.mso                  0.0.4
sandwiches.ham             *
splunk.es                  0.0.5

# /usr/share/ansible/collections/ansible_collections
Collection        Version
----------------- -------
fortinet.fortios  1.0.6
pureport.pureport 0.0.8
sensu.sensu_go    1.3.0
```

### Collections index
> [source](https://docs.ansible.com/ansible/latest/collections/index.html#list-of-collections)
- [amazon.aws](https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html#plugins-in-amazon-aws)
- [ansible.builtin](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html#plugins-in-ansible-builtin)
- [ansible.netcommon](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/index.html#plugins-in-ansible-netcommon)
- [ansible.posix](https://docs.ansible.com/ansible/latest/collections/ansible/posix/index.html#plugins-in-ansible-posix)
- [ansible.utils](https://docs.ansible.com/ansible/latest/collections/ansible/utils/index.html#plugins-in-ansible-utils)
- [ansible.windows](https://docs.ansible.com/ansible/latest/collections/ansible/windows/index.html#plugins-in-ansible-windows)
- [arista.eos](https://docs.ansible.com/ansible/latest/collections/arista/eos/index.html#plugins-in-arista-eos)
- [awx.awx](https://docs.ansible.com/ansible/latest/collections/awx/awx/index.html#plugins-in-awx-awx)
- [azure.azcollection](https://docs.ansible.com/ansible/latest/collections/azure/azcollection/index.html#plugins-in-azure-azcollection)
- [check_point.mgmt](https://docs.ansible.com/ansible/latest/collections/check_point/mgmt/index.html#plugins-in-check-point-mgmt)
- [chocolatey.chocolatey](https://docs.ansible.com/ansible/latest/collections/chocolatey/chocolatey/index.html#plugins-in-chocolatey-chocolatey)
- [cisco.aci](https://docs.ansible.com/ansible/latest/collections/cisco/aci/index.html#plugins-in-cisco-aci)
- [cisco.asa](https://docs.ansible.com/ansible/latest/collections/cisco/asa/index.html#plugins-in-cisco-asa)
- [cisco.dnac](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/index.html#plugins-in-cisco-dnac)
- [cisco.intersight](https://docs.ansible.com/ansible/latest/collections/cisco/intersight/index.html#plugins-in-cisco-intersight)
- [cisco.ios](https://docs.ansible.com/ansible/latest/collections/cisco/ios/index.html#plugins-in-cisco-ios)
- [cisco.iosxr](https://docs.ansible.com/ansible/latest/collections/cisco/iosxr/index.html#plugins-in-cisco-iosxr)
- [cisco.ise](https://docs.ansible.com/ansible/latest/collections/cisco/ise/index.html#plugins-in-cisco-ise)
- [cisco.meraki](https://docs.ansible.com/ansible/latest/collections/cisco/meraki/index.html#plugins-in-cisco-meraki)
- [cisco.mso](https://docs.ansible.com/ansible/latest/collections/cisco/mso/index.html#plugins-in-cisco-mso)
- [cisco.nso](https://docs.ansible.com/ansible/latest/collections/cisco/nso/index.html#plugins-in-cisco-nso)
- [cisco.nxos](https://docs.ansible.com/ansible/latest/collections/cisco/nxos/index.html#plugins-in-cisco-nxos)
- [cisco.ucs](https://docs.ansible.com/ansible/latest/collections/cisco/ucs/index.html#plugins-in-cisco-ucs)
- [cloud.common](https://docs.ansible.com/ansible/latest/collections/cloud/common/index.html#plugins-in-cloud-common)
- [cloudscale_ch.cloud](https://docs.ansible.com/ansible/latest/collections/cloudscale_ch/cloud/index.html#plugins-in-cloudscale-ch-cloud)
- [community.aws](https://docs.ansible.com/ansible/latest/collections/community/aws/index.html#plugins-in-community-aws)
- [community.azure](https://docs.ansible.com/ansible/latest/collections/community/azure/index.html#plugins-in-community-azure)
- [community.ciscosmb](https://docs.ansible.com/ansible/latest/collections/community/ciscosmb/index.html#plugins-in-community-ciscosmb)
- [community.crypto](https://docs.ansible.com/ansible/latest/collections/community/crypto/index.html#plugins-in-community-crypto)
- [community.digitalocean](https://docs.ansible.com/ansible/latest/collections/community/digitalocean/index.html#plugins-in-community-digitalocean)
- [community.dns](https://docs.ansible.com/ansible/latest/collections/community/dns/index.html#plugins-in-community-dns)
- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html#plugins-in-community-docker)
- [community.fortios](https://docs.ansible.com/ansible/latest/collections/community/fortios/index.html#plugins-in-community-fortios)
- [community.general](https://docs.ansible.com/ansible/latest/collections/community/general/index.html#plugins-in-community-general)
- [community.google](https://docs.ansible.com/ansible/latest/collections/community/google/index.html#plugins-in-community-google)
- [community.grafana](https://docs.ansible.com/ansible/latest/collections/community/grafana/index.html#plugins-in-community-grafana)
- [community.hashi_vault](https://docs.ansible.com/ansible/latest/collections/community/hashi_vault/index.html#plugins-in-community-hashi-vault)
- [community.hrobot](https://docs.ansible.com/ansible/latest/collections/community/hrobot/index.html#plugins-in-community-hrobot)
- [community.libvirt](https://docs.ansible.com/ansible/latest/collections/community/libvirt/index.html#plugins-in-community-libvirt)
- [community.mongodb](https://docs.ansible.com/ansible/latest/collections/community/mongodb/index.html#plugins-in-community-mongodb)
- [community.mysql](https://docs.ansible.com/ansible/latest/collections/community/mysql/index.html#plugins-in-community-mysql)
- [community.network](https://docs.ansible.com/ansible/latest/collections/community/network/index.html#plugins-in-community-network)
- [community.okd](https://docs.ansible.com/ansible/latest/collections/community/okd/index.html#plugins-in-community-okd)
- [community.postgresql](https://docs.ansible.com/ansible/latest/collections/community/postgresql/index.html#plugins-in-community-postgresql)
- [community.proxysql](https://docs.ansible.com/ansible/latest/collections/community/proxysql/index.html#plugins-in-community-proxysql)
- [community.rabbitmq](https://docs.ansible.com/ansible/latest/collections/community/rabbitmq/index.html#plugins-in-community-rabbitmq)
- [community.routeros](https://docs.ansible.com/ansible/latest/collections/community/routeros/index.html#plugins-in-community-routeros)
- [community.sap](https://docs.ansible.com/ansible/latest/collections/community/sap/index.html#plugins-in-community-sap)
- [community.sap_libs](https://docs.ansible.com/ansible/latest/collections/community/sap_libs/index.html#plugins-in-community-sap-libs)
- [community.skydive](https://docs.ansible.com/ansible/latest/collections/community/skydive/index.html#plugins-in-community-skydive)
- [community.sops](https://docs.ansible.com/ansible/latest/collections/community/sops/index.html#plugins-in-community-sops)
- [community.vmware](https://docs.ansible.com/ansible/latest/collections/community/vmware/index.html#plugins-in-community-vmware)
- [community.windows](https://docs.ansible.com/ansible/latest/collections/community/windows/index.html#plugins-in-community-windows)
- [community.zabbix](https://docs.ansible.com/ansible/latest/collections/community/zabbix/index.html#plugins-in-community-zabbix)
- [containers.podman](https://docs.ansible.com/ansible/latest/collections/containers/podman/index.html#plugins-in-containers-podman)
- [cyberark.conjur](https://docs.ansible.com/ansible/latest/collections/cyberark/conjur/index.html#plugins-in-cyberark-conjur)
- [cyberark.pas](https://docs.ansible.com/ansible/latest/collections/cyberark/pas/index.html#plugins-in-cyberark-pas)
- [dellemc.enterprise_sonic](https://docs.ansible.com/ansible/latest/collections/dellemc/enterprise_sonic/index.html#plugins-in-dellemc-enterprise-sonic)
- [dellemc.openmanage](https://docs.ansible.com/ansible/latest/collections/dellemc/openmanage/index.html#plugins-in-dellemc-openmanage)
- [dellemc.powerflex](https://docs.ansible.com/ansible/latest/collections/dellemc/powerflex/index.html#plugins-in-dellemc-powerflex)
- [dellemc.unity](https://docs.ansible.com/ansible/latest/collections/dellemc/unity/index.html#plugins-in-dellemc-unity)
- [f5networks.f5_modules](https://docs.ansible.com/ansible/latest/collections/f5networks/f5_modules/index.html#plugins-in-f5networks-f5-modules)
- [fortinet.fortimanager](https://docs.ansible.com/ansible/latest/collections/fortinet/fortimanager/index.html#plugins-in-fortinet-fortimanager)
- [fortinet.fortios](https://docs.ansible.com/ansible/latest/collections/fortinet/fortios/index.html#plugins-in-fortinet-fortios)
- [frr.frr](https://docs.ansible.com/ansible/latest/collections/frr/frr/index.html#plugins-in-frr-frr)
- [gluster.gluster](https://docs.ansible.com/ansible/latest/collections/gluster/gluster/index.html#plugins-in-gluster-gluster)
- [google.cloud](https://docs.ansible.com/ansible/latest/collections/google/cloud/index.html#plugins-in-google-cloud)
- [grafana.grafana](https://docs.ansible.com/ansible/latest/collections/grafana/grafana/index.html#plugins-in-grafana-grafana)
- [hetzner.hcloud](https://docs.ansible.com/ansible/latest/collections/hetzner/hcloud/index.html#plugins-in-hetzner-hcloud)
- [hpe.nimble](https://docs.ansible.com/ansible/latest/collections/hpe/nimble/index.html#plugins-in-hpe-nimble)
- [ibm.qradar](https://docs.ansible.com/ansible/latest/collections/ibm/qradar/index.html#plugins-in-ibm-qradar)
- [ibm.spectrum_virtualize](https://docs.ansible.com/ansible/latest/collections/ibm/spectrum_virtualize/index.html#plugins-in-ibm-spectrum-virtualize)
- [infinidat.infinibox](https://docs.ansible.com/ansible/latest/collections/infinidat/infinibox/index.html#plugins-in-infinidat-infinibox)
- [infoblox.nios_modules](https://docs.ansible.com/ansible/latest/collections/infoblox/nios_modules/index.html#plugins-in-infoblox-nios-modules)
- [inspur.ispim](https://docs.ansible.com/ansible/latest/collections/inspur/ispim/index.html#plugins-in-inspur-ispim)
- [inspur.sm](https://docs.ansible.com/ansible/latest/collections/inspur/sm/index.html#plugins-in-inspur-sm)
- [junipernetworks.junos](https://docs.ansible.com/ansible/latest/collections/junipernetworks/junos/index.html#plugins-in-junipernetworks-junos)
- [kubernetes.core](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/index.html#plugins-in-kubernetes-core)
- [lowlydba.sqlserver](https://docs.ansible.com/ansible/latest/collections/lowlydba/sqlserver/index.html#plugins-in-lowlydba-sqlserver)
- [microsoft.ad](https://docs.ansible.com/ansible/latest/collections/microsoft/ad/index.html#plugins-in-microsoft-ad)
- [netapp.aws](https://docs.ansible.com/ansible/latest/collections/netapp/aws/index.html#plugins-in-netapp-aws)
- [netapp.azure](https://docs.ansible.com/ansible/latest/collections/netapp/azure/index.html#plugins-in-netapp-azure)
- [netapp.cloudmanager](https://docs.ansible.com/ansible/latest/collections/netapp/cloudmanager/index.html#plugins-in-netapp-cloudmanager)
- [netapp.elementsw](https://docs.ansible.com/ansible/latest/collections/netapp/elementsw/index.html#plugins-in-netapp-elementsw)
- [netapp.ontap](https://docs.ansible.com/ansible/latest/collections/netapp/ontap/index.html#plugins-in-netapp-ontap)
- [netapp.storagegrid](https://docs.ansible.com/ansible/latest/collections/netapp/storagegrid/index.html#plugins-in-netapp-storagegrid)
- [netapp.um_info](https://docs.ansible.com/ansible/latest/collections/netapp/um_info/index.html#plugins-in-netapp-um-info)
- [netapp_eseries.santricity](https://docs.ansible.com/ansible/latest/collections/netapp_eseries/santricity/index.html#plugins-in-netapp-eseries-santricity)
- [netbox.netbox](https://docs.ansible.com/ansible/latest/collections/netbox/netbox/index.html#plugins-in-netbox-netbox)
- [ngine_io.cloudstack](https://docs.ansible.com/ansible/latest/collections/ngine_io/cloudstack/index.html#plugins-in-ngine-io-cloudstack)
- [ngine_io.exoscale](https://docs.ansible.com/ansible/latest/collections/ngine_io/exoscale/index.html#plugins-in-ngine-io-exoscale)
- [ngine_io.vultr](https://docs.ansible.com/ansible/latest/collections/ngine_io/vultr/index.html#plugins-in-ngine-io-vultr)
- [openstack.cloud](https://docs.ansible.com/ansible/latest/collections/openstack/cloud/index.html#plugins-in-openstack-cloud)
- [openvswitch.openvswitch](https://docs.ansible.com/ansible/latest/collections/openvswitch/openvswitch/index.html#plugins-in-openvswitch-openvswitch)
- [ovirt.ovirt](https://docs.ansible.com/ansible/latest/collections/ovirt/ovirt/index.html#plugins-in-ovirt-ovirt)
- [purestorage.flasharray](https://docs.ansible.com/ansible/latest/collections/purestorage/flasharray/index.html#plugins-in-purestorage-flasharray)
- [purestorage.flashblade](https://docs.ansible.com/ansible/latest/collections/purestorage/flashblade/index.html#plugins-in-purestorage-flashblade)
- [purestorage.fusion](https://docs.ansible.com/ansible/latest/collections/purestorage/fusion/index.html#plugins-in-purestorage-fusion)
- [sensu.sensu_go](https://docs.ansible.com/ansible/latest/collections/sensu/sensu_go/index.html#plugins-in-sensu-sensu-go)
- [servicenow.servicenow](https://docs.ansible.com/ansible/latest/collections/servicenow/servicenow/index.html#plugins-in-servicenow-servicenow)
- [splunk.es](https://docs.ansible.com/ansible/latest/collections/splunk/es/index.html#plugins-in-splunk-es)
- [t_systems_mms.icinga_director](https://docs.ansible.com/ansible/latest/collections/t_systems_mms/icinga_director/index.html#plugins-in-t-systems-mms-icinga-director)
- [theforeman.foreman](https://docs.ansible.com/ansible/latest/collections/theforeman/foreman/index.html#plugins-in-theforeman-foreman)
- [vmware.vmware_rest](https://docs.ansible.com/ansible/latest/collections/vmware/vmware_rest/index.html#plugins-in-vmware-vmware-rest)
- [vultr.cloud](https://docs.ansible.com/ansible/latest/collections/vultr/cloud/index.html#plugins-in-vultr-cloud)
- [vyos.vyos](https://docs.ansible.com/ansible/latest/collections/vyos/vyos/index.html#plugins-in-vyos-vyos)
- [wti.remote](https://docs.ansible.com/ansible/latest/collections/wti/remote/index.html#plugins-in-wti-remote)