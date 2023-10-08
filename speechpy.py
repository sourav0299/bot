import speech_recognition as sr
import webbrowser
import datetime

def time0299():
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%H:%M:%S")
    print(current_time_str)
    
def leetcode_function():
    webbrowser.open("https://leetcode.com/problemset/all/")


def codechef_function():
    webbrowser.open("https://www.codechef.com/practice-old")


def codeforces_function():
    webbrowser.open("https://codeforces.com/problemset?order=BY_SOLVED_DESC")


def gfg_function():
    webbrowser.open(
        "https://practice.geeksforgeeks.org/problem-of-the-day?itm_source=geeksforgeeks&itm_medium=main_header&itm_campaign=practice_header")


def listen_for_keyword(keyword="computer"):
    time0299()
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(f"Say '{keyword}' to activate:")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {user_input}")

        if keyword in user_input:
            print(f"Activated by keyword '{keyword}'")
            return True
        else:
            print("Activation keyword not detected.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

    return False


def main():
    activation_keyword = "computer"

    while True:
        if listen_for_keyword(activation_keyword):
            time0299()
            print("Listening for a command...")
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                audio = recognizer.listen(source)

            try:
                user_input = recognizer.recognize_google(audio).lower()
                print(f"Recognized: {user_input}")

                if "task 1" in user_input:
                    leetcode_function()
                elif "task 2" in user_input:
                    codechef_function()
                elif "task 3" in user_input:
                    codeforces_function()
                elif "task 4" in user_input:
                    gfg_function()
                else:
                    print("Command not recognized.")
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")


if __name__ == "__main__":
    main()
