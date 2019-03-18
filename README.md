# create-brain-csv
Creating csv data for Machine learning to see if it is possible to predict what activity a person is carrying out

Very simple python script that will read the mqtt brain data from this project I built
[brain-reader-esp8266-mqtt](https://github.com/greallye/brain-reader-esp8266-mqtt)

The goal is to run the data collected through a machine learning algorithm which is in dev at the moment.

Then once enough data is collected we will check against live readings to see how accurate the 33g and the machine learning algorithm is. 

To run the script pass your current activity in like watching_tv and the the filename you want.

```shell
$ python current_activity filename.csv
```
