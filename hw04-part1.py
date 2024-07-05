from pathlib import Path

# функція аналізує файл "salary.txt" і повертає 
# загальну та середню суму заробітної плати всіх розробників.
# файл "salary.txt"  має бути у той же діректорії, де є файл, що виконується
def total_salary(path):
    file_path = Path(path)
    result = ['','']
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sum_salary, count_salary = 0, 0
            for line in f:
                name, salary = line.split(',')
                salary = int(salary.rstrip('\n'))
                sum_salary += salary
                count_salary += 1
            avr_salary = int(sum_salary / count_salary)
            result = [sum_salary, avr_salary]
    except:
        print(f"{file_path} does not exist or is not a file")
    return result

def main():
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()
