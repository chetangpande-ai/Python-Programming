class Facebook:

    def __init__(self):
        # Dictionary to store {username: password}
        self.usercredentials = {}
        # Dictionary to store {username: [messages]}
        self.messages = {}

    def login_or_signup(self, username, password):
        action = input("Do you want to login or signup? ").lower()

        if action == "signup":
            if username in self.usercredentials:
                print("⚠️ Username already exists. Please login instead.")
            else:
                self.usercredentials[username] = password
                self.messages[username] = []
                print(f"✅ Signup successful! Welcome, {username}.")

        elif action == "login":
            if username in self.usercredentials and self.usercredentials[username] == password:
                print(f"✅ Login successful! Welcome back, {username}.")
            else:
                print("❌ Invalid username or password.")

        else:
            print("⚠️ Invalid choice. Please type 'login' or 'signup'.")

    def post_messages(self, username, message):
        if username in self.messages:
            self.messages[username].append(message)
            print(f"📩 All messages by {username}: {self.messages[username]}")
        else:
            print("⚠️ User not found. Please login/signup first.")


# Example usage:
user1 = Facebook()

# First signup or login
user1.login_or_signup("chetan", "pande")

# Post messages
user1.post_messages("chetan", "Hello everyone!")
user1.post_messages("chetan", "Second message on Facebook 🚀")
