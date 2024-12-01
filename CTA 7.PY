def main():
    # Dictionaries for course information
    course_rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    course_instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    course_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    # Get user input for course number
    course_number = input("Enter a course number (e.g., CSC101, NET110): ")

    # Check if course exists and display details
    if course_number in course_rooms:
        print(f"\nCourse Number: {course_number}")
        print(f"Room Number: {course_rooms[course_number]}")
        print(f"Instructor: {course_instructors[course_number]}")
        print(f"Meeting Time: {course_times[course_number]}")
    else:
        print("Course not found. Please enter a valid course number.")

# Run the program
if __name__ == "__main__":
    main()
