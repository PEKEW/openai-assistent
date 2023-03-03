#!/usr/bin/env python3

import os
import openai
from rich.console import Console
from rich.markdown import Markdown

def load_key(pth: str = 'api.ini') -> str:
    """load openai api key from path
    Args:
        pth: path 2 openai api key file
    Return:
        api: openai api key
    """
    if not pth:
        raise ValueError("API file path is required.")
    
    try:
        with open(pth,'r') as f:
            api = f.read().strip()
            return api
    except FileNotFoundError:
        print(f"API file not found form inputted path({pth})")
        return None
    except IOError:
        print(f"Could not read API file.")
        return None

def submit(current_dialog: str, history_dialog: list[str]) -> str:
    """submit dialog to OPENAI
    Args:
        current_dialog: The newest user input
        history_dialog: Hisoory user inputs
    Return:
        gpt_answer: Response from GPT model
    """
    messages = [{"role": "system",
         "content":  "When your output contains codes, formulas,\
                 tables, you should use the Markdown format whenever possible."
                }]
    messages.extend(history_dialog)
    messages.append({"role": "user","content":current_dialog})
    
    try:
        res = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages
        )
        return res["choices"][0]["message"]["content"]
    except openai.error.RateLimitError as e:
        console.print("The rate limit for the API has been exceeded.Please try again later.")
        console.print(f"Error: {e}")
        return ""
    
if __name__ == '__main__':
    console = Console()
    sep = Markdown("---")
    console.print("Loading Keys..")
    openai.api_key = load_key()
    if not openai:
        console.print("API KEY LOAD ERROR!")
    console.print("OPENAI API KEYS HAS LOADED!")

    # todo: In the future, if too long context affects the script's effeciency, array,np.array can be used.print
    context = []

    while True:
        user_in = console.input("[bold yellow]>>[/] ").strip()
        if user_in in ['reset!!']:
            context.clear()
            console.print("The session has been reset")
            continue
        if user_in in ['quit!!']:
            console.print("Bye!")
            break
        gpt_out = submit(user_in, context)
        print(gpt_out)
        console.print(Markdown(gpt_out), sep)
        context.append(
            {"role": "user", "content": user_in}
        )
        context.append(
            {"role": "assistant", "content": gpt_out}
        )
