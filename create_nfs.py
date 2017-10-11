import sys
sys.path.append("/opt/NTAPdfm/lib/python")
from NaServer import *

## Setting connection

s = NaServer("<server name or IP address>", 1 , 14)
s.set_server_type("FILER")
s.set_transport_type("HTTPS")
s.set_port(443)
s.set_style("LOGIN")
s.set_admin_user("<user name>", "<password>")


api = NaElement("volume-create")
api.child_add_string("containing-aggr-name","<containing-aggr-name>")
api.child_add_string("language-code","<language-code>")
api.child_add_string("size","<size>")
api.child_add_string("space-reserve","<space-reserve>")
api.child_add_string("volume","<volume>")

xo = s.invoke_elem(api)
if (xo.results_status() == "failed") :
    print ("Error:\n")
    print (xo.sprintf())
    sys.exit (1)

print ("Received:\n")
print (xo.sprintf())



# Create a new qtree.
api1 = NaElement("qtree-create")

# The file permission bits of the qtree. Similar to UNIX permission bits: 0755 gives read/write/execute permissions to owner and read/execute to group and other users. It consists of 4 octal digits derived by adding up bits 4, 2, and 1. Omitted digits are assumed to be zeros. First digit selects the set user ID (4), set group ID (2), and sticky (1) attributes. The second digit selects permissions for the owner of the file: read (4), write (2), and execute (1); the third selects permissions for other users in the same group; the fourth for other users not in the group. If this argument is missing, use the default value specified in the option "wafl.default_qtree_mode".
api1.child_add_string("mode","<mode>")

# The path of the qtree, relative to the volume.
api1.child_add_string("qtree","<qtree>")

# Name of the volume on which to create the qtree
api1.child_add_string("volume","<volume>")

xo1 = s.invoke_elem(api1)
if (xo1.results_status() == "failed") :
    print ("Error:\n")
    print (xo1.sprintf())
    sys.exit (1)

print ("Received:\n")
print (xo1.sprintf())



# Sets the size of the indicated volume's snapshot reserve to the specified percentage. Reserve space can be used only by snapshots and not by the active file system.
api2 = NaElement("snapshot-set-reserve")

# Percentage to set. Range [0-100].
api2.child_add_string("percentage","<percentage>")

# Name of volume on which to set the snapshot space reserve.
api2.child_add_string("volume","<volume>")

xo2 = s.invoke_elem(api2)
if (xo2.results_status() == "failed") :
    print ("Error:\n")
    print (xo2.sprintf())
    sys.exit (1)

print ("Received:\n")
print (xo2.sprintf())



# Set the snapshot schedule on a specified volume. If number of snapshots requested is greater than ONTAP allows, then ESNAPTOOMANY will be returned with the maximum allow snapshots in the reason.
api3 = NaElement("snapshot-set-schedule")

# Number of snapshots taken daily to keep on line. If not provided, the number of daily snapshots is left at the previous value.
api3.child_add_string("days","<days>")

# Number of snapshots taken hourly to keep on line. If not provided, the number of weekly snapshots is left at the previous value.
api3.child_add_string("hours","<hours>")

# Number of snapshots taken minutely to keep on line. If not provided, the number of minutely snapshots is left at the previous value.
api3.child_add_string("minutes","<minutes>")

# Name of the volume name where the snapshots are located.
api3.child_add_string("volume","<volume>")

# Number of snapshots taken weekly to keep on line. If not provided, the number of weekly snapshots is left at the previous value.
api3.child_add_string("weeks","<weeks>")

# Comma-separated list of the hours at which the hourly snapshots are created. If hours is 0, which-hours is ignored and cleared.
api3.child_add_string("which-hours","<which-hours>")

# Comma-separated list of the minutes at which the minutely snapshots are created. If minutes is 0, which-minutes is ignored and cleared.
api3.child_add_string("which-minutes","<which-minutes>")

xo3 = s.invoke_elem(api3)
if (xo3.results_status() == "failed") :
    print ("Error:\n")
    print (xo3.sprintf())
    sys.exit (1)

print ("Received:\n")
print (xo3.sprintf())



# Adds a quota entry. If the type, target, volume, and tree do not exist, a new entry is created. If the type, target, volume, and tree exist, then an error is returned.
api4 = NaElement("quota-add-entry")

# This is the number of files that the target can have. Set the value to "-" if the limit is to be unlimited. Default is unlimited.
api4.child_add_string("file-limit","<file-limit>")

