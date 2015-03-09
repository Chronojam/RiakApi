# A quick script to attach all the riak instances into a single cluster

IPADDRESSES=$(docker ps | tail -n +2 | while read cid b; do docker inspect $cid | grep IPAddress | cut -d \" -f 4; done)
CIDS=$(docker ps | tail -n +2 | while read cid b; do echo $cid; done)

oldIFS="$IFS"
IFS='
'
IFS=${IFS:0:1}
iplines=( $IPADDRESSES )
cidlines=( $CIDS )
IFS="$oldIFS"
cidcounter=0
for cid in "${cidlines[@]}"
	do
	ipaddrcounter=0
	for ipaddr in "${iplines[@]}"
		do
		if ! [ "$ipaddrcounter" -eq "$cidcounter" ] 
			then 
				echo "attaching : --> $ipaddr to $cid"
				docker-enter $cid riak-admin cluster join riak@$ipaddr
				docker-enter $cid riak-admin cluster plan
				docker-enter $cid riak-admin cluster commit
		fi
		(( ipaddrcounter++ ))
		done
(( cidcounter++ ))
done
