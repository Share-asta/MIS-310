#Problem 1

target = float(input("Enter total sales target:"))

cumulative_sales = 0.0

for day in range(1,6):
    daily_sales = float(input("Enter day {} sales:".format(day)))

    if daily_sales <=0.0:
        print("Invalid sales amount.")
        break

    cumulative_sales += daily_sales
    percentage = (cumulative_sales / target)*100

    print("Cumulative sales {} ({} %)".format(cumulative_sales, percentage))

#Problem 2
route_number = 1
fastest_time = 0
fastest_route = 0

while True:

    distance = float(input("Enter route {} distance in miles: ".format(route_number)))
    speed = float(input("Enter route {} speed in miles per hour: ".format(route_number)))

    time_minutes = (distance / speed) * 60

    if fastest_time == 0 or time_minutes < fastest_time:
        fastest_time = time_minutes
        fastest_route = route_number

    more = input("More routes? (y/n): ").lower()

    if more != "y":
        break

    route_number += 1

print("Route {} is fastest; {} minutes".format(fastest_route, round(fastest_time)))

# Question b) results
    # Route 3 is fastest; 52 minutes












