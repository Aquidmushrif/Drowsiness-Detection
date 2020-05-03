import py2sms
def snd():
    print('Sending SMS')
    s=py2sms.send('#UserMobileNumber','#username','#TargetNumber','Drowsiness Alert')
