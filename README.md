# Problem
The purpose of this code test was to provide a solution the code test to the following problem:

One of the common problems encountered with a data feed is related to transactions and portfolio balances. There were cases where the total value of the transactions for a particular account does not equate to his/her portfolio balance.
 
Create a script where it will take 2 CSVs, one for a list of accounts and their holding balances and another for a list of transactions. Ensure that the total value of the transactions per holding is equal to their holding balance. If not, produce a report stating which holding for a particular account is not correct.


# My approach

I decided to utilise python for this code test due to it's efficiency in running reconciliation operations when implemented propertly.

# Limitations
Whilst this currently can be run locally, to make this a fully automated process, the provisioning of an AWS S3 bucket to store both the transaction and account files then invoking an AWS lambda to run the python code and then email this to relevant parties for easy access where permissible.  
Currently the data received for this test has been read by this script by loading the data directly into this script.  A further iteration of this script would look to read data from a csv file stored in an object store in order to make this a repeatable process to be automatically run at the required intervals.

# Execution Instructions
clone repo to an IDE, I have used VS Code for this.
the required csv files are part of the repo: accounts.csv and transactions.csv
once cloned you should be able to execute the codetestjb.py in VS code 
a csv file name recononciliation_differences.csv should be present.  Refer to the differences column for the difference between the "total product balance" of the accounts file and "adjusted amount"(totals per product and account id from the transactions file).  If there is a value there other than 0, the solution has calculated a difference between the two files and would indicate that an operational/business representative may need to investigate further.

