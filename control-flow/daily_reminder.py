task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  
time_bound = input("Is it time-bound? (yes/no): ").lower()


immediate_attention_suffix = f" that requires immediate attention today!"
low_priority_non_time_bound_suffix = " Consider completing it when you have free time."

# Process the Task Based on Priority and Time Sensitivity:
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            print({reminder_message},{immediate_attention_suffix})
        else:
            # For high priority but not time-bound, still imply importance
            print({reminder_message},".")
    case "medium":
        reminder_message = f"Reminder: '{task}' is a medium priority task"
        if time_bound == "yes":
            print({reminder_message},{immediate_attention_suffix})
        else:
            # For medium priority but not time-bound, still imply importance
            print({reminder_message},".")
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task"
        if time_bound == "yes":
            # Even if low priority, if time-bound, it needs attention
            print({reminder_message},{immediate_attention_suffix})
        else:
            print({reminder_message},{low_priority_non_time_bound_suffix})
    case _:
        # Handle invalid priority input
       print("Invalid user input")


  
  
