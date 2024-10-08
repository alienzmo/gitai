import subprocess  
import requests

def generate_commit_message():  
    try:  
        staged_diff = subprocess.check_output(['git', 'diff', '--cached']).decode('utf-8')  
        
        # ارسال به LLM (مثال با استفاده از یک API فرضی)  
        response = requests.post('https://chat.openai.com/chat', json={'diff': staged_diff})  
        
        if response.status_code == 200:  
            return response.json().get('message', 'Auto-generated commit message based on changes.')  
        else:  
            print("Error from LLM:", response.text)  
            return "Auto-generated commit message based on changes."  
    except subprocess.CalledProcessError as e:  
        print("Error getting staged changes:", e)  
        return None  
 

def read_input(prompt):  
    return input(prompt)  

def gcm():  
    print("Generating AI-powered commit message...")  
    commit_message = generate_commit_message()  

    if not commit_message:  
        print("Failed to generate commit message.")  
        return  

    while True:  
        print("\nProposed commit message:")  
        print(commit_message)  

        choice = read_input("Do you want to (a)ccept, (e)dit, (r)egenerate, or (c)ancel? ")  

        if choice.lower() == 'a':  
            # تأیید و انجام commit  
            try:  
                subprocess.run(['git', 'commit', '-m', commit_message], check=True)  
                print("Changes committed successfully!")  
                return  
            except subprocess.CalledProcessError as e:  
                print("Commit failed. Please check your changes and try again.")  
                return  
        elif choice.lower() == 'e':  
            # ویرایش پیام  
            commit_message = read_input("Enter your commit message: ")  
            if commit_message:  
                try:  
                    subprocess.run(['git', 'commit', '-m', commit_message], check=True)  
                    print("Changes committed successfully with your message!")  
                    return  
                except subprocess.CalledProcessError as e:  
                    print("Commit failed. Please check your message and try again.")  
                    return  
        elif choice.lower() == 'r':  
            # تولید مجدد پیام  
            print("Regenerating commit message...")  
            commit_message = generate_commit_message()  
        elif choice.lower() == 'c':  
            print("Commit cancelled.")  
            return  
        else:  
            print("Invalid choice. Please try again.")  

# برای اجرای تابع gcm می‌توانید در بخش اصلی کد خود از این خط استفاده کنید.  
gcm()