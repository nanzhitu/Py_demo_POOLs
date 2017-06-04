# $language = "Python"
# $interface = "1.0"

#filePath = crt.Dialog.FileOpenDialog("please open a file","open","a.log","(*.log)|*.log")
#crt.Dialog.MessageBox(filePath,"",64|0)

#crt.Dialog.MessageBox("会话已断开","session",64|2)
#crt.Dialog.MessageBox("确认是否退出","session",32|1)
#crt.Dialog.MessageBox("确认是否退出","session",32|3)
#temp = crt.Dialog.MessageBox("是否继续安装","session",48|6)


#crt.Dialog.MessageBox("此会话已打开","session",48|5)
#crt.Dialog.MessageBox("无法连接此窗口","session",16|6)

#temp = crt.Dialog.Prompt("password","session","admin",True)

#crt.Dialog.MessageBox(temp,"",64|0)

#curCol =  crt.Screen.CurrentColumn
#crt.Dialog.MessageBox(str(curCol))
'''
crt.Screen.IgnoreEscape = False

crt.Screen.Send("java -version\r\n");
crt.Screen.WaitForString("64-Bit",2);
outPut = crt.Screen.ReadString(["home","server","$"],10)
index = crt.Screen.MatchIndex
if (index == 0):
    crt.Dialog.MessageBox("Timed out!")
elif (index == 1):
    crt.Dialog.MessageBox("Found 'home'")
elif (index == 2):
    crt.Dialog.MessageBox("Found 'server'")
elif (index == 3):
    crt.Dialog.MessageBox("Found '$'")

crt.Screen.Clear()

out = crt.Screen.Get2(3, 15, 5, 34)
crt.Dialog.MessageBox(out)
crt.Screen.Send("\x04")

crt.Screen.SendSpecial("MENU_NEW_WINDOW")
'''
#temp = crt.Screen.WaitForCursor(5)
temp = crt.Screen.WaitForKey(5)
if temp == None:
    crt.Dialog.MessageBox("asasasasa")
else:
    crt.Dialog.MessageBox("false")



