


while True:
    task= input("Enter your task:")
    task_priority = input("Priority (high/medium/low):")
    time_bound = input("Is it time-bound? (yes/no:)")
    match task_priority:
        case "high":
            if time_bound=="yes":
                print(f"{task} is a high task that requires immediate attention today!") 
                
        case "medium":
            print(f"{task} is not a high priority")
        case "low":
            if time_bound=="no":
                print(f"{task} is a low priority task.Consider completing it when you have free time.")
                break



