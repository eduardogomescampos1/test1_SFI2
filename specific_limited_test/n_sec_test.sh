stress --cpu $1 --timeout $3 &
sleep 2
pid=$(pidof -s stress)
cpulimit -p $pid -l $2 -z &
for i in $(seq 2 $1); do
	pid=$(($pid - 1))
	cpulimit -p $pid -l $2 -z &
done
sleep 360
