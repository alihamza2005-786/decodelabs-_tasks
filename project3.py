# AI Recommendation System
items = {
    "Python Basics": ["programming", "python", "beginner"],
    "Machine Learning": ["ai", "python", "advanced"],
    "Web Development": ["html", "css", "javascript"],
    "Data Science": ["python", "data", "ai"],
    "Graphic Design": ["photoshop", "design", "creative"]

}
user_input = input("Enter your interests separated by commas: ")
user_preferences = user_input.lower().split(",")
user_preferences = [interest.strip() for interest in user_preferences]# Remove extra spaces

# here we use Recommendation logic

recommendations = []
for item, tags in items.items():

    # Count matching interests
    match_score = 0

    for preference in user_preferences:
        if preference in tags:
            match_score += 1

    # If at least one match found
    if match_score > 0:
        recommendations.append((item, match_score))

# Step 4: Sort recommendations by score
recommendations.sort(key=lambda x: x[1], reverse=True)

# Step 5: Display results
print("\nRecommended Courses:\n")

if recommendations:
    for item, score in recommendations:
        print(f"{item}  --> Match Score: {score}")
else:
    print("No recommendations found.")

    # that's it