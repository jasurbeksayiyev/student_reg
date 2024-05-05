import json

class StudentRegistrationSystem:
    def __init__(self, filename='student_records.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.student_records = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.student_records = {}

    def save_records(self):
        with open(self.filename, 'w') as file:
            json.dump(self.student_records, file)

    def add_student(self, student_id, student_info):
        if student_id not in self.student_records:
            self.student_records[student_id] = student_info
            self.save_records()
            print(f"Student with ID {student_id} added successfully.")
        else:
            print(f"Student with ID {student_id} already exists.")

    def view_student_details(self, student_id):
        return self.student_records.get(student_id, f"Student with ID {student_id} does not exist.")

    def update_student_information(self, student_id, updated_info):
        if student_id in self.student_records:
            self.student_records[student_id].update(updated_info)
            self.save_records()
            print(f"Student with ID {student_id} updated successfully.")
        else:
            print(f"Student with ID {student_id} does not exist.")

    def delete_student(self, student_id):
        if student_id in self.student_records:
            del self.student_records[student_id]
            self.save_records()
            print(f"Student with ID {student_id} deleted successfully.")
        else:
            print(f"Student with ID {student_id} does not exist.")

    def run(self):
        while True:
            print("\nStudent Registration System")
            print("1. Add Student")
            print("2. View Student Details")
            print("3. Update Student Information")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter option: ")

            if choice == '1':
                student_id = input("Enter student's ID: ")
                name = input("Enter student's Full-name: ")
                course = input("Enter student's Course: ")
                birthdate  = input("Enter student's Birthdate: ")
                Email_account = input("Enter student's Email account: ")
                nationality = input("Enter student's Nationality: ")
                phone_number = input("Enter student's Phone number: ")
                graduation = input("Enter student's Graduated school: ")
                year_of_graduation = input("Enter student's Year of graduation: ")
                self.add_student(student_id, {"name": name, "course": course, "birthdate":birthdate,"Email_account": Email_account, " nationality":  nationality, "phone_number": phone_number, "graduation": graduation, "year_of_graduation": year_of_graduation })
            elif choice == '2':
                student_id = input("Enter student ID to view details: ")
                print(self.view_student_details(student_id))
            elif choice == '3':
                student_id = input("Enter student ID to update: ")
                name = input("Enter student new name (leave blank if no change): ")
                course = input("Enter student new course (leave blank if no change): ")
                birthdate  = input("Enter student new Birthdate (leave blank if no change): ")
                Email_account = input("Enter student new Email account (leave blank if no change): ")
                nationality = input("Enter student new Nationality (leave blank if no change): ")
                phone_number = input("Enter student new Phone number (leave blank if no change): ")
                graduation = input("Enter student new Graduated school (leave blank if no change): ")
                year_of_graduation = input("Enter student new Year of graduation (leave blank if no change): ")
                updated_info = {}
                if name:
                    updated_info['Name'] = name
                if course:
                    updated_info['Course'] = course
                if birthdate:
                    updated_info['Birthdate'] = birthdate
                if Email_account:
                    updated_info['Email account'] = Email_account
                if nationality:
                    updated_info['Nationality'] = nationality
                if phone_number:
                    updated_info['Phone number'] = phone_number
                if graduation:
                    updated_info['Graduated school'] = graduation
                if year_of_graduation:
                    updated_info['Year of graduation'] = year_of_graduation
                self.update_student_information(student_id, updated_info)
            elif choice == '4':
                student_id = input("Enter student ID to delete: ")
                self.delete_student(student_id)
            elif choice == '5':
                break
            else:
                print("Invalid option, please try again.")

# Run the program
srs = StudentRegistrationSystem()
srs.run()