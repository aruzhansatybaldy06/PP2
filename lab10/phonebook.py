from config import config
import psycopg2
import csv
import os


parameters = config()
conn = psycopg2.connect(**parameters)
cursor  = conn.cursor()


def add_data(): #добавление данных
    rows = []
    mode = int(input("Select input:\n1 - read from console input\nEnter: "))

    if mode not in [1, 2]:
        print("Error")
        return
    
    if mode == 1:
        name   = input("Enter name: ")
        number = input("Enter number: ")
        
        if "--" in name or "--" in number:
            print("Error")
            return
        
        rows.append([name, number])
    
    else:
        path = input("Enter absolute or relative path: ")
        
        if not os.path.exists(path):
            print("Path does not exist")
            return
        
        with open(path) as file:
            data = csv.reader(file)
            next(data)

            for row in data:
                if "--" in row[0] or "--" in row[1]:
                    print("Error")
                    return
                else:
                    rows.append(row)
    
    for row in rows:
        cursor.execute(f"INSERT INTO PhoneBook (name, number) VALUES ('{row[0]}', '{row[1]}')") #Метод который выполняет задание строки

    conn.commit()
    print("Done")

def update_data(): #обновление данных
    initial_name   = input("Enter name of contact: ")
    initial_number = input("Enter number of contact: ")
    if "--" in initial_name or "--" in initial_number:
        print("Error")
        return

    cursor.execute(f"SELECT * FROM PhoneBook WHERE name = '{initial_name}' AND number = '{initial_number}'")
    if cursor.rowcount == 0:
        print("Contact does not exist")
        return

    mode = input("Update name or number:\nname - update name\nnumber - update number\nEnter: ")
    if mode not in ["name", "number"]:
        print("Error")
        return
    
    new_info = input(f"Enter new {mode}: ")
    if "--" in new_info:
        print("Error")
        return
    
    cursor.execute(f"UPDATE PhoneBook SET {mode} = '{new_info}' WHERE name = '{initial_name}' AND number = '{initial_number}'") #метод для выполнения одного выражения SQL
    
    conn.commit()
    print("Done")




def query_data(): #пойск
    query_mode = int(input(
        "Choose query mode:\n1 - search by name\n2 - search by number\n3 - find starts with\n4 - search any attribute\nEnter: "
        ))
    
    if query_mode not in [1, 2, 3, 4]:
        print("Error")
        return

    query_value = input("Enter query: ")
    if "--" in query_value:
        print("Error")
        return
    
    query_dict = {
        1 : f"name = '{query_value}'",
        2 : f"number = '{query_value}'",
        3 : f"starts_with(name, '{query_value}') OR starts_with(number, '{query_value}')",
        4 : f"name ILIKE '%{query_value}%' OR number ILIKE '%{query_value}%'"
        }

    cursor.execute(f"SELECT * FROM PhoneBook WHERE {query_dict[query_mode]}")

    result = cursor.fetchall()
    if len(result) == 0:
        print("No results")
    else:
        print("Results:")

    for row in result:
        print(row)




def delete_data(): #удаление данных
    mode = input("Select delete by:\nname - delete by name\nnumber - delete by number\nEnter: ")
    if mode not in ["name", "number"]:
        print("Error")
        return
    
    info = input(f"Enter {mode}: ")
    if "--" in info:
        print("Error")
        return

    cursor.execute(f"DELETE FROM PhoneBook WHERE {mode} = '{info}'")
    
    conn.commit() #Записать транзакцию
    print("Done")




def main():
    functions = {1 : add_data, 2 : update_data, 3 : query_data, 4 : delete_data}
    mode = int(input("Select mode:\n1 - add data\n2 - update data\n3 - query data\n4 - delete data\nEnter: "))

    if mode not in [1, 2, 3, 4]:
        print("Error")
        return
    
    functions[mode]()

    cursor.close()#немедленно закрывает курсор
    conn.close()
    


if __name__ == "__main__":
    main()