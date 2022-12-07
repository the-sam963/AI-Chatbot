# Intaligent Assistant
it is a very intaligent Chat bot, built with 'nltk'. In this project I use .csv file to store data. It can be use with other databases also.

Here I ignored 'data' directory, becauce it contains very large files. If you want to clone  it you need to do a little task.

* make 2 directories on the root directory called 'data' & 'model'.
* make 2 csv file p_{classname}.py & r_{classname}.py; And every file should have two columns - for p_{classname}.py => ['pattern', 'tag'] & for r_{classname}.py => ['response', 'tag']

* Add more data for more classes
* Run train.py to create brain
* Run test.py and enjoy