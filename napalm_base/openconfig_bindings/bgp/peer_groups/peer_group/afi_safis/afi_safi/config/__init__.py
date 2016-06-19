
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp - based on the path /bgp/peer-groups/peer-group/afi-safis/afi-safi/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for the AFI-SAFI
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__afi_safi_name','__enabled',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    self.__afi_safi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},), is_leaf=True, yang_name="afi-safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='identityref', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'peer-groups', u'peer-group', u'afi-safis', u'afi-safi', u'config']

  def _get_afi_safi_name(self):
    """
    Getter method for afi_safi_name, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/config/afi_safi_name (identityref)

    YANG Description: AFI,SAFI
    """
    return self.__afi_safi_name
      
  def _set_afi_safi_name(self, v, load=False):
    """
    Setter method for afi_safi_name, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/config/afi_safi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_safi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_safi_name() directly.

    YANG Description: AFI,SAFI
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},), is_leaf=True, yang_name="afi-safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_safi_name must be of a type compatible with identityref""",
          'defined-type': "openconfig-bgp:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},), is_leaf=True, yang_name="afi-safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='identityref', is_config=True)""",
        })

    self.__afi_safi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_safi_name(self):
    self.__afi_safi_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},), is_leaf=True, yang_name="afi-safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='identityref', is_config=True)


  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/config/enabled (boolean)

    YANG Description: This leaf indicates whether the IPv4 Unicast AFI,SAFI is
enabled for the neighbour or group
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: This leaf indicates whether the IPv4 Unicast AFI,SAFI is
enabled for the neighbour or group
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  afi_safi_name = property(_get_afi_safi_name, _set_afi_safi_name)
  enabled = property(_get_enabled, _set_enabled)


  _pyangbind_elements = {'afi_safi_name': afi_safi_name, 'enabled': enabled, }


