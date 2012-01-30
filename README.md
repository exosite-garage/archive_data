========================================
About
========================================
This python script exports data from a single data source from the One Platform
into a .csv file with the "Timestamp" in column 1 and "Data" in column 2.

License is BSD, Copyright 2011, Exosite LLC (see LICENSE file)

Built/tested with Python 2.6.5

========================================
Quick Start
========================================
(1) install python<br>
http://www.python.org/download/<br>
http://www.python.org/download/releases/2.7.2/<br>

(2) open a command line window and run the script<br>
python archive_data.py CIK ALIAS SINCE UNTIL<br>

Where CIK: one platform client key<br>
      ALIAS: dataport alias<br>
      SINCE: MM/DD/YYYY<br>
      UNTIL: MM/DD/YYYY<br>
      
For example:<br>
python archive_data.py e6df1111b014e902bcccf09aa758cddde0c47ce5 temp 01/29/2012 01/30/2012

========================================
More Information
========================================
--) CIK can be obtained by by logging into your account and navigating to 
    manage/device page.  Click on the device in the list you would like to 
    export data from, and copy the KEY from the popup.<br>
--) ALIAS is the data source (dataport) to export.  This is the 'Resource' 
    listed in the device popup 'Data List' section, or the 'Reporting As' from 
    the manage/data popup.<br>
--) SINCE is the start time to export, defaulted to 00:00:00<br>
--) UNTIL is the end time of export, defaulted to 23:59:59<br>

--) Notes<br>
* The .csv file exported will be called archive_data.csv.  The process will 
  overwrite any existing archive_data.csv file, so rename or move the file out 
  of the exported folder if there are multiple data sources or time ranges to 
  export. <br>
* The timestamp field is stored in format of seconds-since-epoch.  For example,
  http://www.epochconverter.com/.
