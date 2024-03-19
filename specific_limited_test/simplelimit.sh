stress --cpu 2 --timeout 30 &
pid=$(pidof -s stress)
pid2=$(($pid - 1))
cpulimit -p $pid -l 50 -z & 
cpulimit -p $pid2 -l 50 -z &
