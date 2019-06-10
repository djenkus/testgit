
read -p 'File to transfer: ' fileName
echo $fileName
sshpass -p 'root' scp $fileName root@169.254.68.4:~/pacl

exit
