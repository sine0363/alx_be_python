


while True:
    Task= input("Enter your task:")
    Priority = input("Priority (high/medium/low):")
    Time_bound = input("Is it time-bound? (yes/no):")
    match Priority:
        case "high":
            if Time_bound=="yes":
                print(f"Reminder: {Task} is a high task that requires immediate attention today!") 
                

                
        case "medium":
            print(f"{Task} is not a high priority")
        case "low":
            if Time_bound=="no":
                print(f"Note: {Task} is a low priority task.Consider completing it when you have free time.")
                



