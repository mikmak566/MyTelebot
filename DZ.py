
# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    bot.send_message(chat_id, text="ДОДЕЛАТЬ")
# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    bot.send_message(chat_id, text="ДОДЕЛАТЬ")
# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    bot.send_message(chat_id, text="ДОДЕЛАТЬ")
# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    bot.send_message(chat_id, text="ДОДЕЛАТЬ")
# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz5_proc_answer)

def dz5_proc_answer(bot, chat_id, age_int):
    bot.send_message(chat_id, text=f"О! тебе уже {age_int}! \nА через год будет уже {age_int+1}!!!")
# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    proc_answer = lambda message: bot.send_message(chat_id, f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", proc_answer)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, proc_answer):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, proc_answer)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, proc_answer):

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_return, botQuestion=bot, txtQuestion=txt, proc_answer=proc_answer)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, proc_answer)  # то-же самое, но короче

def my_inputInt_return(message, botQuestion, txtQuestion, proc_answer):
    chat_id = message.chat.id
    try:
        var_int = int(message.text)
        proc_answer(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, proc_answer)

# -----------------------------------------------------------------------
