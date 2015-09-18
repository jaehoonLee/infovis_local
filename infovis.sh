case "$1" in 
    start)
	echo "=========================================Starting Infovis Server============================================"
	nohup python main.py &
	LASTPID=$!
	echo $LASTPID > infovis.pid
    ;;
    stop)
	echo "=========================================Stoping Infovis Server============================================"
	CURDIR=$(pwd)
	INFODIR="$CURDIR/infovis.pid"
	INFOVISPID=$(cat $INFODIR)
	echo $INFOVISPID
	pkill -9 -P $INFOVISPID
	kill -9 $INFOVISPID
    ;;
esac
exit 0
