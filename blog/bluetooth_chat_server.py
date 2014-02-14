import android
import time

droid = android.Android()
droid.toggleBluetoothState(True)
droid.dialogCreateAlert('Be a server?')
droid.dialogSetPositiveButtonText('Yes')
droid.dialogSetNegativeButtonText('No')
droid.dialogShow()
result = droid.dialogGetResponse()
is_server = result.result['which'] == 'positive'
if is_server:
  droid.bluetoothMakeDiscoverable()
  droid.bluetoothAccept()
else:
  droid.bluetoothConnect()

if is_server:
  result = droid.dialogGetInput('Chat', 'Enter a message').result
  if result is None:
    droid.exit()
  droid.bluetoothWrite(result + '\n')

while True:
  result = droid.dialogGetInput('Chat', 'Enter a message').result
  if result is None:
    break
  droid.bluetoothWrite(result + '\n')

droid.exit()
