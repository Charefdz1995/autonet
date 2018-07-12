from enum import Enum 

class architecture(Enum):
	CORE_AGG_ACC = 1 
	COLLAPSED_CORE_AGG = 2
	LEAF_AND_SPINE = 3  

class topology(object):

	def __init__(self,name,devices,links,arch=None,
				terminals=None,network_address=None):

	self.name = name 
	self.devices = devices
	self.terminals = terminals
	self.network_address = network_address

	@Property
	def get_name(self):
		return self.__name

	@name.setter
	def name(self,name):
		self.__name = name

	@Property
	def get_devices(self):
		return self.__devices

	@devices.setter
	def devices(self,devices):
		self.__devices = devices


	@Property
	def get_links(self):
		return self.__links

	@links.setter
	def links(self,links):
		self.__links = links

	@Property
	def get_network_address(self):
		return self.__network_address

	@links.setter
	def network_address(self,network_address):
		self.__network_address = network_address

	@Property
	def get_terminals(self):
		return self.__terminals

	@terminals.setter
	def terminals(self,terminals):
		self.__terminals = terminals


	def add_devices(devices):
		self.devices.extends(devices)

	def add_device(device):
		self.devices.append(device)

	def add_links(links):
		self.links.extends(links)

	def add_link(link):
		self.links.append(link)


