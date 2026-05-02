# Basic Calculator in python with Light/Dark Mode Support

# ANSI color codes for theme support
THEMES = {
    'light': {
        'bg': '\033[47m',      # White background
        'fg': '\033[30m',      # Black text
        'accent': '\033[34m',  # Blue accent
        'success': '\033[32m', # Green success
        'error': '\033[31m',   # Red error
        'reset': '\033[0m'     # Reset colors
    },
    'dark': {
        'bg': '\033[40m',      # Black background
        'fg': '\033[97m',      # White text
        'accent': '\033[96m',  # Cyan accent
        'success': '\033[92m', # Bright green success
        'error': '\033[91m',   # Bright red error
        'reset': '\033[0m'     # Reset colors
    }
}

current_theme = 'light'

def get_theme_color(color_name):
    """Get color code for current theme"""
    return THEMES[current_theme][color_name]

def print_themed(text, color='fg'):
    """Print text with current theme colors"""
    print(f"{get_theme_color(color)}{text}{get_theme_color('reset')}")

def toggle_theme():
    """Toggle between light and dark theme"""
    global current_theme
    current_theme = 'dark' if current_theme == 'light' else 'light'
    print_themed(f"Switched to {current_theme} mode!", 'accent')

# Function to add two numbers 
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return "Error! Division by zero not allowed."
    else:
        return x/y
    
def calculator():
    print_themed("🔢 Calculator - Light/Dark Mode Support", 'accent')
    print_themed("Select Operation:", 'fg')
    print_themed("1. Add", 'fg')
    print_themed("2. Sub", 'fg')
    print_themed("3. Mul", 'fg')
    print_themed("4. Div", 'fg')
    print_themed("5. Switch Theme", 'accent')

    while True:
        choice = input(f"{get_theme_color('fg')}Enter Choices (1/2/3/4/5): {get_theme_color('reset')}")
        # check if the input is one of the options
        if choice in ['1','2','3','4']:
            try:
                n1 = float(input(f"{get_theme_color('fg')}Enter the First Number: {get_theme_color('reset')}"))
                n2 = float(input(f"{get_theme_color('fg')}Enter the Second Number: {get_theme_color('reset')}"))
                
                if choice == '1':
                    result = add(n1,n2)
                    print_themed(f"{n1} + {n2} = {result}", 'success')
                elif choice == '2':
                    result = sub(n1,n2)
                    print_themed(f"{n1} - {n2} = {result}", 'success')
                elif choice == '3':
                    result = mul(n1,n2)
                    print_themed(f"{n1} x {n2} = {result}", 'success')
                elif choice == '4':
                    result = div(n1,n2)
                    if isinstance(result, str):  # Error message
                        print_themed(result, 'error')
                    else:
                        print_themed(f"{n1} / {n2} = {result}", 'success')
            except ValueError:
                print_themed("Error! Please enter valid numbers.", 'error')
        elif choice == '5':
            toggle_theme()
        else:
            print_themed("Invalid choice! Please select 1, 2, 3, 4, or 5.", 'error')

        # option to exit the loop
        next_calculation = input(f"{get_theme_color('fg')}Do you want to perform another calculation? (yes/no): {get_theme_color('reset')}")
        if next_calculation.lower() != "yes":
            break
    
    print_themed("Exiting Calculator, Goodbye! 👋", 'accent')

# call the function 
if __name__ == "__main__":
    calculator()
