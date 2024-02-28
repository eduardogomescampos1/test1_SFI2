echo "Starting the test"
echo "The first part will commence now"
/test1_regular.sh
echo "First part is finished"
sleep 2
echo "The second part will commence now"
./test1_regular.sh&
./test1_hamperer&
echo "The second part is finished and the test is over"
