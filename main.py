from telegram.ext import Updater, CommandHandler
import requests
import re


def get_url():
	contents = requests.get('https://random.dog/woof.json').json()
	image_url = contents['url']
	return image_url


def get_image_url():
	allowed_extensions = ['jpg', 'jpeg', 'png']
	file_extension = ''
	while file_extension not in allowed_extensions:
		url = get_url()
		file_extension = re.search('([^.]*)$',url).group(1).lower()
	return url


def start(update, context):
	url = get_image_url()
	chat_id = update.message.chat.id
	context.bot.send_photo(chat_id=chat_id, photo=url)


def main():
	updater = Updater('5545629304:AAGcYM7zqy1UWYTa-ekX9wGmSmwg1vswAko', use_context=True)

	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()