from android import Android
import time,sys
 
droid = Android()
droid.webViewShow('file:///sdcard/sl4a/scripts/daveTest/index.html')
 
# Complete one iteration for each event
while True: 
    event = droid.eventWait().result
    
    if event['name'] == 'kill':
        sys.exit()
    elif event['name'] == 'bluetooth':
	droid.toggleBluetoothState(True)
	droid.bluetoothConnect()
	while True:
	  message = droid.bluetoothReadLine().result
	  droid.eventPost('bluetoothOut', message)
	  if message =='quit':
	    title = 'dvas0004'
	    text = 'Server told me to turn bluetooth off'
            droid.dialogCreateAlert(title, text)
	    droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse().result
            droid.dialogDismiss()
	    break

    elif event['name'] == 'sayHi':

        droid.notify('dvas0004',event['data'])
	droid.vibrate()	
	title = 'dvas0004'
	text = 'Look at your notifications bar!'
	droid.dialogCreateAlert(title, text)
	droid.dialogSetNeutralButtonText('Ok')
        droid.dialogShow()
        droid.dialogGetResponse().result
        droid.dialogDismiss()
