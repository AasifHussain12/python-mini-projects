# Student Management System

students = {}

print("===================================")
print("   STUDENT MANAGEMENT SYSTEM")
print("===================================")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")

        if roll_no in students:
            print("❌ Student already exists!")
        else:
            name = input("Enter Student Name: ")
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            students[roll_no] = {
                "Name": name,
                "Course": course,
                "Marks": marks
            }

            print("✅ Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("📚 No student records found.")
        else:
            print("\nStudent Records:")
            for roll_no, details in students.items():
                print("-------------------------------")
                print("Roll No :", roll_no)
                print("Name    :", details["Name"])
                print("Course  :", details["Course"])
                print("Marks   :", details["Marks"])

    elif choice == "3":
        roll_no = input("Enter Roll Number to search: ")

        if roll_no in students:
            details = students[roll_no]
            print("\nStudent Found")
            print("Roll No :", roll_no)
            print("Name    :", details["Name"])
            print("Course  :", details["Course"])
            print("Marks   :", details["Marks"])
        else:
            print("❌ Student not found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to delete: ")

        if roll_no in students:
            del students[roll_no]
            print("🗑️ Student record deleted successfully!")
        else:
            print("❌ Student not found.")

    elif choice == "5":
        print("\n👋 Thank you for using Student Management System!")
        break

    else:
        print("❌ Invalid choice! Please try again.")