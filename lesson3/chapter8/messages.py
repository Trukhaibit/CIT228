def show_messages(messages):
    print("Showing messages:")
    for m in messages:
        print(m)
def send_messages(messages):
    print("Sending messages:")
    for m in messages:
        print(m)
        sent_messages.append(m)
original_list = ["LOL","ROFL","TTYL","BRB","TTFN"]
sent_messages = []
send_messages(original_list)
show_messages(sent_messages)