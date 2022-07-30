import pyautogui

def search_pc(query):
    query = query.lower()
    query = query.replace("open app ","")
    query.strip()
    pyautogui.keyDown("win")

    pyautogui.press("s")

    pyautogui.keyUp("win")

    s=query

    for a in s:
        pyautogui.press(a)
    pyautogui.press("enter")
    return query

def switch_tab():
    pyautogui.keyDown("alt")

    pyautogui.press("tab")

    pyautogui.keyUp("alt")
