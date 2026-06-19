items = {
    "Python": ["Python Course", "Machine Learning", "Data Science"],
    "Java": ["Java Course", "Spring Boot", "Android Development"],
    "Web Development": ["HTML & CSS", "JavaScript", "React"],
    "AI": ["Machine Learning", "Deep Learning", "Chatbots"]
}

print("=== AI Recommendation System ===")

interest = input("Enter your interest: ")

if interest in items:
    print("\nRecommended for you:")
    for item in items[interest]:
        print("-", item)
else:
    print("Sorry! No recommendations found.")
    