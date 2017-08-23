#webbrowser.open(url, new=0, autoraise=True)
import webbrowser
import time
#keep a track on time
#open a webrowser when it's time
#using python3.x
#this is a new comment
#hi my name is bharadwaj
print ("this program started on "+time.ctime())
break_count=0
total_breaks=3  #number of breaks
while (break_count<total_breaks):
          time.sleep(10)
          webbrowser.open("https://www.youtube.com/watch?v=pvAsqPbz9Ro") #add your link
          break_count=break_count+1
if(1==1):
	print("true")