# This is the qtree name that the quota resides on. It can be the qtree name or "" if no qtree.
api4.child_add_string("qtree","<qtree>")

# This is the quota target of the type specified. The target can be of the form: &lt;name&gt;, &lt;number&gt;, or &lt;path name&gt;. Multiple targets can be specified by a comma-separated list.
api4.child_add_string("quota-target","<quota-target>")

# This is the quota type: "user", "group", or "tree".
api4.child_add_string("quota-type","<quota-type>")

# This is the amount of disk space the target would have to exceed before a message is logged and an SNMP trap is generated. The value is expressed in kilobytes (1024). Set the value to "-" if the limit is to be unlimited. Default is unlimited.
api4.child_add_string("soft-disk-limit","<soft-disk-limit>")

# This is the number of files the target would have to exceed before a message is logged and an SNMP trap is generated. Set the value to "-" if the limit is to be unlimited. Default is unlimited.
api4.child_add_string("soft-file-limit","<soft-file-limit>")

# This is the amount of disk space the target would have to exceed before a message is logged. The value is expressed in kilobytes (1024). Set the value to "-" if the limit is to be unlimited. Default is unlimited.
api4.child_add_string("threshold","<threshold>")

# This is the volume name that the quota resides on.
api4.child_add_string("volume","<volume>")

xo4 = s.invoke_elem(api4)
if (xo4.results_status() == "failed") :
    print ("Error:\n")
    print (xo4.sprintf())
    sys.exit (1)

print ("Received:\n")
print (xo4.sprintf())



# Starts to turn quotas on for a volume. A successful return from this API does not mean that quotas are on, merely that an attempt to start it has been triggered. Use the quota-status API to check the status.
api5 = NaElement("quota-on")

# Name of the volume on which to enable quotas.
api5.child_add_string("volume","<volume>")

xo5 = s.invoke_elem(api5)
if (xo5.results_status() == "failed") :
    print ("Error:\n")
    print (xo5.sprintf())
    sys.exit (1)

print ("Received:\n")
print (xo5.sprintf())



# Request the secondary system to configure a new snapvault relationship with the given primary and secondary systems and paths. This API is equivalent to the 'snapvault start' Data ONTAP command. All the inputs provided with this request will be stored in the configuration entry maintained by the secondary system. These values will be used as default settings for further incremental update transfers for this relationship. The snapvault-secondary-modify-configuration API can be used to change these configured settings. A successful configuration will automatically be followed by a baseline transfer from the primary to the secondary. The secondary path will be created during the baseline transfer hence it is required that the secondary path must not exist when issuing this request. This request will only begin the baseline transfer and return. The transfer will proceed asynchronously and there is no guarantee that it will succeed. The snapvault-get-relationship-status API should be used to check the status of the transfer.
api6 = NaElement("snapvault-secondary-create-relationship")

# Relationship configuration

xi_6 = NaElement("configuration")
api6.child_add(xi_6)


# Describes the elements of the snapvault configuration entry.

xi_6_1 = NaElement("snapvault-configuration-info")
xi_6.child_add(xi_6_1)


# The maximum transfer rate in kilobytes (1024 bytes) per second that will be used for this relationship as well as baseline transfer. The default value for this parameter will allow transfers to proceed as fast as possible. Range:[1..2^32-1]
xi_6_1.child_add_string("max-transfer-rate","<max-transfer-rate>")

# The primary path that will be used as the source for this relationship as well as for baseline transfer. This can be either in UTF8 or ASCII/extended ASCII depending on whether or not 'is-primary-path-utf8-encoded' flag is set. If option 'is-primary-path-utf8-encoded' is not specified, then the primary-path considered as in ASCII/extended ASCII.
xi_6_1.child_add_string("primary-path","<primary-path>")

# The primary system for this relationship as well as for the baseline transfer. This input will be used by the secondary system to establish contact with the primary. Therefore this input is expected to be a hostname that the primary can resolve.
xi_6_1.child_add_string("primary-system","<primary-system>")

# The secondary path that will be used as destination for this relationship as well as baseline transfer. The secondary path will be created during the baseline transfer and hence it must not exist when issuing this request.
xi_6_1.child_add_string("secondary-path","<secondary-path>")

xo6 = s.invoke_elem(api6)
if (xo6.results_status() == "failed") :
    print ("Error:\n")
    print (xo6.sprintf())
    sys.exit (1)

print ("Received:\n")
print (xo6.sprintf())


