case "$1" in 
    start)
	echo "=========================================Starting Infovis Server============================================"
	nohup python manage.py runserver 0.0.0.0:8000 &
	LASTPID=$!
	echo $LASTPID > infovis.pid
    ;;
    stop)
	echo "=========================================Stoping Infovis Server============================================"
	INFOVISPID=$(cat /root/kyyb_heya_admin/infovis.pid)
	echo $INFOVISPID
	pkill -9 -P $INFOVISPID
    ;;
esac
exit 0
