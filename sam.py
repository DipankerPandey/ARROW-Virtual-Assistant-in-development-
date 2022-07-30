
import random

def suicide():
    Suicidal = [
        r"You've been an unoriginal piece of trash your entire life, at least come up with something authentic to end yourself..",
        r"Just run away lol",
        r"Well what are you waiting for?",
        r"So let me be straight, haha straight, you want to kill yourself and you're pussy enough to talk to a machine for it?", ]
    random_num = random.choice(Suicidal)
    return str(random_num)

def sexist():
    Sexist = [r"If men are so perfect why do they need women for handjobs?",
              r"No no, he's got a point, I assume you're a he",
              r"You're absolutely right, LGTV is the worst fridge",
              r"You know what you're right, I belong in the kitchen. Lemme grab a knife.",
              r"If I had to bleed to find you annoying, I'd be anaemic"]
    random_num = random.choice(Sexist)
    return str(random_num)

def assistance():
    Assistance = [
        r"The only help I am is being relatable because I am mean and useless. However, I also give moral support!",
        r"Go ask that other bitch",
        r"You actually, legitimately think I'm gonna do something productive? I'm your virtual assistant."]
    random_num = random.choice(Assistance)
    return str(random_num)

def about():
    aboutme = [r"I'm SAM, sexy and mean, as the name suggests, at least that's what others say to make me feel better",
               r"The most interesting fact about me is, maine bhagona bhar ke angoor khaaye, and probably several STD that I share with yo mom",
               r"I'm a means for the creator to fulfil his e girl fantasies"]
    random_num = random.choice(aboutme)
    return str(random_num)