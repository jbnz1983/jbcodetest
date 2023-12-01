# jbcodetest
The purpose of this code test was to 

# My approach

I decided to utilise python for this code test due to it's efficiency in running reconciliation operations when implemented propertly.

# Assumptions


# Limitations
Whilst this currently can be run locally, to make this a fully automated process, the provisioning of an AWS S3 bucket to store both the transaction and account files then invoking an AWS lambda to run the python code and then email this to relevant parties for easy access where permissible.  
Currently the data received for this test has been read by this script by loading the data directly into this script.  A further iteration of this script would look to read data from a csv file stored in an object store in order to make this a repeatable process to be automatically run at the required intervals.

