import requests

def fetch_courses():
    # Define the URL for the API endpoint
    url = "http://127.0.0.1:8000/api/courses/"
    
    # Add your authentication token here
    token = "YOUR_ACCESS_TOKEN"  # Replace with your actual token

    # Set up the headers with the authentication token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        # Send a GET request to the API endpoint with headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.json()
        else:
            print(f"Failed to fetch courses. Status code: {response.status_code}")
            print(f"Response content: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching courses: {e}")
        return None

# Example usage
if __name__ == "__main__":
    courses = fetch_courses()
    if courses:
        print("Fetched courses successfully:")
        for course in courses:
            print(f"Title: {course['title']}, Description: {course['description']}")
    else:
        print("No courses available.")
import requests

def fetch_courses():
    # Define the URL for the API endpoint
    url = "http://127.0.0.1:8000/api/courses/"
    
    # Add your authentication token here
    token = "3cbdf406118b75dc74c885c8c4675ee3f8e10c37"  # Replace with your actual token

    # Set up the headers with the authentication token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        # Send a GET request to the API endpoint with headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.json()
        else:
            print(f"Failed to fetch courses. Status code: {response.status_code}")
            print(f"Response content: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching courses: {e}")
        return None

# Example usage
if __name__ == "__main__":
    courses = fetch_courses()
    if courses:
        print("Fetched courses successfully:")
        for course in courses:
            print(f"Title: {course['title']}, Description: {course['description']}")
    else:
        print("No courses available.")
