# tempestwx
This contains an updated version of sensor_codes.csv with all 512 possible error combinations (including None).

It also contains tempest_errors.py, which is a Splunk external lookup program that will return the csv formatted error code when called as a lookup like this:

`| lookup tempest_error_lu sensor_status`

and adding the contents of transforms.conf to $SPLUNK_HOME/etc/apps/tempestwx/default/transforms.conf. The return value from the lookup is **sensor_errors** which
will contain a concatenated string of all errors found for a given sensor status.
