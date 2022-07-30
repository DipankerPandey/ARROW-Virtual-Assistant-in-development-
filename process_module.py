from output_module import output
from time_module import get_time, get_date
from database import *
from input_module import take_input
from internet import *
from automa import *
from details import description
from math_module import calc
from sam import *

def process(query):

    answer = get_answer_from_memory(query)

    hel=""

    if sam_mode():
        hel=assistance()+ " anyway, "

        answer2 = get_answer_from_sam(query)
        if answer2 == "suicidal":
            return suicide()

        elif answer2 == "sexist":
            return sexist()

        elif answer2 == "about me":
            return about()

        elif "is this sam" in query.lower():
            return "Noo, this. is. PATRICK"

    if answer == "":
        answer = check_on_wiki(query)
        if answer != "":
            return hel+answer

    if answer == "get time details":
        return hel+"Time is " + get_time()

    elif answer == "check internet connection":
        if check_internet_connection():
            return "connected"
        return "not connected"

    elif answer == "tell date":
        return hel+"Date is " + get_date()

    elif answer == "on speak":
        return turn_on_speech()

    elif answer == "off speak":
        return turn_off_speech()

    elif answer == "on hear":
        return turn_on_hearing()

    elif answer == "off hear":
        return turn_off_hearing()

    elif answer == "open app":
        a = search_pc(query)
        return hel+"opening " + a

    elif answer == "switch tab":
        switch_tab()
        return hel+"switching tabs"

    elif answer == "search google":
        search_google(query)
        return hel+"This is what I found"

    elif answer == "open youtube":
        youtube_search(query)
        return hel+"Playing"

    elif answer == "give intro":
        return description

    elif answer == "calculate":
        a = str(calc(query))
        if a is not None:
            return hel+"Answer is " + a
        else:
            return hel+r"Can't be solved"


    else:
        output("I don't know this one, can you tell me what it means?")
        ans = take_input()
        if "it means" in ans:
            ans = ans.replace("it means", "")
            ans = ans.strip()

            value = get_answer_from_memory(ans)
            if value == "":
                return "Cant help with this one"
            else:
                insert_question_and_answer(query, value)
                return "Thanks I will remember it"
        else:
            return r"Can't help with this one"
