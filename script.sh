path=/home/loras/SSDDisk/pythonProject/PythonScholar/Task/1111.txt
if tail -n 20 $path | grep -E -i 'Failed|Error';
then exit 1
else echo "Ok"
fi

