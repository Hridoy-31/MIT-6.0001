annual_salary = float(input("Enter the starting salary: "))
down_payment = 0.25 * 1000000   # 25% of $1M
semi_annual_raise = 0.07
r = 0.04    # annual return
months = 36
epsilon = 100   # acceptable tolerance

def calculate_current_savings(annual_salary, savings_rate, semi_annual_raise, months, r):
    current_savings = 0.0
    monthly_salary = annual_salary/12.0
    
    for month in range(1, months+1):
        current_savings += current_savings * (r/12)
        current_savings += monthly_salary*savings_rate
        
        if (month%6 == 0):
            monthly_salary += monthly_salary*semi_annual_raise
        
    return current_savings

def finding_best_savings_rate(annual_salary, semi_annual_raise, months, r, down_payment, epsilon):
    # Bisection search
    step = 0
    high = 10000
    low = 0
    
    while (low <= high):
        savings_rate = (high + low) / 20000
        current_savings = calculate_current_savings(annual_salary, savings_rate, semi_annual_raise, months, r)
        
        if (abs(current_savings - down_payment) <= epsilon):
            return savings_rate, step
        
        if (current_savings < down_payment):
            low = int(savings_rate*10000) + 1
        else:
            high = int(savings_rate*10000) - 1
        
        step += 1
        
    return None, step


best_savings_rate, steps = finding_best_savings_rate(annual_salary, semi_annual_raise, months, r, down_payment, epsilon)

if (best_savings_rate == None):
    print("It is not possible to pay the down payment in three years.")
else:
    print(f"Best savings rate: {best_savings_rate:.4f}")
    print(f"Steps in bisection search: {steps}")    
    
    