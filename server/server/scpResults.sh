read -p 'File to transfer: ' fileName
echo $fileName
sshpass -p 'root' scp -T root@169.254.68.4:~/pacl/$fileName /pacl

exit
