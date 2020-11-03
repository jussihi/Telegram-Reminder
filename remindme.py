import string

secs = ["sec", "secs", "sek", "sekunti", "sekuntia"]
mins = ["min", "mins", "minuutti", "minuuttia"]
hours = ["hour", "h", "tunti", "tuntia"]
days = ["d", "day", "days", "päivä", "päivää"]
weeks = ["w", "week", "weeks", "viikko", "viikkoa"]
months = ["m", "mon", "month", "months", "kuukausi", "kuukautta"]
year = ["y", "year", "years", "vuosi", "vuotta"]

def to_reply(context):
	job = context.job
	context.bot.send_message(chat_id=job.context["chat_id"], text=job.context["text"], reply_to_message_id=job.context["origmessage_id"])

def parse_time(message):
	number = message.strip(string.punctuation)
	number = int(number.strip(string.ascii_letters))
	print(number)
	text = message[9:]
	text = text.strip(string.whitespace)
	text = text.strip(string.digits)
	print(text)
	if text in secs:
		return number
	elif text in mins:
		return number * 60
	elif text in hours:
		return number * 60 * 60
	elif text in days:
		return number * 60 * 60 * 24
	elif text in weeks:
		return number * 60 * 60 * 24 * 7
	elif text in months:
		return number * 60 * 60 * 24 * 30
	elif text in year:
		return number * 60 * 60 * 24 * 365



def remind(update, context):
	print("aaa")
	message = update.message
	if not message.text:
		return
	delay_secs = parse_time(message.text)
	ret = ""
	origmessage = message
	if message.reply_to_message:
		origmessage = message.reply_to_message
	ret = "Got it! Reminding you in %d seconds... " % (delay_secs)
	context.bot.send_message(chat_id=message.chat_id, text=ret)
	ret = "Reminding %s " % (message.from_user.full_name)
	context.job_queue.run_once(to_reply, delay_secs, context={"chat_id": message.chat_id, "text": ret, "origmessage_id": origmessage.message_id})