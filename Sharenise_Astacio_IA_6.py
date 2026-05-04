def main():

    def set_steps_goal():
        goal = int(input("Enter daily steps goal: "))
        return goal

    def record_daily_steps():
        total_steps = 0
        for day in range(1, 8):
            steps = int(input(f"Enter steps for the day {day}: "))
            total_steps += steps
        return total_steps

    def evaluate_weekly_performance(total_steps, goal):
        average_steps = total_steps / 7

        print()
        print(f"Your average daily steps: {average_steps}")

        if average_steps > goal:
            print(f"You went over your daily steps goal of {goal} steps!")
        elif average_steps == goal:
            print(f"Your daily steps goal of {goal} steps have been met!")
        else:
            print(f"You did not meet your daily steps goal of {goal} steps.")

    goal = set_steps_goal()
    total_steps = record_daily_steps()
    evaluate_weekly_performance(total_steps, goal)

main()