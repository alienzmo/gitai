import subprocess  

def generate_commit_message():  
    # دریافت تغییرات استیج شده  
    try:  
        staged_diff = subprocess.check_output(['git', 'diff', '--cached']).decode('utf-8')  
        # در اینجا می‌توانید کد ارسال به LLM را اضافه کنید  
        # فرض بر این است که پیام تولید شده به صورت زیر است  
        return f"Auto-generated commit message based on changes."  # این را با LLM جایگزین کنید  
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