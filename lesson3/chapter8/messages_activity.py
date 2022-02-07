#import messages
#from messages import show_messages, send_messages
#from messages import show_messages as show, send_messages as send
#import messages as ms
from messages import *

original_list = ["LOL","ROFL","TTYL","BRB","TTFN"]
sent_messages = []
send_messages(original_list)
show_messages(sent_messages)