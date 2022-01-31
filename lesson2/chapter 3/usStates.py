print("-------------------------------------")
print("States that support the Macguffin Act")
print("-------------------------------------")
states=["Michigan","Wisconsin","Illinois","Indiana","Ohio"]
print("Original List:", states)

states.append("Baja California Sul")
states.insert(5,"Alaska")
print("List after additions", states)

del states[4]
states.pop()
states.remove("Indiana")
print("List after deletions", states)

print("List with temporary sort:", sorted(states))
states.reverse
print("List sorted in reverse:", states)
states.sort
print("List sorted in alphabetical order:", states)
print(f"There are {len(states)} in the final list")